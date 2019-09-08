# coding=-utf8

class Solution(object):
    def numRookCaptures(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        
        site = {
            # 'roock': [], # 白色车 R
            # 'bishop': [], # 白色象 B
            # 'pawn': [] # 黑色卒 p

        }
        roock_site = []
        board_len = len(board)
        for row_index, row in enumerate(board):
            for col_index, item in enumerate(row):
                save_string = ','.join([row_index, col_index])
                if item == 'R':
                    roock_site = [row_index, col_index]
                elif item == 'B':
                    site[save_string] = 'B'
                elif item == 'p':
                    site[save_string] = 'p'

        if len(roock_site) > 0:
            row = roock_site[0]
            col = roock_site[1]
            # 找行
            

            # 找列

        
                
           
if __name__ == '__main__':
    a = [[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","R",".",".",".","p"],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]
    b = Solution()
    print(b.numRookCaptures(a))
    