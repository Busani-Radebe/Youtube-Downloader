import pyautogui

# 1 find image on Screen ,get coordinates , store in variables
SearchBox = pyautogui.locateAllOnScreen('SearchBox.png')
print(SearchBox)

# # 2Move mouse to Search SearchBox
# pyautogui.moveTo(SearchBox)
# pyautogui.click()
#
# # 3Write in the search box
# pyautogui.write('What is my name?')
# pyautogui.hotkey('enter')
