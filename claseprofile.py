class Profile:
    def __init__(self,id,email,username,password,status="online",level=0):
        self.id=id
        self.email=email
        self.username=username
        self.password=password
        self.status=status
        self.level=level


    def print(self):
        print("El id es: ",self.id)
        print("El username es: ",self.username)
        print("Su contraseña es: ",self.password)

    def get_password(self):
        return self.password

    def change_password(self,a):
        self.password=a
