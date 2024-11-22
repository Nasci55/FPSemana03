from collections import deque

pal=input()

paldiv = (pal.split(" "))

palavras = deque()


for it in paldiv:
    palavras.appendleft(it)

print (palavras)

for i in range(len(palavras)):
    letra = palavras.pop()
    if "o" in letra: 
        print (letra)
