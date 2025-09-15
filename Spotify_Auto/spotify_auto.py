import pyautogui as pa
import time

pa.press("win")
pa.write("spotify")
time.sleep(3)
pa.press("enter")
time.sleep(8)


pa.click(x=589, y=367)  # Coordenadas para clickar na playlist (musicas curtidas)
time.sleep(3)

quantidade_musicas = 50
for i in range(quantidade_musicas):
    pa.click(x=1169, y=533)  #Coordenadas para clicar nos 3 pontinhos
    time.sleep(2)
    pa.click(x=1224, y=477) # Coordenadas do botão achar a playlist
    time.sleep(1)
    pa.click(x=1024, y=553) # Coordenadas de clicar na playlist
    time.sleep(1)
    pa.click(x=1169, y=533)  #Coordenadas para clicar nos 3 pontinhos
    time.sleep(1)
    pa.click(x=1284, y=511) # Coordenadas para clicar em remover da playlist
    time.sleep(1)