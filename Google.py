'''a_list = []
n = int(input())
for k in range(1,n+1):
    sum = 0
    #print(k)
    for j in range(1,k):
        #print(j)
        if (k % j) == 0:
            sum += j
    if sum == k:
        a_list.append(k)
print(a_list)'''

'''S = [1, 3, 4, 8, 13, 17, 20]
a_dict = {}
index = 1
min = S[-1]
for k in S:
    if k != 20:
        j = S[index]
        if min > j-k:
            min = j-k
        a_dict[j-k] = (k, j)
    index += 1
print(a_dict)
if min in a_dict:
    print(a_dict[min])'''

def spair(S):
    dict = {}
    for (x, y) in zip(S[:-1], S[1:]):
        if not dict.get(y-x):
            dict[y-x] = [(x,y)]
        else:
            dict[y-x] = dict[y-x] + [(x,y)]

    return dict[min(dict.keys())]


S = [1, 3, 4, 8, 13, 17, 20]
print(S[:-1])
print(S[:1])
#S = [1,2,4,5,8,15,19]
#print(spair(S))