from datetime import date

class Empleado:
    def __init__(self, nombre, apellidos, dni, tiempo_en_empresa):
        self.nombre = nombre
        self.apellidos = apellidos
        self.dni = dni
        self.tiempo_en_empresa = tiempo_en_empresa

    def mostrar_informacion(self):
        print(f'Nombre: {self.nombre}')
        print(f'Apellidos: {self.apellidos}')
        print(f'DNI: {self.dni}')
        print(f'Tiempo en la empresa: {self.tiempo_en_empresa} meses')


class Desarrollador(Empleado):
    salario_base = 3500.00
    porcentaje_aumento = 0.05

    def __init__(self, nombre, apellidos, dni, tiempo_en_empresa, lenguaje_programacion):
        super().__init__(nombre, apellidos, dni, tiempo_en_empresa)
        self.lenguaje_programacion = lenguaje_programacion
        self.salario = CalculadorContable.calcular_salario(
            Desarrollador.salario_base,
            tiempo_en_empresa,
            Desarrollador.porcentaje_aumento
        )

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f'Lenguaje de programación: {self.lenguaje_programacion}')
        print(f'Salario: S/{self.salario:.2f}')


class Diseñador(Empleado):
    salario_base = 2200.00
    porcentaje_aumento = 0.03

    def __init__(self, nombre, apellidos, dni, tiempo_en_empresa, programa_diseño):
        super().__init__(nombre, apellidos, dni, tiempo_en_empresa)
        self.programa_diseño = programa_diseño
        self.salario = CalculadorContable.calcular_salario(
            Diseñador.salario_base,
            tiempo_en_empresa,
            Diseñador.porcentaje_aumento
        )

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f'Programa de diseño: {self.programa_diseño}')
        print(f'Salario: S/{self.salario:.2f}')


class CalculadorContable:
    @staticmethod
    def calcular_salario(salario_base, tiempo_en_empresa, porcentaje_aumento):
        if tiempo_en_empresa > 6:
            aumento = (tiempo_en_empresa - 6) * salario_base * porcentaje_aumento
            return salario_base + aumento
        else:
            return salario_base

    @staticmethod
    def calcular_cts(empleado):
        mes_actual = date.today().month
        if mes_actual == 5 or mes_actual == 11:
            cts = (empleado.salario / 12) * empleado.tiempo_en_empresa / 12
            print(f'{empleado.nombre} {empleado.apellidos} - CTS a depositar: S/{cts:.2f}')
        else:
            print('Error: No es un mes de pago de CTS (mayo o noviembre).')


# Ejemplo de uso
desarrollador = Desarrollador('Juan', 'Perez', '12345678', 8, 'Python')
diseñador = Diseñador('Maria', 'Lopez', '87654321', 4, 'Photoshop')

desarrollador.mostrar_informacion()
print('---')
diseñador.mostrar_informacion()
print('---')

CalculadorContable.calcular_cts(desarrollador)
CalculadorContable.calcular_cts(diseñador)
