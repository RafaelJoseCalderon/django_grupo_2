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

# Bases de Datos [repo no oficial]
## Instalación PostgreSql (debian 11)
### Instalación
https://www.postgresql.org/download/linux/debian/

```C19
sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -

sudo apt-get update
sudo apt-get -y install postgresql
```

### Instalación (sugerida)
```C20
sudo apt-get install apt-transport-https curl

sudo sh -c 'echo "deb [signed-by=/usr/share/keyrings/apt.postgresql.org.gpg] http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/postgresql.list'
sudo curl -sS https://www.postgresql.org/media/keys/ACCC4CF8.asc | gpg --dearmor --output /usr/share/keyrings/apt.postgresql.org.gpg

sudo apt-get update
sudo apt-get install postgresql
```

## Instalación MySQL Community (GPL) (debian 11)
https://dev.mysql.com/downloads/mysql/

* instalar a travez de gdebi, específicamente en este orden
   * mecab-ipadic-utf8 (1)
   * mysql-common
   * mysql-community-server-core
   * mysql-community-client-plugins
   * mysql-community-client-core
   * mysql-community-client
   * mysql-client
   * mysql-community-server
* configurar la seguridad de mysql (2)
  ```C21
  mysql_secure_installation
  ```

nota (1): Opcional, anda perfectamente sin esto, sin embargo esta en la lista de dependencias. <br>
nota (2): Leer detenidamente la configuración. (no sabe ingles, use Google.)

## Instalación mariabd (debian 11)
### Instalación
https://mariadb.org/download/?t=repo-config

```C22
sudo apt-get install apt-transport-https curl

sudo sh -c "echo 'deb https://mirror1.cl.netactuate.com/mariadb/repo/10.11/debian bullseye main' >>/etc/apt/sources.list"
sudo curl -o /etc/apt/trusted.gpg.d/mariadb_release_signing_key.asc 'https://mariadb.org/mariadb_release_signing_key.asc'

sudo apt-get update
sudo apt-get install mariadb-server
```

nota: "cuidado hay repos sin ReleaseIn"

### Instalacion (sugerida)
```C23
sudo apt-get install apt-transport-https curl

sudo sh -c "echo 'deb [signed-by=/usr/share/keyrings/apt.mariadb.gpg] https://mirror1.cl.netactuate.com/mariadb/repo/10.11/debian $(lsb_release -cs) main' > /etc/apt/sources.list.d/mariadb.list"
sudo curl -sS https://mariadb.org/mariadb_release_signing_key.asc | gpg --dearmor --output /usr/share/keyrings/apt.mariadb.gpg

sudo apt-get update
sudo apt-get install mariadb-server
```

nota: "cuidado hay repos sin ReleaseIn"

### Configurar maria db (1)
```C24
mysql_secure_installation
```

nota (1): Leer detenidamente la configuración. (no sabe ingles, use Google.)

# Bases de Datos [repo oficial]

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
nota (2): Leer detenidamente la configuración. (no sabe ingles, use Google.)

# Creación de usuario

## Usuario Sqlite
No requiere la creación de ningun usuario.

## Usuario PostgreSql
0. primer inicio (solo la primera vez)
    * iniciar a la fuerza
      ```C27
      sudo -u postgres psql
      ```

    * cambio de contraseña al ususario principal
      ```C28
      ALTER USER postgres WITH ENCRYPTED PASSWORD '<pass>';
      ```

    * salir de la terminal de postgres
      ```C29
      quit;
      ```

    * abrir el siguiente archivo
      ```C30
      sudo nano /etc/postgresql/15/main/pg_hba.conf
      ```

    * en el mismo modificar las lineas donde aparezca peer por md5

    * luego guardar y salir

    * reiniciar el servicio
      ```C31
      sudo systemctl restart postgresql.service
      ```

1. ingreso a laterminal de postgres
    ```C32
    psql -U postgres
    ```

2. creacion del usuario propiamente dicho (x)
    ```C33
    CREATE USER usuario WITH PASSWORD 'usuario';
    ```

3. comprobamos su creación y si se le a asignado su contraseña
    ```C34
    SELECT usename, passwd FROM pg_user;
    ```

4. cambiar contraseña
    ```C34
    ALTER USER <usuarios> WITH ENCRYPTED PASSWORD '<pass>';
    ```

5. creacion, base de datos (3)
    ```C35
    CREATE DATABASE <base_de_datos>;
    ```

6. comprobación, creacion de la base de datos
    ```C36
    \list
    ```

7. borrado, base de datos
    ```C37
    CREATE DATABASE <base_de_datos> OWNER <propietario>;
    ```

8. borrado, usuario
    ```C38
    DROP USER <usuario>;
    ```

9. limpiar pantalla
    ```C39
    \! clear;
    ```

10. salir
    ```C40
    quit;
    ```

## Usuario mariabd / mysql
Luego de la instalacion y configuración

1. ingreso a laterminal de mysql
    ```C41
    sudo mysql
    ```

2. creacion del usuario propiamente dicho
    ```C42
    CREATE USER '<usuario>'@'localhost' IDENTIFIED BY '<pass>';
    ```

3. comprobación de creación y si se le a asignado su contraseña
    * mariabd
      ```C43
      SELECT User, Password, Host FROM mysql.user;
      ```
    * mysql
      ```C44
      SELECT User, authentication_string, Host FROM mysql.user;
      ```

4. cambiar contraseña
    ```C45
    SET PASSWORD FOR '<usuario>'@'localhost' = PASSWORD('<pass>');
    ```

5. creacion de la base de datos (3)
    ```C46
    CREATE DATABASE <base_de_datos>;
    ```

6. comprobación, creacion de la base de datos
    ```C47
    SHOW DATABASES;
    ```

7. asignación los permisos
    ```C36
    GRANT ALL PRIVILEGES ON <base_de_datos>.* TO 'user'@'localhost';
    FLUSH PRIVILEGES;
    ```

8. borrado, base de datos
    ```C37
    DROP DATABASE <base_de_datos>;
    ```

9. borrado, usuario
    ```38
    DROP USER '<usuario>'@localhost;
    ```

9. limpiar pantalla
    ```C39
    \! clear;
    ```

10. salir
    ```C40
    quit;
    ```

nota (1): en caso de que root no tenga contraseña se le asigna una.
nota (2): 'usuario', es un generico, puede ir cualquiera que consideremos pertinente.
nota (3): 'base_de_datos', es un generico, puede ir cualquiera que consideremos pertinente.

# Controladores de conexión
## Controlador Sqlite
Viene por defecto, no hay que instalar ni configurar nada.

## Controlador PostgreSql
Nan

## Controlador mysql

Según las instrucciones de la pagina oficial del desarrollador del conector, los pasos son:

### prerequisito

### Prerequisito
```C41
sudo apt-get install python3-dev default-libmysqlclient-dev build-essential
```

### Conector propiamente dicho
```C42
pip install mysqlclient
```

### Respaldo del mismo en el proyecto
```C43
pip freeze > requirements.txt
```

# Extras
Paquete necesario, en tiempo de desarrollo, para visualizar imágenes en los templates

```C44
pip install Pillow
```