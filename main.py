import cv2
from ultralytics import YOLO
import mss
import numpy as np
import keyboard
from pynput.mouse import Button, Controller

# model = YOLO("yolov8n.pt")
model = YOLO(r"runs\detect\train2\weights\best.pt")

monitor = {"top": 362, "left": 551, "width": 801, "height": 481}

mouse = Controller()

exit_flag = False

def on_press_q(e):
    global exit_flag
    if e.name == 'q':
        exit_flag = True

keyboard.on_press(on_press_q)
with mss.mss() as sct:
    while not exit_flag:
        sct_img = sct.grab(monitor)
        frame = np.array(sct_img)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)
        results = model(frame)
        
        for r in results:
            for box in r.boxes:
                xyxy = box.xyxy
                if xyxy.shape[1] == 4:
                    x_min, y_min, x_max, y_max = xyxy[0, 0], xyxy[0, 1], xyxy[0, 2], xyxy[0, 3]
                    print(f"x_min: {x_min:.2f}, y_min: {y_min:.2f}, x_max: {x_max:.2f}, y_max: {y_max:.2f}")
                else:
                    print("Invalid box coordinates format")
                
                abs_x_min = monitor["left"] + x_min
                abs_y_min = monitor["top"] + y_min
                abs_x_max = monitor["left"] + x_max
                abs_y_max = monitor["top"] + y_max
                
                x_center = (abs_x_min + abs_x_max) / 2
                y_center = (abs_y_min + abs_y_max) / 2
                mouse.position = (x_center, y_center)
                mouse.click(Button.left)

        if exit_flag:
            break

cv2.destroyAllWindows()
