# Uses python3

import sys

def optimal_sequence(n):
    
    def backtrack(actions, n):
    
        q = n
        sequence = [n]

        def f1(x):
            return x-1
        def f2(x):
            return x//2
        def f3(x):
            return x//3

        func_dict = {0: f1, 1: f2, 2:f3}

        while q != 1:
            current_action = actions[q]   
            q = func_dict[current_action](q)  
            sequence.append(q)
        
        
        return(sequence[::-1])
    
    S = [0]*int(n+1) # stores the minimum number of ops
    S[0] = 0
    S[1] = 0
    sequence = [0, 0]
    for i in range(2, n+1):
        
        if not i % 6:
            poss = [S[i-1],S[i//2],S[i//3]]
            actions = [0, 1, 2]
            minmove = min(poss)
            S[i] = 1+minmove
            index = poss.index(minmove)
            sequence.append(actions[index])
            
            
        elif not i % 3:
            poss = [S[i-1],S[i//3]]
            actions = [0, 2]
            minmove = min(poss)
            S[i] = 1+minmove
            index = poss.index(minmove)
            sequence.append(actions[index])           
            
        elif not i % 2:
            poss = [S[i-1],S[i//2]]
            actions = [0, 1]
            minmove = min(poss)
            S[i] = 1+minmove
            index = poss.index(minmove)
            sequence.append(actions[index])
            
        else:
            poss = [S[i-1]]
            actions = [0]
            minmove = S[i-1]
            S[i] = 1+minmove 
            index = poss.index(minmove)
            sequence.append(actions[index])
            

    return(backtrack(sequence,n))

input = sys.stdin.read()
n = int(input)
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')