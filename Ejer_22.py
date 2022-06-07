from cola import Cola

class Personaje:
    def __init__(self, n_personaje=None, n_superheroe=None, genero=None):
        self.nombre_personaje = n_personaje
        self.nombre_superheroe = n_superheroe
        self.genero = genero

    def __str__(self):
        return f"{self.nombre_personaje}, {self.nombre_superheroe}, {self.genero}"

def mostrar_cola(cola):
    for i in range(0,cola.tamanio()):
        print(cola.mover_al_final())

def buscar_por_nombre_de_superheroe(cola, buscado):
    for i in range(0,cola.tamanio()):
        superheroe=cola.mover_al_final()
        if superheroe.nombre_superheroe == buscado:
            return superheroe

def mostrar_personaje_de_x_genero(cola, genero):
    if cola.tamanio() > 0:
        for i in range(0,cola.tamanio()):
            superheroe=cola.mover_al_final()
            if superheroe.genero == genero:
                #print(superheroe)
                print(superheroe.nombre_personaje,', ', superheroe.nombre_superheroe)
    else:
        print('No hay personajes del genero elegido')

def buscar_por_nombre_de_personaje(cola, buscado):
    for i in range(0,cola.tamanio()):
        superheroe=cola.mover_al_final()
        if superheroe.nombre_personaje == buscado:
            return superheroe

def mostrar_personajes_que_comienzan_con_x_letra(cola, buscado):
    for i in range(0,cola.tamanio()):
        personaje=cola.mover_al_final()
        if buscado in (personaje.nombre_personaje[0], personaje.nombre_superheroe[0]):
            print(personaje)



cola_de_personajes=Cola()
cola_de_personajes.arribo(Personaje('Tony Stark','Iron Man', 'M'))
cola_de_personajes.arribo(Personaje('Steve Rogers', 'Capitan America', 'M'))
cola_de_personajes.arribo(Personaje('Natasha Romanoff','Black Widow', 'F'))
cola_de_personajes.arribo(Personaje('Carol Danvers', 'Capitana Marvel', 'F'))
cola_de_personajes.arribo(Personaje('Scott Lang', 'Ant-Man', 'M'))
cola_de_personajes.arribo(Personaje('Bruce Banner', 'Hulk', 'M'))
cola_de_personajes.arribo(Personaje('Peter Parker', 'Spider Man', 'M'))


print('Cola de personajes:')
mostrar_cola(cola_de_personajes)

print()
print('a. Determinar el nombre del personaje de la superheroe Capitana Marvel.')
personaje = buscar_por_nombre_de_superheroe(cola_de_personajes,'Capitana Marvel')
if(personaje != None):
    print('El nombre del personaje de la superhéroe Capitana Marvel es :', personaje.nombre_personaje)
else:
    print('No se encontro a Capitana Marvel en la cola.')

print()
print('b. Mostrar los nombre de los superheroes femeninos.')
print('Nombres de los superheroes femeninos:')
mostrar_personaje_de_x_genero(cola_de_personajes,'F')

print()
print('c. Mostrar los nombres de los personajes masculinos.')
print('Nombres de los superheroes masculinos:')
mostrar_personaje_de_x_genero(cola_de_personajes,'M')


print()
print('d. Determinar el nombre del superhéroe del personaje Scott Lang.')
personaje = buscar_por_nombre_de_personaje(cola_de_personajes,'Scott Lang')
if(personaje != None):
    print('El nombre del personaje del superhéroe Scott Lang es :', personaje.nombre_superheroe)
else:
    print('No se encontro a Scott Lang en la cola.')


print()
print('e. Mostrar todos los datos de los superheroes o personajes cuyos nombres comienzan con la letra S.')
mostrar_personajes_que_comienzan_con_x_letra(cola_de_personajes,'S')


print()
print('f. Determinar si el personaje Carol Danvers se encuentra en la cola e indicar su nombre de superheroe.')
personaje= buscar_por_nombre_de_personaje(cola_de_personajes,'Carol Danvers')
if personaje!=None:
    print('Carol Danvers se encuentra en la cola, y su nombre de superheroe es: ', personaje.nombre_superheroe)
else:
    print('Carol Danvers no se encuentra en la cola.')