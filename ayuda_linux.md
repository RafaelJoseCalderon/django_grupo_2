# Proyecto desde cero

## Tener instalado

* virtualenv
* python3-venv

```C1
sudo apt-get install virtualenv python3-venv
```

luego se usa, para crear o gestionar el proyecto.

## Creación de un proyecto, en la versión default

para la creación de un entorno virtual, aplicamos el siguiente comando (en debian 11.04)

```C2
python3 -m venv .venv
```

nota: ".venv" es el nombre de nuestro entorno virtual de desarrollo.

## Inicio del entorno virtual

nos situamos dento de la raiz de ".venv" y aplicamos

```C3
source .venv/bin/activate
```

## Salida del entorno virtual

estando dentro del entorno virtual aplicamos

```C4
deactivate
```

## Instalación de dependencias

* para instalar dependencias aplicamos
```
pip install algun_paquete
```
* para instalar dependencias con una versión especifica aplicamos
```
pip install otro_paquete==2.6.0
```

# Respaldando el proyecto en github

## Archivo ".gitignore"

el mismo deberá contener, como mínimo, las siguientes lineas

```C5
.venv
*__pycache__*
*.pyc
```

nota: dependiendo del ide que se este usando quizás halla que agregar más omisiones al gitignore, si se trabaja a pelo con lo anterior alcanza.

## Respaldo de las dependencias instaladas en el entorno virtual

una vez dento del entorno virtual, las dependencias se respaldan con el siguiente comando

```C6
pip freeze > requirements.txt
```

## A seguir

se aplica los pasos convenidos para github, dentro de el directorio de desarrollo se hace "git init", "git add .", "git push"

# Clonación de un proyecto desde github

* se clona el proyecto desde github
* se instala un nuevo proyecto con el nombre con el cual a sido la clonación. Se aplica (1)

```C7
python3 -m venv .venv
```
* se instalan las dependencias, estando dentro del directorio donde se encuentra el entorno virtual/proyecto, aplicando (2)

```C8
pip install -r requirements.txt
```

* se construye la base de datos con
```C9
python manage.py migrate
```

nota (1): se debe estar dentro de la carpeta clonada. <br>
nota (2): se debe estar con el entorno virtual corriendo.

# Testing en python

## Ejecución de los test (sobre pytyhon)

los test se ejecutan parándose en la raíz del proyecto y ejecutando

```C10
python3 -m unittest
```

da resultados, por ejemplo:

```
........................
------------------------

Ran 24 tests in 0.002s

OK
```

## Ejecución de los test (sobre django)

los test se ejecutan con

```C11
./manage.py test
```

da resultados, por ejemplo:

```
Found 2 test(s).
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
..
----------------------------------------------------------------------
Ran 2 tests in 0.040s

OK
Destroying test database for alias 'default'...
```

# Crear proyecto django

## Crear proyecto

para crear un proyecto se utiliza el siguiente comando:

```C12
django-admin startproject <nombre del preyacto>
```

nota: se debe estar con el entorno virtual corriendo.

## Crear app

para crear una app django se utiliza el siguiente comando:

```C13
python manage.py startapp <nombre de la app>
```

nota: se debe estar con el entorno virtual corriendo.

## Levantar el server de django

para levantar el server de django se utiliza el siguiente comando:

```C14
python manage.py runserver
```

nota: se debe estar con el entorno virtual corriendo. <br>
nota: por defecto corre en el puerto 8000.

## Creación de administrador django

```C15
python manage.py createsuperuser
```

## Actualización de la base de datos, en tiempo de desarrollo

### Construcción de la migracion

se debe crear el archivo con los pasos que aplicara django a posteriori en la base de datos

```C16
python manage.py makemigrations < app >
```

nota: si no se especifica recorre todos las apps dentro del paquete.

### Aplicacion de la construccion

se aplica en base de datos los cambios marcados en "makemigrations"

```C17
python manage.py migrate <app>
```

nota: pueden aparecer problemas de coherencia, los cuales se tienen que arreglar a mano, por ejemplo, si a su base de datos se le agrega una columna y esta no puede ser nula django no sabrá que hacer y le presentara varias opciones. Se arregla a mano o puede en el archivo de migración marcar un valor por defecto para esas columna, por ejemplo "default='visita_apellido'".

### Aplicar sql sobre base de datos

se puede aplicar cambios sobre la base de datos, desde un código python con:

```C18
python manage.py sqlmigrate < app > < archivo migracion >
```

# Bases de Datos

## Instalación de la base de datos en local

### Sqlite3

Viene por defecto, no requiere configuracion.

### Instalación Mysql (debian 11)

1. instalar a travez de gdebi, específicamente en este orden
   * mecab-ipadic-utf8 (1)
   * mysql-common
   * mysql-community-server-core
   * mysql-community-client-plugins
   * mysql-community-client-core
   * mysql-community-client
   * mysql-client
   * mysql-community-server

---

2. configurar la seguridad de mysql (2)

  ```C19
  mysql_secure_installation
  ```

nota (1): Opcional, anda perfectamente sin esto, sin embargo esta en la lista de dependencias. <br>
nota (2): Leer detenidamente la configuración. (no sabe ingles, use Google.)

### Instalación mariabd (debian 11) [repo no oficial]

1. agregar los repos en sourses.list

  * los repos de mariadb son: (1)

  ```C20
  deb [arch=amd64] https://mirror1.cl.netactuate.com/mariadb/repo/10.5/debian buster main
  deb-src https://mirror1.cl.netactuate.com/mariadb/repo/10.5/debian buster main
  ```
2. instalar la clave

  * para instalar la clave se tiene que tener instalado los siguientes paquetes
  ```C21
  apt-get install software-properties-common dirmngr apt-transport-https
  ```
  * luego instalar la clave
  ```C22
  apt-key adv --fetch-keys 'https://mariadb.org/mariadb_release_signing_key.asc'
  ```
3. intslar maria db

  ```C23
  apt-get install mariadb-server
  ```
4. configurar maria db (2)

  ```C24
  mysql_secure_installation
  ```

nota (1): A la hora de instalar buscar los repos más actuales. <br>
nota (2): Leer detenidamente la configuración. (no sabe ingles, use Google.)

### Instalacion mariabd (debian 11) [repo oficial]

1. intslar maria db (1)

  ```C25
  apt-get install mariadb-server
  ```

2. configurar maria db (2)

  ```C26
  mysql_secure_installation
  ```

nota (1): A la hora de instalar siempre tener repos más actuales (de lo contrario pueden haber desagradables sorpresas). <br>
nota: (2)Leer detenidamente la configuración. (no sabe ingles, use Google.)

## Controlador mysql

Según las instrucciones de la pagina oficial del desarrollador del conector, los pasos son:

### prerequisito

```C27
sudo apt-get install python3-dev default-libmysqlclient-dev build-essential
```

### Conector propiamente dicho

```C28
pip install mysqlclient
```

### Respaldo del mismo en el proyecto

```C29
pip freeze > requirements.txt
```

## Extras

paquete necesario, en tiempo de desarrollo, para visualizar imágenes en los templates

```C30
pip install Pillow
```