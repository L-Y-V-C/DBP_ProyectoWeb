class Config():
    SECRET_KEY='BB'

class DeveloConfig(Config):
    DEBUG=True
    MYSQL_HOST='localhost'
    MYSQL_USER='root'
    MYSQL_PASSWORD=''
    MYSQL_DB='pag_sv'

config ={
    'develo':DeveloConfig
}