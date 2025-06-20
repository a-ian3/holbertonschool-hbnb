from flask import Flask
from flask_restx import Api
from app.presentation.api.v1.routes import api_v1

app = Flask(__name__)
api = Api(app, version="1.0", title="HBnB API", description="HBnB Backend API")

api.add_namespace(api_v1, path="/api/v1")

if __name__ == "__main__":
    app.run(debug=True)

