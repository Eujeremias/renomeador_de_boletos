## FLUXO DO CÓDIGO
# copiar CNPJ do nome do arquivo (boleto)
# ir para o whatsapp
# buscar contato pelo CNPJ
# selecionar contato (tab)
# recortar arquivo para o whatsapp (ctrl + x)
# colar (enviar) para contato
# pressionar enter
# retornar para aba dos boletos (alt+tab)
# arrow down

import pyautogui as py

posicao_mouse_buscador = 0
qtd_arquivos = 0
auxiliador = 0

def solicitacoes():
    print("=========================")
    input("Posicione o cursor do mouse no buscador do whatsapp: ")

    global posicao_mouse_buscador
    posicao_mouse_buscador = py.position()

    input("Selecione o arquivo inicial (boleto) ")
    
def enviar_boleto(mes, ano): 
    global auxiliador
       
    py.hotkey("f2")
    py.PAUSE = 1
    py.hotkey("ctrl","c")
    py.PAUSE = 1
    py.press("esc")
    py.hotkey("alt","tab")
    py.click(posicao_mouse_buscador[0], posicao_mouse_buscador[1])
    py.PAUSE = 1
    py.hotkey("ctrl","v")
    py.PAUSE = 1
    py.press("tab")
    py.PAUSE = 1
    py.press("enter")
    # COPIANDO ARQUIVO - INICIO
    py.hotkey("alt","tab")
    py.PAUSE = 1
    py.hotkey("ctrl","x")
    py.PAUSE = 1
    py.hotkey("alt","tab")
    py.PAUSE = 1
    py.hotkey("ctrl","v")
    py.PAUSE = 1
    py.write(f"Segue o anexo do mes de {mes} do ano {ano}")
    # ENVIANDO ARQUIVO
    py.press("enter")
    # COPIANDO ARQUIVO - FINAL
    py.PAUSE = 1
    py.hotkey("alt","tab")
    py.PAUSE = 1
    py.press("down")
    py.PAUSE = 1
    
    auxiliador = auxiliador + 1
    
# py.PAUSE = 1
solicitacoes()
escolha = input("(1) - Continuar\n(2) - Refazer operação\nDigite: ")

while(True):
    if(escolha == "1"):
        print("=========================")
        try:
            qtd_arquivos = int(input("Informe a quantidade de arquivos (também será a quantidade de contatos) "))
                        
            # nome_executador = input("Informe o nome do executador: ")
            mes_atual = input("Informe o mês referente ao pagamento: ")
            ano_atual = input("Informe o ano referente ao pagamento: ")
        except:
            print("Opção inválida, informe um número válido")
        print(f"{qtd_arquivos} serão enviados para os contatos")
        print("=========================")
        aceite = input("O Script será executado, deseja continuar?\n(1) - Sim\n(2) - Não\nDigite: ")
        if(aceite == "1"):
            py.hotkey("alt","tab")
            py.PAUSE = 1
            py.keyDown('alt')
            py.press('tab')
            py.PAUSE = 1
            py.press('tab')
            py.keyUp('alt')
            py.PAUSE = 1
            while(auxiliador < qtd_arquivos):
                enviar_boleto(mes_atual, ano_atual)
            break
        elif(escolha == "2"):
            print("Processo encerrado!")
        else:
            print("=========================")
            print("Opção inválida...")
    elif(escolha == "2"):
        solicitacoes()
        print("Posições gravadas!")
        print("=========================")
        escolha = input("Continuar - (1)\nRefazer operação - (2)\nDigite: ")
    else:
        print("=========================")
        print("Opção inválida...")
print("finalizado")


# py.moveTo(posicao_mouse_buscador[0], posicao_mouse_buscador[1])
# py.PAUSE = 2
# py.click()