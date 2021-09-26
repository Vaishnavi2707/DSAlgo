
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
            dic = {ch : c} 


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
for i in range(len(all_ch)):
    print(all_ch[i],end="")
    print(all_counts[i],end="")

print("Maximum repeating character in input string : ",op)



