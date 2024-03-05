import pyautogui
import time
import pandas

pyautogui.PAUSE = 0.5
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
pyautogui.hotkey ("win", "up")
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")
time.sleep(2)
pyautogui.click(x=2513, y=482)
pyautogui.write("pythonimpressionador@gmail.com")
pyautogui.press("tab")
pyautogui.write("sua senha aqui")
pyautogui.press("enter")
time.sleep(2)
tabela=pandas.read_csv("PythonPowerUp/produtos.csv")

for linha in tabela.index:
    pyautogui.click(x=2656, y=320)
    for coluna in tabela.columns:
        codigo=tabela.loc[linha,coluna]
        if not pandas.isna(codigo):
            pyautogui.write(str(codigo))
        pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.scroll(5000)