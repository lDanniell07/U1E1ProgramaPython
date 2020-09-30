def Ordena(array2,array1):
    for i in range(len(array1)-1):
        for j in range(len(array1)-1):
            if not(array1[j] == array2[j]):
                temporal = array1[j]
                array1[j] = array1[j+1]
                array1[j+1] = temporal
    return array1
print("------------------------")
frase = ["Me","llamo","daniel"]

archivo2 = open("demo.txt")  
texto = archivo2.read().split(' ')

for i in range(len(frase)-1):
        for j in range(len(frase)-1):
            if not(texto[j] == frase[j]):
                temporal = texto[j]
                texto[j] = texto[j+1]
                texto[j+1] = temporal

print("Frase Ordenada:")
print(texto)
