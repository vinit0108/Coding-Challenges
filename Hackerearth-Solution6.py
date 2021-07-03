n = int(input())

a=[]

b=[]

maxAB = -1

com = []

for i in range(n):

  a.append(int(input()))

for i in range(n):

  b.append(int(input()))

  com.append((a[i],b[i]))

maxt = com[0][0]+com[0][1]

com.sort(key = lambda x: x[1], reverse = True)

time_of_comp = []

time_of_comp.append(com[0][0])

for i in range(1,n):

  time_of_comp.append(time_of_comp[i-1]+com[i][0])

  maxt = max(maxt, time_of_comp[i]+com[i][1])

print('Time taken is : ', maxt)
