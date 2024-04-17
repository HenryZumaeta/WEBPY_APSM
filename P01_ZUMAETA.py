def pedir_datos_empleado():
    empleado = {
        'id': input("- Id: ").strip(),
        'nombre': input("- Nombre completo: ").strip(),
        'dni': input("- DNI: ").strip(),
        'telefono': input("- Telefono: ").strip(),
        'tiempo_trabajando': int(input("- Tiempo trabajando (meses): ").strip()),
        'cargo': input("- Cargo: ").strip().lower(),
    }
    return empleado

def calcular_salario(cargo):
    salarios = {
        'limpieza': 1025,
        'mesero': 1500,
        'cajero': 1500,
        'vigilante': 1400,
        'gerente': 2500
    }
    return salarios.get(cargo, 0)

def visualizar_informacion_empleado(registro_empleados):
    id_empleado = input(">>> Ingrese el Id del empleado: ")
    if id_empleado in registro_empleados:
        empleado = registro_empleados[id_empleado]
        for clave, valor in empleado.items():
            print(f"{clave.title()}: {valor}")
    else:
        print(">>> Lo sentimos, no se encontró un empleado con ese Id.")

def mostrar_empleado_minimo_tiempo(registro_empleados):
    min_tiempo = min(registro_empleados.values(), key=lambda x: x['tiempo_trabajando'])['tiempo_trabajando']
    empleados_min = [emp for emp in registro_empleados.values() if emp['tiempo_trabajando'] == min_tiempo]
    for emp in empleados_min:
        print(f"Id: {emp['id']}\nNombre: {emp['nombre']}\nTiempo trabajando (meses): {emp['tiempo_trabajando']}")

def actualizar_salario_empleado(registro_empleados):
    id_empleado = input(">>> Ingrese el Id del empleado: ")
    if id_empleado in registro_empleados:
        try:
            aumento = float(input(">>> Ingrese el aumento que recibirá el empleado en soles: "))
            registro_empleados[id_empleado]['salario'] += aumento
            print(f"Nuevo salario: S/ {registro_empleados[id_empleado]['salario']}")
        except ValueError:
            print(">>> Error: Ingrese un número válido.")

def ingresar_empleados(registro_empleados):
    while True:
        empleado = pedir_datos_empleado()
        empleado['salario'] = calcular_salario(empleado['cargo'])
        registro_empleados[empleado['id']] = empleado
        if input("> ¿Quiere ingresar un nuevo empleado al registro? (Si/ No): ").strip().lower() != 'si':
            break

def mostrar_menu(registro_empleados):
    while True:
        print("""
====================== Gestión de Empleados =======================
|| 1. Visualizar información de un empleado.                      ||
|| 2. Mostrar empleado cuyo tiempo en la empresa sea el menor.    ||
|| 3. Actualizar salario de un empleado.                          ||
|| 4. Terminar programa.                                          ||
===================================================================
""")
        opcion = input("> Elija la opción que desee realizar (1/2/3/4): ").strip()
        if opcion == '1':
            visualizar_informacion_empleado(registro_empleados)
        elif opcion == '2':
            mostrar_empleado_minimo_tiempo(registro_empleados)
        elif opcion == '3':
            actualizar_salario_empleado(registro_empleados)
        elif opcion == '4':
            print("El programa ha finalizado. ¡Hasta la próxima!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

def main():
    registro_empleados = {}
    ingresar_empleados(registro_empleados)
    mostrar_menu(registro_empleados)

if __name__ == "__main__":
    main()
