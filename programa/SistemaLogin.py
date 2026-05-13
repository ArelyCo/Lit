# Sistema de login simple

# Usuario y contraseña guardados
usuario_correcto = "admin"
contrasena_correcta = "1234"

# Número máximo de intentos
intentos_maximos = 3
intentos = 0

print("=== SISTEMA DE LOGIN ===")

while intentos < intentos_maximos:
    usuario = input("Ingresa tu usuario: ")
    contrasena = input("Ingresa tu contraseña: ")

    if usuario == usuario_correcto and contrasena == contrasena_correcta:
        print(" Bienvenido al sistema")
        break
    else:
        intentos += 1
        print(f" Datos incorrectos. Intento {intentos} de {intentos_maximos}")

if intentos == intentos_maximos:
    print(" Has alcanzado el número máximo de intentos. Acceso bloqueado.")
    