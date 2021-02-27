global1 = 34

import datetime

def cambiar_global(a):
    '''Cambiar una variable global

    Esta función debe asignarle a la variable global `global1` el valor que se
    le pasa como único argumento posicional.
    '''
    global global1
    global1 = a
    pass


def anio_bisiesto(a):
    '''Responder si el entero pasado como argumento es un año bisiesto
    
    Para determinar si un año es bisiesto, se deben tener en cuenta las 
    siguientes condiciones:

    - Si el año es divisible por 4 es bisiesto, a menos que:
        - Si el año es divisible por 100 no es bisiesto a menos que:
            - Si el año es divisible por 400 es bisiesto.

    Retorna True o False
    '''
    if a%4 == 0:
      if a%100 == 0:
        return False
      elif a%400 == 0:
        return True
      else:
        return True
    else:
      return False
    pass

def contar_valles(a):
    r'''Contar el número de valles

    Esta función debe recibir como argumento una lista de -1's, 0's y 1's, y lo 
    que representan son las subidas y las bajadas en una ruta de caminata. -1
    representa un paso hacia abajo, el 0 representa un paso hacia adelante y el 
    1 representa un paso hacia arriba, entonces por ejemplo, para la lista
    [-1,1,0,1,1,-1,0,0,1,-1,1,1,-1,-1] representa la siguiente ruta:

                /\
         /\__/\/  \
       _/  
     \/

    El objetivo de esta función es devolver el número de valles que estén 
    representados en la lista, que para el ejemplo que se acaba de mostrar es
    de 3 valles.
    '''
    cont = 0
    b = False
    for el in a:
      if el == -1 and b == False:
        b = True
      if el == 1 and b == True:
        b = False
        cont += 1
    return cont
    print(cont)
    pass

#test = [-1,1,0,1,1,-1,0,0,0,0,1,-1,1,1,-1,-1]
#print(test)
#print(contar_valles(test))
def saltando_rocas(li):
    '''Mínimo número de saltos en las rocas

    Esta función hace parte de un juego en el que el jugador debe cruzar un río
    saltando de roca en roca hasta llegar al otro lado. Hay dos tipo de rocas, 
    secas y húmedas, y el jugador debe evitar saltar encima de las húmedas para 
    no resbalarse y caer. Además el jugador puede saltar 1 o 2 rocas, siempre y 
    cuando no caiga en una húmeda.

    Esta función debe recibir como argumento una lista de ceros y unos. Los ceros 
    representan las rocas secas y los unos las húmedas.
    El objetivo es devolver el número mínimo de saltos que debe realizar el 
    jugador para ganar la partida
    '''
    saltos = 0
    el = 0
    print(len(li))
    while el < len(li)-1:
      print(el)
      if el < len(li)-2:
        if li[el+2] == 0:
          print('a')
          saltos += 1
          el += 2
        elif li[el+1] == 0:
          print('b')
          saltos += 1
          el += 1
      elif el < len(li)-1:
        print('c')
        if li[el+1] == 0:
          print('d')
          saltos += 1
          el += 1
        else:
          el += 1
    el += 1
    return saltos
    pass
#test = [0,0,1,0,0,1,0,0,1,0,1]
#print(test)
#print(saltando_rocas(test))
def pares_medias(li):
    '''Contar pares de medias

    Esta función debe recibir como argumento una lista de enteros. Cada elemento
    de esta lista representa el color de una media, y por lo tanto si hay dos 
    elementos que tienen el mismo entero, esas dos medias tienen el mismo color.
    El objetivo de esta función es devolver un diccionario cuyas keys son cada 
    uno de los colores que se encuentren en la lista, y los valores son la 
    cantidad de pares que se han encontrado para cada color.
    '''
    dic = {}
    nopar = []
    print('colores')
    for el in li:
      dic.setdefault(el,0)
      print(dic)
    print('medias')
    for el in li:
      dic[el] += 1
      print(dic)
    print('pares')
    for el2 in dic:
      dic[el2] = dic[el2]//2
    print(dic)
    for el2 in dic:
      if dic[el2] == 0:
        nopar.append(el2)
    print('no pares')
    print(nopar)
    for el3 in nopar:
      del dic[el3]    
    return dic
    pass
#test = [1,2,3,4,1,3,6,2,3,3,6]
#print(test)
#print(pares_medias(test))

# Crear una clase llamada `ListaComa` que reciba en su constructor un iterable
# con el valor inicial para una lista que se guardará en un atributo llamado 
# `lista`. Implementar el método __str__ para que devuelva un string con todos
# los elementos del atributo `lista` unidos a través de comas. Ejemplo:
# si `lista` es [1,2,3,4], __str__ debe devolver '1,2,3,4'

class ListaComa:
  def __init__(self,li):
    self.li = li
  
  def __str__(self):
    listr = []
    for el in self.li:
      listr.append(str(el))
    salida = ','.join(listr)
    return salida
#[1,2,3,4]
#lista = ListaComa([1,2,3,4])
#print(str(lista))

# Crear una clase llamada `Persona` que reciba en su constructor como 1er 
# argumento un iterable con el valor inicial para una lista que se guardará en
# un atributo llamado `nombres` y como 2do argumento un iterable con el valor 
# inicial para una lista que se guardará en un atributo llamado `apellidos`.
# Antes de guardar estos atributos se debe verificar que todos los elementos 
# de estas dos listas deben ser de tipo str y procesar todos los elementos de
# cada una de las dos listas para que su primera letra sea mayúscula y las demás
# minúsculas.
#
# Implementar el método `nombre_completo` para que devuelva un string con todos 
# los elementos de `nombres` concatenados con espacio, y esto a su vez 
# concatenado con todos los elementos de `appelidos` concatenados con espacio.
# Ejemplo:
# si `nombres` es ['Juan', 'David'] y `apellidos` es ['Torres', 'Salazar'],
# el método `nombre completo` debe devolver  'Juan David Torres Salazar'

class Persona:
  def __init__(self,nombres,apellidos):
    self.nombres = []
    self.apellidos = [] 
    for el in nombres:
      self.nombres.append(str(el).capitalize())
    for el in apellidos:
      self.apellidos.append(str(el).capitalize())
  
  def nombre_completo(self):
    salida =  ' '.join(self.nombres)+' '+' '.join(self.apellidos)
    return salida

#personas = Persona(['sergio','daniel','andres',1],['laverde','bonilla','lopez',2])
#print(personas.nombre_completo())


# Crear una clase llamada `Persona1` que herede de la clase `Persona`, y que en su
# constructor reciba además de los atributos del padre, una variable tipo 
# `datetime` como 3er argumento para guardar en atributo `fecha_nacimiento`.
#
# Implementar el método `edad` para que devuelva un `int` que represente la edad
# de la persona y que se calcule restando los años entre la fecha actual y 
# el atributo `fecha_nacimiento`.
# Ejemplo:
# si `fecha_nacimiento` es 1985-10-21 y la fecha actual es 2020-10-20, el método
# `edad` debe devover 35.

class Persona1(Persona):
  def __init__(self,nombres,apellidos,fecha_nacimiento):
    super().__init__(nombres,apellidos)
    self.fecha_nacimiento = fecha_nacimiento
  
  def edad(self):
    hoy = datetime.datetime.today()
    delta = (hoy.year - self.fecha_nacimiento.year) -1
    print(hoy.month)
    print(self.fecha_nacimiento.month)
    print(hoy.day)
    print(self.fecha_nacimiento.day)
    if hoy.month >= self.fecha_nacimiento.month and hoy.day >= self.fecha_nacimiento.day:
      print('a')
      delta += 1
    #salida = delta.years()
    print(delta)
    return delta

fecha = datetime.datetime.strptime('2008-02-27', '%Y-%m-%d')
personas = Persona1(['sergio','daniel','andres'],['laverde','bonilla','lopez'],fecha)
print(personas.edad())