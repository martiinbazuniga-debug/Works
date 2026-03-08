usuario_correcto = "SHAGI"
contraseña_correcta = "para que"

#Variables de control
intentos_maximos = 3
intento_realizados = 0
acceso_concedido = False

#Paso 3
print ('=== Login sesion ===')

print (f'tienes {intentos_maximos} intentos disponibles')

while intento_realizados < intentos_maximos and not acceso_concedido:
    intentos_restantes = intentos_maximos - intento_realizados
    print (f'\n Intento {intentos_restantes} intentos disponibles')

    #Solicitar datos
    usuario = input('Usuario: ')
    contraseña = input ('Contraseña: ')

    #Paso 5 Validar campos vacios
    if usuario == '' or contraseña == '':
        print('ERROR DE AUNTENTICIDAD: Los campos no pueden estar vacios')
        intento_realizados = intento_realizados + 1
        continue

    #Paso 6 Validar credenciales 
    if usuario == usuario_correcto and contraseña == contraseña_correcta:
        print ('ACCESO PERMITIDO: Credenciales correctas')
        acceso_concedido = True 
    else:
        print('El usuario o la contraseña no son correctos')
        intento_realizados = intento_realizados + 1 

if not acceso_concedido:
    print ('Acceso Bloqueado: Has agotado tus tres intentos')



