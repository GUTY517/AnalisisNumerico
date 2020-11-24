import React, { useState, useEffect } from 'react';
import Geogebra from '../assets/Geogebra';
import json_data from '../../json_data/bisection.json';
import axios from 'axios';

import FalseRuleHelp from "../../Help/NonLinealEcuations/FalseRuleHelp";

const Bisection = () => {
	const [data, setData] = useState([]);
	const [table, setTable] = useState([]);
	const [root, setRoot] = useState(null);
	const [showResults, setShowResults] = useState(false);
	const [error, setError] = useState(null);
	const [showError, setShowError] = useState(false);
  const [initial_a, setInitialA] = useState(null);
  const [func, setFunction] = useState(null);
  const [initial_b, setInitialB] = useState(null);
  const [tolerance, setTolerance] = useState(null);
  const [iterations, setIterations] = useState(null);
	// const [form_data, setFormData] = useState({
	// 	func: '',
	// 	initial_a: '0',
	// 	initial_b: '0',
	// 	tolerance: '1e-7',
	// 	iterations: '100',
	// });

	// const handleInputChange = (e) => {
	// 	setFormData({
	// 		...form_data,
	// 		[e.target.name]: e.target.value,
	// 	});
	// };

	const round = (value, decimals) => {
		return Number(Math.round(value + 'e' + decimals) + 'e-' + decimals);
	};

	const handleSubtmit = async (e) => {
		e.preventDefault();
    // const { func, initial_a, initial_b, tolerance, iterations } = form_data;
    let func_inputed = document.querySelector(".func-input").value;
    let initial_a_inputed = document.querySelector(".initial-a-input").value;
    let initial_b_inputed = document.querySelector(".initial-b-input").value;
    let tolerance_inputed = document.querySelector(".tolerance-input").value;
    let iterations_inputed = document.querySelector(".iterations-input").value;

		const number_regex = new RegExp('[+-]?([1-9]\d*(\.\d*[1-9])?|0\.\d*[1-9]+)|\d+(\.\d*[1-9])?')
		const notation = new RegExp('[-+]?[0-9]*.?[0-9]+([eE][-+]?[0-9]+)?');
		if (func_inputed === '' || func_inputed === null) {
			setError('Function can not be empty');
			setShowError(true);
			return;
    }
		if (number_regex.test(initial_a_inputed) === false) {
			setError('Enter valid number for A value');
			setShowError(true);

			return;
		}
		if (number_regex.test(initial_b_inputed) === false) {

			setError('Enter valid number for B value');
			setShowError(true);

			return;
		}
		if (!tolerance_inputed.match(notation)) {
			setError('Enter a valid error notation');
			setShowError(true);
			return;
		}
		setShowError(false);
		setError(null);
    setInitialA(initial_a_inputed);
    setInitialB(initial_b_inputed);
    setFunction(func_inputed);
    setIterations(iterations_inputed)
		const body = {
			function: func_inputed,
			initial_a: parseFloat(initial_a_inputed),
			initial_b: parseFloat(initial_b_inputed),
			tolerance: parseFloat(tolerance_inputed),
			iterations: parseFloat(iterations_inputed),
		};
		try {
			const result = await axios.post('http://127.0.0.1:5000/false_rule', body);
      const { Table, Root } = result.data;
      
			console.log(result.data);
			setTable(Table);
			setRoot(Root);
			setShowResults(true);
			// showData();
		} catch (error) {
			console.log(error);
			const { message } = error.response.data;
			setError(message);
			setShowError(true);
			setShowResults(false);
		}
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
			const root_to_show = root;
			// console.log(results);
			return (
				<React.Fragment>
					<table class="table">
						<thead>
							<tr>
								
									<th scope="col">Iteration</th>
									<th scope="col">a</th>
									<th scope="col">xm</th>
									<th scope="col">b</th>
									<th scope="col">f(xm)</th>
								
							</tr>
						</thead>
						<tbody>
							{table_to_show.map((result, index) => (
								<tr id={index}>
									<th>{round(result.Iteration, 4)}</th>
									<th>{round(result.a, 4)}</th>
									<th>{round(result.xm, 4)}</th>
									<th>{round(result.b, 4)}</th>
									<th>{result['f(xm)']}</th>
									<th>{result.Error}</th>
								</tr>
							))}
						</tbody>
					</table>
					<p>{`Root in ${root_to_show}`}</p>
				</React.Fragment>
			);
		}
		return null;
	};

	return (
		<div className="mt-3">
			<h2 className="text-center mt-2">False Rule</h2>
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
									// onChange={handleInputChange}
								></input>
							</div>
							<div className="form-group">
								<input
									type="text"
									className="form-control initial-a-input"
									placeholder="Initial a"
									name="initial_a"
									// onChange={handleInputChange}
								></input>
								<small id="initialAHelp" className="form-text text-muted">
									First element included in a range
								</small>
							</div>
							<div className="form-group">
								<input
									type="text"
									className="form-control initial-b-input"
									placeholder="Initial b"
									name="initial_b"
									// onChange={handleInputChange}
								></input>
								<small id="initialAHelp" class="form-text text-muted">
									Last element included in a range
								</small>
							</div>
							<div className="form-group">
								<input
									type="text"
									className="form-control tolerance-input"
									placeholder="Tolerance"
									name="tolerance"
									value={tolerance}
									// onChange={handleInputChange}
								></input>
							</div>
							<div className="form-group">
								<input
									type="text"
									className="form-control iterations-input"
									placeholder="Iterations"
									name="iterations"
									value={iterations}
									// onChange={handleInputChange}
								></input>
							</div>
							<div className="form-group">
								<button type="submit" class="btn btn-primary">
									Calculate
								</button>
							</div>
						</form>
					<FalseRuleHelp/>
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

export default Bisection;
