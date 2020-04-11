from collections import Counter

def es_primo(numero):
  if (numero <= 1): 
    return False
  for i in range(2, numero):
    if (numero % i) == 0:
      return False
  return True

string = input("Ingrese un string ").lower()
diccionario = Counter(string)                   # crea un diccionario donde las claves son las letras del string y los valores son la cantidad de veces que aparece la letra
lista_primos = []

for letra in diccionario:
  cantidad = diccionario[letra]
  if (cantidad > 1): 
    print("La letra", letra, "aparece:", cantidad, "veces")
  else: 
    print("La letra", letra, "aparece:", cantidad, "vez")
  if (es_primo(cantidad)):
    letra = "'" + letra + "'"
    lista_primos += [letra]

if (len(lista_primos) == 0): 
    print("Por lo tanto, no hay ninguna letra que aparezca un número primo de veces.")
elif (len(lista_primos) == 1): 
    print("Por lo tanto, la letra", lista_primos[0], "aparece un número primo de veces.")
else: 
    print("Por lo tanto, las letras", ", ".join(lista_primos), "son letras que aparecen un número primo de veces.")
input()