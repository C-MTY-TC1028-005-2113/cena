# Nombre - 
# Matricula - 
# Carrera -

"""
En una tienda de laptops se venden de 3 tipos: corei5, corei7, corei9
La tienda además tiene clasificados a sus  clientes en las siguientes categorias: frecuentes, registrados y nuevos

Ya pronto se acerca la venta del Buen Fin, por lo tanto El director de la tienda a decidido dar los siguientes
descuentos dependiendo del cliente:

Clientes frecuentes(F o f):
- se les dará un descuento del 30%  por cualquier monto de compra

Clientes registrados(R o r):
- si su compra es superior a $20,000  e inferior a $30,000 un 15% de descuento
- si su compra es superior $30,000 un 25% de descuento

Clientes nuevos(N o n:
- se les dará un 10% de descuento por cualquier monto de compra

Lleva a cabo el análisis, diseño y codificación en python de un programa
que lea la categoria de la laptop (que puede ser i5, i7, i9 que puede ser ingresada cómo Mayúscula o minúscula),
el tipo de cliente (que es una letra f,r,n que puede ser ingresada cómo Mayúscula o minúscula)
y la cantidad a comprar (que es un número entero).
Para esta versión que vas a diseñar solo se le permite al cliente realizar una comprar de un solo tipo de laptop.

El programa debe tener las siguientes funciones:
Función llamada total_antes_descuento que recibe como parámetros: tipo_laptop y la cantidad: 
        La función retorna el total incial, antes del descuento.
Función llamada calcula_descuento que recibe como parámetros: el total inicial y el tipo_cliente: 
         La función retorna el monto del descuento.
El programa debe calcular y mostrar los siguientes datos 
(todos los datos son flotantes y debes mostrar uno en cada renglón):

El total inicial, antes de aplicar descuento
La cantidad de dinero que se otorga por descuento y
El total a pagar por el cliente.
La salida del programa debe de ser exactamente como se indica en los casos de prueba - 

Si No Funciona en GitHub -10 ptos.

"""

def total_antes_descuento(tipo_laptop, cantidad):
    """Los precios de las laptops  son:
corei5 $7_500.00 c/u
corei7 $9_500.00 c/u
corei9 $11_500.00 c/u
 3 tipos: i5, i7, i9 Nota - podría ingresar también como I5, I7, I9
 """
    pass


def calcula_descuento(total_inicial, tipo_cliente):
    """Clientes frecuentes(F o f):
- se les dará un descuento del 30%  por cualquier monto de compra

Clientes registrados(R o r):
- si su compra es superior a $20,000  e inferior a $30,000 un 15% de descuento
- si su compra es superior  o igual a $30,000 un 25% de descuento

Clientes nuevos(N o n):
- se les dará un 10% de descuento por cualquier monto de compra
"""
    pass


def main() :
    # 1º Leer los datos de entrada
    laptops = input("Tipo de laptop i5, i7, i9: ")
    cliente = input("Tipo de cliente F, R, N: ")
    cantidad = int( input("Cantidad de laptops: "))





if __name__=='__main__':
    main()
