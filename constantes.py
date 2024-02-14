# Define the capture area (top-left corner, 200x200 pixels)
from datetime import datetime, timedelta
import cv2
import numpy as np
import pyautogui


tension_bar_icons_location = {'left': 1145, 'top': 1000, 'width': 250, 'height': 50}
tension_bar_fish_hooked = {'left': 507, 'top': 999, 'width': 101, 'height': 76}
fish_name = {"left": 777, "top": 68, "width": 348, "height": 105}
keep_release = {"left": 691, "top": 894, "width": 268, "height": 152}
tackle_ready_screen_location = {'left': 525, 'top': 1009, 'width': 165, 'height': 35}
fish_selection_screen = {'left': 809, 'top': 61, 'width': 397, 'height': 110}

# Specify the file path to save the screenshot
screenshot_file_path = 'screenshot.png'
line_length_icon = './images/line-length.png'
keep_fish_button = './images/keep.png'
rod_up_at_5_meters = './images/rod-up.png'
fish_hooked_bar_icon = './images/fish_hooked.png'
tackle_ready = './images/ready.png'

length_30 = './images/15-meters.png' # modify here temporary...
movement_bottom = './images/movement.png'
marker_fish = './images/mark.png'

# Define states
STATES = {
    'FISH_HOOKED': 'Fish Hooked',
    'TAKE_THE_FISH': 'Take the Fish',
    'CASTING': 'Casting',
    'RETRIEVING': 'Retrieving',
    'ROD_UP': 'Rod Up',
    'PIRKING': 'Pirking'
}

def take_screenshot_and_save(file_path, x, y, width, height):
    screenshot = pyautogui.screenshot(region=(x, y, width, height))
    screenshot = np.array(screenshot)
    screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2BGR)
    cv2.imwrite(file_path, screenshot)
    return screenshot

def compare_images(screenshot, small_image_path, confidence=0.9):
    # Load images using OpenCV
    screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2BGR)
    small_image = cv2.imread(small_image_path)

    # Apply template matching
    result = cv2.matchTemplate(screenshot, small_image, cv2.TM_CCOEFF_NORMED)
    _, max_val, _, _ = cv2.minMaxLoc(result)

    return max_val >= confidence

def screenshotCompare(path, source, static_image):
    screenshot = take_screenshot_and_save(path, source['left'], source['top'],
                                    source['width'], source['height'])
    is_present = compare_images(screenshot, static_image)
    return is_present

def reset_keys():
        pyautogui.keyDown('shift')
        pyautogui.keyUp('shift')
        pyautogui.keyDown(']')
        pyautogui.keyUp(']')
        pyautogui.keyDown('[')
        pyautogui.keyUp('[')

def get_elapsed_time(start_time):
    current_time = datetime.now()
    elapsed_time = current_time - start_time
    elapsed_seconds = int(elapsed_time.total_seconds())
    return elapsed_seconds