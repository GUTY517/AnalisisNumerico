import React, { useState, useEffect } from 'react';
import Geogebra from '../assets/Geogebra';
import axios from 'axios';

import FixedPointHelp from "../../Help/NonLinealEcuations/FixedPointHelp";
import SpecialInputHelp from '../../Help/SpecialInputHelp';

const FixedPoint = () => {
	const [data, setData] = useState([]);
	const [table, setTable] = useState([]);
	const [roots, setRoots] = useState(null);
	const [showResults, setShowResults] = useState(false);
	const [error, setError] = useState(null);
	const [showError, setShowError] = useState(false);
  const [f_function, setFFunction] = useState(null);
  const [g_function, setGFunction] = useState(null);
  const [initial_x0, setInitialX0] = useState(null);
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

	const handleSubmit = async (e) => {
		e.preventDefault();
    // const { func, initial_a, initial_b, tolerance, iterations } = form_data;
    let f_func_inputed = document.querySelector(".f-func-input").value;
    let g_func_inputed = document.querySelector(".g-func-input").value;
    let initial_x0_inputed = document.querySelector(".initial-x0-input").value;
    let tolerance_inputed = document.querySelector(".tolerance-input").value;
    let iterations_inputed = document.querySelector(".iterations-input").value;

		const number_regex = new RegExp('[+-]?([1-9]\d*(\.\d*[1-9])?|0\.\d*[1-9]+)|\d+(\.\d*[1-9])?')
		const notation = new RegExp('[-+]?[0-9]*.?[0-9]+([eE][-+]?[0-9]+)?');
		if (f_func_inputed === '' || f_func_inputed === null) {
			setError('Function f can not be empty');
			setShowError(true);
			return;
    }
		if (g_func_inputed === '' || g_func_inputed === null) {
			setError('Function g can not be empty');
			setShowError(true);
			return;
    }
		if (number_regex.test(initial_x0_inputed) === false) {
			setError('Enter valid number for x0 value');
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
    setInitialX0(initial_x0_inputed);
    setFFunction(f_func_inputed);
    setGFunction(g_func_inputed);
    setTolerance(tolerance_inputed);
    setIterations(iterations_inputed);
		const body = {
			function_f: f_func_inputed,
			function_g: g_func_inputed,
			initial_x0: parseFloat(initial_x0_inputed),
			tolerance: parseFloat(tolerance_inputed),
			iterations: parseFloat(iterations_inputed),
		};
		try {
			const result = await axios.post('https://euclid-api.herokuapp.com/fixed_point', body);
			const { Table, Root } = result.data;
			console.log(result.data);
			setTable(Table);
			setRoots(Root);
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
			const root_to_show = roots;
			// console.log(results);
			return (
				<React.Fragment>
					<table class="table">
						<thead>
							<tr>
                <th scope="col">Iteration</th>
                <th scope="col">xi</th>
                <th scope="col">g(xi)</th>
                <th scope="col">f(xi)</th>
                <th scope="col">Error</th>
								{/* {header_to_show.map((column) => (
								))} */}
							</tr>
						</thead>
						<tbody>
							{table_to_show.map((result, index) => (
								<tr id={index}>
									<th>{result.Iteration}</th>
									<th>{round(parseFloat(result.xi), 4)}</th>
									<th>{round(parseFloat(result["g(xi)"]), 4)}</th>
									<th>{round(parseFloat(result["f(xi)"]), 4)}</th>
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
			<h2 className="text-center mt-2">Fixed Point</h2>
			<div className="container mt-2">
				<div className="row">
					<div className="col-6 mt-3">
						<form className="m-auto" onSubmit={handleSubmit}>
							<div className="form-group">
								<input
									type="text"
									className="form-control f-func-input"
									placeholder="f(x)="
									name="func"
									// onChange={handleInputChange}
								></input>
							</div>
							<div className="form-group">
								<input
									type="text"
									className="form-control g-func-input"
									placeholder="g(x)="
									// onChange={handleInputChange}
								></input>
								<small id="initialAHelp" class="form-text text-muted">
									First element included in a range
								</small>
							</div>
							<div className="form-group">
								<input
									type="text"
									className="form-control initial-x0-input"
									placeholder="Initial x0"
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
									// onChange={handleInputChange}
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
            <FixedPointHelp/>
            <SpecialInputHelp/>
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

export default FixedPoint;
