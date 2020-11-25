import React from 'react';
import { Link } from 'react-router-dom';
const Header = () => {
	return (
		<div>
			<nav className="navbar navbar-expand-lg navbar-light bg-secondary">
				<Link className="navbar-brand" to="/">
					Euclid
				</Link>
				<button
					className="navbar-toggler"
					type="button"
					data-toggle="collapse"
					data-target="#navbarSupportedContent"
					aria-controls="navbarSupportedContent"
					aria-expanded="false"
					aria-label="Toggle navigation"
				>
					<span className="navbar-toggler-icon"></span>
				</button>
				<div className="collapse navbar-collapse" id="navbarNavDropdown">
					<ul className="navbar-nav">
						<li className="nav-item dropdown">
							<Link
								className="nav-link dropdown-toggle"
								id="navbarDropdownMenuLink"
								role="button"
								data-toggle="dropdown"
								aria-haspopup="true"
								aria-expanded="false"
							>
								One Variable Ecuations
							</Link>
							<div className="dropdown-menu" aria-labelledby="navbarDropdownMenuLink">
								<Link className="dropdown-item" to="/incremental_search">
									Incremental Search
								</Link>
								<Link className="dropdown-item" to="/bisection">
									Bisection
								</Link>
								<Link className="dropdown-item" to="/newton">
									Newton
								</Link>
								<Link className="dropdown-item" to="/fixed_point">
									Fixed Point
								</Link>
								<Link className="dropdown-item" to="/multiple_roots">
									Multiple Roots
								</Link>
								<Link className="dropdown-item" to="/false_rule">
									False Rule
								</Link>
								<Link className="dropdown-item" to="/secant">
									Secant
								</Link>
							</div>
						</li>
						<li className="nav-item dropdown">
							<Link
								className="nav-link dropdown-toggle"
								to="#"
								id="navbarDropdownMenuLink"
								role="button"
								data-toggle="dropdown"
								aria-haspopup="true"
								aria-expanded="false"
							>
								Equations Systems
							</Link>
							<div className="dropdown-menu" aria-labelledby="navbarDropdownMenuLink">
								<Link className="dropdown-item" to="gauss">
									Gauss
								</Link>
								<Link className="dropdown-item" to="partial_pivoting">
									Parcial Pivoting
								</Link>
								<Link className="dropdown-item" to="total_pivoting">
									Total Pivoting
								</Link>
								<Link className="dropdown-item" to="cholesky">
									Cholesky
								</Link>
								<Link className="dropdown-item" to="crout">
									Crout
								</Link>
								<Link className="dropdown-item" to="doolittle">
									Dolittle
								</Link>
								<Link className="dropdown-item" to="lu_gauss">
									LU Gauss
								</Link>
								<Link className="dropdown-item" to="lu_partial">
									LU Partial
								</Link>
								<Link className="dropdown-item" to="jacobi">
									Jacobi
								</Link>
								<Link className="dropdown-item" to="gauss_seidel">
									Gauss Seidel
								</Link>
								<Link className="dropdown-item" to="/jacobi_sor">
									Jacobi SOR
								</Link>
								<Link className="dropdown-item" to="/gauss_seidel_sor">
									Gauss Seidel SOR
								</Link>
								{/* <Link className="dropdown-item" to="#">
                  Something else here
                </Link> */}
							</div>
						</li>
						<li className="nav-item dropdown">
							<Link
								className="nav-link dropdown-toggle"
								to="#"
								id="navbarDropdownMenuLink"
								role="button"
								data-toggle="dropdown"
								aria-haspopup="true"
								aria-expanded="false"
							>
								Interpolation
							</Link>
							<div className="dropdown-menu" aria-labelledby="navbarDropdownMenuLink">
								<Link className="dropdown-item" to="vandermonde">
									Vandermonde
								</Link>
								<Link className="dropdown-item" to="newton_interpolation">
									Newton
								</Link>
								<Link className="dropdown-item" to="lagrange">
									Lagrange
								</Link>
								<Link className="dropdown-item" to="lineal_spline">
									Linear Spline
								</Link>
								<Link className="dropdown-item" to="cuadratic_spline">
									Quadratic Spline
								</Link>
								<Link className="dropdown-item" to="cubic_spline">
									Cubic Spline
								</Link>

								{/* <Link className="dropdown-item" to="#">
                  Something else here
                </Link> */}
							</div>
						</li>
						{/* <li className="nav-item"> */}
						<Link className="navbar-brand" to="/">
							About
						</Link>
						{/* </li> */}
					</ul>
				</div>
			</nav>
		</div>
	);
};

export default Header;
