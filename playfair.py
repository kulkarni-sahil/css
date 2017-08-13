import string

plain_text = input("enter plain text: ")
key = input("enter key: ")

print()
print ("name : " + plain_text)
print()
print ("roll no : " + key)
print()
singleCharsInKey = []
for i in  key:
	if i not in singleCharsInKey:
		singleCharsInKey.append(i)
	else:
		pass

#print singleCharsInKey

alphabets =  list(string.ascii_lowercase)
#print alphabets

for i in singleCharsInKey:
	for j in alphabets:
		if i == j:
			alphabets.remove(j)
			break

alphabets.remove('b')
#print alphabets

matrixelements = [] 
for i in singleCharsInKey:
	matrixelements.append(i)

for j in alphabets:
	matrixelements.append(j)

#print matrixelements

matrix = []
posKey = 0
for i in range(1,6):
	matrixElement = []
	for j in range(1,6):	
		matrixElement.append(matrixelements[posKey])
		posKey += 1
	matrix.append(matrixElement)
		
#print matrix

plain_text_list = list(plain_text)
#print plain_text_list
if len(plain_text_list)%2:
	plain_text_list.append('x')
	charadded = 1


#print plain_text_list

correct_list = []
i = 0 
while i < len(plain_text_list):	
	if plain_text_list[i] == plain_text_list[i+1]:
		#print "double"
		correct_list.append(plain_text_list[i])
		correct_list.append("x")
		correct_list.append(plain_text_list[i+1])
	else:	
		correct_list.append(plain_text_list[i])
		correct_list.append(plain_text_list[i+1])
	#print i
	i += 2



if len(correct_list)%2:
	correct_list.append('x')


i=0
ciphertext = ""
while i < len(correct_list):
	letter1 = correct_list[i]
	letter2 = correct_list[i+1]
	i+=2
	letter1pos=[]
	letter2pos=[]
	temp1=""
	temp2=""
	for l in range(len(matrix)):
		for j in range(5):
			if matrix[l][j] == letter1:
				letter1pos.append(l)
				letter1pos.append(j)			
			if matrix[l][j] == letter2:
				letter2pos.append(l)
				letter2pos.append(j)
	#print letter1pos,letter2pos
	if letter1pos[0]==letter2pos[0]:
		#print"row same"
		temp1 = (letter1pos[1]+1)%5
		temp2 = (letter2pos[1]+1)%5
		#print temp1,temp2
		ciphertext += matrix[letter1pos[0]][temp1]
		ciphertext += matrix[letter1pos[0]][temp2]
		#print ciphertext		
	elif letter1pos[1]==letter2pos[1]:
		#print"col same"
		temp1 = (letter1pos[0]+1)%5
		temp2 = (letter2pos[0]+1)%5
		#print temp1,temp2
		ciphertext += matrix[temp1][letter1pos[1]]
		ciphertext += matrix[temp2][letter2pos[1]]		
		#print ciphertext
	else:
		#print"both diff"
		ciphertext += matrix[letter1pos[0]][letter2pos[1]]
		ciphertext += matrix[letter2pos[0]][letter1pos[1]]
		#print ciphertext

print ("cipher text : " + ciphertext)

d_list = list(ciphertext)
i=0
dtext = ""
while i < len(correct_list):
	letter1 = d_list[i]
	letter2 = d_list[i+1]
	i+=2
	letter1pos=[]
	letter2pos=[]
	temp1=""
	temp2=""
	for l in range(len(matrix)):
		for j in range(5):
			if matrix[l][j] == letter1:
				letter1pos.append(l)
				letter1pos.append(j)			
			if matrix[l][j] == letter2:
				letter2pos.append(l)
				letter2pos.append(j)
	#print letter1pos,letter2pos
	if letter1pos[0]==letter2pos[0]:
		#print"row same"
		temp1 = (letter1pos[1]-1)%5
		temp2 = (letter2pos[1]-1)%5
		#print temp1,temp2
		dtext += matrix[letter1pos[0]][temp1]
		dtext += matrix[letter1pos[0]][temp2]
		#print ciphertext		
	elif letter1pos[1]==letter2pos[1]:
		#print"col same"
		temp1 = (letter1pos[0]-1)%5
		temp2 = (letter2pos[0]-1)%5
		#print temp1,temp2
		dtext += matrix[temp1][letter1pos[1]]
		dtext += matrix[temp2][letter2pos[1]]		
		#print ciphertext
	else:
		#print"both diff"
		dtext += matrix[letter1pos[0]][letter2pos[1]]
		dtext += matrix[letter2pos[0]][letter1pos[1]]

if charadded == 1:
	dtext = dtext[:-1]
print("decrypted text:",dtext)



























