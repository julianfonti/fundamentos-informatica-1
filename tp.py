# Trabajo Practico -


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

#Funcion que registra las materias ingresadas por el usuario como aprobadas. Verifica que esté en lista materias, en caso de ser correcto la almacena.
#Para finalizar con el ingreso de materias aprobadas ingresa -1.
# Lista vacía donde se almacenarán los códigos de materias aprobadas
lista_aprobadas = []

# Función para registrar materias aprobadas

def registrar_materias_aprobadas(materias, lista_aprobadas):
    print("Ingresá los códigos de las materias que aprobaste.")
    print("Escribí -1 para terminar.")

    salir = False  # Bandera de control para salir de ciclo while.

    while salir == False:
        codigo = input("Código de materia aprobada: ")

        if codigo == "-1":
            salir = True  # Activamos la bandera para salir del while.
        else:
            i = 0
            materia_encontrada = False

            # Buscamos si el código está en la lista de materias
            while i < len(materias):
                if materias[i][0] == codigo:
                    materia_encontrada = True

                    # Verificamos si ya está en la lista de aprobadas
                    j = 0
                    ya_aprobada = False
                    while j < len(lista_aprobadas):
                        if lista_aprobadas[j] == codigo:
                            ya_aprobada = True
                        j = j + 1

                    if ya_aprobada == False:
                        lista_aprobadas.append(codigo)
                        print("Materia registrada como aprobada:", materias[i][1])
                    else:
                        print("Ya registraste esta materia.")
                i = i + 1

            if materia_encontrada == False:
                print("Código no encontrado en la lista de materias.")


# Funcion que reciba por parametro ID con materia cursada previamente para evaluar si puede cursar una materia siguiente (Puede devolver un booleano como true - false)


def habilitado_para_cursar(lista_con_materias_aprobadas, id_materia_que_quiero_cursar):
    print("Hay que crear la funcion que devuelve si estoy en condiciones de cursar o no la materia")
#FALTA ESTA DEF.

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
        codigo_buscar = input("Ingrese el código de la materia para verificar si se puede cursar online: ")

        # 2 Recorro cada materia dentro de la lista "materias"
        encontrada = False
        for materia in materias:
            # materia[0] es el código de la materia
            if materia[0] == codigo_buscar:
                encontrada = True
                # 3 Verifico si se puede cursar online (último valor de la lista)
                if materia[-1] == True:
                    print("La materia '" + materia[1] + "' se puede cursar online.")
                else:
                    print("La materia '" + materia[1] + "' NO se puede cursar online.")

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
        codigo_buscar = input("Ingrese el código de la materia para verificar si se puede cursar online: ")

        # 2 Recorro cada materia dentro de la lista "materias"
        encontrada = False
        for materia in materias:
            # materia[0] es el código de la materia
            if materia[0] == codigo_buscar:
                encontrada = True
                # 3 Verifico si se puede cursar online (último valor de la lista)
                if materia[-1] == True:
                    print("La materia '" + materia[1] + "' se puede cursar online.")
                else:
                    print("La materia '" + materia[1] + "' NO se puede cursar online.")

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

def formateo_lista(lista):
    largo = len(lista)
    for i in range(largo):
        print(lista[i], end="")
        print()
    return


# hay que setear el ultimo booleano (update: Listo, esta en base a la lista igual de licenciatura habria que evaluar que materias faltan de la ingenieria) jp:espectacular :)
materias = [
    ["3.4.069", "Fundamentos de Informática", [], ["3.4.071"], True],
    ["3.4.164", "Sistemas de Información I", [], ["3.4.207"], True],
    ["2.1.002", "Pensamiento Crítico y Comunicación", [], [], True],
    ["3.4.043", "Teoría de Sistemas", [], [], True],
    ["3.1.050", "Elementos de Álgebra y Geometría", [], ["3.1.051"], False],
    ["3.4.071", "Programación I", ["3.4.069"], ["3.4.074", "3.4.208"], False],
    ["3.3.121", "Sistemas de Representación", [], [], True],
    ["3.2.178", "Fundamentos de Química", [], [], True],
    ["3.4.072", "Arquitectura de Computadores", [], ["3.4.075"], True],
    ["3.1.024", "Matemática Discreta", [], ["3.4.209", "3.4.215"], True],
    ["3.1.051", "Álgebra", ["3.1.050"], ["3.1.052"], False],
    ["3.4.074", "Programación II", ["3.4.071"], ["3.4.077", "3.4.211"], True],
    ["3.4.207", "Sistemas de Información II", ["3.4.164"], [
        "3.4.214", "3.4.211", "3.4.089", "3.4.094"], True],
    ["3.4.075", "Sistemas Operativos", ["3.4.072"], [], True],
    ["3.1.052", "Física I", ["3.1.051"], ["3.1.055"], False],
    ["3.1.053", "Cálculo I", [], ["3.1.054", "3.1.049"], True],
    ["3.4.077", "Programación III", ["3.4.074"], ["3.4.215"], False],
    ["3.4.208", "Paradigma Orientado a Objetos", [
        "3.4.071"], ["3.4.210", "3.4.082"], True],
    ["3.4.078", "Fundamentos de Telecomunicaciones", [], ["3.4.212"], True],
    ["3.4.209", "Ingeniería de Datos I", ["3.1.024"], ["3.4.213", "3.4.211"], False],
    ["3.1.054", "Cálculo II", ["3.1.053"], ["3.1.025"], False],
    ["3.4.210", "Proceso de Desarrollo de Software",
        ["3.4.208"], ["3.4.216", "3.4.218"], False],
    ["3.4.211", "Seminario de Integración Profesional",
        ["3.4.074", "3.4.207", "3.4.209"], [], False],
    ["3.4.212", "Teleinformática y Redes", ["3.4.078"], ["3.4.092"], False],
    ["3.4.213", "Ingeniería de Datos II", ["3.4.209"], ["3.4.217"], False],
    ["3.1.049", "Probabilidad y Estadística", ["3.1.053"],
        ["3.1.056", "3.4.086", "3.4.217"], False],
    ["2.4.216", "Examen de Inglés", [], [], True],
    ["3.4.082", "Aplicaciones Interactivas", ["3.4.208"], ["3.4.218"], False],
    ["3.4.214", "Ingeniería de Software", ["3.4.207"], ["3.4.098"], False],
    ["3.1.055", "Física II", ["3.1.052"], [], False],
    ["3.4.215", "Teoría de la Computación", ["3.1.024", "3.4.077"], [], True],
    ["3.1.056", "Estadística Avanzada", ["3.1.049"], ["3.4.096"], False],
    ["3.4.216", "Desarrollo de Aplicaciones I", ["3.4.210"], [], False],
    ["3.4.089", "Dirección de Proyectos Informáticos", ["3.4.207"], [], False],
    ["3.4.217", "Ciencia de Datos", ["3.1.049", "3.4.213"], [], False],
    ["3.4.092", "Seguridad e Integridad de la Información", ["3.4.212"], [], False],
    ["3.1.025", "Modelado y Simulación", ["3.1.054"], [], False],
    ["OPT1", "Optativa I", [], [], True],
    ["3.4.218", "Desarrollo de Aplicaciones II", ["3.4.082", "3.4.210"], [], False],
    ["3.4.086", "Evaluación de Proyectos Informáticos", ["3.1.049"], [], False],
    ["3.4.096", "Inteligencia Artificial", ["3.1.056"], [], False],
    ["3.4.219", "Tecnología y Medio Ambiente", [], [], True],
    ["PPS06", "Práctica Profesional Supervisada", [], [], True],
    ["OPT2", "Optativa II", [], [], True],
    ["3.4.094", "Arquitectura de Aplicaciones", ["3.4.207"], [], False],
    ["3.4.220", "Tendencias Tecnológicas", [], [], True],
    ["3.4.100", "Proyecto Final de Ingeniería en Informática", [], [], True],
    ["3.4.098", "Calidad de Software", ["3.4.214"], [], False],
    ["OPT3", "Optativa III", [], [], True],
    ["3.4.221", "Negocios Tecnológicos", [], [], True],
    ["3.4.135", "Tecnología e Innovación", [], [], True],
    ["2.3.056", "Derecho Informático", [], [], True]
]

materias_harcodeadas_aprobadas = [
    ["3.4.069", "Fundamentos de Informática", [], ["3.4.071"], True],
    ["3.4.164", "Sistemas de Información I", [], ["3.4.207"], True],
    ["2.1.002", "Pensamiento Crítico y Comunicación", [], [], True],
    ["3.4.043", "Teoría de Sistemas", [], [], True],
    ["3.1.050", "Elementos de Álgebra y Geometría", [], ["3.1.051"], False],
]


programa_inicial = print(
    "Bienvenidos al programa, por favor indique una de las siguientes opciones o -1 para finlalizar el programa")

print("1: Ver plan de estudios completo")
print("2: Ingresar materias aprobadas para ver cuales restan cursar")
print("3: Ver que materias tengo que tener aprobadas, para cursar una materia")
print("4: Ver listado de materias online")
print("5: Ver si una materia esta disponible para cursar online")
#ver si agregamos la función de promedio.
#ver si sumamos la opcion de mostrar nota en materia ya aprobada


opcion_elegida = int(input())
# Ejemplo de uso:

while opcion_elegida != -1:
    # Bucle por si se ingresa un valor fuera de rango. Se solicita que se reingrese una opcion válida
    while opcion_elegida <1 or opcion_elegida >5:

        print('Disculpe, la opcion elegída no es válida, ingrese un numero del 1 al 5 según lo que desee consultar.')
        print("1: Ver plan de estudios completo")
        print("2: Ingresar materias aprobadas para ver cuales restan cursar")
        print("3: Ver que materias tengo que tener aprobadas, para cursar una materia")
        print("4: Ver listado de materias online")
        print("5: Ver si una materia esta disponible para cursar online")
        #ver si agregamos la función de promedio.

        opcion_elegida = int(input())

    if opcion_elegida == 1:
        resultado = listas_de_materias(materias)
        print(formateo_lista(resultado))

    if opcion_elegida == 2:
        print('Ingrese las materias aprobadas para ver cuales restan cursar')
        materias_aprobadas = int(float())
        resultado = listas_de_materias(materias)
        print(formateo_lista(resultado))
        #FALTA ESTA DEF

    if opcion_elegida == 3: #3: Ver que materias tengo que tener aprobadas, para cursar una materia
        resultado = materia_online_id(materias)
        print(formateo_lista(resultado))

    if opcion_elegida == 4: #4: Ver listado de materias online
        resultado = listas_de_materias(materias)
        print(formateo_lista(resultado))

    if opcion_elegida == 5: #5: Ver si una materia esta disponible para cursar online
        resultado = listas_de_materias(materias)
        print(formateo_lista(resultado))
