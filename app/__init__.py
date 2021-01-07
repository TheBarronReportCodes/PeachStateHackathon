from flask import Flask
from app.model.database import Database
from flask_login import LoginManager

db = Database()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '6h6wzwJzZp' #used for flash messaging. Every app using a secret key should be unique
    
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login' #controls where the user will be redirected if they attempt to access a login_required view without being logged in
    login_manager.init_app(app)
    
    @login_manager.user_loader
    def load_user(email):
        return db.users.get_user(email)
    
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app