from flask import Flask



def create_app():
    app = Flask('this is an app')

    @app.route('/')
    def index():
        return 'hello this is petfax'

   # @app.route('/pets')
    #def pets_page():
       # return 'these are our pets up for adoption'

    from . import pet
    app.register_blueprint(pet.bp)
    return app