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

function App() {
	return (
		<div className="App">
			<Router>
				<Header />

				<Switch>
					<Route path="/bisection">
						<Bisection />
					</Route>
					<Route path="/newton">
						<Newton />
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
				</Switch>
			</Router>
		</div>
	);
}

export default App;
