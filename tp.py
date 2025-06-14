import os

# Función para limpiar la consola de forma multiplataforma


def limpiar_consola():
    if os.name == 'nt':
        os.system('cls')  # Windows
    else:
        os.system('clear')  # Unix (Linux, macOS, iOS)


def mostrar_bienvenida():
    print("\n" * 2)
    print("****************************************************")
    print("*                                                  *")
    print("*        BIENVENIDO AL SISTEMA DE GESTIÓN          *")
    print("*                                                  *")
    print("*           DE MATERIAS UNIVERSITARIAS             *")
    print("*                                                  *")
    print("*        Creado por Iair, Julian y Juan Pablo      *")
    print("*                                                  *")
    print("****************************************************")
    print("\n" * 2)


# Acá van a ir y todas las funciones que se van a utilizar para el programa
# ? Funcion que reciba por parametro ID con las materias cursadas (en base al input del usuario) y devuelve como lista la lista de materias filtradas
#! flowchart listo
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


# def pedirle_materia_al_usuario():

# Funcion que registra las materias ingresadas por el usuario como aprobadas. Verifica que esté en lista materias, en caso de ser correcto la almacena.
# Para finalizar con el ingreso de materias aprobadas ingresa -1.
# Lista vacía donde se almacenarán los códigos de materias aprobadas

# Función para registrar materias aprobadas
#! ya esta el flawchart
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
    
    lista_aprobadas = ordenar_lista_enteros(lista_aprobadas) #! anotar en el flawchart que se ordena la lista de materias aprobadas
    return lista_aprobadas


def ordenar_lista_enteros(lista):
    n = len(lista)
    if n > 1:
        for i in range(n): 
            for j in range(0, n-i-1):
                if lista[j] > lista[j+1]:
                    temp = lista[j]
                    lista[j] = lista[j+1]
                    lista[j+1] = temp
    
    return lista

# funcin que devuelve true o false si pueede cursar una materia o no


""" 
def puede_cursar_materia(codigo_materia, lista_materias_aprobadas, materias):
    # Recorremos la lista de materias aprobadas
    correlativas = verificar_correlativas(codigo_materia, materias)
    puede_cursar = True
    if len(correlativas) == 0:
        # Si no tiene correlativas, puede cursar la materia
        print("La materia con código", codigo_materia, "no tiene correlativas.")

    else:
        for i in range(len(correlativas)):  # [5]
            tiene_materia_aprobada = False

            # Verificamos si cada correlativa está en la lista de materias aprobadas
            for j in range(len(lista_materias_aprobadas)):  # [,]
                nombre_materia_a_cursar = devolver_nombre_segun_codigo(
                    codigo_materia, materias)
                if correlativas[i] == lista_materias_aprobadas[j]:
                    nombre_correlativa = devolver_nombre_segun_codigo(
                        correlativas[i], materias)
                    print("Tiene aprobada la correlativa: ", nombre_correlativa)
                    tiene_materia_aprobada = True

            if tiene_materia_aprobada == False:
                # Si alguna correlativa no está aprobada, no puede cursar la materia
                nombre_correlativa = devolver_nombre_segun_codigo(
                    correlativas[i], materias)
                print("No puede cursar la materia: ", nombre_materia_a_cursar,
                      "porque le falta aprobar la correlativa: ", nombre_correlativa)
                puede_cursar = False

    # Si no encontramos el código, devolvemos False
    return puede_cursar """

#! Flowchart hecho


def puede_cursar_materia(codigo_materia, lista_materias_aprobadas, materias):
    correlativas = verificar_correlativas(codigo_materia, materias)
    aprobadas = []
    faltantes = []

    for i in range(len(correlativas)):
        esta_aprobada = False
        for j in range(len(lista_materias_aprobadas)):
            if correlativas[i] == lista_materias_aprobadas[j]:
                esta_aprobada = True
        nombre_correlativa = devolver_nombre_segun_codigo(
            correlativas[i], materias)
        if esta_aprobada:
            aprobadas.append(nombre_correlativa)
        else:
            faltantes.append(nombre_correlativa)

    nombre_materia = devolver_nombre_segun_codigo(codigo_materia, materias)

    if len(correlativas) == 0:
        print("La materia con código", codigo_materia, "no tiene correlativas.")
    elif len(faltantes) == 0:
        print("Puede cursar la materia:", nombre_materia)
        print("Tiene aprobadas todas las correlativas:")
        for nombre in aprobadas:
            print("-", nombre)
    else:
        print("No puede cursar la materia:", nombre_materia)
        if len(aprobadas) > 0:
            print("Ya tiene aprobadas:")
            for nombre in aprobadas:
                print("-", nombre)
        print("Le falta aprobar:")
        for nombre in faltantes:
            print("-", nombre)


# Funcion que reciba por parametro ID con materia cursada previamente para evaluar si puede cursar una materia siguiente (Puede devolver un booleano como true - false)

#! flowchart iair
# ? No es mejorar retornar las correlativas en vez de estar retornando los pendientes, porque retornamos los pendientes??


def verificar_correlativas(codigo_materia, materias):
    pendientes = []
    indice = 0

    # Buscamos la materia inicial y agregamos sus correlativas directas a pendientes
    for i in range(len(materias)):
        if materias[i][0] == codigo_materia:
            correlativas = materias[i][2]
            for cod_corr in correlativas:
                pendientes.append(cod_corr)

    # Ahora recorremos correlativas en cadena
    while indice < len(pendientes):
        actual = pendientes[indice]
        indice = indice + 1
        for i in range(len(materias)):
            if materias[i][0] == actual:
                correlativas = materias[i][2]
                for cod_corr in correlativas:
                    # Chequear que no esté ya en pendientes
                    ya_esta = False
                    for x in range(len(pendientes)):
                        if pendientes[x] == cod_corr:
                            ya_esta = True
                    if ya_esta == False:
                        pendientes.append(cod_corr)
    
    return pendientes

# Funcion que devuelva listado de materias online

#! flowchart iair


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
#! flowchart iair
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

# ? Estamos repitiendo codigo, cual va?


def materia_online_id(materias):
    verificar = True
    while verificar == True:
        # 1 Pido al usuario que escriba el código de una materia
        codigo_buscar = int(input(
            "Ingrese el código de la materia para verificar si se puede cursar online: "))

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

        print(lista[i][0], "-", lista[i][1])


def recorrer_menu():
    print("Ingrese una opción del menú:")
    for i in range(len(lista_menu)):
        print(lista_menu[i])


def devolver_nombre_segun_codigo(codigo, materias):
    nombre_materia = ""
    for i in range(len(materias)):
        if materias[i][0] == codigo:
            nombre_materia = materias[i][1]
    return nombre_materia


def consulta_correlativas_necesarias(mensaje, funcion, materias):
    codigo = 0
    while codigo != -1:
        codigo = int(input("Ingrese el código de la materia que desea verificar (o -1 para salir): "))
        if codigo != -1:
            lista_requerimientos = verificar_correlativas(codigo, materias)
            if len(lista_requerimientos) == 0:
                print("La materia no tiene correlativas.")
            else:
                print("Correlativas necesarias para cursar la materia:")
                for i in range(len(lista_requerimientos)):
                    cod = lista_requerimientos[i]
                    print("-", cod, ":", devolver_nombre_segun_codigo(cod, materias))

def bucle_consulta_dos_param(mensaje, funcion, materias, lista_materias_aprobadas):
    codigo = 0
    while codigo != -1:
        codigo = int(input(mensaje))
        if codigo != -1:
            funcion(codigo, lista_materias_aprobadas, materias)


def listar_matrias_aprobadas(lista_materias_aprobadas):

    for i in range(len(lista_materias_aprobadas)):
        for j in range(len(materias)):
            if lista_materias_aprobadas[i] == materias[j][0]:
                print("Materia aprobada: ✅",
                      materias[j][1], "- Código:", materias[j][0])


def mostrar_materias_online(materias):
    print("Listado de materias que se pueden cursar online:")
    rango = range(len(materias))
    for i in rango:
        if materias[i][4] == True:
            print(materias[i][0], "-", materias[i][1])


def menu_seleccionado(opcion_elegida, materias, lista_materias_aprobadas):
    # lista_materias_aprobadas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52] # Lista de materias aprobadas para pruebas
    lista_materias_aprobadas = []

    print("Bienvenido al sistema de consulta de materias de la carrera de Ingeniería en Informática.")
    if opcion_elegida == 1:
        # resultado = listas_de_materias(materias)
        # print(formateo_lista(resultado))
        recorrer_plan_completo(materias)

    if opcion_elegida == 2:
        print('Ingrese las materias aprobadas para ver cuales restan cursar')
        lista_materias_aprobadas = registrar_materias_aprobadas(materias, lista_materias_aprobadas)
        listar_matrias_aprobadas(lista_materias_aprobadas)
    
        # FALTA ESTA DEF

    if opcion_elegida == 3:
        lista_requerimientos = consulta_correlativas_necesarias(
            "Ingrese el código de la materia que desea verificar (o -1 para salir): ",
            verificar_correlativas,
            materias
        )
        

    if opcion_elegida == 4:
        if realizo_ingreso_materias == False:
            print("Primero debe ingresar las materias aprobadas.(opcion 2)")
        else: 
            bucle_consulta_dos_param(
            "Ingrese el código de la materia que desea verificar (o -1 para salir): ",
            puede_cursar_materia,
            materias,
            lista_materias_aprobadas
        )

    if opcion_elegida == 5:  # 5: Ver si una materia esta disponible para cursar online
        mostrar_materias_online(materias)

    if opcion_elegida == 6:  # 6: Ver si una materia esta disponible para cursar online
        materia_online_id(materias)

    if opcion_elegida == 7:  # 7: Ver si pudo cursar una materia, segun mis materias aprobadas
        if realizo_ingreso_materias == False:
            print("Primero debe ingresar las materias aprobadas.(opcion 2)")
        else:
            validar_titulo_intermedio(lista_materias_aprobadas)
    
    return lista_materias_aprobadas#devuelvo la lista para cambiar la lista y no hacerl global



# ------------------ Listas de Datos ------------------#

# hay que setear el ultimo booleano (update: Listo, esta en base a la lista igual de licenciatura habria que evaluar que materias faltan de la ingenieria) jp:espectacular :)
materias = [
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

# Lista para almacenar las materias aprobadas por el usuario
lista_materias_aprobadas = []

realizo_ingreso_materias = False

lista_menu = [
    "1: Ver plan de estudios completo",
    "2: Ingresar materias aprobadas",
    "3: Ver que materias tengo que tener aprobadas, para cursar una materia",
    "4: Ver si pudo cursar una materia, segun mis materias aprobadas",
    "5: Ver listado de materias online",
    "6: Ver si una materia esta disponible para cursar online",
    "7:  Ver si puedo reclamar el titulo intermedio",
    "-1: Salir del sistema"]
# ver si agregamos la función de promedio.
# ver si sumamos la opcion de mostrar nota en materia ya aprobada


def validar_titulo_intermedio(lista_materias_aprobadas):
    print(lista_materias_aprobadas)
    requisito = 27
    lista_requisitos = []
    for z in range(requisito):
        lista_requisitos.append(z + 1)
    
    cantidad_aprobadas_requisito = 0
    for i in range(len(lista_requisitos)):
        for j in range(len(lista_materias_aprobadas)):
            if lista_materias_aprobadas[j] == lista_requisitos[i]:
                cantidad_aprobadas_requisito += 1

    if cantidad_aprobadas_requisito == len(lista_requisitos):
        print("✅ Tenés todas las materias necesarias para reclamar el título intermedio.")
    else:
        print("❌ Te faltan materias para el título intermedio.")
        print("Te faltan las siguientes:")
        for i in range(len(lista_requisitos)):
            esta_aprobada = False
            for j in range(len(lista_materias_aprobadas)):
                if lista_materias_aprobadas[j] == lista_requisitos[i]:
                    esta_aprobada = True
            if not esta_aprobada:
                print("-", lista_requisitos[i], ":", devolver_nombre_segun_codigo(lista_requisitos[i], materias))

mostrar_bienvenida()
opcion_elegida = 0


while opcion_elegida != -1:
    recorrer_menu()
    opcion_elegida = int(input("Por favor, elija una opción del menú:   "))
    while opcion_elegida < -1 or opcion_elegida > len(lista_menu):
        print("Opción no válida. Por favor, ingrese una opción del menú:")
        recorrer_menu()
        opcion_elegida = int(input("Por favor, elija una opción del menú:"))

    if opcion_elegida != -1:

        #seteo la bandera de ingreso de materias aprobadas
        if len(lista_materias_aprobadas) > 0:
            realizo_ingreso_materias = True
        

        lista_materias_aprobadas = menu_seleccionado(opcion_elegida, materias, lista_materias_aprobadas)

        print(end="\n")

        input("Presione Enter para continuar...")

        print(end="\n")

    limpiar_consola()

print("Gracias por utilizar el sistema de consulta de materias. ¡Hasta luego!")
