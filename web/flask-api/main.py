from flask import Flask
from flask_restful import Api, Resource
from resources.bisection import Bisection
from resources.false_rule import False_Rule
from resources.fixed_point import Fixed_Point
# space for incremental searches importation
from resources.multiple_roots import Multiple_Roots
from resources.newton import Newton
from resources.secant import Secant


app = Flask(__name__)
api = Api(app)


api.add_resource(Bisection, "/bisection")
api.add_resource(False_Rule, "/false_rule")
api.add_resource(Fixed_Point, "/fixed_point")
api.add_resource(Multiple_Roots, "/multiple_roots")
api.add_resource(Newton, "/newton")
api.add_resource(Secant, "/secant")


if __name__ == "__main__":
    app.run(debug=True)
