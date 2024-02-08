from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
from flask_migrate import Migrate
from config import Config
from app.routes import api_bp

app = Flask(__name__)
app.config.from_object(Config)

# db = SQLAlchemy(app)

# migrate = Migrate(db, app)

app.register_blueprint(api_bp)

if __name__ == '__main__':
    app.run()