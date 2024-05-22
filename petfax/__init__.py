from flask import Flask

# Application Factory
def create_app():
    app = Flask(__name__, template_folder='../templates')

    # Index Route
    @app.route('/')
    def hello():
        return 'Hello, PetFax!'
    
    # Pet Blueprint
    from . import pet
    app.register_blueprint(pet.bp)

    # Fact Blueprint
    from . import fact
    app.register_blueprint(fact.bp)

    return app
