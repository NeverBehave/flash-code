class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        op = ['(', '{', '[']
        cs = [')', '}', ']']
        
        for i in s:
            if i in op:
                stk.append(i)
            else:
                if len(stk) == 0:
                    return False
                x = stk.pop()
                if op.index(x) != cs.index(i):
                    return False
                
        if len(stk) != 0:
            return False
        
        return True