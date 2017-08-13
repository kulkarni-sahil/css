pt = input("enter pt : ")
#print (pt)
key = input("enter key :")
#print (key)
lenkey = len(key)
# print (lenkey)
mod = len(pt)%lenkey
#print(mod)
fillersToBeAdded = lenkey-mod
ptnew  = pt + 'x'*fillersToBeAdded
print(ptnew)

keylist = list(key)
#print(keylist)

i = 0
mat = []
while(i<len(ptnew)):
	ele = []
	for j in range(lenkey):
		ele.append(ptnew[i])
		i+=1
	mat.append(ele)

print(mat)

cmat=[]
for i in mat:
	ele=[]
	for k, j in zip(keylist,i):
		intk = int(k)-1
		ele.insert(intk,j)
	cmat.append(ele)
print(cmat)

ct = ""
for i in cmat:
	for j in i:
		ct+=j

print("ciphertext :", ct)
