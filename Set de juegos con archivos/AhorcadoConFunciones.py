import random

def elegir_categoria():
  categorias_posibles = {1 : ['gato', 'perro', 'pato', 'elefante', 'lobo'], 
                         2 : ['rojo', 'azul', 'verde', 'amarillo'], 
                         3 : ['milanesa', 'pure', 'pizza', 'salchicha']}
  print('Categorías disponibles:')
  print()
  print('1 --> Animales')
  print('2 --> Colores')
  print('3 --> Comidas')
  print()
  opcion_valida = False
  while (not opcion_valida): 
    opcion_elegida = input('Ingresá el número de la categoría deseada: ')
    print()
    if (not opcion_elegida.isdigit()):
      print('Debe ingresar un número')
      print()
      continue
    opcion_elegida = int(opcion_elegida)
    if (opcion_elegida < 1 or opcion_elegida > len(categorias_posibles)): 
      print('El número ingresado no es válido')
      print()
    else: 
      opcion_valida = True
  print('Categoría seleccionada con éxito')
  print()
  return categorias_posibles[opcion_elegida]

def elegir_palabra(categoria):
  numero_random = random.randrange(len(categoria))
  print('Ya elegí una palabra de la categoría...')
  print()
  return categoria[numero_random]

def elegir_cantidad_intentos():
  print('¿Cuántos intentos querés tener?')
  print()
  cantidad = input('Podés tener 3 (sumás 20 puntos si adivinás) o 6 (sumás 10 puntos si adivinás): ')       
  print()                                                                        
  while (cantidad != '3' and cantidad != '6'):                                   # el usuario de elige la cantidad de intentos y la función
    cantidad = input('Ingresá una cantidad correcta: ')                          # retorna una tupla con los caracteres para imprimir el dibujo
    print()
  print('Genial, vas a tener ' + cantidad + ' intentos...')
  print()
  if (cantidad == '3'):
    dibujo_ahorcado = (' O ', '/|\\', '/ \\')
  else:
    dibujo_ahorcado = (' O ', ' | ', '/|', '/|\\', '/', '/ \\')
  return dibujo_ahorcado

def inicializar_palabra_adivinada(palabra_random): 
  palabra_adivinada = []
  for i in range(len(palabra_random)):
    palabra_adivinada += ["_"]
  return palabra_adivinada

def dibujar_ahorcado(dibujo_ahorcado, intento):                                  # imprime el dibujo correspondiente a la cantidad de intentos
  if len(dibujo_ahorcado) == 3:
    for i in range(intento):
      print(dibujo_ahorcado[i])
  else:
    for i in range(intento): 
      if (intento >= 3 and i == 1):
        continue
      if (intento >= 4 and i == 2):
        continue
      if (intento == 6 and i == 4):
        continue
      print(dibujo_ahorcado[i])

def jugar(palabra_random, palabra_adivinada, dibujo_ahorcado, puntos):
  intento = 1
  cantidad_intentos = len(dibujo_ahorcado)
  letras_adivinadas = 0
  gano = False
  copia_palabra_random = palabra_random[::]
  palabra_random = list(palabra_random)                                          # convierte la palabra a una lista para poder manipular 
  print('¡Intentá adivinar la palabra!')                                         # las letras (ya que los strings son inmutables)
  print()
  print(" ".join(palabra_adivinada))
  print()
  while (intento < (cantidad_intentos + 1) and not gano):
    if (intento == cantidad_intentos): 
      print('¡Te queda 1 solo intento!')
      print()
    letra_jugador = input("Ingresá una letra: ").lower()
    print()
    letra_correcta = False
    for i in range(len(palabra_random)):
      if (palabra_random[i] == letra_jugador):
        palabra_adivinada[i] = letra_jugador
        palabra_random[i] = '-'                                                  # "borra" esa letra de la palabra original, para no volver
        letra_correcta = True                                                    # a contarla si el usuario vuelve a ingresar la misma letra
        letras_adivinadas += 1
        if (letras_adivinadas == len(palabra_random)):
          gano = True
          break
    print(" ".join(palabra_adivinada))
    print()
    if (not letra_correcta):
      dibujar_ahorcado(dibujo_ahorcado, intento)
      intento += 1
      print()
  if (gano): 
    print('¡Felicitaciones, adivinaste la palabra!')
    if (len(dibujo_ahorcado) == 3):
      puntos[0] += 20
    else:
      puntos[0] += 10
  else: 
    print('¡Perdiste! La palabra era: ' + copia_palabra_random)
  print()

def main():
  sigue_jugando = True
  print()
  print('AHORCADO EN PYTHON')
  print()
  puntos = [0]
  while (sigue_jugando):
    categoria_elegida = elegir_categoria()
    palabra_random = elegir_palabra(categoria_elegida)
    dibujo_ahorcado = elegir_cantidad_intentos()
    palabra_adivinada = inicializar_palabra_adivinada(palabra_random)  
    jugar(palabra_random, palabra_adivinada, dibujo_ahorcado, puntos)
    sigue_jugando = (input('Si querés seguir jugando presioná "1"... ') == '1')
    print()
  print('Obtuviste un total de', puntos[0], 'puntos')

if __name__ == '__main__':
  main()