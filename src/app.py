from flask import Flask
from config.config import Config
from model.models import db
from manager.routes import api
from utility.utils import setup_logger
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

app_logger = setup_logger('app')

swaggerui_blueprint = get_swaggerui_blueprint(
    Config.SWAGGER_URL,
    Config.API_URL,
    config={
        'app_name': "Sample Flask API"
    }
)

app.register_blueprint(swaggerui_blueprint, url_prefix=Config.SWAGGER_URL)
app.register_blueprint(api, url_prefix='/api')

@app.cli.command('create_tables')
def create_tables():
    db.create_all()
    app_logger.info("Tables created")

if __name__ == '__main__':
    app.run(debug=True)
