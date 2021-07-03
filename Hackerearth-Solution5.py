def max_value(n, k):
    ans = int(n)%k
    for i in range(len(n)-1, -1, -1):
        s = ''
        for j in range(len(n)):
            if i != j:
                s += n[j]
        if s != None:
            res = int(s)%k
            if res > ans:
                ans = res
    return ans

def main():
    T = int(input("No.of test cases : "))

    for i in range(T):
        n = input("Enter the number : ")
        k = int(input("Enter the divisor : "))

        out_ = max_value(n, k)
        print(out_)

if __name__ == "__main__":
    main()
