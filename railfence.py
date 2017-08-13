plain_text = input("enter text : ")
ciphertext = ""
i=0
while(i<len(plain_text)):
	#print(plain_text[i])
	ciphertext += plain_text[i]
	i+=2
i=1
while(i<len(plain_text)):
	#print(plain_text[i])
	ciphertext += plain_text[i]
	i+=2
print(ciphertext)

print()
print("decryption:")

if(len(ciphertext)%2):
        mid = (len(ciphertext)/2)+0.5
        ciphertext += "x"
else:
        mid = len(ciphertext)/2
#print(mid)

originaltext = ""
midint = int(mid)
for i in range(midint):
        originaltext += ciphertext[i] + ciphertext[midint+i]
#print(originaltext)

if(len(plain_text)%2):
        originaltext = originaltext[:-1]
print(originaltext)
