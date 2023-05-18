import random
import os
from termcolor import colored

# Cabeçalho de boas vindas
def bem_vindo_dados():
    os.system("cls")
    print("")
    print(colored("BEM VINDO A CORRIDA DE DADOS", "blue", attrs=["bold"]), end="\n\n")
    menu_escolha_dados()
    
# Menu de escolha principal
def menu_escolha_dados(): 
    print("[1] Começar a jogar")
    print("[2] Como o jogo funciona")
    escolha_dados()
    
# Verificação da escolha 
def escolha_dados():
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
        menu_escolha_dados()
  
# Manual de funcionamento do jogo      
def funcionamento():
    os.system("cls")
    print(colored("""O jogo se baseia em sorte, nele você irá rolar uma dado de 6 lados e escolher um lado, se o dado cair no lado escolhido vc ganha, se não, perde tudo.
Lembresse de não apostar tudo que tem, visto que é um jogo de sorte""", attrs=["bold"]), end="\n\n")
    input(colored("Aperte ENTER para voltar ao menu principal", "red", attrs=["bold"]))
    os.system("cls")
    menu_escolha_dados()
    
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
    
def tem_dinheiro(saldo):
    aposta = float(input("Insira o valor que deseja apostar: "))
    if(aposta > saldo):
        os.system("cls")
        print("Você não tem tanto dinheiro assim, insira um valor menor ou igual ao seu saldo atual de", saldo, "reais")
        tem_dinheiro(saldo)
    else:
        jogo_dados(saldo, aposta)
    
def jogo_dados(saldo, aposta):
    os.system("cls")
    chute = int(input("Chute um lado [1 a 6]: "))
    
    lados = round(random.randrange(1, 7))
    
    if(chute == lados):
        saldo = saldo + aposta
        print("Você acertou!!! Seu saldo agora é", saldo, "reais")
        continuar_jogo(saldo, aposta)
    else:
        saldo = saldo - aposta
        print("Você errou!!! O dado caiu no lado", lados) 
        print("Seu saldo agora é", saldo, "reais")
        continuar_jogo(saldo, aposta)

def continuar_jogo(saldo):
    escolha_continuar = input("Deseja continuar jogando? ")
    escolha_continuar = escolha_continuar.lower()
    if(escolha_continuar == 'sim' and saldo == 0):
        os.system("cls")
        print(colored("Você não tem dinheiro suficiente para continuar jogando"))
        escolha_rejogar = input("Deseja começar novamente?")
        if(escolha_rejogar == 'sim'):
            os.system("cls")
            bem_vindo_dados()
        elif(escolha_rejogar == "nao"):
            os.system("cls")
            print("Obrigado por jogar")
    elif(escolha_continuar == 'sim'):
        os.system("cls")
        tem_dinheiro(saldo)
    elif(escolha_continuar == "nao"):
        os.system("cls")
        print("Obrigado por jogar")

bem_vindo_dados()