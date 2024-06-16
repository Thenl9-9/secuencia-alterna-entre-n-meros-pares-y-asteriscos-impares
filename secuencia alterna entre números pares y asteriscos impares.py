def secuencia_impares_1_13(nm): #"def" inica una función que en este caso es "nm"
    total='*' #es nuestra variable para la secuencia de numeros inpares
    totaI=2 #es nuestra variable para la secuencia de numeros pares
    for i in range(1, nm): # en nuestra i se almacenara un numero entre 1 y un valor indefinido representado por nm   
        if i % 2==1: #la condición de nuestro if es un modulo en el cual el resultado deve ser igual a 1, de no cumplirse se usara el else
            print(total)  #   para poder comenzar la secuencia con un '*' debemos de imprimir el resultado antes de seguir con la secuencia completa 
            total=total+'**' # esta le sumara dos '*' al total creando asi la secuencia de numeros impares expresados en '*'
        else: # este se ejecutara si no se cumplen las funciones del if       
            print(totaI) # para comenzar la secuencia con dos, primero debemos imprimir el valor de la variable total
            totaI=(totaI)*2 # para continuar la secuencia multiplicaremos nuestra variable "total" por 2 esto nos indica el numero de veces que se ejecutara todo+
secuencia_impares_1_13(10)