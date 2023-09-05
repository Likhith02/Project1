import numpy as np

class GameOfLife:
    def gameOfLife(self, board):
        p, q = len(board), len(board[0])
        xp = [1, 1, 0, -1, -1, -1, 0, 1]
        xq = [0, 1, 1, 1, 0, -1, -1, -1]
        
        def directions(x, y, A, B):
            return 0 <= x < A and 0 <= y < B
        
        for i in range(p):
            for j in range(q):
                liveCounts = 0
                for r in range(8):
                    if directions(i + xp[r], j + xq[r], p, q) and abs(board[i + xp[r]][j + xq[r]]) == 1:
                        liveCounts += 1
                
                if board[i][j] == 0 and (liveCounts == 3 or liveCounts == 2):
                    board[i][j] = 2
                if board[i][j] == 1 and (liveCounts < 2 or liveCounts > 3):
                    board[i][j] = -1
        
        for i in range(p):
            for j in range(q):
                board[i][j] = 1 if board[i][j] > 0 else 0
        
        return board

    @staticmethod
    def display(board):
        for row in board:
            print(" | ".join(map(str, row)))
            print()

def main():
    rows = int(input("Enter the number of rows: "))
    columns = int(input("Enter the number of columns: "))
    generations = int(input("Enter the number of generations: "))  # Adjust the number of generations

    board = np.random.randint(2, size=(rows, columns))
    
    game = GameOfLife()
    stage = 0

    print(f"Generation: {stage}")
    game.display(board)
    
    while stage < generations:
        temp = board.copy()
        stage += 1
        print(f"Generation: {stage}")
        finalarr = game.gameOfLife(board)
        
        if np.array_equal(finalarr, temp):
            game.display(board)
            break
        else:
            board = finalarr.copy()
            game.display(finalarr)

if __name__ == "__main__":
    main()
