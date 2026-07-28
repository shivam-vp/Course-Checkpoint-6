class Usuario:
    def __init__(self, nombre_usuario, contrasena):
        self.nombre_usuario = nombre_usuario
        self.contrasena = contrasena


# Crear un objeto de la clase Usuario
usuario1 = Usuario("Shivam", "Password123")

# Mostrar los datos
print("Nombre de usuario:", usuario1.nombre_usuario)
print("Contraseña:", usuario1.contrasena)