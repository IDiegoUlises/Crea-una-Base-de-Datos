# Analisis de Datos

Para crear una base de datos Sqlite se utiliza el comando ```connect = sqlite3.connect("database.db")``` en esta ocasion no vamos a profundir en el codigo ya que es muy sencillo de implementar vamos a mostrar como comercializar nuestro producto utilizando tecnicas de mercados que usa en la bolsa de valores de New York en Silocon Valley para que sus servicios sean exitosos.

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

