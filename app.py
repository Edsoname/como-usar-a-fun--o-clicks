# como usar a função clicks
import pyautogui

pyautogui.click(x=1127,y=543,clicks=1000, interval=0.2,
button='left',duration=2)
#click na posição atual( com botão esquerdo)
pyautogui.click()
pyautogui.click(button='left')
pyautogui.click(button='rigth')
pyautogui.click(button='middle')
# clicar x vezez 
pyautogui.click(clicks=10)
# funções prontas para clicks 
pyautogui.doubleClick()
pyautogui.rightClick()
pyautogui.middleClick()
pyautogui.tripleClick()




