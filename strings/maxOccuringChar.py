
test_str = "vaishnavi"

print ("The original string is : " + test_str)

all_freq = {}
for i in test_str:
	if i in all_freq:
		all_freq[i] += 1
	else:
		all_freq[i] = 1

max1 = 0
r = ' '
for i in all_freq:
    temp = all_freq[i]
    if(temp>max1):
        max1 = temp
        r = i

print ("The maximum of all characters in %s is : %c"  %(test_str , r))
