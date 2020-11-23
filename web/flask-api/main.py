#! /usr/bin/env python3
'''Path definitions and methods imports'''

from flask import Flask
from flask_restful import Api, Resource
from resources.incremental_searches import IncrementalSearch
from resources.bisection import Bisection
from resources.false_rule import FalseRule
from resources.fixed_point import FixedPoint
from resources.multiple_roots import MultipleRoots
from resources.newton import Newton
from resources.secant import Secant
from resources.gauss import Gauss
from resources.partial_pivoting import PartialPivoting
from resources.total_pivoting import TotalPivoting
from resources.lu_gauss import LuGauss
from resources.lu_pivoting import LuPivoting
from resources.crout import Crout
from resources.doolittle import Doolittle
from resources.cholesky import Cholesky
from resources.jacobi import Jacobi
from resources.gauss_seidel import GaussSeidel
from resources.gauss_seidel_sor import GaussSeidelSor
from resources.jacobi_sor import JacobiSor
from resources.vandermonde import Vandermonde
from resources.newton_interpolation import NewtonInterpolation
from resources.lagrange import Lagrange
from resources.lineal_spline import LinealSpline
from resources.cuadratic_spline import CuadraticSpline
from resources.cubic_spline import CubicSpline
from flask_cors import CORS


app = Flask(__name__)
CORS(app)
api = Api(app)

api.add_resource(IncrementalSearch, "/incremental_searches")
api.add_resource(Bisection, "/bisection")
api.add_resource(FalseRule, "/false_rule")
api.add_resource(FixedPoint, "/fixed_point")
api.add_resource(MultipleRoots, "/multiple_roots")
api.add_resource(Newton, "/newton")
api.add_resource(Secant, "/secant")
api.add_resource(Gauss, "/gauss")
api.add_resource(PartialPivoting, "/partial_pivoting")
api.add_resource(TotalPivoting, "/total_pivoting")
api.add_resource(LuGauss, "/lu_gauss")
api.add_resource(LuPivoting, "/lu_pivoting")
api.add_resource(Crout, "/crout")
api.add_resource(Doolittle, "/doolittle")
api.add_resource(Cholesky, "/cholesky")
api.add_resource(Jacobi, "/jacobi")
api.add_resource(GaussSeidel, "/gauss_seidel")
api.add_resource(GaussSeidelSor, "/gauss_seidel_sor")
api.add_resource(JacobiSor, "/jacobi_sor")
api.add_resource(Vandermonde, "/vandermonde")
api.add_resource(NewtonInterpolation, "/newton_interpolation")
api.add_resource(Lagrange, "/lagrange")
api.add_resource(LinealSpline, "/lineal_spline")
api.add_resource(CuadraticSpline, "/cuadratic_spline")
api.add_resource(CubicSpline, "/cubic_spline")

if __name__ == "__main__":
    app.run(debug=True)
