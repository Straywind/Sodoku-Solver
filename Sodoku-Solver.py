ROWS = 9
COLUMNS = 9
BLOCK_LEN = 3
BLOCK_WID = 3

grid = [[0, 0, 7, 0, 1, 0, 0, 3, 0],
        [0, 0, 5, 0, 0, 0, 0, 0, 6],
        [0, 6, 0, 7, 0, 0, 0, 9, 0],
        [0, 0, 0, 3, 0, 0, 0, 7, 2],
        [0, 0, 4, 9, 0, 2, 1, 0, 0],
        [7, 3, 0, 0, 0, 4, 0, 0, 0],
        [0, 9, 0, 0, 0, 7, 0, 2, 0],
        [1, 0, 0, 0, 0, 0, 3, 0, 0],
        [0, 4, 0, 0, 6, 0, 9, 0, 0]]

class Sodoku:
    checked_spots = set()
    
    def __init__(self):
        pass
    
    def display(self):
        for num in grid:
            print (*num, sep=' ')
        print('\n')

    def gameComplete(self):
        """Checks if the board is complete"""
        for num in grid:
            if num == 0:
                return True
        return False

    def num_viable(self, row, col, number):
        """Checks if given number is acceptable in given pos"""
        
        for x in range(ROWS):
            if grid[x][col] == number:
                return False

        for x in range(ROWS):
            if grid[row][x] == number:
                return False

        block_top_left_row = int((row/3)//1)
        block_top_left_column = int((col/3)//1)

        for x in range(3):
            for y in range(3):
               if grid[(block_top_left_row * BLOCK_LEN) + x][(block_top_left_column * BLOCK_WID) + y] == number:
                    return False

        return True


    def check_all_spots(self):
        """orders every spot to be assigned a viable number"""
        for x in range(ROWS):
            for y in range(COLUMNS):
                if grid[x][y] == 0:
                    for num in range(1, 10):
                        if self.num_viable(x, y, num):
                            grid[x][y] = num
                            self.check_all_spots()
                            grid[x][y] = 0
                    return
        self.display()
            
sodoku_game = Sodoku()
sodoku_game.check_all_spots()
