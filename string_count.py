# Python3 program to rearrange a string to
# make palindrome.


def createPalindrome(x):
    y = ""
    i = 0
    j = len(x) - 1
    a = 0
    while i < j:
        if x[i] < x[j]:
            a += ord(x[j]) - ord(x[i])
            x[j] = x[i]

        else:
            a += ord(x[i]) - ord(x[j])
            x[i] = x[j]

        i = i + 1
        j = (len(x) - 1) - 1
        new = list(''.join(x))
        return new

# Driver code
if __name__ == "__main__":
    length = int(input())
    s , q = input().split()
    S = list(s)
    Q = int(q)

    L , R = map(int, input().split())
    before = S[:L]
    str = S[L:R]
    after = S[R:]

    pallindrome = createPalindrome(str)

    op = before + pallindrome + after

    print(op)





#print(length,S,Q,L,R)




"""
#print max repeating char in input string
def index_of(m,all_counts):
    ind=0
    for i in all_counts:
        if(i==m):
            return ind
        ind = ind + 1



def max_num(all_counts):
    n = all_counts[0]
    for i in all_counts:
        if(n<i):
            temp=n
            n = i
            i=temp
    return n


def count_ch(ch,str):
    num=0
    for i in str:
        if(i==ch):
            num=num+1
    return num


def find_counts(str):
    for ch in str:
        #c = str.count(ch)

        if ch not in all_ch:
            c = count_ch(ch, str)
            all_counts.append(c)
            all_ch.append(ch)


def find_element():
    #m = max(all_counts)
    m = max_num(all_counts)
    #ind = all_counts.index_of(m)
    ind = index_of(m , all_counts)
    return all_ch[ind]

#driver code
#input string
str = list(input("Enter a string :"))

all_counts = []
all_ch = []

find_counts(str)

op = find_element()
print(all_ch )
print(all_counts)
print("Maximum repeating character in input string : ",op)


"""