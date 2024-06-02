from PIL import Image
import pyautogui

# Получаем разрешение экрана
screen_width, screen_height = pyautogui.size()

# Заданные координаты и размеры области
top = 362
left = 551
width = 801
height = 481

# Расчет новых координат с округлением
new_left = round(left * screen_width / 1920)
new_width = round(width * screen_width / 1920)
new_top = round(top * screen_height / 1080)
new_height = round(height * screen_height / 1080)

# Создаем скриншот области экрана
screenshot = pyautogui.screenshot(region=(left, top, width, height))

# Сохраняем скриншот
screenshot.save("screenshot.png")

# Открываем и отображаем скриншот
image = Image.open("screenshot.png")
image.show()