import string
import numpy as np
key = "goodnight"

plain_text = "sahil"

print("plain text : ",plain_text)
print("key : ", key)

if (len(plain_text)%3==1):
	plain_text += "xx"
elif(len(plain_text)%3==2):
	plain_text += "x"

alphabets = list(string.ascii_lowercase)

matrix=[]
i=0
while i<len(key):
	ele=[]
	for j in range(3):
		pos = alphabets.index(key[i])
		i+=1
		ele.append(pos)
	matrix.append(ele)

print ("key matrix :",matrix)

ciphertext=''
total = 0
i=0
while i<len(plain_text):
	ele=[]
	for j in range(3):
		pos = alphabets.index(plain_text[i])
		i+=1
		ele.append(pos)
	print(ele)
	for element in matrix:
		total = 0
		k=0
		while(k<len(element)):
			e=0
			while (e<len(ele)):
				total += element[k]*ele[e]
				k+=1
				e+=1
		total = total%26
		print(total)
		ciphertext += alphabets[total]

print ("ciphertext : ",ciphertext)

dmat = np.matrix(matrix)
inversemat = np.linalg.inv(dmat)
inversemat = inversemat.tolist()
print()
print("inverse mat : ", inversemat)

originaltext = ""
i=0
while i<len(ciphertext):
	ele=[]
	for j in range(3):
		pos = alphabets.index(ciphertext[i])
		i+=1
		ele.append(pos)
	print(ele)
	for element in inversemat:
		total = 0
		k=0
		while(k<len(element)):
			e=0
			while (e<len(ele)):
				total += element[k]*ele[e]
				k+=1
				e+=1
		total = int(total)
		total = total%26
		print(total)
		originaltext += alphabets[total]

print(np.matmul(matrix,inversemat))