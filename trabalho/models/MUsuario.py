from .entidades.usuario import usuario
class MUsuario():
    @classmethod
    def login(self,db,usuarioo):
        try:
            cursor=db.connection.cursor()
            sql="SELECT id,username,password,nom_comple,estado,rol FROM usuarios WHERE username='{}'".format(usuarioo.username)
            cursor.execute(sql)
            row=cursor.fetchone()
            if row != None:
                user=usuario(row[0],row[1],usuario.verificar_contrasena(row[2],usuarioo.password),row[3],row[4],row[5])
                return user
            else:
                return None
        except Exception as ex:
            raise Exception(ex)
    @classmethod
    def get_by_id(self,db,id):
        try:
            cursor=db.connection.cursor()
            sql="SELECT id,username,nom_comple,estado,rol FROM usuarios WHERE id='{}'".format(id)
            cursor.execute(sql)
            row=cursor.fetchone()
            if row != None:
                log_user=usuario(row[0],row[1],None,row[2],row[3],row[4])
                return log_user
            else:
                return None
        except Exception as ex:
            raise Exception(ex)