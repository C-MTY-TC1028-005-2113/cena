# Nombre:
# Matricula:
# Carrera:
# Fecha:

"""
Diseña y códifica un programa en Python que haga lo siguiente: 

Datos de Entrada:
El programa ya tiene una matriz con la información de las Series de Amazon 
- cada renglón de la matriz se organiza de la siguiente forma
       Titulo ,         genero,    código_serie, País, duracion_min, fecha_lanzamiento, calificación
['I Am Not an Animal', 'Animation',   '11.164',  'GB',  '349',         '10/05/04',          '9.5']

la matriz podría tener cualquier otra información - no siempre tendra la misma,
solo por cuestiones de tiempo se puso fija - debes programar tu solución para que
funcione para cualquier otro contenido de la matriz no únicamente para el actual,
de lo contrario TU SOLUCIÓN NO TENDRÁ SE TOMARA EN CUENTA (0 PTOS.).

Salidas:
El programa debe desplegar un listado de las series, con una numeración de 1 hasta n Serie (la cantidad de renglones de la matriz)
el programa debe tener la programación para calcular lo siguiente usando los datos de la matriz 
       - NOTA IMPORTANTE - debes diseñar tu solución para que funcione para cualquier otro contenido de la matriz 
         no únicamente para el actual, de lo contrario TU SOLUCIÓN NO SE TOMARÁ EN CUENTA(0 PTOS).
    - Contar la cantidad de series que existen para cada genero (TIP - contar la cantidad del mismo genero usa listas)
    - Calcular el porcentaje % de series de ese genero que se calcula de la siguiente forma
                            cantidad / total * 100
        si por ejemplo son     9    / 20 * 100 = 45.0, que corresponde a un 45.0% 
        (TIP - se calcula hasta el final puede ser al desplegar o antes y dejar los resultaods en una lista)
    - Contar la cantidad total de series.  
    - Calcular el promedio de todas las series de Amazon
       (TIP - usa un acumulador - inicializar antes del ciclo e incrementar al ir recorriendo la matriz)

La salida debería ser :
1 I Am Not an Animal Animation
2 Chernobyl Drama
3 Rick and Morty Animation
4 Breaking Bad Drama
5 Hunter x Hunter Animation
6 Sherlock Crime
7 Planet Earth II Documentary
8 Peaky Blinders Crime
9 Stranger Things Drama
10 DEATH NOTE Animation
11 Avatar: The Last Airbender Animation
12 The Twilight Zone Drama
13 The Wire Crime
14 Gravity Falls Animation
15 The Sopranos Drama
16 Neon Genesis Evangelion Animation
17 The Marvelous Mrs. Maisel Comedy
18 Young Justice Animation
19 Band of Brothers Drama
20 Futurama Animation
Animation 9 45.0%
Drama 6 30.0%
Crime 3 15.0%
Documentary 1 5.0%
Comedy 1 5.0%
Total de series: 20
Promedio: 8.38


"""
def main():

    series = [['I Am Not an Animal', 'Animation', '11.164', 'GB', '349', '10/05/04', '9.5'],
    ['Chernobyl', 'Drama', '46.429', 'US', '595', '06/05/19', '8.6'],
    ['Rick and Morty', 'Animation', '132.429', 'US', '1395', '02/12/13', '8.5'],
    ['Breaking Bad', 'Drama', '161.35', 'US', '3560', '20/01/08', '8.4'],
    ['Hunter x Hunter', 'Animation', '136.761', 'JP', '152', '02/10/11', '8.3'],
    ['Sherlock', 'Crime', '35.74', 'GB', '1885', '25/07/10', '8.3'],
    ['Planet Earth II', 'Documentary', '17.744', 'GB', '348', '06/11/16', '8.3'],
    ['Peaky Blinders', 'Crime', '59.824', 'GB', '572', '12/09/13', '8.3'],
    ['Stranger Things', 'Drama', '81.441', 'US', '2671', '15/07/16', '8.3'],
    ['DEATH NOTE', 'Animation', '56.677', 'JP', '599', '04/10/06', '8.3'],
    ['Avatar: The Last Airbender', 'Animation', '15.668', 'US', '552', '21/02/05', '8.3'],
    ['The Twilight Zone', 'Drama', '12.384', 'US', '295', '02/10/59', '8.3'],
    ['The Wire', 'Crime', '30.153', 'US', '869', '02/06/02', '8.3'],
    ['Gravity Falls', 'Animation', '40.365', 'US', '298', '15/06/12', '8.3'],
    ['The Sopranos', 'Drama', '25.922', 'US', '846', '10/01/99', '8.3'],
    ['Neon Genesis Evangelion', 'Animation', '29.844', 'JP', '233', '04/10/95', '8.3'],
    ['The Marvelous Mrs. Maisel', 'Comedy', '23.354', 'US', '105', '16/03/17', '8.3'],
    ['Young Justice', 'Animation', '30.096', 'US', '121', '26/11/10', '8.3'],
    ['Band of Brothers', 'Drama', '19.555', 'GB', '1500', '09/09/01', '8.2'],
    ['Futurama', 'Animation', '40.574', 'US', '919', '28/03/99', '8.2']]

  



    print("Total de series:", total)
    print("Promedio:", round(promedio, 2))

if __name__=='__main__':
    main()
