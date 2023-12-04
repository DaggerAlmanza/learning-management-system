# learning-management-system
API básica para un LMS utilizando Django y DRF, que permita la gestión de cursos, instructores y estudiantes.


## Acerca del proyecto
Proyecto en el cual hacemos una implementación de un LMS básico, proporcionando una base para la gestión de cursos, instructores y estudiantes a través de una interfaz de programación de aplicaciones (API) construida con Django y Django Rest Framework (DRF). 

## Requisitos del proyecto:
1.	Configuración del Proyecto

Configuración Inicial:

* Configurar un proyecto Django con DRF.
* Utilizar SQLite como base de datos.

2.	Modelado de Datos

Models:
* Crear modelos para Course , Instructor y Student.
* Definir relaciones adecuadas (e.g., un instructor puede tener varios cursos, un estudiante puede inscribirse en varios cursos).

Migrations:
* Generar y aplicar migraciones para los modelos creados.

3.	API con Django Rest Framework

Serializers:
* Crear serializadores para los modelos.

Views and Routes:
* Implementar vistas utilizando las clases de DRF.
* Configurar las rutas de la API para el CRUD (Crear, Leer, Actualizar, Eliminar) de cursos, instructores y estudiantes.

Authentication and Permissions (Opcional pero recomendado):
* Implementar un sistema de autenticación.
* Definir permisos para diferentes tipos de usuarios (e.g., solo instructores pueden crear cursos).

4.	Documentación

README:
* Crear un archivo README que documente cómo configurar y ejecutar el
proyecto.

### Construido con
* Lenguaje: Python 3.10.12
* Framework: Django REST Framework 
* Base de dato: sqlite3

### Modelo de la base de datos

[![lms.jpg](https://i.postimg.cc/XYHK1CPp/lms.jpg)](https://postimg.cc/xXmbccn2)

<!-- GETTING STARTED -->
## Iniciando

Este es un ejemplo de como deberian instalar el proyecto localmente dada las instruciones.


### Intalacion 

1. Instalar virtualEnv e instalarlo
```sh
$ virtualenv -p python3 venv
o
$ python3 -m venv venv
```
```sh
$ source venv/bin/activate
o
$ . venv/bin/activate
```
2. Instalar requirements.txt
```sh
$ pip3 install -r requirements.txt
```
### Base de datos
1. Las migraciones encarga de crear nuevas migraciones en función de los cambios que haya realizado en sus modelos
```sh
$ python manage.py makemigrations
```
2. Encargado de aplicar y desaplicar migraciones.
```sh
$ python manage.py migrate
```

### Correr la api
1. Inicio del servidor 
```sh
$ python manage.py runserver
```

### Documentacion de la API

La documentacion esta hecha cumpliendo los estadares de OpenAPI con ayuda del Django y Usage.

La ruta de la documentacion se encuentra disponible en http://localhost:8000/docs


#### Instructivo del api
1.	Crear un Superusuario:

* Para comenzar, es necesario crear un superusuario que tendrá acceso a la administración del sistema. Ejecute el siguiente comando.
```sh
$ python manage.py createsuperuser
```
* Siga las instrucciones para proporcionar un nombre de usuario, dirección de correo electrónico y contraseña para el superusuario.

2.	Autenticación:

* Diríjase a la URL /api/token/ para obtener el token de autenticación. Utilice las credenciales del superusuario creadas anteriormente para autenticarse.

3.	 Acciones según el Rol:

3.1 Rol: Estudiante

Creación y Actualización de la Cuenta de Estudiante:

* Solo el estudiante puede realizar la creación y actualización de su propia cuenta de estudiante.

3.2 Rol: Instructor

Creación, Actualización y Eliminación de la Cuenta de Instructor:

* Solo el instructor puede realizar la creación, actualización y eliminación de su propia cuenta de instructor.

Eliminación de un Estudiante:

* Solo el instructor puede eliminar a un estudiante.

Creación, Actualización y Eliminación de un Curso a Cargo:

* Solo el instructor puede realizar la creación, actualización y eliminación de un curso a cargo.

* Consultas de todos los cursos del instructor.

4.	Para salir del api se hace el logout.


Nota: Se realizó un análisis estático del código, arrojando:
~~~
0 Bugs                                                                      Reliability A
~~~
~~~
0 Vulnerabilities                                                           Security A
~~~
~~~
1 Security Hotspots                     0.0%Reviewed                        Security Review E
~~~
~~~
8min Debt		                        1Code Smells		                Maintainability A
~~~
~~~
0.0% Coverage on 119 Lines to cover	    0.0% Duplications on 284 Lines 	0 Duplicated Blocks
~~~
			
