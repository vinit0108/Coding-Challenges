def addAP(N,A,Q,operation):
    finallist=[] #It will contain the final list which will be returned
    for ele in range(Q):
        list1=[]
        list1=operation[ele]#contain each operation
        for i in range(1,N+1):#iterating on contents of list A
            if (i>=list1[0] and i<=list1[1]):#checking the condition L<=i<=R
                a=A[i-1]#accessing element from Array by index
                p=i-int(list1[0])+1#calculating i for B
                b=list1[2]+((p-1)*list1[3])#calculating B[i]
                A[i-1]=a+b#final value assigned to element after carrying out operation
    for i in range(N):#iterating over final array to mod 10**9 +7
        finallist.append(A[i]%((10**9)+7))
    return finallist 
T=int(input())
for _ in range(T):
    out_=[]
    N=int(input())
    A=list(map(int,input().split()))
    Q=int(input())
    operation = [list(map(int,input().split())) for i in range(Q)]
    out_ = addAP(N,A,Q,operation)
    print('  '.join(map(str,out_)))
        
