from collections import deque

numeros=input()

numerosdiv = numeros.split(" ")

palavras = deque()

for k in numerosdiv:
    n1 = int(k)
    palavras.append(n1)



print (palavras)
for i in range(len(numerosdiv)):
    pal = palavras.pop()
    print(int(pal)**2)