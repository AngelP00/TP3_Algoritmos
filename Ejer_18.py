from cola import Cola


from random import randint
def mostrar_cola(cola):
    for i in range(0,cola.tamanio()):
        print(cola.mover_al_final())

def letra_con_mas_turnos(cola):
    a,b,c,d,e,f = 0,0,0,0,0,0
    for i in range(0,cola.tamanio()):
        dato=cola.mover_al_final()
        if dato[0]=='A':
            a+=1
        elif dato[0]=='B':
            b+=1
        elif dato[0]=='C':
            c+=1
        elif dato[0]=='D':
            d+=1
        elif dato[0]=='E':
            e+=1
        elif dato[0]=='F':
            f+=1
    vec=[]
    if a==max(a,b,c,d,e,f):
        vec.append('a')
    if b==max(a,b,c,d,e,f):
        vec.append('b')
    if c==max(a,b,c,d,e,f):
        vec.append('c')
    if d==max(a,b,c,d,e,f):
        vec.append('d')
    if e==max(a,b,c,d,e,f):
        vec.append('e')
    if f==max(a,b,c,d,e,f):
        vec.append('f')
    if max(a,b,c,d,e,f)>0:
        return vec, max(a,b,c,d,e,f)
    else:
        return None

def turnos_mayores_a_506(cola):
        for i in range(0,cola.tamanio()):
            turno=cola.mover_al_final()
            if int(turno[1:])>506:
                print(turno)

#a. cargar 1000 turnos de manera aleatoria a la cola.
print('a. Cargar 1000 turnos de manera aleatoria a la cola.')
cola_de_turnos=Cola()
for i in range(10):
    letra = chr(randint(65, 70))
    codigo = letra+str(randint(0,9))+str(randint(0,9))+str(randint(0,9))
    cola_de_turnos.arribo(codigo)
print('Cola original:')
mostrar_cola(cola_de_turnos)

#b. separar la cola con datos en dos colas, cola_1 con los turnos que empiezan con la letra A, C
#y F, y la cola_2 con el resto de los turnos (B, D y E).
print()
print('b. Separar la cola con datos en dos colas, cola_1 con los turnos que empiezan con la letra A, C y F, y la cola_2 con el resto de los turnos (B, D y E)')
cola_1=Cola()
cola_2=Cola()
for i in range(0,cola_de_turnos.tamanio()):
    codigo=cola_de_turnos.atencion()
    if codigo[0] in ('A','C','F'):
        cola_1.arribo(codigo)
    else:
        cola_2.arribo(codigo)

print('#cola_1 con (A, C y F):')
mostrar_cola(cola_1)
print()
print('#cola_2 con (B, D y E):')
mostrar_cola(cola_2)


#c. determinar cuál de las colas tiene mayor cantidad de turnos, y de esta cuál de las letras
#tiene mayor cantidad.
print()
print('c. Determinar cuál de las colas tiene mayor cantidad de turnos, y de esta cuál de las letras tiene mayor cantidad.')
if cola_1.tamanio() != cola_2.tamanio():
    if cola_1.tamanio()>cola_2.tamanio():
        print('cola_1 tiene la mayor cantidad de turnos')
        vector_resultado = letra_con_mas_turnos(cola_1)
        print('En cola_1 la letra con mayor cantidad de turnos es:',vector_resultado[0],'y su cantidad es:',vector_resultado[1])

        print()
        print('d. Mostrar los turnos de la cola con menor cantidad de elementos, cuyo número de turno sea mayor que 506.')
        print('cola_2 tiene la menor cantidad de turnos.')
        print('Los numeros mayores a 506 de la cola_2 son: ')
        turnos_mayores_a_506(cola_2)
    else:
        print('cola_2 tiene la mayor cantidad de turnos.')
        vector_resultado = letra_con_mas_turnos(cola_2)
        print('En cola_2 la letra con mayor cantidad de turnos es:',vector_resultado[0],'y su cantidad es:',vector_resultado[1])
        
        print()
        print('d. Mostrar los turnos de la cola con menor cantidad de elementos, cuyo número de turno sea mayor que 506.')
        print('cola_1 tiene la menor cantidad de turnos.')
        print('Los numeros mayores a 506 de la cola_1 son: ')
        turnos_mayores_a_506(cola_1)        
else:
    print('cola_1 y cola_2 tienen la misma cantidad de turnos.')