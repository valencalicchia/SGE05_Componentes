# Enunciado
Este ejercicio práctico va a tener tres partes:

1. Una primera parte, en la que nos familiarizaremos con el lenguaje de programación Python y haremos algunos módulos (programas en Python) que podamos utilizar posteriormente (actividades 1 a 4). 
2. Una segunda parte (actividades 5 y 6), en el que aprovecharemos los módulos generado en las anteriores actividades para crear nuestra propia aplicación.
3. Una tercera parte en la que intentaremos que el módulo o aplicación creados en las actividades 5 y 6 se integren en Odoo 17.0 como un módulo más.

A la hora de programar podemos utilizar el paradigma imperativo (estructurado, procedimental, modular) o el paradigma de programación orientada a objetos (POO). Lo lógico es que utilicemos este último, ayudados del primero. Por tanto los programas serán orientados a objetos, utilizando por tanto clases y con control de excepciones.
## ACTIVIDADES

### PARTE I

1. Crear un módulo para validación de nombres de usuarios en Python

- El nombre de usuario debe contener un mínimo de 6 caracteres y un máximo de 12.
- El nombre de usuario debe ser alfanumérico.
- Un nombre de usuario válido, retorna 0 o el mensaje “El nombre de usuario es válido”
- Un nombre de usuario con menos de 6 caracteres, retorna 1 o el mensaje "El nombre de usuario debe contener al menos 6 caracteres".
- Un nombre de usuario con más de 12 caracteres, retorna 2 o el mensaje "El nombre de usuario no puede contener más de 12 caracteres".
- Un nombre de usuario con caracteres distintos a los alfanuméricos, retorna 3 o el mensaje "El nombre de usuario puede contener solo letras y números".

2. Crear un módulo para validación de contraseñas

- La contraseña debe contener un mínimo de 8 caracteres. 
- La contraseña debe contener letras minúsculas, mayúsculas, números y al menos 1 carácter no alfanumérico. 
- La contraseña no puede contener espacios en blanco. 
- Contraseña válida, retorna True 
- Contraseña no válida (segura) según estos criterios, retorna False

3. Crear un módulo que solicite un nombre de usuario y contraseña y los valide utilizando los módulos generados en los dos ejercicios anteriores.

### PARTE II

4. Crear un módulo que construya una tabla con datos proporcionados por el usuario y posteriormente permita la búsqueda en la tabla, mediante clave en los datos introducidos.

- Utilizaremos diccionarios.
- El programa constará de un menú con las siguientes opciones: 
  - Solicitar los datos para almacenar (apellidos, nombre, fecha nacimiento, dirección, contraseña, etc.) 
  - Permitir buscar datos correspondientes a un nombre o apellido introducidos y mostrar en pantalla.
  - Añadir los datos de la tabla a un fichero CSV 
  - Recuperar datos de un fichero CSV debidamente formateado, para completar la tabla.

5. Módulo Stock
   
- Acceder a la correspondiente tabla de Odoo, para mostrar al usuario un listado de productos. El usuario podrá seleccionar uno para obtener información del Código, descripción y stock actual. 
- Generar un fichero CSV con el stock de todos los productos. En el fichero deben mostrarse como mínimo el código, la descripción y el stock actual de cada producto. Las líneas del fichero estarán ordenadas por descripción del producto.

### PARTE III

6.Módulo Clientes/proveedores

- A partir de un fichero CSV y utilizando el módulo generado en la Actividad 4, con datos de clientes, añadirlos a la tabla o tablas correspondientes de la base de datos de Odoo, el fichero CSV contendrá como información los siguientes datos:
  - Nombre del cliente
  - Nombre a mostrar
  - Dirección
  - Teléfono
  - e-mail
  - Página web
  - Población
  - Código Postal
  - Tipo: (P: proveedor, C: cliente, T: proveedor y cliente)

- Comprobar previamente si el cliente existe (coincide el Nombre del cliente), en este caso se modificará el registro correspondiente con los datos del fichero.
- Para crear el login se tomará la primera letra del nombre y el primer apellido, todo en minúsculas, además mediante el módulo de la Actividad 1 de esta misma tarea, se validará que el usuario (login) sea correcto.
- Teniendo en cuenta que los nombres de usuarios del fichero estarán formados por Nombre Apellido1 Apellido2, el campo password se actualizará con el dato generado según la siguiente regla:
  - Se mezclarán aleatoriamente el Nombre, Apellido1 y Apellido2 
  - Se tomará la primera letra del primer elemento, seguido de los segundos de la hora actual, seguido de las letras 2 y 3 del segundo elemento (la tercera letra se convertirá a mayúscula), seguido los minutos de la hora actual, seguido de la letra 4 del tercer elemento, finalizando con uno de estos tres símbolos: $, %, &, escogidos al azar.
  - Ejemplo son las 18:55:43 y el usuario se llama Manolo Martín Pajares. Tras mezclar aleatoriamente obtenemos Martín Pajares Manolo. La password sería: M43aJ55a&.
  - Mediante el módulo de la Actividad 2 de esta misma tarea, se validará si es correcta la contraseña generada.
  - Se almacenarán en la tabla correspondiente el login y contraseña generados.
  - Se informará si se ha procedido o no a las modificaciones. En caso de que se hayan realizado modificaciones se indicará cuantos registros se han añadido y cuantos se han modificado.
Nota: Tipo hace referencia a las posibles Categorías en Contactos. Si no existieran las categorías de contacto Proveedor (Vendor), Cliente (Custom) o Ambos (Vendor- Custom), se pueden crear previamente desde Odoo.

