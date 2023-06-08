from romannumbers import *

class RomanNumber:
    def __init__(self, entrada):
        # if isinstance(entrada, int): # funcion d python q comprueva el primer parametro si es str o int
        if type(entrada) == int:
            self._numero = entrada
            self._simbolo = entero_a_romano(entrada)
        elif type(entrada) == str:
            self._numero = romano_a_entero(entrada)
            self._simbolo = entrada
        else:
            raise RomanNumberError("No se admiten decimales")
        
    @property
    def numero(self):
        return self._numero
    
    @numero.setter
    def numero(self, entrada):
        self._numero = entrada
        self._simbolo = entero_a_romano(entrada)
    
    @property
    def simbolo(self):
        return self._simbolo
    
    @simbolo.setter
    def simbolo(self, entrada):
        self._simbolo = entrada
        self._numero = romano_a_entero(entrada)



    '''
    metodos magicos para logica
    ''' 


    def __eq__(self, other):
        other = self.__to_roman(other)
        return self.numero == other.numero
    
    def __lt__(self, other):
        other = self.__to_roman(other)
        return self.numero < other.numero
    
    def __rlt__(self, other):
        return other.__lt__(self)

    def __le__(self, other):
        other = self.__to_roman(other)
        return self.numero <= other.numero
    def __gt__(self, other):
        other = self.__to_roman(other)
        return self.numero > other.numero
    
    def __ge__(self, other):
        other = self.__to_roman(other)
        return self.numero >= other.numero
    
    def __ne__(self, other):
        other = self.__to_roman(other)
        return self.numero != other.numero
    

    '''
    metodos mágicos para aritmética
    '''
    def __to_roman(self, other):
        if not isinstance(other, RomanNumber):
            other = RomanNumber(other)
        return other

    def __add__(self, other):
        if not isinstance(other, RomanNumber):
            other = RomanNumber(other)
        resultado = self.numero + other.numero
        return RomanNumber(resultado)
    
    def __radd__(self, other):
        return self.__add__(other)
    
    def __sub__(self, other):
        if not isinstance(other, RomanNumber):
            other = RomanNumber(other)
        
        return RomanNumber(self.numero - other.numero)
    
    def __rsub__(self, other):
        other = self.__to_roman(other)

        return other.__sub__(self)


        
    def __mod__(self, other):
        if not isinstance(other, RomanNumber):
            other = RomanNumber(other)
        resultado = self.numero % other.numero
        return RomanNumber(resultado)

    def __pow__(self, other):
        if not isinstance(other, RomanNumber):
            other = RomanNumber(other)
        resultado = self.numero ** other.numero
        return RomanNumber(resultado)
    
    def __rpow__(self, other):
        other = self.__to_roman(other)
        return other.__pow__(self)

    def __floordiv__(self, other):
        if not isinstance(other, RomanNumber):
            other = RomanNumber(other)
        resultado = self.numero // other.numero
        return RomanNumber(resultado)
    
    def __rfloordiv__(self, other):
        other = RomanNumber(other)
        return other.__floordiv__(self)
        

    def __mul__(self, otro):
        if not isinstance(otro, RomanNumber):
            otro = RomanNumber(otro)
        resultado = self.numero * otro.numero
        return RomanNumber(resultado)
    
    def __rmul__(self, otro):
        return self.__mul__(otro)
    '''
    metodos magicos para representación
    '''   
    def __repr__(self):
        return f"{self.numero} - {self.simbolo}"
    def __str__(self):
        return self.__repr__()

