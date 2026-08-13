class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        
        rows,cols = len(board),len(board[0])
        l = len(word)

        def check(i,j,idx):
            if idx==l:
                return True

            if (i < 0 or i >= rows or
                j < 0 or j >= cols or
                board[i][j] != word[idx]):
                return False

            temp_val = board[i][j]
            board[i][j] = '-'
            
            if check(i+1,j,idx+1) or check(i,j+1,idx+1) or check(i-1,j,idx+1) or check(i,j-1,idx+1):
                board[i][j] = temp_val
                return True

            board[i][j] = temp_val
            return False


        for i in range(rows):
            for j in range(cols):
                if check(i,j,0):
                    return True
        return False


