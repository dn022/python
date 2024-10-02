# Tentei algumas muitas vezes, pesquisei no w3, li, vi video e foi isso ai que saiu prof. 
# Tinha feito um outro projeto com a biblioteca curses tambem, mas depois que vi o enunciado do trabalho ai refiz.

branco = " "
token = ["X", "O"]

def criarBoard():
    board = [
        [branco, branco, branco],
        [branco, branco, branco],
        [branco, branco, branco],
    ]
    return board

def printBoard(board):
    for i in range(3):
        print("|".join(board[i]))
        if i < 2:
            print("-----")

def getInputValido(mensagem):
    while True:
        try:
            n = int(input(mensagem))
            if 1 <= n <= 3:
                return n - 1
            else:
                print("Número precisa estar entre 1 e 3")
        except ValueError:
            print("Número não válido. Por favor, insira um número inteiro.")

def verificaMovimento(board, i, j):
    return board[i][j] == branco

def fazMovimento(board, i, j, jogador):
    board[i][j] = token[jogador]

def verificaGanhador(board):
    # Linhas
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != branco:
            return board[i][0]
    
    # Colunas
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] != branco:
            return board[0][i]

    # Diagonal principal
    if board[0][0] == board[1][1] == board[2][2] != branco:
        return board[0][0]

    # Diagonal secundária
    if board[0][2] == board[1][1] == board[2][0] != branco:
        return board[0][2]

    # Verifica se há espaços disponíveis
    for i in range(3):
        for j in range(3):
            if board[i][j] == branco:
                return None  # Não há vencedor ainda, jogo continua

    return "EMPATE"

def main():
    board = criarBoard()
    jogador_atual = 0
    ganhador = None

    while ganhador is None:
        printBoard(board)
        print(f"Jogador {token[jogador_atual]}'s vez.")
        
        linha = getInputValido("Escolha a linha (1, 2, 3): ")
        coluna = getInputValido("Escolha a coluna (1, 2, 3): ")

        if verificaMovimento(board, linha, coluna):
            fazMovimento(board, linha, coluna, jogador_atual)
            ganhador = verificaGanhador(board)
            jogador_atual = 1 - jogador_atual  # Alterna entre 0 e 1
        else:
            print("Movimento inválido, tente novamente.")
    
    printBoard(board)
    if ganhador == "EMPATE":
        print("O jogo empatou!")
    else:
        print(f"Parabéns! O jogador {ganhador} ganhou!")

if __name__ == "__main__":
    main()
