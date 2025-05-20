[ID, Nombre, Código, Correlativas Anteriores (lista), Correlativas Posteriores (lista), online(bool)]

Por ejemplo:

[01, "Fundamentos de informática",100.0,[],[101.0], True ]
[02, "Programación I", 101.0,[100.0],[102.0, 103.0], False]
[03, "Programación II", 102.0,[101.0],[115.0, 122.0], False]
[04, "Programación III", 115.0,[102.0],[102.0, 103.0], False]

Formato de materias aprobadas:
[codigo de la materia ,nombre de la materia, nota]
```py
materia_aprobada = ["3.4.069","fundamentos de informática",8]
 ```
Entradas Posibles:
-- Materias ya aprobadas --[Saldria en funcion a eso la lista - las materias que el usuario ya aprobo]
-- Cantidad de materias que quiere hacer por semana (daria como salida las recomendaciones nuestra en funcion a analisis de las correlativas posteriores -- en la salida se debe priorizar las que tengan correlativas posteriores AND que el usuario haya aprobado las anteriores)
-- Materias online --

<!--
Fundamentos de informatica (no tiene correlativa anterior, posterior tiene PROGRAMACION I)
Sistema de informacion (no tiene correlativa anterior, posterior SISTEMA DE INFORMACION II)
Pensamiento critico y comunicacion (No tiene correlativa anterior, no tiene correlativa posterior)
Teoria de Sistemas (No tiene correlativa anterior, no tiene correlativa posterior)
Elementos de algebra y geometria (No tiene correlativa anterior, posterior Algebra)

Fundamentos de Informática → 1.1 Programación I
Sistemas de Información I → 2.1 Sistemas de Información II
Pensamiento Crítico y Comunicación
Teoría de Sistemas
Elementos de Álgebra y Geometría → 1.2 Álgebra
Programación I ← 1.1 Fundamentos de Informática → 1.3 Programación II, 1.4 Paradigma Orientado a Objetos
Sistemas de Representación
Fundamentos de Química
Arquitectura de Computadoras → 2.2 Sistemas Operativos
Matemática Discreta → 2.3 Ingeniería de Datos I, 2.4 Teoría de la Computación
Álgebra ← 1.2 Elementos de Álgebra y Geometría → 2.5 Física I
Programación II ← 1.3 Programación I → 3.1 Programación III, 3.2 Seminario de Integración Profesional
Sistemas de Información II ← 2.1 Sistemas de Información I → 3.3 Dirección de Proyectos Informáticos, 3.4 Arquitectura de Aplicaciones, 3.5 Seminario de Integración Profesional, 3.6 Ingeniería de Software
Sistemas Operativos ← 2.2 Arquitectura de Computadoras
Física I ← 2.5 Álgebra → 3.7 Física II
Cálculo I → 3.8 Probabilidad y Estadística, 3.9 Cálculo II
Programación III ← 3.1 Programación II → 4.1 Teoría de la Computación
Paradigma Orientado a Objetos (POO) ← 1.4 Programación I → 4.2 Aplicaciones Interactivas, 4.3 Proceso de Desarrollo de Software
Fundamentos de Telecomunicaciones → 4.4 Teleinformática y Redes
Ingeniería de Datos I ← 2.3 Matemática Discreta → 4.5 Ingeniería de Datos II, 4.6 Seminario de Integración Profesional
Cálculo II ← 3.9 Cálculo I → 4.7 Modelado y Simulación
Proceso de Desarrollo de Software ← 4.3 POO → 5.1 Desarrollo de Aplicaciones I, 5.2 Desarrollo de Aplicaciones II
Seminario de Integración Profesional ← 3.2 Programación II, 3.5 Sistemas de Información II, 4.6 Ingeniería de Datos
Teleinformática y Redes ← 4.4 Fundamentos de Telecomunicaciones → 5.3 Seguridad e Integridad de la Información
Ingeniería de Datos II ← 4.5 Ingeniería de Datos I → 5.4 Ciencia de Datos
Probabilidad y Estadística ← 3.8 Cálculo I → 5.5 Estadística Avanzada, 5.6 Evaluación de Proyectos Informáticos, 5.7 Ciencia de Datos
Examen de Inglés
Aplicaciones Interactivas ← 4.2 POO → 5.2 Desarrollo de Aplicaciones II
Ingeniería de Software ← 3.6 Sistemas de Información II → 5.8 Calidad de Software
Física II ← 3.7 Física I
Teoría de la Computación ← 2.4 Matemática Discreta, 4.1 Programación III
Estadística Avanzada ← 5.5 Probabilidad y Estadística → 6.1 Inteligencia Artificial (IA)
Desarrollo de Aplicaciones I ← 5.1 Proceso de Desarrollo de Software
Dirección de Proyectos Informáticos ← 3.3 Sistemas de Información II
Ciencia de Datos ← 5.4 Ingeniería de Datos II, 5.7 Probabilidad y Estadística
Seguridad e Integridad de la Información ← 5.3 Teleinformática y Redes
Modelado y Simulación ← 4.7 Cálculo II
Optativa I
Desarrollo de Aplicaciones II ← 4.2 Aplicaciones Interactivas, 5.1 Proceso de Desarrollo de Software
Evaluación de Proyectos Informáticos ← 5.6 Probabilidad y Estadística
Inteligencia Artificial (IA) ← 6.1 Estadística Avanzada
Tecnología y Medio Ambiente
Práctica Profesional Supervisada
Optativa II
Arquitectura de Aplicaciones ← 3.4 Sistemas de Información II
Tendencias Tecnológicas
Proyecto Final de Ingeniería
Calidad de Software ← 5.8 Ingeniería de Software
Optativa III
Negocios Tecnológicos
Tecnología e Información
Derecho Informático

-->

Materias online:

Materias online
-Programación II

- Arquitectura de computadores
- Diseño y desarrollo web
- Fundamentos de informática
- Liderazgo y negociación
- Marketing
- Matemática discreta
- Paradigma orientado a objetos
- Pensamiento critico y comunicación
- Programación I
- Programación III
- Redes de datos
- Sistemas operativos
- Sistemas de información I
- Sistemas de información II
- Teoría de la computación
- Testing de aplicaciones
