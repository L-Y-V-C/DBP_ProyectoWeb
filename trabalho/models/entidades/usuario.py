from flask_login import UserMixin

class usuario(UserMixin):
    def __init__(self,id,username,password,nom_comple="",estado="",rol="") -> None:
        self.id=id
        self.username=username
        self.password=password
        self.nom_comple=nom_comple
        self.estado=estado
        self.rol=rol
    def verificar_contrasena(passs,otra_contrasena):
        return passs == otra_contrasena
