from PIL import Image
import pyautogui

screen_width, screen_height = pyautogui.size()

top = 362
left = 551
width = 801
height = 481

new_left = round(left * screen_width / 1920)
new_width = round(width * screen_width / 1920)
new_top = round(top * screen_height / 1080)
new_height = round(height * screen_height / 1080)

screenshot = pyautogui.screenshot(region=(left, top, width, height))

screenshot.save("screenshot.png")

image = Image.open("screenshot.png")
image.show()
