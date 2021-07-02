The Code for the problem is given below.

def solve(Q, query):
    max_length = (max(max(query)))
    l=[]
    c = 1
    output = []

    # Generating Series Here
    while len(l)!= max_length:
        sr = c**(1/2)
        if (int(sr*sr) == c):
            t = int(2*(c**(1/2)))
        else:
            pass
        for k in range(t):
            l.append(c)
            if len(l) == max_length:
                break
        c = c + 1

    # Finding the unique number here    
    for i in query:
        cut_l = l[i[0]-1:i[1]]
        number = len(set(cut_l))
        output.append(number)
    
    return output

        
            
Q = int(input())
query = [list(map(int,input().split())) for i in range(Q)]
out_ = solve(Q, query)
print(' '.join(map(str,out_)))
