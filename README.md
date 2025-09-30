# Invera ToDo-List Challenge (Python/Django Jr-SSr)

## Cómo levantar la aplicación

Requiere tener Docker instalado el sistema. Una vez hecho esto, en el directorio base del repositorio clonado, correr el comando ```docker-compose up```. Esto iniciara una base de datos PostgreSQL, una instancia de pgAdmin4 y el Backend de Django. En caso de que se quieran utilizar puertos o variables de entorno distintas se debe modificar desde el archivo ```docker-compose-yaml```. Tambien se puede comentar el bloque de pgAdmin4 en caso de que no se utilice.
Al levantar la aplicación correrá automáticamente todas las migraciones necesarias, por lo que el paso anterior es suficiente para tener el servicio funcionando.

## Qué contiene la aplicación

La aplicación contiene:

- Autenticación de usuario, utilizando autenticación de Tokens (Rutas POST /login y /register).
- Creación, actualización, consulta y eliminación de estados de tareas (Rutas /task/state para múltiples y /task/state/\<id> para estados individuales).
- Creación, actualización, consulta y eliminación de tareas (Rutas /task para múltiples y /task/\<id> para tareas individuales).
- Logs tanto a consola como a un archivo (El archivo y el nivel de logeo son configurables a través de variables de entorno en el docker-compose).