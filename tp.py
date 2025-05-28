# Trabajo Practico -


# Acá van a ir y todas las funciones que se van a utilizar para el programa
# ? Funcion que reciba por parametro ID con las materias cursadas (en base al input del usuario) y devuelve como lista la lista de materias filtradas
def programa_restante_post_ingreso_de_materias(lista_con_materias_aprobadas, lista_materias):
    materias_restantes = []
    for i in range(len(lista_materias)):
        ya_aprobada = False
        for j in range(len(lista_con_materias_aprobadas)):
            if lista_materias[i] == lista_con_materias_aprobadas[j]:
                ya_aprobada = True
        if ya_aprobada == False:
            materias_restantes.append(lista_materias[i])
    return materias_restantes


# Funcion que registra las materias ingresadas por el usuario como aprobadas. Verifica que esté en lista materias, en caso de ser correcto la almacena.
# Para finalizar con el ingreso de materias aprobadas ingresa -1.
# Lista vacía donde se almacenarán los códigos de materias aprobadas

# Función para registrar materias aprobadas
def registrar_materias_aprobadas(materias, lista_aprobadas):
    print("Ingresa 0 si querés ver la lista nuevamente")
    print("Ingresá los códigos de las materias que aprobaste.")
    print("Escribí -1 para terminar.")
    codigo = int(input("Código de materia aprobada: "))
    while codigo != -1:
        if codigo == 0:
            recorrer_plan_completo(materias)
        else:
            existe = False
            for materia in materias:
                if materia[0] == codigo:
                    existe = True
                    if codigo in lista_aprobadas:
                        print("Ya ingresaste esa materia previamente")
                    else:
                        lista_aprobadas.append(codigo)
            if existe == False:
                print(
                    "No se encontró ese código de materia. Presione 0 para ver la lista de materias nuevamente")
        codigo = int(input("Código de materia aprobada: "))
    return lista_aprobadas


""" def registrar_materias_aprobadas(materias, lista_aprobadas):
    print("Ingresá los códigos de las materias que aprobaste.")
    print("Escribí -1 para terminar.")
    codigo = int(input("Código de materia aprobada: "))
    while codigo != -1:
        i = 0
        materia_encontrada = False

        # Buscamos el código en la lista de materias
        while i < len(materias):
            if materias[i][0] == codigo:
                materia_encontrada = True

                j = 0
                ya_aprobada = False
                while j < len(lista_aprobadas):
                    if lista_aprobadas[j] == codigo:
                        ya_aprobada = True
                    j = j + 1

                if ya_aprobada == False:x
                    lista_aprobadas.append(codigo)
                    print("Materia registrada como aprobada:", materias[i][1])
                else:
                    print("Ya registraste esta materia.")
            i = i + 1

        if materia_encontrada == False:
            print("Código no encontrado en la lista de materias.")

        codigo = input("Código de materia aprobada: ")
 """

# Funcion que reciba por parametro ID con materia cursada previamente para evaluar si puede cursar una materia siguiente (Puede devolver un booleano como true - false)


def habilitado_para_cursar(lista_con_materias_aprobadas, id_materia_que_quiero_cursar):
    print("Hay que crear la funcion que devuelve si estoy en condiciones de cursar o no la materia")
# FALTA ESTA DEF.

# Funcion que reciba por parametro ID con la materia que quiere cursar y devuelve una lista de materias que necesita cursar previamente para poder cursar la materia deseada.


def materias_necesarias_previas(id_materia_que_quiero_cursar):
    print("hay que crear la funcion que me retorna una lista con las materias que necesito cursar previamente para poder cursarla")


# Funcion que responda si ya puede reclamar el titulo intermedio de la carrera🔥


def titulo_intermedio(lista_con_materias_aprobadas):
    print("Con la lista que me viene como parametro tengo que analizar si estoy en condiciones para reclamar el titulo intermedio o no")


# Funcion que le permita ingresar dichas notas con su materia final y le calcule el promedio que lleva en la carrera


def promedio(notas):
    print("Hay que calcular el promedio")


# Funcion que devuelva listado de materias online
def materias_online(lista_materias):
    nombres = []
    print(lista_materias)
    cantidad_total = len(lista_materias)
    print(cantidad_total)
    index = 0
    while index < cantidad_total:
        if lista_materias[index][4] == True:
            nombre_materia = lista_materias[index][1]
            nombres.append(nombre_materia)
        index = index + 1
    return nombres


# Funcion que devuelve si una materia con ID (pasado por parametro) puede ser cursada por online o no

def materia_online_id(materias):
    verificar = True
    while verificar == True:
        # 1 Pido al usuario que escriba el código de una materia
        codigo_buscar = input(
            "Ingrese el código de la materia para verificar si se puede cursar online: ")

        # 2 Recorro cada materia dentro de la lista "materias"
        encontrada = False
        for materia in materias:
            # materia[0] es el código de la materia
            if materia[0] == codigo_buscar:
                encontrada = True
                # 3 Verifico si se puede cursar online (último valor de la lista)
                if materia[-1] == True:
                    print("La materia '" +
                          materia[1] + "' se puede cursar online.")
                else:
                    print("La materia '" +
                          materia[1] + "' NO se puede cursar online.")

        # 4 Si no se encontró la materia
        if encontrada == False:
            print("Código de materia no encontrado.")

        # 5 Pregunto si quiere verificar otra materia
        respuesta = input("¿Querés verificar otra materia? (si/no): ")
        if respuesta != "si":
            verificar = False
            print("Fin de la verificación.")


def materia_online_id(materias):
    verificar = True
    while verificar == True:
        # 1 Pido al usuario que escriba el código de una materia
        codigo_buscar = input(
            "Ingrese el código de la materia para verificar si se puede cursar online: ")

        # 2 Recorro cada materia dentro de la lista "materias"
        encontrada = False
        for materia in materias:
            # materia[0] es el código de la materia
            if materia[0] == codigo_buscar:
                encontrada = True
                # 3 Verifico si se puede cursar online (último valor de la lista)
                if materia[-1] == True:
                    print("La materia '" +
                          materia[1] + "' se puede cursar online.")
                else:
                    print("La materia '" +
                          materia[1] + "' NO se puede cursar online.")

        # 4 Si no se encontró la materia
        if encontrada == False:
            print("Código de materia no encontrado.")

        # 5 Pregunto si quiere verificar otra materia
        respuesta = input("¿Querés verificar otra materia? (si/no): ")
        if respuesta != "si":
            verificar = False
            print("Fin de la verificación.")

# Valores puestos en array de las materias universitarias


def listas_de_materias(materias):
    nombres = []
    cantidad_de_materias_totales = len(materias)
    index = 0
    while index < cantidad_de_materias_totales:
        nombre_materia = materias[index][1]
        nombres.append(nombre_materia)
        index = index + 1
    return nombres


# formateo de lista
def recorrer_plan_completo(lista):
    largo = len(lista)
    for i in range(largo):
        # printeo unicamente el nombre que esta en la segunda posicion de cada lista
        print(lista[i][0], "-", lista[i][1])


def menu_seleccionado(opcion_elegida, materias):
    print("Bienvenido al sistema de consulta de materias de la carrera de Ingeniería en Informática.")
    if opcion_elegida == 1:
        # resultado = listas_de_materias(materias)
        # print(formateo_lista(resultado))
        recorrer_plan_completo(materias)

    if opcion_elegida == 2:
        print('Ingrese las materias aprobadas para ver cuales restan cursar')
        registrar_materias_aprobadas(materias, lista_materias_aprobadas)
        print(lista_materias_aprobadas)
        # FALTA ESTA DEF

    if opcion_elegida == 3:  # 3: Ver que materias tengo que tener aprobadas, para cursar una materia
        resultado = materia_online_id(materias)
        # print(formateo_lista(resultado))

    if opcion_elegida == 4:  # 4: Ver listado de materias online
        resultado = listas_de_materias(materias)
        # print(formateo_lista(resultado))

    if opcion_elegida == 5:  # 5: Ver si una materia esta disponible para cursar online
        resultado = listas_de_materias(materias)
        # print(formateo_lista(resultado))


# hay que setear el ultimo booleano (update: Listo, esta en base a la lista igual de licenciatura habria que evaluar que materias faltan de la ingenieria) jp:espectacular :)
materias = materias = [
    [1, "Fundamentos de Informática", [], [6], True],
    [2, "Sistemas de Información I", [], [13], True],
    [3, "Pensamiento Crítico y Comunicación", [], [], True],
    [4, "Teoría de Sistemas", [], [], True],
    [5, "Elementos de Álgebra y Geometría", [], [11], False],
    [6, "Programación I", [1], [12, 18], False],
    [7, "Sistemas de Representación", [], [], True],
    [8, "Fundamentos de Química", [], [], True],
    [9, "Arquitectura de Computadores", [], [14], True],
    [10, "Matemática Discreta", [], [19, 30], True],
    [11, "Álgebra", [5], [15], False],
    [12, "Programación II", [6], [17, 22], True],
    [13, "Sistemas de Información II", [2], [29, 22, 35, 42], True],
    [14, "Sistemas Operativos", [9], [], True],
    [15, "Física I", [11], [33], False],
    [16, "Cálculo I", [], [20, 26], True],
    [17, "Programación III", [12], [30], False],
    [18, "Paradigma Orientado a Objetos", [6], [21, 28], True],
    [19, "Fundamentos de Telecomunicaciones", [], [24], True],
    [20, "Ingeniería de Datos I", [10], [25, 22], False],
    [21, "Cálculo II", [16], [36], False],
    [22, "Proceso de Desarrollo de Software", [18], [32, 38], False],
    [23, "Seminario de Integración Profesional", [12, 13, 20], [], False],
    [24, "Teleinformática y Redes", [19], [34], False],
    [25, "Ingeniería de Datos II", [20], [37], False],
    [26, "Probabilidad y Estadística", [16], [40, 45, 37], False],
    [27, "Examen de Inglés", [], [], True],
    [28, "Aplicaciones Interactivas", [18], [38], False],
    [29, "Ingeniería de Software", [13], [47], False],
    [30, "Física II", [15], [], False],
    [31, "Teoría de la Computación", [10, 17], [], True],
    [32, "Estadística Avanzada", [26], [44], False],
    [33, "Desarrollo de Aplicaciones I", [22], [], False],
    [34, "Dirección de Proyectos Informáticos", [13], [], False],
    [35, "Ciencia de Datos", [26, 25], [], False],
    [36, "Seguridad e Integridad de la Información", [24], [], False],
    [37, "Modelado y Simulación", [21], [], False],
    [38, "Optativa I", [], [], True],
    [39, "Desarrollo de Aplicaciones II", [28, 22], [], False],
    [40, "Evaluación de Proyectos Informáticos", [26], [], False],
    [41, "Inteligencia Artificial", [32], [], False],
    [42, "Tecnología y Medio Ambiente", [], [], True],
    [43, "Práctica Profesional Supervisada", [], [], True],
    [44, "Optativa II", [], [], True],
    [45, "Arquitectura de Aplicaciones", [13], [], False],
    [46, "Tendencias Tecnológicas", [], [], True],
    [47, "Proyecto Final de Ingeniería en Informática", [], [], True],
    [48, "Calidad de Software", [29], [], False],
    [49, "Optativa III", [], [], True],
    [50, "Negocios Tecnológicos", [], [], True],
    [51, "Tecnología e Innovación", [], [], True],
    [52, "Derecho Informático", [], [], True]
]


materias_harcodeadas_aprobadas = [
    ["3.4.069", "Fundamentos de Informática", [], ["3.4.071"], True],
    ["3.4.164", "Sistemas de Información I", [], ["3.4.207"], True],
    ["2.1.002", "Pensamiento Crítico y Comunicación", [], [], True],
    ["3.4.043", "Teoría de Sistemas", [], [], True],
    ["3.1.050", "Elementos de Álgebra y Geometría", [], ["3.1.051"], False],
]


lista_materias_aprobadas = [

]


def recorrer_menu():
    print("Ingrese una opción del menú:")
    for i in range(len(Lista_menu)):
        print(Lista_menu[i])


Lista_menu = [
    "1: Ver plan de estudios completo",
    "2: Ingresar materias aprobadas para ver cuales restan cursar",
    "3: Ver que materias tengo que tener aprobadas, para cursar una materia",
    "4: Ver listado de materias online",
    "5: Ver si una materia esta disponible para cursar online"]
# ver si agregamos la función de promedio.
# ver si sumamos la opcion de mostrar nota en materia ya aprobada


def main(materias):
    opcion_elegida = 0
    while opcion_elegida != -1:
        recorrer_menu()
        opcion_elegida = int(input())
        if opcion_elegida >= 1 and opcion_elegida <= len(Lista_menu):
            menu_seleccionado(opcion_elegida, materias)
            opcion_elegida = 0
        else:
            print("Opción no válida. Por favor, ingrese una opción del menú:")
            recorrer_menu()
        opcion_elegida = int(input())


main(materias)
