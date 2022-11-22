from claseprofile import Profile
username1 = input("Ingrese su username: ")
email= input("Ingrese su correo: ")
while True:
            password1 = input("Escriba la contraseña: ")
            password2 = input("Vuelva a escribir la contraseña: ")
            if password1 ==  password2:
                break
            else:
                print("Las contraseñas no coinciden.")

profile1 = Profile(1,username1,email,password1)
profile1.print()
x = input("Desea cambiar la contraseña? si/no: ")
while x=="si":
    while True:
        act = input("Ingrese la contraseña actual:")
        if act == profile1.get_password():
            break
        else:
            print("La contraseña no coincide.")

    pasw1 = input("Escriba la nueva contraseña: ")
    pasw2 = input("Vuelva a escribir la contraseña: ")
    if pasw1 ==  pasw2 and pasw1 != profile1.get_password():
        break
    elif pasw1 == pasw2:
        print("La contraseña debe ser distinta de la anterior")
profile1.change_password(pasw1)
profile1.print()
