import asyncio
import keyboard
from constantes import *
import pyautogui

async def jigging():
    current_state = None
    tea_count = 0
    max_tea = 1
    complete_retrive = False

    while not keyboard.is_pressed('P'):
        pyautogui.press('space')
        print("My Current State is : " + str(current_state))
        ready = screenshotCompare(screenshot_file_path, tension_bar_icons_location, line_length_icon)
        take_rod_up = screenshotCompare(screenshot_file_path, tension_bar_icons_location, rod_up_at_5_meters)
        fish_hooked = screenshotCompare(screenshot_file_path, tension_bar_fish_hooked, fish_hooked_bar_icon)
        take_the_fish = screenshotCompare(screenshot_file_path, keep_release, keep_fish_button)
        tackle_ready_check = screenshotCompare(screenshot_file_path,tackle_ready_screen_location,tackle_ready)
        if(take_rod_up):
            complete_retrive = True

        if ready and tackle_ready_check:
            pyautogui.press('space')
            pyautogui.keyUp('[')
            pyautogui.keyUp(']')
            pyautogui.keyUp('shift')

            print("Charging in 1 sec")
            pyautogui.keyDown('shift')
            pyautogui.keyDown('[')
            await asyncio.sleep(1)
            pyautogui.keyUp('[')
            pyautogui.keyUp('shift')

            await asyncio.sleep(10)
            print("Release in 4 sec")
            tea_count = 0
            complete_retrive = False

        if complete_retrive and not tackle_ready_check:
            while keyboard.is_pressed('['):
                pyautogui.keyUp('[')
            pyautogui.keyDown(']')
            pyautogui.keyDown('shift')


        if not ready and not fish_hooked:
            pyautogui.press('space') 
            pyautogui.keyDown('[')
            if not fish_hooked and not complete_retrive:
                await asyncio.sleep(1.3)
                pyautogui.keyUp('[')
                await asyncio.sleep(2)
            pyautogui.keyUp('shift')

        if fish_hooked:
            pyautogui.press('control')
            pyautogui.press(']')
            pyautogui.keyDown('[')
            pyautogui.keyDown(']')
            pyautogui.keyDown('shift')

        if take_the_fish:
            pyautogui.keyUp('shift')
            pyautogui.keyDown('.') # the net
            pyautogui.press('space')
            current_state = STATES['TAKE_THE_FISH']

        if fish_hooked and current_state != STATES['FISH_HOOKED']:
            pyautogui.press('control')
            pyautogui.press(']')
            pyautogui.keyDown('[')
            pyautogui.keyDown(']')
            pyautogui.keyDown('shift')
            if tea_count < max_tea:
                pyautogui.keyDown('4')
                pyautogui.keyUp('4')
                tea_count+=1
                print("Tea Drinked: " + str(tea_count))
            current_state = STATES['FISH_HOOKED']

        if fish_hooked and ready and current_state != STATES['ROD_UP']:
            pyautogui.keyDown(']')
            pyautogui.keyDown('.') # the net
            continue


        if not fish_hooked and current_state == STATES['FISH_HOOKED']:
            current_state = None

async def start_script():
    print("Press 'L' to start the script.")
    keyboard.wait('L')  # Wait for the 'L' key to be pressed
    print("Script started!")
    await jigging()

if __name__ == "__main__":
    asyncio.run(start_script())