from typing import List, Optional, Tuple

class Solution:
    def __init__(self) -> None:
        self._row_used:List[List[bool]] = [{i:False for i in range(1,10)} for _ in range(9)]
        self._column_used:List[List[bool]] = [{i:False for i in range(1,10)} for _ in range(9)]
        self._block_used:List[List[bool]] = [{i:False for i in range(1,10)} for _ in range(9)]
        self.find = False

    def _coordinate_to_block(self, x:int, y:int):
        return int(x/3) * 3 + int(y/3)

    def _find_next_coordinate(self, board:List[List[int]], start_x:int, start_y:int)->Optional[Tuple[int,int]]:
        for y in range(start_y, 9):
            if board[start_x][y] == -1:
                return (start_x, y)
        
        for x in range(start_x + 1, 9):
            for y in range(9):
                if board[x][y] == -1:
                    return (x, y)
        
        return None

    def _search(self, board:List[List[int]], x:int, y:int):
        block = self._coordinate_to_block(x,y)
        for candidate in range(1, 10):
            if not self._row_used[x][candidate] and not self._column_used[y][candidate] and not self._block_used[block][candidate]:
                board[x][y] = candidate
                self._row_used[x][candidate] = True
                self._column_used[y][candidate] = True
                self._block_used[block][candidate] = True
                next_coordinate = self._find_next_coordinate(board, x, y)
                # print('Place {}'.format(next_coordinate))
                if next_coordinate is None:
                    self.find = True
                    return
                else:
                    self._search(board, next_coordinate[0], next_coordinate[1])
                    if self.find:
                        return
                    board[x][y] = -1
                    self._row_used[x][candidate] = False
                    self._column_used[y][candidate] = False
                    self._block_used[block][candidate] = False



    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        new_board = [list(map(lambda x : int(x) if x != '.' else -1 , row)) for row in board]
        for row in range(9):
            for column in range(9):
                if new_board[row][column] != -1:
                    val = new_board[row][column]
                    self._row_used[row][val] = True
                    self._column_used[column][val] = True
                    self._block_used[self._coordinate_to_block(row, column)][val] = True
        
        coordinate = self._find_next_coordinate(new_board, 0, 0)
        # print('Place {}'.format(coordinate))
        if coordinate is not None:
            self._search(new_board, coordinate[0], coordinate[1])
        else:
            return

        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    board[i][j] = str(new_board[i][j])


solution = Solution()
board = [
["5","3",".",".","7",".",".",".","."],
["6",".",".","1","9","5",".",".","."],
[".","9","8",".",".",".",".","6","."],
["8",".",".",".","6",".",".",".","3"],
["4",".",".","8",".","3",".",".","1"],
["7",".",".",".","2",".",".",".","6"],
[".","6",".",".",".",".","2","8","."],
[".",".",".","4","1","9",".",".","5"],
[".",".",".",".","8",".",".","7","9"]
]

solution.solveSudoku(board)

for row in board:
    print(row)


