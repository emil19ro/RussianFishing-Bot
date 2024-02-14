from constantes import *

# screenshot_file_path = 'screenshot.png'
# marker_fish = './images/mark.png'
# fish_selection_screen = {'left': 809, 'top': 61, 'width': 397, 'height': 110}
# ready = screenshotCompare(screenshot_file_path, fish_selection_screen, marker_fish)
# print(ready)
is_marker = list(pyautogui.locateCenterOnScreen(marker_fish, confidence=0.9))

if is_marker:
    print("Marker found!")
    
    # Move the mouse to each found location
    for location in is_marker:
        pyautogui.moveTo(location)
        # Add additional actions if needed, like clicking or other mouse operations
else:
    print("Marker not found.")