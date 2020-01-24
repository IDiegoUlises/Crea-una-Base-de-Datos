# Analisis de Datos

Mostrararemos como comercializar nuestro producto utilizando tecnicas de mercados que usa en la bolsa de valores de New York en Silocon Valley para que sus servicios sean exitosos.

**Crer la Database:** Crea un archivo el cual contiene nuestros datos.

```python
connect = sqlite3.connect("database.db")
```

**Crear una Tabla:** Crear una tabla que contiene los detalles de un producto 

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

**Seguridad:** El ataque mas comun a la base de datos es **SQL INYECCTOR** que es que el usuario cambia los valores de una consulta para 

* Eliminar la base de datos
* Cambiar valores de la base de datos
* Recibir valores restrigindos.

para evitar esto se puede solucionar con verificar 
