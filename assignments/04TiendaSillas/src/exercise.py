def total_antes_descuento(tipo_laptop, cantidad):
    """Los precios de las laptops  son:
corei5 $7500.00 c/u
corei7 $9,500.00 c/u
corei9 $11,500.00 c/u
 3 tipos: i5, i7, i9
 """
    pass


def calcula_descuento(total_inicial, tipo_cliente):
    """Clientes frecuentes(F o f):
- se les dará un descuento del 30%  por cualquier monto de compra

Clientes registrados(R o r):
- si su compra es superior a $20,000  e inferior a $30,000 un 15% de descuento
- si su compra es superior  o igual a $30,000 un 25% de descuento

Clientes nuevos(N o n:
- se les dará un 10% de descuento por cualquier monto de compra
"""



def main() :
    # 1º Leer los datos de entrada
    laptops = input("Tipo de laptop i5, i7, i9: ")
    cliente = input("Tipo de cliente F, R, N: ")
    cantidad = int( input("Cantidad de laptops: "))





if __name__=='__main__':
    main()
