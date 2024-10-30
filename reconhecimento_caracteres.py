# Programa feito por Cauê Spalla Rovaron
# Programa de classificação de números
# Formatação do padrão número 1
# 400 Linhas


import tkinter as tk

# Criar janela principal
root = tk.Tk()
root.title("Reconhecimento de padrões")

# Criar frame para os botões e labels
esquerda_frame = tk.Frame(root)
esquerda_frame.pack()
direita_frame = tk.Frame(root)
direita_frame.pack(side="right")
botao_frame = tk.Frame(root)
botao_frame.pack()

# Adicionar título, nome e desenhe
titulo_label = tk.Label(esquerda_frame, text="Reconhecimento de padrões", font=("Arial", 16))
titulo_label.pack(pady=10)

nome_label = tk.Label(esquerda_frame, text="Aluno: Cauê Spalla Rovaron", font=("Arial", 14))
nome_label.pack()

desenhe_label = tk.Label(esquerda_frame, text="Desenhe caractere abaixo:", font=("Arial", 12))
desenhe_label.pack(pady=10)

# Lista de referências dos botões
botao = [[None for _ in range(3)] for _ in range(5)]

# Lista de status dos botões
sts = [[0 for _ in range(3)] for _ in range(5)]

# Criar os botões em grid
for row in range(5):
    for col in range(3):
        botao[row][col] = tk.Button(botao_frame, text=" ", width=3, height=1, bg="white",
                                      command=lambda r=row, c=col: botao_click(r, c))
        botao[row][col].grid(row=row, column=col, padx=2, pady=2)

# Criar labels para mostrar a similaridade e confiança
similaridade_label = tk.Label(direita_frame,text=f"Similaridade:", font=("Arial", 12))
similaridade_label.pack(pady=2)

confianca_label = tk.Label(direita_frame,text=f"Confiança:",  font=("Arial", 12))
confianca_label.pack(pady=2)

# Cria o rótulo para exibir o conjunto de caracteres
caracteres_label = tk.Label(direita_frame, text="Set de caracteres:\n1234567890\nABCDEF-+=,", font=("Arial", 12))
caracteres_label.pack(pady=5)

# Espaçamento
tk.Label(root, text="", height=2).pack()

# Função de clique no botão
def botao_click(row, col):
    if sts[row][col] == 0:
        botao[row][col].config(bg="black")
        sts[row][col] = 1
    else:
        botao[row][col].config(bg="white")
        sts[row][col] = 0

    valor, padrao = ler(sts)
    similaridade_label.config(text=f"Similaridade: {padrao}")
    confianca_label.config(text=f"Confiança: {round(valor,2)} %")

# Padrões de comparação e os seus maiores.
def ler(sts):
    #Linha de comparação do padrão do numero 1
    P1 = ((sts[0][1] + sts[1][1] + sts[2][1] + sts[3][1] + sts[4][1])*20
          - (sts[0][2] + sts[1][2] + sts[2][2] + sts[3][2] + sts[4][2] + sts[0][0] + sts[1][0] + sts[2][0] + sts[3][0] + sts[4][0])*10)
    #Linha de comparação do padrão do numero 2
    P2 = ((sts[0][0] + sts[0][1] + sts[0][2] + sts[1][2] + sts[2][0] + sts[2][1] + sts[2][2] + sts[3][0] + sts[4][0] + sts[4][1] + sts[4][2])
          *round(100/11, 2)- (sts[1][0] + sts[1][1] + sts[3][1] + sts[3][2])*25)
    #Linha de comparação do padrão do numero 3
    P3 = ((sts[0][0] + sts[0][1] + sts[0][2] + sts[1][2] + sts[2][1] + sts[2][2] + sts[3][2] + sts[4][0] + sts[4][1] + sts[4][2])*10
          - (sts[1][0] + sts[1][1] + sts[2][0] + sts[3][0] + sts[3][1])*20)
    #Linha de comparação do padrão do numero 4
    P4 = ((sts[0][0] + sts[0][2] + sts[1][0] + sts[1][2] + sts[2][0] + sts[2][1] + sts[2][2] + sts[3][2] + sts[4][2])*round(100/9, 2)
          - (sts[0][1] + sts[1][1] + sts[3][0] + sts[3][1] + sts[4][0] + sts[4][1])*round(100/6, 2))
    #Linha de comparação do padrão do numero 5
    P5 = ((sts[0][0] + sts[0][1] + sts[0][2] + sts[1][0] + sts[2][0] + sts[2][1] + sts[2][2] + sts[3][2] + sts[4][0] + sts[4][1] + sts[4][2])
          *round(100/11, 2) - (sts[1][1] + sts[1][2] + sts[3][0] + sts[3][1])*25)
    #Linha de comparação do padrão do numero 6
    P6 = (sts[0][0] + sts[0][1] + sts[0][2] + sts[1][0] + sts[2][0] + sts[2][1] + sts[2][2] + sts[3][0] + sts[3][2] + sts[4][0] + sts[4][1]
          + sts[4][2])*round(100/12, 2) - (sts[3][1] + sts[1][1] + sts[1][2])*round(100/3, 2)
    #Linha de comparação do padrão do numero 7
    P7 = ((sts[0][0] + sts[0][1] + sts[0][2] + sts[1][2] + sts[2][2] + sts[3][2] + sts[4][2])*round(100/7, 2)
          - (sts[1][0] + sts[1][1] + sts[2][0] + sts[2][1] + sts[3][0] + sts[3][1] + sts[4][0] + sts[4][1])*round(100/8, 2))
    #Linha de comparação do padrão do numero 8
    P8 = (sts[0][0] + sts[1][0] + sts[2][0] + sts[3][0] + sts[4][0] + sts[1][2] + sts[2][2] + sts[3][2] + sts[4][2] + sts[0][1]
          + sts[2][1] + sts[4][1] + sts[0][2])*round(100/13, 2) - (sts[3][1] + sts[1][1])*50
    #Linha de comparação do padrão do numero 9
    P9 = (sts[0][0] + sts[1][0] + sts[2][0] + sts[4][0] + sts[1][2] + sts[2][2] + sts[3][2] + sts[4][2] + sts[0][1]+ sts[2][1]
          + sts[4][1] + sts[0][2])*round(100/12, 2) - (sts[3][1] + sts[1][1] + sts[3][0])*round(100/3, 2)
    #Linha de comparação do padrão do numero 0
    P0 = (sts[0][0] + sts[1][0] + sts[2][0] + sts[3][0] + sts[4][0] + sts[1][2] + sts[2][2] + sts[3][2] + sts[4][2] + sts[0][1]
          + sts[4][1] + sts[0][2])*round(100/12, 2) - (sts[3][1] + sts[1][1] + sts[2][1])*round(100/3, 2)

    #Linha de comparação do padrão da letra a
    Pa = ((sts[0][1] + sts[1][0] + sts[1][2] + sts[2][0] + sts[2][1] + sts[2][2] + sts[3][0] + sts[3][2] + sts[4][0] + sts[4][2])*round(100/10, 2)
          - (sts[0][0] + sts[0][2] + sts[1][1] + sts[3][1] + sts[4][1])*round(100/5, 2))
    #Linha de comparação do padrão da letra b
    Pb = ((sts[0][0] + sts[0][1] + sts[1][0] + sts[1][2] + sts[2][0] + sts[2][1] + sts[3][0] + sts[3][2] + sts[4][0] + sts[4][1])*round(100/10, 2)
          - (sts[0][2] + sts[1][1] + sts[2][2] + sts[3][1] + sts[4][2])*round(100/5, 2))
    #Linha de comparação do padrão da letra c
    Pc = ((sts[0][0] + sts[0][1] + sts[0][2] + sts[1][0] + sts[2][0] + sts[3][0] + sts[4][0] + sts[4][1] + sts[4][2])*round(100/9, 2)
          - (   sts[1][1] + sts[1][2] + sts[2][1] + sts[2][2] + sts[3][1] + sts[3][2])*round(100/6, 2))
    #Linha de comparação do padrão da letra d
    Pd = ((sts[0][0] + sts[0][1] + sts[1][0] + sts[2][0] + sts[3][0] + sts[4][0] + sts[4][1] + sts[3][2] + sts[2][2] + sts[1][2])*round(100/10, 2)
          - (sts[0][2] + sts[1][1] + sts[2][1] + sts[3][1] + sts[4][2])*round(100/5, 2))
    # Linha de comparação do padrão da letra e
    Pe = ((sts[0][0] + sts[0][1] + sts[0][2] + sts[1][0] + sts[2][0] + sts[2][1] + sts[3][0] + sts[4][2] + sts[4][1] + sts[4][0])*round(100/10, 2)
          - (sts[1][2] + sts[1][1] + sts[2][2] + sts[3][1] + sts[3][2])*round(100/5, 2))
    #Linha de comparação do padrão da letra f
    Pf = ((sts[0][0]  + sts[0][1] + sts[0][2] + sts[1][0] + sts[2][1] + sts[2][0] + sts[3][0] + sts[4][0])*round(100/8, 2)
          - (sts[1][2] + sts[1][1] + sts[2][2] + sts[3][1] + sts[3][2] + sts[4][1] + sts[4][2])*round(100/7, 2))
    #Linha de comparação do padrão do símbolo -
    Pminus = ((sts[2][0] + sts[2][1] + sts[2][2])*round(100/3, 2)
              - (sts[0][0] + sts[0][1] + sts[0][2] + sts[1][2] + sts[1][1] + sts[1][0] + sts[3][0] + sts[3][1] + sts[3][2] + sts[4][0] + sts[4][1] + sts[4][2])
              *round(100/12, 2))
    #Linha de comparação do padrão do símbolo +
    Pplus = ((sts[2][0] + sts[2][1] + sts[2][2] + sts[1][1] + sts[3][1])*round(100/5, 2)
             - (sts[0][0] + sts[0][1] + sts[0][2] + sts[1][2] + sts[1][0] + sts[3][0] + sts[3][2] + sts[4][0] + sts[4][1] + sts[4][2])*round(100/10, 2))
    #Linha de comparação do padrão do símbolo =
    Pequals = ((sts[1][0] + sts[1][1] + sts[1][2] + sts[3][0] + sts[3][1] + sts[3][2])*round(100/6, 2)
               - (sts[0][0] + sts[0][1] + sts[0][2] + sts[2][0] + sts[2][1] + sts[2][2] + sts[4][0] + sts[4][1] + sts[4][2])*round(100/9, 2))
    #Linha de comparação do padrão do símbolo ,
    Pcomma = ((sts[3][1] + sts[4][1])*round(100/2, 2)
              -(sts[0][0] + sts[0][1] + sts[0][2] + sts[1][0] + sts[1][1] + sts[1][2] +
                sts[2][0] + sts[2][1] + sts[2][2] + sts[3][0] + sts[3][2] + sts[4][0] + sts[4][2])*round(100/13, 2))
    valores = {
        '1': P1,
        '2': P2,
        '3': P3,
        '4': P4,
        '5': P5,
        '6': P6,
        '7': P7,
        '8': P8,
        '9': P9,
        '0': P0,
        'A': Pa,
        'B': Pb,
        'C': Pc,
        'D': Pd,
        'E': Pe,
        'F': Pf,
        '-': Pminus,
        '+': Pplus,
        '=': Pequals,
        ',': Pcomma,
    }
    # Encontre o maior valor e o respectivo padrão
    maior_padrao = max(valores, key=valores.get)
    maior_valor = valores[maior_padrao]

    return maior_valor, maior_padrao

# Executa o loop principal
root.mainloop()