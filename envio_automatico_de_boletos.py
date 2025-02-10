# Abrir arquivo
# identificar ângulo X e Y do arquivo
# Copiar nome do pagante
# fechar arquivo ctrl+w
# Renomear arquivo f2
# Apertar seta baixo
# repetir processo 
    
# Biblioteca

import pyautogui as py

# Variáveis

tempo_de_delay = 1  
tempo_de_abertura = 3
auxiliador = 1

posicao_texto_inicial_x = 0
posicao_texto_inicial_y = 0

posicao_texto_final_x = 0
posicao_texto_final_y = 0

computador_off = 0


# APRESENTAÇÃO
print("=========================")
print("Este executável tem por finalidade automatizar renomeação de arquivos baseado nos parâmetros passados!")
print("Estima-se que, por arquivo, será um total de 10 segundos.")
print("=========================")

def copia_texto():
    global auxiliador
    
    py.moveTo(x=posicao_texto_inicial_x,y=posicao_texto_inicial_y)
    py.PAUSE = tempo_de_delay
    py.mouseDown()
    py.PAUSE = tempo_de_delay
    py.moveTo(x=posicao_texto_final_x, y=posicao_texto_final_y)
    py.PAUSE = tempo_de_delay
    py.mouseUp()
    py.PAUSE = tempo_de_delay
    py.hotkey("ctrl","c")
    py.PAUSE = tempo_de_delay
    py.hotkey("ctrl","w")
    py.PAUSE = tempo_de_delay
    py.press("f2")
    py.PAUSE = tempo_de_delay
    py.hotkey("ctrl","v")
    py.PAUSE = tempo_de_delay
    py.press("enter")
    py.PAUSE = tempo_de_delay
    py.press("esc")
    py.PAUSE = tempo_de_delay
    
    py.press("down")
    py.PAUSE = tempo_de_delay
    py.press("enter")
    # py.PAUSE = tempo_de_delay
    # py.press("enter")
    auxiliador = auxiliador + 1

def perguntar_desligar_computador():
    global computador_off
    
    computador_off = input("Gostaria que o computador fosse desligado após a operação?\n(1) - Sim\n(2) - Não\nDigite: ")
    if(computador_off == "1"):
        print("=========================")
        print("O computador desligará após a execução do script")
    elif(computador_off == "2"):
        print("=========================")
        print("O computador não será desligado!")
    else:
        print("=========================")
        print("Opção inválida")
        perguntar_desligar_computador()

def solicita_posicao_mouse():
    
    global posicao_texto_inicial_x
    global posicao_texto_inicial_y
    
    global posicao_texto_final_x
    global posicao_texto_final_y
    
    global escolha
    
    input("Abra o arquivo inicial e aperte 'Enter'\n(O navegador só pode ter uma aba aberta, que é a aba do arquivo): ")
    print("=========================")
    input("Posicione o cursor do mouse no inicio do texto a ser copiado: (Aperte Enter para continuar)")
    texto_inicial = py.position()
    print("=========================")
    posicao_texto_inicial_x = texto_inicial[0]
    posicao_texto_inicial_y = texto_inicial[1]

    input("Posicione o cursor do mouse no final do texto a ser copiado: ")
    texto_final = py.position()
    print("=========================")
    posicao_texto_final_x = texto_final[0]
    posicao_texto_final_y = texto_final[1]
    
    escolha = input("(1) - Continuar\n(2) - Refazer operação\nDigite: ")
    if(escolha == "1"):
        print("Posições gravadas!")
        return "1"
    elif(escolha == "2"):
        print("=========================")
        print("Refazendo operação")
        solicita_posicao_mouse()
    else:
        print("Opção inválida")
        print("=========================")
        solicita_posicao_mouse()

perguntar_desligar_computador()

while(True):
    solicita_posicao_mouse()
    print("=========================")
    qtd_arquivos = int(input("Informe a quantidade de arquivos: "))
    print(f"{qtd_arquivos} serão nomeados.") 
    print("=========================")
    aceite = input("O Script será executado, deseja continuar?\n(1) - Sim\n(2) - Não\nDigite: ")
    match aceite: 
        case "1":
            py.hotkey("alt","tab")
            py.PAUSE = tempo_de_delay
            py.press("enter")
            py.PAUSE = tempo_de_abertura
            while auxiliador <= qtd_arquivos: 
                copia_texto()
            break
        case "2":
                print("Processo encerrado!")
        case _:
            print("=========================")
            print("Opção inválida...")
    
        
if(computador_off == "1"):
    py.PAUSE = 2
    py.hotkey("win","d")
    py.Pause = 2
    py.hotkey("alt","f4")
    py.Pause = 2
    py.press("enter")
print("Execução finalizada!")
        