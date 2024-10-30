#Programinha feito por: Cauê Spalla Rovaron


#Perguntar se quer saber a produção ou encolhimento.

def Menu():
    kghprod = 2 * 0.290 * 60  # unidade kg/h produzida
    escolha = input("Deseja saber a produção (digite P), a regulagem (digite R) ou sair (digite S)?").upper()

    if escolha == "P":
        print("Você escolheu saber a produção.")
        Menu_producao(kghprod)
    elif escolha == "R":
        print("Você escolheu saber a regulagem.")
        Menu_regulagem(kghprod)
    elif escolha == "S":
        return None
    else:
        print("Opção inválida. Por favor, digite P ou R.")
        Menu()

def Menu_producao(kghprod):
    try:
        v2 = float(input("Digite a velocidade de saida (m/min): "))
    except ValueError:
        print("Erro: entrada inválida. Por favor, digite um número.")
        Menu_producao(kghprod)
    print(f"A produção é de = {Eq_producao(v2,kghprod): .2F} kg/h")
    Menu()

def Menu_regulagem(kghprod):
    try:
        producao_alvo = float(input("Digite a produção (kg/h): "))
    except ValueError:
        print("Erro: entrada inválida. Por favor, digite um número.")
        Menu_regulagem(kghprod)
    try:
        encolhimento_alvo = float(input("Digite o encolhimento (%): "))
    except ValueError:
        print("Erro: entrada inválida. Por favor, digite um número.")
        Menu_regulagem(kghprod)
    print(f"A velocidade de V2 é : {Eq_v2(producao_alvo, kghprod): .2F} \n")
    print(f"A velocidade de V1 é : {Eq_v1(Eq_v2(producao_alvo, kghprod), encolhimento_alvo): .2F} ")
    Menu()

def Eq_v2(producao_alvo, kghprod):
    return producao_alvo / kghprod

def Eq_v1(v2, encolhimento_alvo):
    return v2 /( 1 -  0.01 * encolhimento_alvo)

def Eq_producao(v2, kghprod):
    return v2 * kghprod

Menu()