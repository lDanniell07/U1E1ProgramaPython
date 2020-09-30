def Ordena(array2,array1):
    for i in range(len(array1)-1):
        for j in range(len(array1)-1):
            if not(array1[j] == array2[j]):
                temporal = array1[j]
                array1[j] = array1[j+1]
                array1[j+1] = temporal
    return array1
print("-------> Bienvenid@ <-----------")
fra = 'Me llamo daniel'
frase = fra.split(' ')
archivo = open("frase.txt")  
texto = archivo.read().split(' ')
print("Frase Ordenada:")
print(Ordena(frase,texto))
print("-------> ¡BYE! <-----------")