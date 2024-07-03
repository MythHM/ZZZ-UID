import pyautogui
import time
import keyboard

# 定义 List
List = [(0.468933, 0.589155), (0.948047, 0.7625), (0.128516, 0.404167), (0.844922, 0.30625), (0.855469, 0.435417), (0.849219, 0.366667),(0.442969,0.572222)]

# 单点
def click(point):
    x = List[point][0] * screen_width
    y = List[point][1] * screen_height
    pyautogui.moveTo(x, y)
    pyautogui.click()
    return 0

# 检测
def checkcolor(point):
    x = int(List[point][0] * screen_width)
    y = int(List[point][1] * screen_height)
    time.sleep(0.3)
    return pyautogui.pixel(x, y)

# 切换语音保障快速恢复“操作频繁”
def changelang():
    global lang
    lang = lang + 1
    o = (-1)**lang
    time.sleep(0.2)
    click(1)
    time.sleep(0.2)
    click(2)
    time.sleep(0.2)
    click(3)
    time.sleep(0.2)
    if o > 0:
        click(5)
    else:
        click(4)
    time.sleep(0.2)

if __name__ == "__main__":
    lang = 0
    screen_width, screen_height = pyautogui.size()
    time.sleep(1)
    pyautogui.FAILSAFE = False

    while True:
        if keyboard.is_pressed('p'):
            print("程序已停止")
            break
        click(0)
        if checkcolor(6) == (0, 204, 13):
            print("操作频繁")
            click(0)
            changelang()
