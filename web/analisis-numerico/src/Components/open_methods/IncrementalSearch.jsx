import React, { useState, useEffect } from 'react';
import Geogebra from '../assets/Geogebra';
import axios from 'axios';

import NewtonHelp from '../../Help/NonLinealEcuations/NewtonHelp';
import SpecialInputHelp from '../../Help/SpecialInputHelp';
import IncrementalSearchHelp from '../../Help/NonLinealEcuations/IncrementalSearchHelp';
const IncrementalSearch = () => {
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
		let delta_x_inputed = document.querySelector('.delta-x-input').value;
		let iterations_inputed = document.querySelector('.iterations-input').value;

		const number_regex = new RegExp('[+-]?([1-9]d*(.d*[1-9])?|0.d*[1-9]+)|d+(.d*[1-9])?');
		const notation = new RegExp('[-+]?[0-9]*.?[0-9]+([eE][-+]?[0-9]+)?');
		if (func_inputed === '' || func_inputed === null) {
			setError('Function can not be empty');
			setShowError(true);
			return;
		}
		if (number_regex.test(initial_x0_inputed) === false) {
			setError('x0 must be different than zero (0)');
			setShowError(true);

			return;
		}
		if (number_regex.test(delta_x_inputed) === false) {
			setError('Enter valid number for delta x value');
			setShowError(true);

			return;
    }
    setShowError(false);
    setError(null);
		const body = {
			function: func_inputed,
			x0: parseFloat(initial_x0_inputed),
			delta_x: parseFloat(delta_x_inputed),
			iterations: parseFloat(iterations_inputed),
		};
		try {
			console.log(body);
			const result = await axios.post('https://euclid-api.herokuapp.com/incremental_searches', body);
			const { Roots } = result.data;
			console.log(Roots);
			setRoots(Roots);
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
			const root_to_show = roots;
			// console.log(results);
			return (
				<React.Fragment>
					<table class="table">
          <thead>
            <tr>
              <th scope="col">X Lower</th>
              <th scope="col">X Upper</th>

            </tr>
          </thead>
						<tbody>
							{root_to_show.map((row, indexRow) => (
								<tr id={indexRow}>
									{row.map((column, indexColumn) => (
										<th>{round(column, 4)}</th>
									))}
								</tr>
							))}
						</tbody>
					</table>
				</React.Fragment>
			);
		}
		return null;
	};

	return (
		<div>
			<h2 className="text-center mt-2">Incremental Search</h2>
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
								<input type="text" className="form-control delta-x-input" placeholder="delta x"></input>
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
						<IncrementalSearchHelp />
						<SpecialInputHelp />
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

export default IncrementalSearch;
