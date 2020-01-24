# Analisis de Datos

Mostrararemos como comercializar nuestro producto utilizando tecnicas de mercados que usa en la bolsa de valores de New York en Silocon Valley para que sus servicios sean exitosos.

**Crer la Database:** Crea un archivo el cual contiene nuestros datos.

```python
connect = sqlite3.connect("database.db")
```

**Crear una Tabla:** Crear una tabla que contiene los detalles de un producto o servicio.

```python

cursor.execute("""CREATE TABLE product
                  (name text, business text, price int, 
                   quantity int, comment text)""")
```

**Enviar un Consulta:**

```python
consulta = db.cursor()
consulta.execute("select * from tabla")
```

**Seguridad:** El ataque mas comun a la base de datos es **SQL INYECCTOR** que se base en que el usuario cambia los valores de una consulta para 

* Eliminar la base de datos
* Cambiar valores de la base de datos
* Recibir datos prohibidos.

para evitar esto debe usar un comparador de **contenido**  en el caso que utilize ```==```  usted tiene un enorme fallo de seguridad.

### ¿Porque es un agujero de seguridad utilizar ```==``` ?
Porque es un operador que compara la direccion de memoria ram del objeto no compara por el valor que contiene la variable.

**Realizando una comparacion correcta**
 
 ```java
        if(mensaje.equals("contenido"))
        {
           System.out.println("El contenido de los mensajes son iguales");
        }
 ´``
