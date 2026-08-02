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

Para ello utilizamos el método especial `__init__()`, que se ejecuta automáticamente cuando se crea el objeto.

```python
class Persona:

    def __init__(self, nombre):
        self.nombre = nombre
```

En este ejemplo, cada objeto de la clase **Persona** tendrá un atributo llamado **nombre**.

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

![Clase y Objetos](course_checkpoint_6_images/python_class_image.jpg)

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
