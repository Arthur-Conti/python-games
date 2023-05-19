from termcolor import colored
import os
import random
import json
import bem_vindo

# Cabeçalho de boas vindas
def bem_vindo_roleta():
    os.system("cls")
    print("")
    print(colored("BEM VINDO A ROLETA", "blue", attrs=["bold"]), end="\n\n")
    menu_escolha_roleta()
    
# Menu de escolha principal
def menu_escolha_roleta(): 
    print("[1] Começar a jogar")
    print("[2] Como o jogo funciona")
    escolha_roleta()
    
# Verificação da escolha 
def escolha_roleta():
    escolha_1 = int(input("Opção: "))
    
    if(escolha_1 == 1):
        os.system("cls")
        print(colored("Vamos começar!", "red", attrs=["bold"]))
        cadastro()
    elif(escolha_1 == 2):
        funcionamento()
    else:
        os.system("cls")
        print(colored("Favor escolher uma opção valida!", "red", attrs=["bold"]))
        menu_escolha_roleta()
  
# Manual de funcionamento do jogo      
def funcionamento():
    os.system("cls")
    print(colored("""O jogo se baseia em sorte, nele você irá rolar uma roleta, o número que parar define o premio, podendo ser 
algo bom ou ruim , lembresse de não apostar tudo que tem, visto que é um jogo de sorte""", attrs=["bold"]), end="\n\n")
    input(colored("Aperte ENTER para voltar ao menu principal", "red", attrs=["bold"]))
    os.system("cls")
    menu_escolha_roleta()
    
# Cadostro do usuário
def cadastro():
    nome = input("Qual o seu nome? ")
    saldo = float(input("Quanto deseja depositar na sua carteira virtual? "))
    if(saldo < 0):
        os.system("cls")
        print(colored("Favor inserir um valor de saldo maior que 0", "red", attrs=["bold"]))
        cadastro()
    else:
        tem_dinheiro(saldo)
    #inserir_no_json(nome, saldo)
    
# Verifica se o jogador não está apostando um valor maior do que ele tem
def tem_dinheiro(saldo):
    aposta = float(input("Insira o valor que deseja apostar: "))
    if(aposta > saldo):
        os.system("cls")
        print("Você não tem tanto dinheiro assim, insira um valor menor ou igual ao seu saldo atual de", saldo, "reais")
        tem_dinheiro(saldo)
    else:
        jogo_roleta(saldo, aposta)
        
def premios_roleta():
    os.system("cls")
    print("Opções da roleta: ")
    print("1 - Perdeu tudo")
    print("2 - Ganha o dobro do apostado")
    print("3 - Perde metade do apostado")
    print("4 - Ganha 10 mil")
    print("5 - Ganha 10 vezes mais que o apostado")
    print("")
    
def jogo_roleta(saldo, aposta):
    premios_roleta()
    
    roleta = round(random.randrange(1, 6))
    
    if(roleta == 4 or roleta == 5 or roleta == 2):
        roleta = round(random.randrange(1, 6))
    else:
        pass
    
    if(roleta == 1):
        saldo = saldo - aposta
        print("A roleta caiu no 1, você perdeu tudo que foi apostado")
        print(f"Seu saldo agora é {saldo}")
    elif(roleta == 2):
        saldo = saldo + (aposta * 2)
        print("A roleta caiu no 2, você ganhou o dobro do que foi apostado")
        print(f"Seu saldo agora é {saldo}")
    elif(roleta == 3):
        aposta = aposta / 2
        saldo = saldo - aposta
        print("A roleta caiu no 3, você perdeu metade do que foi apostado")
        print(f"Seu saldo agora é {saldo}")
    elif(roleta == 4):
        saldo = saldo + 10000
        print("A roleta caiu no 4, você ganhou 10 mil reais")
        print(f"Seu saldo agora é {saldo}")
    elif(roleta == 5):
        aposta = aposta + (aposta * 10) 
        saldo = saldo + aposta
        print("A roleta caiu no 5, você ganhou 10 vezes mais do que foi apostado")
        print(f"Seu saldo agora é {saldo}")
    
    continuar_jogo(saldo)

def escolha_outro_jogo():
    escolha = input("Deseja escolher outro jogo? ")
    escolha = escolha.lower()
    
    if(escolha == "sim"):
        bem_vindo.bem_vindo()
    elif(escolha == "nao"):
        os.system("cls")
        print("Obrigado por jogar")
    else:
        print("Opção invalida, por favor responda com sim ou nao")
        escolha_outro_jogo()
        
# Oferece a opção de continuar jogando ao jogador
def continuar_jogo(saldo):
    escolha_continuar = input("Deseja continuar jogando? ")
    escolha_continuar = escolha_continuar.lower()
    if(escolha_continuar == 'sim' and saldo == 0):
        os.system("cls")
        print(colored("Você não tem dinheiro suficiente para continuar jogando"))
        escolha_rejogar = input("Deseja começar novamente?")
        if(escolha_rejogar == 'sim'):
            os.system("cls")
            bem_vindo_roleta()
        elif(escolha_rejogar == "nao"):
            os.system("cls")
            print("Obrigado por jogar")
    elif(escolha_continuar == 'sim'):
        os.system("cls")
        tem_dinheiro(saldo)
    elif(escolha_continuar == "nao"):
        os.system("cls")
        print("Obrigado por jogar")
        escolha_outro_jogo()