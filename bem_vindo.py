from termcolor import colored
import os
import corrida_carros
import dados
import roleta

def bem_vindo():
    os.system("cls")
    print(colored("BEM VINDO A CADA DE APOSTAS", "blue", attrs=["bold"]), end="\n\n")
    print(colored("Escolha onde quer apostar:", attrs=["bold"]), end="\n\n")
    menu_jogos()
    
def menu_jogos():
    print("[1] Corrida de carros")
    print("[2] Jogo de dados")
    print("[3] Roleta", end="\n\n")
    escolha_de_jogos()

def escolha_de_jogos():
    escolha_jogo = int(input(colored("Onde quer apostar? ", "red", attrs=["bold"])))

    if(escolha_jogo == 1):
        os.system("cls")
        print("Apostando nos carros")
        corrida_carros.bem_vindo_carros()
    elif(escolha_jogo == 2):
        os.system("cls")
        print("Apostando nos dados")
        dados.bem_vindo_dados()
    elif(escolha_jogo == 3):
        os.system("cls")
        print("Apostando na roleta")
        roleta.bem_vindo_roleta()
    else:
        os.system("cls")
        print("Favor escolher uma opção valida!")
        menu_jogos()

if(__name__ == "__main__"):
    bem_vindo()