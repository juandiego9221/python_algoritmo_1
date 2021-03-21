"""
REALIZAR BUQUEDA POR INDCE
REALIZAR UN SUBSET DE LOS ELEMETOS ESPCFIFICAMDO RANGO
TAMBIEN SE PUEDE USAR UN INDEX NEGATIVO PARA REDECUIR LA LISTA ORGINAL PARTIENDO DE LA DERECHA
TENER EN CUENTA QUE EN AMBOS CASOS DE SLICE EL END ES EXCLUSIVO
ACCEDER A LISTA SOBRE LISTA
Y TAMBIEN SE PUEDE RECORRER
TAMBIEN SE PUEDE HACER DE FUNCIONES LAMBDA
"""
from functools import reduce
import pandas as pd
import numpy as np

# aList = ["jhon", 33, "thronto", True]
# print(aList)
colors = ["red", "green", "blue", "yellow"]
# print(colors[1])
# print(colors[0:2])
# print(colors[2:])
# print(colors[0:])
# print(colors[:])
# print(colors[:3])
# print("--------")
# print(colors[:-1])
# print(colors[:-2])
# print(colors[-2:-1])
# print(colors[:-2])
# print(colors[:-1])
# print(colors[-2:0])
a = [1, 2, [100, 200, 300], 6]
# print(max(a[2]))
# print(a[2][2])
# for aColor in colors:
#     print(aColor + " xxx")

# FILTRAR DATA
result = list(filter(lambda x: x > 100, [-5, 200, 300, -10, 10, 1000]))
#print(result)

# TRANSFORMACION DE DATA
result2 = list(map(lambda x: x ** 2, [11, 22, 33, 44, 55]), )
#print(result2)

def doSum(x1,x2):
    return x1+x2

x=reduce(doSum,[1,2,3,4,5,6])
#print(x)


"""
FUNCION RANGE
UTILIZADA PARA PODER GENERAR UNA LISTA LARGEA DE NUMEROS , USADA PARA AUTOPOPULAR SECUANDICA DE NUMEROS EN UNA LISTA
"""

x1=range(6)
#print(x1)

oddNum=range(3,10,2)
#print(oddNum)

"""
TUPLES --> ()
A DIFERENCIA DE LA LISTA , LOS TUPLES SON INMUTABLES (solo lectura))
TUPLES USA ()
LISTA USA []
)

LA HABILIDAD DE CREAR ESTRURAS ANIDADAS ES IMPORTANTE PARA LA ITERACION Y RECURSIVIDAD DE ALGORITMOS

TENER EN CONSIDERACION QUE SE DEBE PREFEREIR ESTRUCTURAS INMUTABLES EN LUGAR DE INMUTABLES, POR LO QUE SE DEBE ANALIZAR SI ES NECESARIO REALEMENTE TENER UNA LISTA MUTABLE
"""
#print(colors[1])
#print(colors[2:])
#print(colors[:-1])

a=(1,2,(100,200,300),6)
#print(a[2])
#print(a[2][1])

"""
DICTIONARY --> {}
ENCARGADO DE ALAMCENAR DATA EN EL CONTEXTO LLAVE VALOR
SE PUEDEN CREAR DICIONARIOS ANIDADOS USANDO LOS MISIOS DICIONARIOS COMO EL TIPO DE DATO DE UN VALOR
"""
bin_colors={
        "manual_color":"Yellow",
        "approved_color":"Green",
        "refused_color":"Red"
        }

#print(bin_colors)
#print(bin_colors.get("approved_color"))
#print(bin_colors["approved_color"])

bin_colors["approved_color"]="Purple"
#print(bin_colors)


"""
SETS --> {}
COLLCION DE ELEMENTIOS QUE PUEDEN SER  DE DIFERENETS TIPOS 
LA PRINCIPAL CARACTERISTICA ES QUE LOS VALORES NO PUEDEN SER eEPETIDOS

SET1|SET2 -> UNIIR DOS SETS
SET1&SET2 -> DEVOLVER CONJUNTO COMUN DE DOS SETS
"""
green={"graas","leaves","leaves"}
#print(green)

yellow={"dandelion","fire hydrant","leaves"}
red={"fire hydrant","rose","leaves"}

#print(yellow|red)
#print(yellow&red)


"""
DATAFRAME
ESTRUCTURA DE DATOS PARA ALMACER DATA EN FORMA DE TABLA , DISPOBIVLE EN EL PAQUETE PANDAS, USADO PARA PROCESA DATA ESTRCUTURADA DE MANERA TRADICIONAL
AXIS , ES UNA SOLA COLUMNA O FILA DE UN DATAFREME
AXES , CONJUNTOS DE AXIS
LABEL , NOMBRE DE LA COLUMNA , O FILA

SE PUEDE CREAR UN SUBSET DE LA TABLA YA SEA HACIENDO UNA SELECCION DE COLUMNA O SELECCION DE FILA

"""
df=pd.DataFrame([
        ["1","Juan",32,True],
        ["2","Elena",23,False],
        ["3","Steven",40,True]

    ])
df.columns=["id","name","age","decision"]
print(df)
print("xxxxxxxxxxxxx")

#SELECCION DE COLUMNA
print(df[["name","age"]])

print(df.iloc[:,3])
print(df.iloc[:,2])
print(df.iloc[:,0])

print("xxxxxxxxxxxxx")
#SELECCION DE FILA

print(df.iloc[1:3,:])
print(df[(df.age<35)&(df.decision==True)])

"""
MATRIX
"""
myMatrix=np.array([[11,12,13],[21,22,23],[31,32,33]])
print(myMatrix)
print(myMatrix.transpose())




