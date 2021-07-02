def check_string(n,k,s):
    for i in range(k,n):
        if(s[i]!=s[abs(k-i)]):
            return 0
    return 1

def find_character(ind,k):
    while(ind<n):
        if(s[ind]!='?'):
            return s[ind]
        else:
            ind+=k
    return -1

def solve(n,k,s):
    for i in range(n):
        if(s[i]=='?'):
            char=find_character(i%k,k)
            if(char==-1):
                s[i]='a'
            else:
                s[i]=char
    if(check_string(n,k,s)):
        return ''.join(s)
    return -1



if __name__=='__main__':
    for t in range(int(input())):
        n,k=map(int,input().split())
        s=list(input())
        ans=solve(n,k,s)
        print(ans)
'''
first we are taking inputs , then we call function solve() to get the ans
Let's talk about some functions

solve()
this fucntion runs a loop , and whenever we encounter with a character ? , it means we have to find the replacement for this character , and we know s[i]==s[i+k] , using this property it is very easy to find the replacement
let's say str = "abcdea????abcde" and k=5
at index = 6 we have s[6]=? , thus find replacement for it , ind=6 , either go back or go forward in the search of replacement , what i did is i started the search from the begining
how ? , ind=6 , ind%k == 1 , so index-6 family is - 1,6,11,16,21,..... , so we start from the 1st memeber if(1st member != ?) return it's value , else look for another member and return it's value , if it is not ?

BUT, if all the member are ? , then we should assign 'A' to all of them , so that resulting string becomes lexographically smaller

Check_string()
this function checks whether this string is correct or not , whether it is possible to fill thse missing place in the string such that resulting string has period K
to check this , see if every s[i] == s[i+k] or not , if they are equal then it's okay , else return -1 .
'''
