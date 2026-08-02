# 1. ¿Para qué usamos Clases en Python?

## Introducción

Cuando empezamos a programar, normalmente utilizamos variables y funciones para resolver pequeños problemas. Sin embargo, cuando nuestros programas crecen, el código puede volverse difícil de organizar.

Las **clases** nos ayudan a mantener el código ordenado y a agrupar información relacionada en un mismo lugar.

Las clases forman parte de la **Programación Orientada a Objetos (POO)**, una forma de programar muy utilizada para desarrollar aplicaciones, videojuegos, páginas web y muchos otros programas.

---

## ¿Qué es una clase?

Una **clase** es como un **molde** o una **plantilla**.

Imagina un molde para hacer galletas. Con un solo molde puedes hacer muchas galletas iguales. De la misma manera, una clase sirve para crear muchos objetos que comparten las mismas características.

---

## ¿Qué es un objeto?

Un **objeto** es una instancia creada a partir de una clase.

Por ejemplo, si tenemos una clase llamada **Perro**, podemos crear varios objetos:

- Toby
- Luna
- Max

Todos son perros, pero cada uno tiene un nombre y una edad diferentes.

---

## ¿Por qué usamos clases?

Las clases se utilizan porque permiten:

- Organizar mejor el código.
- Evitar repetir el mismo código varias veces.
- Crear programas más fáciles de entender y modificar.
- Representar objetos de la vida real, como personas, coches o productos.

---

## Sintaxis básica

Para crear una clase utilizamos la palabra reservada `class`.

```python
class Persona:
    pass
```

En este ejemplo hemos creado una clase llamada **Persona**.

La palabra `pass` indica que la clase está vacía por el momento.

---

## El método `__init__()`

Cuando creamos un objeto, normalmente queremos darle información, como un nombre o una edad.

Para ello utilizamos el método especial `__init__()`, que se ejecuta automáticamente cuando se crea el objeto. Entonces, esto también responde a la segunda pregunta: "¿Qué método se ejecuta automáticamente cuando se crea una instancia de una clase?"

```python
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        print("Se ha creado una nueva persona.")
```

En este ejemplo, cada objeto de la clase **Persona** tendrá un atributo llamado **nombre** y  **edad** .

---

## ¿Qué significa `self`?

`self` representa al objeto que estamos creando.

Gracias a `self`, cada objeto puede guardar su propia información.

Por ejemplo:

```python
self.nombre = nombre
```

Esto significa que el nombre que recibe el objeto se almacenará dentro de él.

---

## Crear un objeto

Una vez creada la clase, podemos crear un objeto.

```python
persona1 = Persona("Carlos")
```

Para acceder a la información del objeto utilizamos un punto (`.`).

```python
print(persona1.nombre)
```

**Salida:**

```text
Carlos
```

---

## Métodos

Además de almacenar información, las clases también pueden realizar acciones mediante **métodos**.

```python
class Persona:

    def __init__(self, nombre):
        self.nombre = nombre

    def saludar(self):
        print("Hola, soy", self.nombre)
```

Crear el objeto:

```python
persona1 = Persona("Carlos")
```

Llamar al método:

```python
persona1.saludar()
```

**Salida:**

```text
Hola, soy Carlos
```

---

## Ejemplo completo

```python
class Coche:

    def __init__(self, marca, color):
        self.marca = marca
        self.color = color

    def mostrar_informacion(self):
        print("Marca:", self.marca)
        print("Color:", self.color)
```

Crear un objeto:

```python
coche1 = Coche("Toyota", "Rojo")
```

Mostrar la información:

```python
coche1.mostrar_informacion()
```

**Salida:**

```text
Marca: Toyota
Color: Rojo
```

---

## Imagen 1

![Python Class](Course%20Checkpoint%206%20Images/Python%20Class%20Image.jpg)

Aquí tenemos un ejemplo de una clase llamada **Carro**. A partir de esta clase hemos creado tres **objetos** (también llamados **instancias**) llamados **ObjetoCarroVerde**, **ObjetoCarroAzul** y **ObjetoCarroRojo**. Cada uno de estos objetos tiene sus propios **atributos**, como el color o la marca, pero todos comparten los mismos **métodos**, ya que fueron definidos dentro de la clase **Carro**.

---

## ¿Dónde se utilizan las clases?

Las clases están presentes en casi cualquier programa moderno.

Algunos ejemplos son:

- Aplicaciones móviles.
- Videojuegos.
- Tiendas online.
- Redes sociales.
- Sistemas bancarios.
- Programas de gestión de empresas.

---

# 2. ¿Qué es una API?

## Introducción

En el desarrollo de software es muy común que diferentes aplicaciones necesiten comunicarse entre sí para compartir información o ejecutar determinadas acciones. Sin embargo, sería muy complicado que cada programa tuviera acceso directo al código o a la base de datos de otro sistema.

Para resolver este problema existen las **APIs (Application Programming Interface)** o **Interfaces de Programación de Aplicaciones**, que actúan como un intermediario entre dos aplicaciones.

Una API define un conjunto de reglas que permiten que un programa solicite información o servicios a otro programa de forma segura, organizada y controlada.

---

# ¿Qué significa API?

API es el acrónimo de:

- **A** → Application (Aplicación)
- **P** → Programming (Programación)
- **I** → Interface (Interfaz)

En español significa:

> **Interfaz de Programación de Aplicaciones.**

Una API es un conjunto de reglas, protocolos y funciones que permiten que dos aplicaciones puedan comunicarse entre sí sin necesidad de conocer cómo funciona internamente cada una.

Podemos imaginar una API como un **puente** que conecta dos sistemas.

La aplicación que necesita información realiza una solicitud (Request), la API recibe esa solicitud, la procesa y devuelve una respuesta (Response).

Todo este proceso ocurre en pocos milisegundos.

---

# Analogía: Un restaurante

Una de las mejores formas de entender una API es imaginar un restaurante.

Supongamos que llegamos a un restaurante.

Nosotros somos el cliente.

La cocina representa el servidor donde se prepara toda la información.

Sin embargo, nosotros no podemos entrar directamente a la cocina.

Existe un **mesero** que recibe nuestro pedido y lo lleva a la cocina.

Después regresa con nuestra comida.

En este ejemplo:

- Cliente → Aplicación que necesita información.
- Mesero → API.
- Cocina → Servidor.
- Comida → Información solicitada.

El cliente nunca necesita saber cómo se cocina la comida.

Solo necesita hacer el pedido correcto.

Una API funciona exactamente igual.

---

# ¿Por qué existen las APIs?

Las APIs fueron creadas para facilitar la comunicación entre diferentes sistemas.

Sin APIs, cada aplicación tendría que acceder directamente al código interno o a la base de datos de otra aplicación.

Esto ocasionaría numerosos problemas:

- Baja seguridad.
- Mayor complejidad.
- Difícil mantenimiento.
- Mayor riesgo de errores.
- Dependencia entre sistemas.

Con una API, el acceso está completamente controlado.

---

# ¿Para qué se utilizan las APIs?

Las APIs están presentes prácticamente en todas las aplicaciones modernas.

Algunos ejemplos son:

- Aplicaciones móviles.
- Sitios web.
- Bancos.
- Redes sociales.
- Plataformas de pago.
- Sistemas de mapas.
- Servicios meteorológicos.
- Inteligencia Artificial.
- Videojuegos.
- Comercio electrónico.

---

# Ejemplos de APIs que utilizamos todos los días

## Google Maps

Cuando una aplicación muestra un mapa, normalmente no crea el mapa desde cero.

Simplemente utiliza la API de Google Maps.

La aplicación solicita:

"Muéstrame el mapa de Madrid."

La API devuelve el mapa correspondiente.

---

## Clima

Una aplicación del clima obtiene información mediante una API meteorológica.

Solicitud:

```
¿Qué temperatura hace en Barcelona?
```

Respuesta:

```
Temperatura: 29°C
Humedad: 65%
Viento: 15 km/h
```

---

## WhatsApp

Cuando enviamos un mensaje:

1. La aplicación envía una solicitud.
2. Los servidores reciben el mensaje.
3. La API procesa la información.
4. El destinatario recibe el mensaje.

---

## Banco

Cuando consultamos nuestro saldo:

- La aplicación móvil solicita el saldo.
- La API verifica nuestra identidad.
- Obtiene la información.
- Devuelve el saldo actualizado.

---

# ¿Cómo funciona una API?

## Imagen 2
![How API Works](Course%20Checkpoint%206%20Images/API%20Image.avif)

Generalmente una API sigue este flujo:

```
Usuario
   │
   ▼
Aplicación
   │
   ▼
API
   │
   ▼
Servidor
   │
   ▼
Base de datos
```

Después la información regresa siguiendo el camino inverso.


---

# Paso a paso del funcionamiento

## Paso 1

El usuario realiza una acción.

Ejemplo:

```
Buscar un producto.
```

---

## Paso 2

La aplicación genera una solicitud.

```
Necesito el producto número 35.
```

---

## Paso 3

La API recibe la solicitud.

Verifica que todo sea correcto.

---

## Paso 4

La API consulta el servidor.

---

## Paso 5

El servidor busca la información.

---

## Paso 6

El servidor devuelve la respuesta.

---

## Paso 7

La API entrega la respuesta a la aplicación.

---

## Paso 8

La aplicación muestra la información al usuario.

---

# Componentes principales de una API

Una API normalmente está formada por los siguientes elementos.

## Cliente

Es quien realiza la solicitud.

Puede ser:

- Un sitio web.
- Una aplicación móvil.
- Un programa en Python.
- Otro servidor.

---

## Servidor

Es quien posee la información o ejecuta la acción solicitada.

---

## Solicitud (Request)

Es el mensaje enviado por el cliente.

Ejemplo:

```
Quiero obtener todos los usuarios.
```

---

## Respuesta (Response)

Es la información enviada por el servidor.

Ejemplo:

```
Lista de usuarios encontrada.
```

---

# ¿Qué información contiene una solicitud?

Una solicitud suele incluir:

- Dirección (URL)
- Método HTTP
- Encabezados (Headers)
- Parámetros
- Cuerpo (Body) cuando es necesario

---

Ejemplo:

```
GET https://api.tienda.com/productos/15
```

Aquí:

```
GET
```

es el método.

```
https://api.tienda.com/productos/15
```

es la dirección del recurso.

---

# ¿Qué contiene una respuesta?

Una respuesta normalmente devuelve:

- Código de estado
- Información solicitada
- Mensajes de error si ocurre algún problema

Ejemplo:

```json
{
    "id": 15,
    "nombre": "Laptop",
    "precio": 950
}
```

---

# Métodos HTTP más utilizados

Las APIs REST utilizan principalmente estos métodos.

## GET

Obtiene información.

Ejemplo:

```
GET /usuarios
```

---

## POST

Crea información nueva.

Ejemplo:

```
POST /usuarios
```

---

## PUT

Actualiza completamente un recurso.

```
PUT /usuarios/5
```

---

## PATCH

Actualiza parcialmente un recurso.

```
PATCH /usuarios/5
```

---

## DELETE

Elimina información.

```
DELETE /usuarios/5
```

---

# Ejemplo completo

Supongamos una tienda en línea.

El usuario quiere ver todos los productos.

La aplicación realiza esta solicitud:

```
GET /productos
```

El servidor responde:

```json
[
    {
        "id":1,
        "nombre":"Mouse",
        "precio":20
    },
    {
        "id":2,
        "nombre":"Teclado",
        "precio":40
    }
]
```

La aplicación muestra esa información al usuario.

---

# ¿Qué es JSON?

La mayoría de las APIs envían la información utilizando JSON.

JSON significa:

**JavaScript Object Notation**

Es un formato muy ligero y fácil de leer tanto para humanos como para programas.

Ejemplo:

```json
{
    "nombre":"Carlos",
    "edad":25,
    "pais":"México"
}
```

---

# Consumiendo una API desde Python

Python facilita enormemente el consumo de APIs mediante la librería `requests`.

Primero instalamos la librería:

```bash
pip install requests
```

Después hacemos una petición:

```python
import requests

respuesta = requests.get(
    "https://jsonplaceholder.typicode.com/users"
)

print(respuesta.status_code)
print(respuesta.json())
```

---

## Explicación

```python
requests.get(...)
```

Realiza una petición GET.

```
status_code
```

Devuelve el código HTTP.

```
200
```

significa que todo salió correctamente.

```
json()
```

Convierte la respuesta JSON en un objeto de Python (listas y diccionarios) para poder trabajar con ella fácilmente.

---

# Códigos de estado HTTP más comunes

| Código | Significado |
|---------|-------------|
| 200 | Solicitud exitosa |
| 201 | Recurso creado correctamente |
| 204 | Solicitud exitosa sin contenido de respuesta |
| 400 | Solicitud incorrecta |
| 401 | No autorizado |
| 403 | Acceso prohibido |
| 404 | Recurso no encontrado |
| 500 | Error interno del servidor |

---

