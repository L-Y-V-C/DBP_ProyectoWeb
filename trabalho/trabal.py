from flask import Flask, render_template,request,redirect,url_for,flash
from flask_mysqldb import MySQL
from flask_login import LoginManager,login_user,logout_user
from config import config
from models.MUsuario import MUsuario
from models.entidades.usuario import usuario
import os

app= Flask(__name__)

conexion=MySQL(app)
login_man=LoginManager(app)

@login_man.user_loader
def load(id):
    user = MUsuario.get_by_id(conexion, id)
    if user:
        print("Rol del usuario cargado:", user.rol)
    else:
        print("Usuario no encontrado")
    return user

base_dir = os.path.abspath(os.path.dirname(__file__))
UPLOAD_FOLDER = os.path.join(base_dir, 'static', 'uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return redirect(url_for('login'))
@app.route('/login',methods=['GET','POST'])
def login():
    if request.method=='POST':
        user=usuario(0,request.form['username'],request.form['password'])
        logged=MUsuario.login(conexion,user)
        if(logged != None):
            if(logged.password):
                login_user(logged)
                return redirect(url_for('inicio'))
            else:
                flash("Contraseña invalida..")
                return render_template('index.html')
        else:
            flash("No encontrado el usuario..")
            return render_template('index.html')
    else:
        return render_template('index.html')
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))
@app.route('/inicio')
def inicio():
    return render_template('inicio.html')

@app.route('/registro')
def reg():
    return render_template('registro.html')
@app.route('/crear-reg',methods=['GET','POST'])
def crear_reg():
    username=request.form['username']
    password=request.form['password']
    nom_comple=request.form['nom_comple']
    curs=conexion.connection.cursor()
    curs.execute(" INSERT INTO usuarios (username,password,nom_comple,estado,rol) VALUES (%s,%s,%s,'1','2')",(username,password,nom_comple))
    conexion.connection.commit()
    return render_template('index.html')

@app.route('/formulario', methods=['GET', 'POST'])
def formulario():
    if request.method == 'POST':
        alias = request.form['alias']
        descripcion = request.form['descripcion']
        
        archivo = request.files['archivo']
        archivo_nombre = archivo.filename
        
        archivo_guardado = os.path.join(app.config['UPLOAD_FOLDER'], archivo_nombre)
        archivo.save(archivo_guardado)
        
        curs = conexion.connection.cursor()
        curs.execute("INSERT INTO publicaciones (nombre_publicacion, descripcion, ruta_imagen) VALUES (%s, %s, %s)",
                     (alias, descripcion, archivo_nombre))
        conexion.connection.commit()
        
        return render_template('form_datos.html', alias=alias, descripcion=descripcion, archivo_nombre=archivo_nombre)
    
    return render_template('form_file.html')

@app.route('/listarUsuarios', methods=['GET','POST'])
def listarUsuarios():
    curs=conexion.connection.cursor()
    curs.execute("SELECT * FROM usuarios")
    usuarios1 = curs.fetchall()
    curs.close()
    return render_template('admiListaUsuarios.html', usuarios=usuarios1)

@app.route('/listarUsuariosOrdUsuAsc', methods=['GET','POST'])
def listarUsuariosOrdUsuAsc():
    curs=conexion.connection.cursor()
    curs.execute("SELECT * FROM usuarios ORDER BY username ASC")
    usuarios1 = curs.fetchall()
    curs.close()
    return render_template('admiListaUsuarios.html', usuarios=usuarios1)

@app.route('/listarUsuariosOrdUsuDesc', methods=['GET','POST'])
def listarUsuariosOrdUsuDesc():
    curs=conexion.connection.cursor()
    curs.execute("SELECT * FROM usuarios ORDER BY username DESC")
    usuarios1 = curs.fetchall()
    curs.close()
    return render_template('admiListaUsuarios.html', usuarios=usuarios1)

@app.route('/listarUsuariosOrdNomAsc', methods=['GET','POST'])
def listarUsuariosOrdNomAsc():
    curs=conexion.connection.cursor()
    curs.execute("SELECT * FROM usuarios ORDER BY nom_comple ASC")
    usuarios1 = curs.fetchall()
    curs.close()
    return render_template('admiListaUsuarios.html', usuarios=usuarios1)

@app.route('/listarUsuariosOrdNomDesc', methods=['GET','POST'])
def listarUsuariosOrdNomDesc():
    curs=conexion.connection.cursor()
    curs.execute("SELECT * FROM usuarios ORDER BY nom_comple DESC")
    usuarios1 = curs.fetchall()
    curs.close()
    return render_template('admiListaUsuarios.html', usuarios=usuarios1)

@app.route('/eliminarUsuario/<id>')
def eliminarUsuario(id):
    curs=conexion.connection.cursor()
    curs.execute("DELETE FROM usuarios WHERE id = %s", ([id]))
    conexion.connection.commit()
    return redirect(url_for('listarUsuarios'))

@app.route('/editarUsuario/<id>')
def obtenerUsuario(id):
    curs=conexion.connection.cursor()
    curs.execute("SELECT * FROM usuarios WHERE id = %s", ([id]))
    data = curs.fetchall()
    return render_template('admiEditarUsuario.html', usuario=data[0])

@app.route('/actualizarUsuario/<id>', methods=['POST'])
def actualizarUsuario(id):
    if request.method=='POST':
        username=request.form['username']
        password=request.form['password']
        nom_comple=request.form['nom_comple']
        estado=request.form['estado']
        rol=request.form['rol']
    curs=conexion.connection.cursor()
    curs.execute("""
        UPDATE usuarios
        SET username = %s,
            password = %s,
            nom_comple = %s,
            estado = %s,
            rol = %s
        WHERE id = %s
        """, (username, password, nom_comple, estado, rol, [id]))
    conexion.connection.commit()
    return redirect(url_for('listarUsuarios'))

@app.route('/listarPublicaciones', methods=['GET','POST'])
def listarPublicaciones():
    curs=conexion.connection.cursor()
    curs.execute("SELECT * FROM publicaciones")
    publi1 = curs.fetchall()
    curs.close()
    return render_template('admiListaPublicaciones.html', publicaciones=publi1)

@app.route('/eliminarPublicacion/<id>')
def eliminarPublicacion(id):
    curs=conexion.connection.cursor()
    curs.execute("DELETE FROM publicaciones WHERE id = %s", ([id]))
    conexion.connection.commit()
    return redirect(url_for('listarPublicaciones'))

@app.route('/listaMenu', methods=['GET','POST'])
def listaMenu():
    curs=conexion.connection.cursor()
    curs.execute("SELECT * FROM publicaciones")
    publi2 = curs.fetchall()
    curs.close()
    return render_template('listaMenu.html', publicaciones=publi2)

def pag_no_encontrada1(error):
    return redirect(url_for('index'))

def pag_no_encontrada2(error):
    return "<h1>No encontrada la pagina</h1>",404

if __name__ == '__main__':
    app.config.from_object(config['develo'])
    app.register_error_handler(401,pag_no_encontrada1)
    app.register_error_handler(404,pag_no_encontrada2)
    app.run()