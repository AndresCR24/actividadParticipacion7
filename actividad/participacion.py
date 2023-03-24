from dataclasses import dataclass

@dataclass
class Elemento:
    nombre: str
    
    def __eq__(self, other):
        if isinstance(other, Elemento):
            return self.nombre == other.nombre
        return False
    
class Conjunto:
    contador = 0

    def __init__(self, nombre):
        self.__id = Conjunto.contador
        Conjunto.contador += 1
        self.nombre = nombre
        self.__elementos = []

    @property
    def __id(self):
        return self.__id

    def contiene(self, elemento):
        return any(e == elemento for e in self.__elementos)

    def agregar_elemento(self, elemento):
        if not self.contiene(elemento):
            self.__elementos.append(elemento)

    def __add__(self, other):
        resultado = Conjunto(f"{self.nombre} + {other.nombre}")
        for elemento in self.__elementos:
            resultado.agregar_elemento(elemento)
        for elemento in other.__elementos:
            resultado.agregar_elemento(elemento)
        return resultado
    
    def intersectar(cls, conjunto1, conjunto2):
        resultado = Conjunto(f"{conjunto1.nombre} INTERSECTADO {conjunto2.nombre}")
        for elemento in conjunto1.__elementos:
            if conjunto2.contiene(elemento):
                resultado.agregar_elemento(elemento)
        return resultado

    def __str__(self):
        elementos_str = ", ".join(str(e) for e in self.__elementos)
        return f"Conjunto {self.nombre}: ({elementos_str})"
