import React, { useState, useEffect } from 'react';
import Geogebra from '../assets/Geogebra';
import axios from 'axios';

const MultipleRoots = () => {
	const [data, setData] = useState([]);

	const [table, setTable] = useState([]);
	const [roots, setRoots] = useState([]);
	const [showResults, setShowResults] = useState(false);
	const [error, setError] = useState(null);
	const [showError, setShowError] = useState(false);
	const [tolerance, setTolerance] = useState(null);
	const [iterations, setIterations] = useState(null);
	const [initial_x0, setInitialX0] = useState(null);

	const handleSubtmit = async (e) => {
		e.preventDefault();
		let func_inputed = document.querySelector('.func-input').value;
		let initial_x0_inputed = document.querySelector('.x0-input').value;
		let tolerance_inputed = document.querySelector('.tolerance-input').value;
		let iterations_inputed = document.querySelector('.iterations-input').value;

		const number_regex = new RegExp('[+-]?([1-9]d*(.d*[1-9])?|0.d*[1-9]+)|d+(.d*[1-9])?');
		const notation = new RegExp('[-+]?[0-9]*.?[0-9]+([eE][-+]?[0-9]+)?');
		if (func_inputed === '' || func_inputed === null) {
			setError('Function can not be empty');
			setShowError(true);
			return;
		}
		if (number_regex.test(initial_x0_inputed) === false) {
			setError('Enter valid number for A value');
			setShowError(true);

			return;
		}
		if (!tolerance_inputed.match(notation)) {
			setError('Enter a valid error notation');
			setShowError(true);
			return;
		}
		const body = {
			function: func_inputed,
			initial_x0: parseFloat(initial_x0_inputed),
			tolerance: parseFloat(tolerance_inputed),
			iterations: parseFloat(iterations_inputed),
		};
		try {
			console.log(body);
			const result = await axios.post('http://127.0.0.1:5000/multiple_roots', body);
			const { Table, Root } = result.data;
			console.log(Table);
			console.log(Root);
			setTable(Table);
			setRoots(Root);
			setShowResults(true);
		} catch (error) {
			console.log(error);
			const { message } = error.response.data;
			setError(message);
			setShowError(true);
			setShowResults(false);
		}
	};

	const round = (value, decimals) => {
		return Number(Math.round(value + 'e' + decimals) + 'e-' + decimals);
	};
	const showData = () => {
		if (error || showError) {
			return (
				<div className="d-inline-flex p-2 m-3 text-danger font-weight-bold">
					<p>{error}</p>
				</div>
			);
		}
		if (showResults) {
			const table_to_show = table;
			const roots_to_show = roots;
			// console.log(results);
			return (
				<React.Fragment>
					<table class="table">
						<thead>
							<tr>
								<th scope="col">Iteration</th>
								<th scope="col">xi</th>
								<th scope="col">f(xi)</th>
								<th scope="col">Error</th>
							</tr>
						</thead>
						<tbody>
							{table_to_show.map((result, index) => (
								<tr id={index}>
									<th>{round(result.Iteration, 4)}</th>
									<th>{round(result.xi, 4)}</th>
									<th>{result['f(xi)']}</th>
									<th>{result.Error}</th>
								</tr>
							))}
						</tbody>
					</table>
					<div className="">
						{roots_to_show.map((root, rootIndex) => {
							return <p>{`Root in ${root}`}</p>;
						})}
					</div>
				</React.Fragment>
			);
		}
		return null;
	};

	return (
		<div>
			<h2 className="text-center mt-2">Multiple Roots</h2>
			<div className="container mt-2">
				<div className="row">
					<div className="col-6 mt-3">
						<form className="m-auto" onSubmit={handleSubtmit}>
							<div className="form-group">
								<input
									type="text"
									className="form-control func-input"
									placeholder="f(x)="
									name="func"
								></input>
							</div>
							<div className="form-group">
								<input
									type="text"
									className="form-control x0-input"
									placeholder="Initial x0"
									name="initial_x0"
								></input>
								<small id="initialAHelp" class="form-text text-muted">
									First aproximation
								</small>
							</div>
							<div className="form-group">
								<input
									type="text"
									className="form-control tolerance-input"
									placeholder="Tolerance"
									name="tolerance"
								></input>
							</div>
							<div className="form-group">
								<input
									type="text"
									className="form-control iterations-input"
									placeholder="Iterations"
									name="iterations"
								></input>
							</div>
							<div className="form-group">
								<button type="submit" class="btn btn-primary">
									Calculate
								</button>
							</div>
						</form>
					</div>
					<div>
						<Geogebra />
					</div>
				</div>
				<div className="row">
					<div className="col">
						<h3>Results</h3>
						{showData()}
					</div>
				</div>
			</div>
		</div>
	);
};

export default MultipleRoots;
