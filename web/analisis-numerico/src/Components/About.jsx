import React from 'react';

const About = () => {
	return (
		<div className="container">
			<div class="jumbotron">
				<div className="mb-5">
					<h2>Euclid project was built by three persons.</h2>
				</div>
				<ul>
					<li>Mateo Marulanda Cifuentes</li>
					<li>Mateo Gutiérrez Gómez</li>
					<li>Yashúa Narváez Pulgarín</li>
				</ul>
				<p>Our project is focused on using numerical analysis methods.</p>
				<p>We've divided Euclid project in three sections. </p>
				<br />
				<p className="font-weight-bold">Available methods:</p>
				<div className="d-inline-flex mb-4">
					<div className="m-2">
          <p className="font-weight-bold"> Non linear equations</p>
						<ul>
							<li>Bisection</li>
							<li>False Rule</li>
							<li>Fixed Point</li>
							<li>Multiple Roots</li>
							<li>Newton</li>
							<li>Secant</li>
						</ul>
					</div>
					<div className="m-2 ml-2 ">
          <p className="font-weight-bold">Ecuation systems</p>
						<ul className="text-wrap">
							<li>Cholesky</li>
							<li>Crout</li>
							<li>Doolittle</li>
							<li>Gauss</li>
							<li>Gauss Seidel</li>
							<li>Gauss -Partial -Total Pivoting</li>
							<li>Gauss SOR</li>
							<li className="text-wrap">Gauss LU for simple, seidel, partial and total pivoting</li>
							<li>Jacobi</li>
						</ul>
					</div>
					<div className="m-2 ml-2 ">
          <p className="font-weight-bold">Interpolation methods</p>
						<ul className="text-wrap">
							<li>Newton interpolating</li>
							<li>Vandermonde</li>
							<li>Lineal splines</li>
							<li>Cuadratic splines</li>
							<li>Cubic splines</li>
						</ul>
					</div>
				</div>
      <p>This project uses <a href="https://flask.palletsprojects.com/en/1.1.x/">Python Flask</a> for Backend and <a href="https://es.reactjs.org/">React.js</a> for Front-end</p>
			<br/>
      <p className="font-weight-bold">Python Libraries</p>
        <ul>
          <li><a href="https://numpy.org/">numpy</a></li>
          <li><a href="https://pandas.pydata.org/">pandas</a></li>
          <li><a href="https://pypi.org/project/prettytable/">prettytable</a></li>
          <li><a href="https://www.scipy.org/">scipy</a></li>
          <li><a href="https://www.sympy.org/es/">sympy</a></li>
        </ul>
      </div>
		</div>
	);
};

export default About;
