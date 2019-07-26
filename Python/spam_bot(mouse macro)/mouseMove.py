import pyautogui

def mouseMove(x, y):
    #pyautogui.moveTo(500, 600, duration=1)
    pyautogui.scroll(10, pause=1., x=500, y=600)
    pyautogui.scroll(-10)
    import pdb; pdb.set_trace()

if __name__ == "__main__":
    mouseMove(1,2)