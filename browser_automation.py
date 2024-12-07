import pyautogui
import time

pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True
#abre o site
pyautogui.hotkey("win", "r")
pyautogui.typewrite("https://www.gabrielcasemiro.com.br/atividade_pyautogui \n")

time.sleep(5)


#pega a planilha e poem na var f 
with open ("membros.csv") as f:
    next(f)
#pega linha por linha da planilha
    for line in f:
        #tira os espaços em branco
        line = line.strip()
        #divide as linhas por delimitadores específicos 
        line = line.split(";")
        print(line)

        name = line[0]
        sex = line[1]
        email = line[2]
        phone = line[3]
        #Localiza o campo clica e escreve
        pyautogui.click(pyautogui.locateCenterOnScreen("img//nome.png", confidence=0.8), duration= 1 )
        pyautogui.typewrite(name, interval= 0.25)

        pyautogui.click(pyautogui.locateCenterOnScreen("img//email.png", confidence=0.8), duration= 1 )
        pyautogui.typewrite(email, interval= 0.25)

        pyautogui.click(pyautogui.locateCenterOnScreen("img//telefone.png", confidence=0.8), duration= 1 )
        pyautogui.typewrite(phone, interval= 0.25)
        #clica no campo e confere se é masculino ou feminino 
        pyautogui.click(pyautogui.locateCenterOnScreen("img//sexo.png", confidence=0.8), duration= 1 )
        if sex == "Masculino":
            pyautogui.click(pyautogui.locateCenterOnScreen("img//masculino.png", confidence=0.8), duration= 1 )
        else: 
            pyautogui.click(pyautogui.locateCenterOnScreen("img//feminino.png", confidence=0.8), duration= 1 )
        # Printa todos os cadrastos e salva por nome
        pyautogui.screenshot(f"cadrasto_{name}.png")
        pyautogui.click(pyautogui.locateCenterOnScreen("img//Cadastrar.png", confidence=0.8), duration= 1 )
        time.sleep(5)
# botão de aviso para avisar que o programa encerrou
pyautogui.alert(text = "Programa finalizado!", title = "Aviso do sistema", button = "OK")

