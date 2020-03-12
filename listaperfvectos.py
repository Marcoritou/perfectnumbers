from detectorperfectos import divisores

N = int(input("INGRESE UN VALOR ======================================>"))
entry = 0
i = 0
suma = 0

for j in range(1,N+1):
    entry = j
    if divisores(i, entry, suma) == j:
        print(j)