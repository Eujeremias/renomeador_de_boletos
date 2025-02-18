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
tempo_total = 0

posicao_texto_inicial_x = 0
posicao_texto_inicial_y = 0

posicao_texto_final_x = 0
posicao_texto_final_y = 0

computador_off = 0


# APRESENTAÇÃO
print("=========================")
print("Este programa tem como objetivo automatizar a renomeação de arquivos com base nos parâmetros fornecidos.")
print("A estimativa é de que o processo levará cerca de 15 segundos por arquivo.")
print("Instruções importantes:")
print("1 - Para alternar entre janelas, use 'Alt + Tab'.")
print("2 - Durante o processo de alternância de pastas, evite usar o mouse.")
print("3 - Certifique-se de que a alternância de janelas ocorra do terminal para a página de boletos (usando 'Alt + Tab').")
print("4 - Você pode alternar entre o terminal e a página que contém os boletos usando 'Alt + Tab'.")

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
        print("=========================")
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
    
    input("Ação - Selecione o arquivo inicial e aperte enter no terminal\nDica¹ - Pressione Alt + Tab e clique, só uma vez, no arquivo\nDica² - Após a 1° dica, pressiona Alt + Tab e aperte 'Enter' no terminal")
    print("=========================")
    input("Ação - Posicione o cursor do mouse no início do texto que será copiado\nDica¹ - Pressione Alt + Tab e mova o cursor do mouse até o início do texto a ser copiado\nDica² - Após a 1° dica, pressiona Alt + Tab e aperte 'Enter' no terminal (Sem  mover o mouse)")
    texto_inicial = py.position()
    print("=========================")
    posicao_texto_inicial_x = texto_inicial[0]
    posicao_texto_inicial_y = texto_inicial[1]

    input("Ação - Posicione o cursor do mouse no final do texto que será copiado\nDica¹ - Pressione Alt + Tab e mova o cursor do mouse até o final do texto a ser copiado\nDica² - Após a 1° dica, pressiona Alt + Tab e aperte 'Enter' no terminal (Sem  mover o mouse)")
    texto_final = py.position()
    print("=========================")
    posicao_texto_final_x = texto_final[0]
    posicao_texto_final_y = texto_final[1]
    
    escolha = input("(1) - Continuar\n(2) - Refazer operação\nDigite: ")
    if(escolha == "1"):
        print("=========================")
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
    tempo_total = qtd_arquivos * 11
    if(tempo_total < 60):
        print(f"Demorará {tempo_total} segundos")
    elif(tempo_total < 3600):
        print(f"Demorará {round((tempo_total / 60),2)} minutos")
    else:
        print(f"Demorará {round((tempo_total / 3600),2)} horas")
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
        