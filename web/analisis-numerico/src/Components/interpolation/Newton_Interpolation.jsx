import React, { useState, useEffect } from 'react';
import json_data from '../../json_data/total_pivoting.json';
import MatrixInput from '../assets/MartrixInput';
import axios from 'axios';
import '../../App.css';
const Newton_Interpolation = () => {
	const [matrix_size, setMatrixSize] = useState(3);
	const [show_matrix, setShowMatrix] = useState(false);
	const [show_matrix_result, setShowMatrixResult] = useState(false);
	const [error, setError] = useState(null);
	const [showError, setShowError] = useState(false);
	const [sizeError, setSizeError] = useState(null);

	const [coefficients, setCoefficients] = useState([]);
	const [polynomials, setPolynomials] = useState([])
	const [x_values, setXValues] = useState(new Array(matrix_size));
	const [y_values, setYValues] = useState(new Array(matrix_size));
	const [showHelp, setShowHelp] = useState(false);

	const showHelpCard = (e) => {
		if (showHelp) {
			setShowHelp(false);
		} else {
			setShowHelp(true);
		}
	};

	const handleChangeSizeMatrix = (event) => {
		let value = event.target.value;
		setMatrixSize(value);
	};

	const setOnesMatrix = (e) => {
		e.preventDefault();
		const regex = new RegExp('[0-9]+');
		setError(null);
		if (matrix_size < 2 || matrix_size === null) {
			setSizeError('Error performing table size, the value must be greater than 1');
			setShowError(true);
			return;
		} else if (!matrix_size.toString().match(regex)) {
			setSizeError('Only numbers are allowed in the table size');
			setShowError(true);
			return;
		} else if (matrix_size > 5) {
			setSizeError('The table size should be less than 6 for helping to perform operations');
			setShowError(true);
			return;
		} else {
			setSizeError(null);
		}
		setShowError(false);
		const matrix_size_aux = parseInt(matrix_size);
		const x_values_ones = new Array(matrix_size_aux).fill(1);
		const y_values_ones = new Array(matrix_size_aux).fill(1);
		// const x_values_ones = [-1, 0, 3, 4];
		// const y_values_ones = [15.5, 3, 8, 1];
		// setMatrix(matrix_ones);
		setXValues(x_values_ones);
		setYValues(y_values_ones);
		// setMatrix();
		// setBVector(vector_ones);
		// setX0Vector(x0_ones);
		setShowMatrix(true);
	};

	const handleSubmit = async (event) => {
		event.preventDefault();

		let x_values_inputed = [...document.querySelectorAll('.x-values')];
		let y_values_inputed = [...document.querySelectorAll('.y-values')];

		let count = 0;
		for (let i = 0; i < x_values.length; i++) {
			// If the floating point number cannot be parsed, we set 0 for this value
			x_values_inputed[i] = x_values_inputed[i].value.replace(',', '.');
			console.log(x_values_inputed[i]);
			x_values[i] = !isNaN(parseFloat(x_values_inputed[i])) ? parseFloat(x_values_inputed[i]) : 0;
			count += 1;
		}
		for (let i = 0; i < y_values.length; i++) {
			// If the floating point number cannot be parsed, we set 0 for this value
			y_values_inputed[i] = y_values_inputed[i].value.replace(',', '.');
			console.log(y_values_inputed[i]);

			y_values[i] = !isNaN(parseFloat(y_values_inputed[i])) ? parseFloat(y_values_inputed[i]) : 0;
			count += 1;
		}

		// setX0(inputed_x0);
		setYValues(y_values_inputed);
		setXValues(x_values_inputed);
		console.log(x_values);
		console.log(y_values);
		const body = {
			x_values: x_values,
			y_values: y_values,
		};
		console.log(body);
		try {
			const result = await await axios.post(`https://euclid-api.herokuapp.com/newton_interpolation`, body);
			console.log(result.data);
			const { Coefficients, Polynomials } = result.data;
			setCoefficients(Coefficients);
			setPolynomials(Polynomials);
			setShowMatrixResult(true);
			setShowError(false);
			setError(null);
		} catch (error) {
			console.error(error);
			const { message } = error.response.data;
			setError(message);
			setShowError(true);
		}
	};

	const round = (value, decimals) => {
		return Number(Math.round(value + 'e' + decimals) + 'e-' + decimals);
	};

	const showResults = () => {
		if (error && showError) {
			return (
				<div className="d-inline-flex p-2 m-3 text-danger font-weight-bold">
					<p>{error}</p>
				</div>
			);
		} else if (show_matrix_result) {
			const coefficients_to_show = coefficients;
			const polynomials_to_show = polynomials;

			return (
				<React.Fragment>
					<div className="d-column-flex">
						<div className="d-column-flex p-2 m-3">
							<div>
								<p className="font-weight-bold">Polynomials</p>
							</div>
							<div>
								{polynomials_to_show.map((row, indexRow) => {
									return (
										<div className="d-flex-inline" key={indexRow}>
											<p
												key={indexRow}
												valueId={indexRow}
												className="font-weight-bold"
												readOnly
											>
												{row}
											</p>
										</div>
									);
								})}
							</div>
						</div>
						<div className="d-flex-column p-2 m-3">
							<p className="font-weight-bold">Coefficients:</p>
							<div className="d-inline-flex justify-content-between">
								{coefficients_to_show.map((value, key) => {
									let rounded = round(value, 4);
									return (
										<div className="m-2">
											<p className="font-weight-bold">{rounded}</p>
										</div>
									);
								})}
							</div>
						</div>
						</div>
				</React.Fragment>
			);
		}
		return null;
	};

	const showMatrixInput = () => {
		if (sizeError && showError) {
			return (
				<div className="d-flex">
					<p className="text-danger font-weight-bold">{sizeError}</p>
				</div>
			);
		} else if (show_matrix) {
			return (
				<div className="d-flex justify-content-center">
					<form onSubmit={handleSubmit}>
						<div className="d-column-flex">
							<div className="d-flex  mb-3 justify-content-center ">
								<div className="d-column-flex p-2">
									<div>
										<div className="d-inline-flex">
											<div>
												<p className="text-center font-weight-bold">X values</p>
											</div>
											{x_values.map((column, index) => {
												return (
													<MatrixInput
														defaultValue={x_values[index]}
														key={index}
														valueId={index}
														className="x-values"
													/>
												);
											})}
										</div>
									</div>
								</div>
							</div>
							<div className="d-flex  mb-3 justify-content-center ">
								<div className="d-column-flex p-2">
									<div>
										<div className="d-inline-flex">
											<div>
												<p className="text-center font-weight-bold">Y values</p>
											</div>
											{y_values.map((column, index) => {
												return (
													<MatrixInput
														defaultValue={y_values[index]}
														key={index}
														valueId={index}
														className="y-values"
													/>
												);
											})}
										</div>
									</div>
								</div>
							</div>

							<div className="d-flex justify-content-center">
								<button class="btn btn-primary">Calculate</button>
							</div>
						</div>
					</form>
				</div>
			);
		}
	};

	const HelpCard = () => {
		if (showHelp) {
			return (
				<div className="d-flex">
					<div className="card">
						<ul className="list-group list-group-flush">
							<li className="list-group-item">Data in table can't have repeated values.</li>
						</ul>
					</div>
				</div>
			);
		}
		return null;
	};

	return (
		<div className="m-5">
			<h2 className="text-center mt-2">Newton Interpolation</h2>
			<div className="d-flex justify-content-center">
				<div className="d-column-flex">
					<form onSubmit={setOnesMatrix}>
						<div className="d-flex justify-content-center">
							<input
								className="m-3"
								placeholder="Enter the table size"
								name="matrix_size"
								type="number"
								onChange={handleChangeSizeMatrix}
							></input>
							<div className="d-flex justify-content-center m-3">
								<div className="d-flex">
									<button class="btn btn-primary" type="submit">
										Generate Table
									</button>
								</div>
							</div>
						</div>
					</form>
					<div className="d-flex justify-content-center">
						<button class="btn btn-primary" onClick={showHelpCard}>
							Help
						</button>
						{HelpCard()}
					</div>
					{showMatrixInput()}
					{showResults()}
				</div>
			</div>
		</div>
	);
};

export default Newton_Interpolation;
