# Analisis de Datos

Para crear una base de datos Sqlite se utiliza el comando ```connect = sqlite3.connect("database.db")``` en esta ocasion no vamos a profundir en el codigo ya que es muy sencillo de implementar vamos a mostrar como comercializar nuestro producto utilizando tecnicas de mercados que usa en la bolsa de valores de New York en Silocon Valley para que sus servicios sean exitosos.

**Crear una Tabla:** Para crear la database

```python

cursor.execute("""CREATE TABLE albums
                  (title text, artist text, release_date text, 
                   publisher text, media_type text)""")
```

