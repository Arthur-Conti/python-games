from termcolor import colored
import os
import random
import json
import bem_vindo

# Cabeçalho de boas vindas
def bem_vindo_carros():
    os.system("cls")
    print("")
    print(colored("BEM VINDO A CORRIDA DE CARROS", "blue", attrs=["bold"]), end="\n\n")
    menu_escolha_carros()
    
# Menu de escolha principal
def menu_escolha_carros(): 
    print("[1] Começar a jogar")
    print("[2] Como o jogo funciona")
    escolha_carros()
    
# Verificação da escolha 
def escolha_carros():
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
        menu_escolha_carros()
  
# Manual de funcionamento do jogo      
def funcionamento():
    os.system("cls")
    print(colored("""O jogo se baseia em sorte, nele você irá correr contra outros dois carros quem tiver a maior velocidade ganha, lembresse de não apostar 
tudo que tem, visto que é um jogo de sorte""", attrs=["bold"]), end="\n\n")
    input(colored("Aperte ENTER para voltar ao menu principal", "red", attrs=["bold"]))
    os.system("cls")
    menu_escolha_carros()
    
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
        jogo_carros(saldo, aposta)
    
# Define velocidade aleatoria para cada carro e valida vencedor
def jogo_carros(saldo, aposta):
    velocidade_jogador = round(random.randrange(1, 101))
    velocidade1 = round(random.randrange(1, 101))
    velocidade2 = round(random.randrange(1, 101))
    
    if(velocidade_jogador > velocidade1 and velocidade_jogador > velocidade2):
        aposta = aposta + (aposta * 2)
        saldo = saldo + aposta
        os.system("cls")
        print("Você venceu!!!")
        print(f"O valor do seu saldo agora é: {saldo}")
        print(f"A velocidade do seu carro era {velocidade_jogador} km/h, a do segundo carro era {velocidade1} km/h, e a do terceiro carro era {velocidade2} km/h")
        continuar_jogo(saldo)
    else:
        os.system("cls")
        saldo = saldo - aposta
        print("Você perdeu :(")
        print(f"O valor do seu saldo agora é: {saldo}")
        print(f"A velocidade do seu carro era {velocidade_jogador} km/h, a do segundo carro era {velocidade1} km/h, e a do terceiro carro era {velocidade2} km/h")
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
            bem_vindo_carros()
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
           
#def inserir_no_json(nome, saldo):
#    dif_dados = {"nome": nome, "saldo": saldo}
    