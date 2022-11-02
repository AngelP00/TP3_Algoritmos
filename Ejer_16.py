'''
Utilice cola de prioridad, para atender la cola de impresión tomando en cuenta el siguiente
criterio (1- empleados, 2- staff de tecnologías de la información “TI”, 3- gerente), y resuelva la
siguiente situación:
'''
from heap import HeapMax, HeapMin

#h = HeapMin()
h = HeapMax()

'''
a. cargue tres documentos de empleados (cada documento se representa solamente con
un nombre).
'''
h.agregar(['Doc_epleado1'], 1)
h.agregar(['Doc_epleado2'], 1)
h.agregar(['Doc_epleado3'], 1)

'''
b. imprima el primer documento de la cola (solamente mostrar el nombre de este por pantalla).
'''
print('primer elemento de la cola:', h.quitar()[0][0])



'''
c. cargue dos documentos del staff de TI.
'''
h.agregar(['Doc_staff1'], 2)
h.agregar(['Doc_staff2'], 2)

#d. cargue un documento del gerente.
h.agregar(['Doc_gerente1'], 3)

#e. imprima los dos primeros documentos de la cola.
print('primer elemento de la cola:', h.quitar()[0][0])
print('segundo elemento de la cola:', h.quitar()[0][0])


#f. cargue dos documentos de empleados y uno de gerente.
h.agregar(['Doc_epleado4'], 1)
h.agregar(['Doc_epleado5'], 1)
h.agregar(['Doc_gerente2'], 3)

#g. imprima todos los documentos de la cola de impresión.
print('')
print('h.tamanio:',h.tamanio)
for i in range(h.tamanio):
    print('elemento impreso:', h.quitar()[0][0])
    #print(h.vector)
    #a= input()
print(h.vector, h.tamanio)