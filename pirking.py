import asyncio
import keyboard
from time import time
from constantes import *


async def sea():
    current_state = None
    tea_count = 0
    max_tea = 2
    reel_closed = False

    while not keyboard.is_pressed('O'):
        #pyautogui.press('space')
        #print("My Current State is : " + str(current_state))
        ready = screenshotCompare(screenshot_file_path, tension_bar_icons_location, line_length_icon)
        length_30_result = screenshotCompare(screenshot_file_path, tension_bar_icons_location, length_30)
        take_rod_up = screenshotCompare(screenshot_file_path, tension_bar_icons_location, rod_up_at_5_meters)
        fish_hooked = screenshotCompare(screenshot_file_path, tension_bar_fish_hooked, fish_hooked_bar_icon)
        take_the_fish = screenshotCompare(screenshot_file_path, keep_release, keep_fish_button)
        tackle_ready_check = screenshotCompare(screenshot_file_path,tackle_ready_screen_location,tackle_ready)#


        try:
            if take_the_fish:
                is_marker = list(pyautogui.locateOnScreen(marker_fish, confidence=0.5))
                pyautogui.keyDown('.')  # Press the net key
                if is_marker: 
                    print("Is Marker")     
                    pyautogui.press('space')
        except Exception as e:
            print("Is Not Marker") 
            pyautogui.press('backspace')
            # Handle other exceptions if needed
            #print(f"An error occurred: {e}")


        if fish_hooked:
            pyautogui.press('control')
            pyautogui.press(']')
            pyautogui.keyDown('[')
            pyautogui.keyDown(']')
            if tea_count < max_tea:
                pyautogui.keyDown('4')
                pyautogui.keyUp('4')
                tea_count+=1
                #print("Tea Drinked: " + str(tea_count))
            current_state = STATES['FISH_HOOKED']
            reel_closed = False

        #cast
        if ready and tackle_ready_check:
            pyautogui.press('space')
            pyautogui.keyUp('[')
            pyautogui.keyUp(']')
            pyautogui.keyUp('enter')
            pyautogui.click()
            current_state = STATES['CASTING']
            reel_closed = False

        #wait 30 meters
        if not length_30_result and not fish_hooked:        
            continue

        if length_30_result and not reel_closed and not fish_hooked:
            reel_closed = True
            pyautogui.press('[')

        #pirking
        if length_30_result and not fish_hooked:
            pyautogui.keyDown(']')
            await asyncio.sleep(1)
            pyautogui.keyUp(']')
            await asyncio.sleep(1)
            current_state = STATES['PIRKING']

        if fish_hooked and ready and current_state != STATES['ROD_UP']:
            pyautogui.keyDown(']')
            #pyautogui.keyDown('.') # the net
            continue


async def start_script():
    print("Press 'L' to start the script.")
    keyboard.wait('L')  # Wait for the 'L' key to be pressed
    print("Script started!")
    await sea()

if __name__ == "__main__":
    asyncio.run(start_script())