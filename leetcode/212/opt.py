class TireNode:
    def __init__(self):
        self.edge = dict()
        self.word = None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.board = board
        self.words = words
        self.x_len = len(board)
        self.y_len = len(board[0])
        self.res = []
        
        self.tnode = TireNode()

        # build tire
        for i in self.words:
            n = self.tnode
            for l in i:
                if n.edge.get(l) == None:
                    n.edge[l] = TireNode()
                n = n.edge[l]
            
            n.word = i
            
              
        for x in range(self.x_len):
            for y in range(self.y_len):
                self.start_search(x, y, self.tnode)
        
        return self.res
    
    def start_search(self, x, y, tire):    
        c = self.board[x][y]
        
        if c == '#':
            return 
        
        t = tire
        tire = tire.edge.get(c)
        
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
        
        # Remove node from parent if empty
        if tire.edge == {}:
            t.edge[c] = None