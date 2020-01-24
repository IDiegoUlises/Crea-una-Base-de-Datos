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

### ¿Porque es un agujero de seguridad el ```==``` ?
Porque es un operador que compara la direccion de memoria ram del objeto no compara por el valor que contiene la variable.

**Comparador de contenido para una consulta correcta**
 
 ```java
        if(mensaje.equals("contenido"))
        {
           System.out.println("El contenido de los mensajes son iguales");
        }
 
```

# Ofrecer un buen producto o servicio


**Buen Nombre:** Si tu nombre del servicio o producto se llama ``Service Web`` pero cambias de ideas lo llamas ```بخير شكرا``` sera dificil para el consumidor acordarse de tu nombre o encontrar tu producto o servicio. 

**Imagen de Producto o Servicio:** Se trata que tu producto debe ser diferente al resto para que pueda ser diferenciado por el consumidor puede ser en ser mas barato tener una mejor calidad o ofrecer una mejor experencia. **Ejemplo** realizas una comprar por **Aliexpress** buscas un producto ves que todos son iguales y no sabes cual elegir terminas eligiendo un producto al azar.

**Entregar una buena experencia:** Se trata que tu producto puede ser mas caro que todos tus demas competidores tus clientes van elegirte por entregar una experiencia inolvidable **Ejemplo** tu tienes un empresa que realiza **tour** por Francia los turistas no van a preguntar por precio del **Paseo** sino la experiencia que va a ofrecer el viaje, esto tambien se aplica en videojuegos y en productos de comida. 

**Entregar Esclusividad:** Los telefonos de **Huawei** son baratos los del **IPhone** y se venden mucho mas aunque los dos productos hacen exactamente lo mismo aqui no se vende un telefono sino la **esclusividad.** Usted puede aplicar esto en crear un servicio premium esclusivo para que los usuarios se sientan con mas status.

**Ventajas Competitivas:** Tu eres una empresa que vende servidores que usan una computadora raspberry en caso que usted fabrica el producto puede salir 60 dolares y mandarlo a pedir por **Amazon** puede costar 25 dolares al vender un servicio mas barato que la competencia compite por tener los precio mas bajos otra ventaja es que usted invertir en crear una fabrica para reducir el precio de fabricacion del producto para bajar los costos y tener mayores beneficios.

**Nicho de Mercado:** Mucha gente piensa que ofrecer un producto o servicio para todo el mundo es lo correcto por lo general esta razon es por que fracasan la mayoria de empresas un **Ejemplo** es **Facebook** que no salio para todo el mundo sino era una red para los universitarios de **Hardvar** pudieran y se centro en sus necesidad que tenia los universitarios luego se fue expandiendo por todo el mundo.

**Buena Atencion al Cliente:** Tu puedes utilizar **Whatsap** para que los consumidores puedan comunicarte contigo en el caso que tengan un inconveniente puedas ayudarlo a resolver su problema tambien para responder las dudas. **Ejemplo** en Chile la empresa **Telefonica Movistar** que presta servicios de internet la mayor perdida de sus clientes es porque ofrece una pesima atencion al cliente.

**Redes Sociales:** Facebook y Instagram es utilizado por 8 de 10 personas de la poblacion mundial es decir puedes hacer que todo el planeta entero conozca tu producto o servicio.

# Como Utilizar los datos para mejorar tu producto o servicio(big data)

Un ejemplo **Instagram** elimino el boton de tranmisiones en vivo que se encontraba en el perfil porque nadie lo usaba tu puedes recolectar los datos que generar tus usuarios para mejorar la calidad de tu servicio.

**Tiempo de Retenccion:** Debemos retener la mayor cantidad de tiempo a los consumidores utilizando nuestro servicio por ejemplo si tienes un videojuego debemos hacer que el usuario pase la mayor cantidad de tiempo posible.

**Interacciones:** Un ejemplo **Facebook* utiliza 

**Dependencia de Nuestros Servicio:** Debemos crear una dependencia a los clientes de nuestros servicios ahi que ```mal acostumbrarlos``` a depender de nuestro servicio un  **Ejemplo** en Estados Unidos en la famosa prision de **Alcatraz** que tiene al peligroso criminal **Alkaponi** los presisioneros se bañaban con agua caliente para acostumbrarlo al agua caliente para cuando intentaran escapar nadando no pudieran soporta el frio del mar.









