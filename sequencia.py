def sequencia(n):
   if n <= 1:
       return n
   return sequencia(n-1) + sequencia(n-2)
n = int(input("Digite o n-ésimo termo: "))
for i in range(n):
   print(sequencia(i), end=" ")