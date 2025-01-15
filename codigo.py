import pyautogui
import pandas as pd
import time

pyautogui.PAUSE = 0.5

#importando tabela

tabela = pd.read_csv('produtos.csv')

#acessando o chrome
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')

#digitando uma url
time.sleep(3)
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')
time.sleep(2)

#clicando no primeiro campo login
pyautogui.click(x=643, y=507)
pyautogui.write('docslaercio@gmail.com')
pyautogui.press('tab')
pyautogui.write('minhasenhadoida')
pyautogui.press('tab')
pyautogui.press('enter')

#cadastrando produtos

for linha in tabela.index:
    pyautogui.click(x=638, y=360)
    pyautogui.write(str(tabela.loc[linha, 'codigo']))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'marca']))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'tipo']))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'categoria']))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'preco_unitario']))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'custo']))
    pyautogui.press('tab')
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    time.sleep(0.5)
    pyautogui.press('tab')
    pyautogui.press('enter')
    pyautogui.scroll(5000)