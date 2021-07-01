#Contest Problem

def contests(D):
    #find  the length of the list
    l = len(D)
    #Sort the list in ascending order
    D.sort()
    #calculate number of possible difficulties i.e, value of k as per given instructions
    return (D[l/2] - D[l/2 - 1])
def main():
    N = int(raw_input())
    D = [None]*N
    for j in xrange(N):
        D[j] = int(raw_input())
    result = contests(D);
    print result
if __name__ == "__main__":
    main()
