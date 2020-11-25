import React from 'react';
import Header from './Components/Header';
import useScript from 'react-script-hook';

import { BrowserRouter as Router, Switch, Route, Link } from 'react-router-dom';
import Bisection from './Components/open_methods/Bisection';
import Newton from './Components/open_methods/Newton';
import False_Rule from './Components/open_methods/False_Rule';
import Fixed_Point from './Components/open_methods/Fixed_Point';
import Secant from './Components/open_methods/Secant';
import MultipleRoots from './Components/open_methods/MultipleRoots';
import Gauss from './Components/Gauss/Gauss';
import PartialPivoting from './Components/Gauss/PartialPivoting';
import TotalPivoting from './Components/Gauss/TotalPivoting';
import Cholesky from './Components/Gauss/Cholesky';
import Crout from './Components/Gauss/Crout';
import Doolittle from './Components/Gauss/Doolittle';
import LUGauss from './Components/Gauss/LUGauss';
import LUPartial from "./Components/Gauss/LUPartial";
import Jacobi from './Components/Gauss/Jacobi';
import GaussSeidel from './Components/Gauss/GaussSeidel';
import Jacobi_SOR from './Components/Gauss/Jacobi_SOR';
import Gauss_Seidel_SOR from './Components/Gauss/Gauss_Seidel_SOR';
import Newton_Interpolation from './Components/interpolation/Newton_Interpolation';
import Vandermonde from './Components/interpolation/VanderMonde';
import Lagrange from './Components/interpolation/Lagrange';
import LinearSpline from './Components/interpolation/LinearSpline';
import CuadraticSpline from './Components/interpolation/CuadraticSpline';
import CubicSpline from './Components/interpolation/CubicSpline';
import IncrementalSearch from './Components/open_methods/IncrementalSearch';
import About from './Components/About';
import NotFound from './NotFound';

function App() {
	return (
		<div className="App">
			<Router>
				<Header />

				<Switch>
					<Route  exact path="/">
						<About/>
					</Route>
					<Route exact path="/bisection">
						<Bisection />
					</Route>
					<Route path="/newton">
						<Newton />
					</Route>
					<Route path="/incremental_search">
						<IncrementalSearch />
					</Route>
					<Route path="/gauss">
						<Gauss/>
					</Route>
					<Route path="/partial_pivoting">
						<PartialPivoting/>
					</Route>
					<Route path="/total_pivoting">
						<TotalPivoting/>
					</Route>
					<Route path="/cholesky">
						<Cholesky/>
					</Route>
					<Route path="/doolittle">
						<Doolittle/>
					</Route>
					<Route path="/crout">
						<Crout/>
					</Route>
					<Route path="/lu_gauss">
						<LUGauss/>
					</Route>
					<Route path="/lu_partial">
						<LUPartial/>
					</Route>
					<Route path="/false_rule">
						<False_Rule />
					</Route>
					<Route path="/fixed_point">
						<Fixed_Point />
					</Route>
					<Route path="/secant">
						<Secant />
					</Route>
					<Route path="/multiple_roots">
						<MultipleRoots />
					</Route>
					<Route path="/jacobi">
						<Jacobi/>
					</Route>
					<Route path="/gauss_seidel">
						<GaussSeidel/>
					</Route>
					<Route path="/jacobi_sor">
						<Jacobi_SOR/>
					</Route>
					<Route path="/gauss_seidel_sor">
						<Gauss_Seidel_SOR/>
					</Route>
					<Route path="/newton_interpolation">
						<Newton_Interpolation/>
					</Route>
					<Route path="/vandermonde">
						<Vandermonde/>
					</Route>
					<Route path="/lagrange">
						<Lagrange/>
					</Route>
					<Route path="/lineal_spline">
						<LinearSpline/>
					</Route>
					<Route path="/cuadratic_spline">
						<CuadraticSpline/>
					</Route>
					<Route path="/cubic_spline">
						<CubicSpline/>
					</Route>
					<Route path="*" component={NotFound}></Route>
				</Switch>
			</Router>
		</div>
	);
}

export default App;
