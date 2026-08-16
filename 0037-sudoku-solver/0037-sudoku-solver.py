class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        rows = [set() for i in range(9)]
        cols = [set() for i in range(9)]
        boxes = [set() for i in range(9)]
        empty = []

        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val==".":
                    empty.append((i,j))
                else:
                    rows[i].add(val)
                    cols[j].add(val)
                    boxes[3*(i//3)+(j//3)].add(val)
        
        def backtrack(index):
            if index==len(empty): return True

            i,j = empty[index]
            box_idx = 3*(i//3)+(j//3)

            for digit in '123456789':
                if digit not in rows[i] and digit not in cols[j] and digit not in boxes[box_idx]:
                    rows[i].add(digit)
                    cols[j].add(digit)
                    boxes[box_idx].add(digit)
                    board[i][j] = digit

                    if backtrack(index+1):
                        return True
                    
                    rows[i].remove(digit)
                    cols[j].remove(digit)
                    boxes[box_idx].remove(digit)
                    board[i][j] = "."

            return False
        backtrack(0)

                