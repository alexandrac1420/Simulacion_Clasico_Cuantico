# Simulador de Clásico a Cuántico
En este módulo, vamos a explorar cómo pasamos de entender las cosas de manera clásica a adentrarnos en el intrigante mundo de la física cuántica. Empezaremos observando sistemas donde todo es predecible y los gráficos son simples. Luego, nos sumergiremos en números reales para entender cómo modelar sistemas con probabilidades, típicos en el mundo clásico. Finalmente, nos aventuraremos en el uso de números complejos, lo que nos llevará al emocionante terreno de los modelos cuánticos.

Para hacer este viaje más claro, utilizaremos experimentos como el de las canicas con coeficientes booleanos, los experimentos de las múltiples rendijas clásicas probabilísticas (con más de dos rendijas) y los experimentos de las múltiples rendijas cuánticas.
## Operaciones disponibles 
Dentro del programa se pueden realizar las siguientes operaciones:
* Simulación de sistemas deterministicos (canicas booleanas)
* Simulación de sistemas probabilisticos
* Simulacion de sistemas cuánticos

Las simulaciones de los sistemas probabilisticos junto con las cuanticas generan un diagrama de barras donde se muestran las probabilidades de cada uno de los estados según el número de clicks ingresados.
## ¿Cómo obtener una copia del repositorio?
### Pre-requisitos
Antes de comenzar con la ejecución de este proyecto, es necesario asegurarse de que se tiene instalado Python en su computador, debido a que este es el lenguaje de programación utilizado para desarrollar este proyecto. 
En caso de no tenerlo siga los siguientes pasos:
1. Dirigirse a la página https://www.python.org/downloads/
2. Dar click en la opción de descarga
   ![image](https://github.com/alexandrac1420/CNYT/assets/138069735/03d02dfb-a346-4bc8-8e9c-066816e2f80e)
3. Ejecutar el programa que se descarga automáticamente.

### Instalación 
Para instalar la librería debe tener en cuenta estos pasos:
1. Abra la carpeta en donde desea guardar la librería.
2. De click derecho y seleccione la opción "Git Bash"
3. Clone el repositorio utilizando el comando 'https://github.com/alexandrac1420/Libreria_Vectores_Matrices_Complejas.git'
4. Importe el modulo de la libreria en el programa que vaya a utilizar.
   
Completado el proceso anterior podrá trabajar con la librería proporcionada.

Ademas se recomienda descargar la libreria de phyton numpy. Esta se puede descargar de la siguiente manera:
1. Abre una terminal o línea de comandos en tu sistema.
2. Ejecuta el siguiente comando: 'pip install numpy'
3. Una vez que la instalación se complete con éxito, abre el intérprete de Python y ejecuta 'import numpy as np'. Si no se produce ningún error, significa que NumPy se ha instalado correctamente.

## Modo de uso
Para utilizar esta librería es necesario conocer la estructura de entrada de las operaciones disponibles junto con la sintaxis adecuada de cada una de las operaciones.

### Representación 
El programa reconoce de entrada de numero complejo una parte real y una imaginaria representadas en tuplas. Por ejemplo, si quiero realizar alguna operación con el numero 5 + 2i, este se ingresará al programa de la siguiente manera complex(5,2).

Para ingresar un vector de números complejos se debe seguir la siguiente estructura __vector = [complex(numero1), complex(numero2)]__

Para ingresar una matriz de números complejos se debe ingresar las filas en el formato de los vectores __matriz = [[complex(numero1), complex(numero2)], [complex(numero3), complex(numero4)]]__, siendo la primera fila  _[complex(numero1), complex(numero2)]_ y la segunda  _[complex(numero3), complex(numero4)]_

### Sintaxis operaciones 
A continuación se presenta la sintaxis correcta para el uso de las operaciones disponibles:
* __Simulador del experimento de las canicas booleanas__:simulaCanicas (_matriz de comportamiento, vector del estado inicial, numero de clicks_)
* __Simulador del experimento múltiples rendijas clásico probabilístico, con más de dos rendijas.__:simul_multi_slit (_matriz de comportamiento, numero de clicks_)
* __Simulador del experimento de las múltiples rendijas cuántico__:simul_multi_slit_imag (_matriz de comportamiento, numero de clicks_)

Tenga en cuenta que es necesario utilizar la representacion de los numeros mencionada anteriormente.

### Ejemplo de uso 
~~~python
import numpy as np
import ClasicoCuantico as lb

#Ejemplo de uso del simulador de un sistema deterministico

# Ingrese la matriz del comportamiento del sistema, junto con el vector de valores iniciales
# y el numero de clicks en el que desea ver el estado
m1 = np.array([[1,0,0],[0,1,0],[0,0,1]])
v1 = [2,3,5]
clicks = 3

#Realice la simulación
resultado_deterministico = lb.simulaCanicas(m1,v1,clicks)
print(resultado_deterministico)

# Ejemplo del simulador de un sistema probabilistico

# Ingrese la matriz del comportamiento del sistema en numeros reales
m2= np.array([[0,0,0,0,0,0,0],[1/3,0,0,0,0,0,0],[1/3,0,0,0,0,0,0],[1/3,0,0,0,0,0,0],[0,1/2,0,0,1,0,0],[0,1/2,1/2,0,0,1,0],[0,0,1/2,0,0,0,1]])
clicks = 2

#Realice la simulación
# Por defecto se genera un diagrama de barras con las probabilidades del vector resultante
resultado_probabilistico = lb.simul_multi_slit(m2, clicks)
print(resultado_probabilistico)

# Ejemplo del simulador de un sistema cuantico

# Ingrese la matriz del comportamiento del sistema en numeros imaginarios
m3= np.array([[1/2,1,0],[complex(0,-1/2),complex(0,1/2),0],[0,0,complex(0,1)]])
clicks = 2

#Realice la simulación
# Por defecto se genera un diagrama de barras con las probabilidades del vector resultante
resultado_cuantico = lb.simul_multi_slit_imag(m3, clicks)
print(resultado_cuantico)

~~~


## Construido con
* Phyton 3.11.4
  
## Autor 
__Alexandra Cortes Tovar__ 
