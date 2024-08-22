#
# EJERCICIOS
# 02-Ejercicio-Limpieza (cleaning) de datos.
#
# Fecha: 16.08.2024
# Nombre: MARTIN LUNA
#

# importacion de librerias y de dataset.
import pandas as pd
import numpy as np
import re

pd.options.display.max_columns = None

#df = pd.read_csv("../data/01-tiburon_4.csv", index_col = 0)
df = pd.read_csv("C:/Users/martin.luna/01-tiburon_4.csv", index_col = 0)
df.head(2)


# (previamente) Reconocimiento del dataframe (df).

# -lecturas del df.
df
df.head(100)
print(df.head(1000))
# -tipo del objeto de datos.
type(df) 
# -dimension del objeto de datos.
df.size
# -caracteristicas/aspectos del objeto de datos.
df.info()
# -resguardo del objeto de datos.
df_copy = df


#
# PAIR PROGRAMMING LIMPIEZA II
#
#   Acciones a realizar:
#

# 01. Columna species: Dado que existen aqui muchos valores unicos, clasificar tiburones en 5 especies diferentes a saber:
#   tiburon blanco (White)
#   tiburon tigre (Tiger)
#   tiburon gris (Grey)
#   tiburon limon (Lemon)
#   tiburon toro (Bull)
#   resto tiburones (Unspecified)
# nota1: los valores son strings, ideal utilizar regex (regular expressions) para buscar palabras clave en cada celda y asi, asignarlo a una de las categorias que hemos definido previamente.
#        ejemplo: valor de celda: 'White shark, 3.5 m'
#                patron para extraer 'White shark' (dato de interes): patron_t_blanco = r".Ww."#
#
# nota2: para emplear regex, desarrollar una funcion para aplicar sobre columna 'species' para que asi devuelva nueva columna con valores clasificados.
#

def clasif_shark(df):
    tope = len(df)
    for indice, valor in df.iterrows():
        if 
        df['situacion'] = df.apply(escala_situacion, axis=1)

    return '_____'








# 02. Columna age: De tipo string, deberia ser de tipo integer. Sus valores incluyen errores de tipeo, tales como: 
#                   -edad en formato string
#                   -edades separadas por &, or, to, >
#                   -edades con ?
# nota1: se deberan eliminar todos esos simbolos especiales que aparecen. Ideal usar metodo regex() para extraer solo los numeros (datos de interes).
# nota2: para emplear regex (regular expressions), desarrollar una funcion para aplicar sobre columna 'age'.
# nota3: en caso de error "TypeError: expected string or bytes-like-object, ejecutar siguiente codigo: 
#        df['nombre_columna'] = df['nombre_columna'].astype(str)
# nota4: luego de extraidos los numeros de 'age', se apreciara que el campo tiene 2 edades...
#        en tal caso, utilizar metodo explode() para resolver tal situacion.
# nota5: cambiar el tipo de dato de la columna, de string a integer.

# 03. Guardar el (archivo).csv con columnas limpias para seguir trabajando con este dataframe limpio.

#
# REGEX
#

# Filtrar filas que contengan números en la columna 'texto'
df_filtrado = df[df['texto'].str.contains(r'\d+', regex=True)]

# Reemplazar dígitos con un carácter específico
df['texto_modificado'] = df['texto'].str.replace(r'\d+', 'X', regex=True)

# Extraer solo los números de la columna 'texto'
df['numeros'] = df['texto'].str.extract(r'(\d+)', expand=False)

# Verificar si el texto comienza con letras y termina con números
df['coincide'] = df['texto'].str.match(r'^[a-zA-Z]+\d+$')

# Resumen de Expresiones Regulares
#   \d: Coincide con cualquier dígito.
#   \w: Coincide con cualquier carácter alfanumérico (letras y números).
#   \s: Coincide con cualquier carácter de espacio en blanco.
#   ^: Coincide con el inicio de una cadena.
#   $: Coincide con el final de una cadena.
#   []: Coincide con cualquier carácter dentro de los corchetes.
#



# --.


