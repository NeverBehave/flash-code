class TireNode:
    def __init__(self):
        self.edge = [None] * 26
        self.word = None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.board = board
        self.words = words
        self.x_len = len(board)
        self.y_len = len(board[0])
        self.res = []
        
        self.tnode = TireNode()
        self.z = ord('z')
        
        # build tire
        for i in self.words:
            n = self.tnode
            for l in i:
                idx = self.z - ord(l)
                if n.edge[idx] == None:
                    n.edge[idx] = TireNode()
                n = n.edge[idx]
            
            n.word = i
            
              
        for x in range(self.x_len):
            for y in range(self.y_len):
                self.start_search(x, y, self.tnode)
        
        return self.res
    
    def start_search(self, x, y, tire):    
        c = self.board[x][y]
        
        if c == '#':
            return 
        
        tire = tire.edge[self.z - ord(c)]
        
        if tire == None:
            return
        
        
        if tire.word != None:
            self.res.append(tire.word)
            tire.word = None
        
        self.board[x][y] = "#"
        
        if x < self.x_len - 1:
            self.start_search(x + 1, y, tire)
        if y < self.y_len - 1:
            self.start_search(x, y + 1, tire)
        if x > 0:
            self.start_search(x - 1, y, tire)
        if y > 0:
            self.start_search(x, y - 1, tire)

        self.board[x][y] = c