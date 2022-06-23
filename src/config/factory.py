import logging
from quart import jsonify, Quart
from api.routes.health import blueprint as health_api
from constants.http_responses import *
from quart_schema import QuartSchema
from quart_cors import cors
from config.log import get_logging_handler
from config import Config
from secure import Secure

def create_app(config: Config): 
    secure_headers = Secure()

    app = Quart(__name__)
    QuartSchema(app, title = 'My API')
    cors(app) # TODO: restrict this
    
    # flask/quart uses upper case letters for config, override them here:
    app.config.update(
        DEBUG=config.debug,
        ENV='development' if config.debug == True else 'production'
    )

    app.config.from_object(config)

    # app.register_blueprint(<new_api_route>, url_prefix='/api')
    app.register_blueprint(health_api)    

    @app.after_request
    def add_header(response):
        secure_headers.framework.flask(response)
        return response

    @app.errorhandler(400)
    def bad_request(e):
        logging.error(e)
        return jsonify(errorCode=BAD_REQUEST_400['code'],
                errorDescription=BAD_REQUEST_400['message']), 400

    @app.errorhandler(500)
    def server_error(e):
        logging.error(e)
        return jsonify(errorCode=SERVER_ERROR_500['code'],
                errorDescription=SERVER_ERROR_500['message']), 500

    @app.errorhandler(404)
    def not_found(e):
        logging.error(e)
        return jsonify(errorCode=SERVER_ERROR_404['code'],
                errorDescription=SERVER_ERROR_404['message']), 404

    app.logger.addHandler(get_logging_handler())
    app.logger.setLevel(logging.DEBUG if config.debug == True else logging.INFO)
    
    return app

