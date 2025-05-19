app = Flask(__name__)  
app.secret_key = "chave-super-secreta" 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db' 
