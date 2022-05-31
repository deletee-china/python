import pyautogui as gui

gui.click(740,849)
print(gui.position())
gui.click(252,52)
gui.write('机械')
gui.press('enter')
for i in range(100):
    gui.write("666_"+str(i))
    gui.press('enter')
