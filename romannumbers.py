
unidades = {
    1: "I",
    5: "V",
    10: "X"
}

decenas = {
    1: "X",
    5: "L",
    10: "C"
}

centenas = {
    1: "C",
    5: "D",
    10: "M"
}

millares = {

    1: "M"
}


class RomanNumberError(Exception):
    pass

def listar_numero(num):
    n_mil = num // 1000 * 1000
    n_cent = (num % 1000) // 100 * 100
    n_dec = (num % 100) // 10 * 10
    n_uni = (num % 10)

    return n_mil, n_cent, n_dec, n_uni 

def sacar_clave(num):

    if num >= 1000:
        clave = millares
        num = num // 1000

    elif num >= 100:
        clave = centenas
        num //= 100

    elif num >= 10:
        clave = decenas
        num = num // 10
    else:
        clave = unidades
    return clave, num

def logica_aplastante(digito, clau):
    res = ""

    if digito < 4:
        res += digito * clau[1]

    elif digito == 4:
        res += clau[1] + clau[5]

    elif digito < 9:
        num_palitos = digito - 5
        res += clau[5] + num_palitos * clau[1]

    else:
        res += clau[1] + clau[10]

    return res

def entero_a_romano(n_int):
    if n_int > 3999:
        raise RomanNumberError("RomanNumber must be less of 4000")

    digitos = listar_numero(n_int)

    resultado = ""
    for digito in digitos:
        if digito == 0:
            continue

        clave, digito = sacar_clave(digito)
        resultado += logica_aplastante(digito, clave)
       
    return resultado




numeros_romanos = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}

def comprueba_excepciones(romano):
    for simbolo in numeros_romanos:
        if simbolo * 4 in romano:
            raise RomanNumberError("No se admiten más de tres símbolos iguales")
        elif simbolo in "VLD" and simbolo * 2 in romano:
            raise RomanNumberError("No se pueden repetir V, L, o D")

def romano_a_entero(letras):

    valor_total = 0
    ultimo_valor = 0
    valor_final = 0

    comprueba_excepciones(letras)

    for numeral in reversed(letras):
        valor_actual = numeros_romanos[numeral]

        if valor_actual <= 5 and ultimo_valor >= 50:
            raise RomanNumberError("Resta no permitida")
        
        if valor_actual <= 50 and ultimo_valor >= 500:
            raise RomanNumberError("Resta no permitida")

        if valor_actual < valor_final:
            raise RomanNumberError("No esta ordenado de forma ascendente")

        elif valor_final == valor_actual and ultimo_valor > valor_actual:
            raise RomanNumberError("Otras dos restas seguidas")

        if valor_actual >= ultimo_valor:
            valor_total += valor_actual
            
        elif numeral not in "VLD": 
            valor_total -= valor_actual
                
        else:
            raise RomanNumberError("Resta de multiplo de 5 no permitida")
        
        valor_final = ultimo_valor
        ultimo_valor = valor_actual # Si el if i el else comparten lo mismo podemos sacarlos fuera, aqui actualizamos el ultimo valor.
        
    return valor_total




if __name__ == "__main__":
    print(entero_a_romano(11))
























































''' 
# Diccionario de Símbolos Romanos
simbolos = {
    1: "I", 4: "IV", 5: "V",
    9: "IX", 10: "X", 40: "XL",
    50: "L", 90: "XC", 100: "C",
    400: "CD", 500: "D", 900: "CM",
    1000: "M"
}

# Función convertir cualquier numero a romano
def entero_a_romano(n_ent):

    resultado = ""
    n  = n_ent
    numeros = sorted(simbolos.keys(), reverse=True) # Descomponemos el numero de mayor a menor con los valores del diccionario 

    # Encuentra el valor mas alto que tenga el diccionario segun la entrada y le resta el valor del diccionario. Acomula en Resultado los simbolos del diccionario
    for num in numeros:

        while n_ent >= num:

            resultado += simbolos[num]
            n_ent -= num

    return resultado

# Cojemos el numero y lo dividimos en subcadenas de 3, en caso de no ser completa la subcadena la rellena de 0 para que no pete. 
def longitud(numero):

    numero = str(numero)

    while len(numero)%3 != 0:
        numero= "0" + numero

    return numero

# Esta función añade n paréntesis en función de la necesidad de los mismos, además, tiene la lógica incorporada para los numeros menores a 3999 y superiores al mismo.
def devolver_total_romano(numero):

    num = str(numero)
    simbolo_romano = ""
    num_parentesis = 0

    # Elige entre los numeros iferiores a 4 digitos o superiores al mismo
    if len(num) <= 4:

        if numero<=3999: # Coge los numeros inferiores al límite del conteo romano simple

            simbolo_romano = entero_a_romano(numero)

        else: # Captura apartir del 4000 y le añade la lógica del parentesis. Controla el error de las 4M envez del (IV)

            simbolo_romano = "(" + entero_a_romano(int(num[0])) + ")"
            simbolo_romano = simbolo_romano + entero_a_romano(int(num[-3:]))

    else: # Todos los numeros superiores a 4 dígitos entran por aquí

        num = longitud(num)

        while len(num) != 0: # Mientras la lonitud del numero sea mayor a 4 se concatena la representación en numeros romanos de los últimos 3 dígitos 
                
                vari = entero_a_romano(int(num[-3:]))
                if vari != "":
                         
                    simbolo_romano = "("* num_parentesis + vari + ")" * num_parentesis + simbolo_romano
               
                # Si esta vacía la cadena se restablece.
                if simbolo_romano == "()":
                    simbolo_romano = ""

                num = num[:-3]
                num_parentesis += 1

    return simbolo_romano



print(devolver_total_romano(1))
print(devolver_total_romano(10))
print(devolver_total_romano(100))
print(devolver_total_romano(1000))
print(devolver_total_romano(3999))
print(devolver_total_romano(10000))
print(devolver_total_romano(100000))
print()
print(devolver_total_romano(1000000))
print(devolver_total_romano(4000000))
print(devolver_total_romano(3999999))
print(devolver_total_romano(4000004040004000040000))

#un millon es = (M)



'''