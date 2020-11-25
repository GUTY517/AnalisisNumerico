import React, { useState, useEffect } from 'react';
import json_data from '../../json_data/total_pivoting.json';
import MatrixInput from '../assets/MartrixInput';
import axios from 'axios';
import '../../App.css';
const MatrixMethod = ({ matrix_method, endpoint }) => {
	const [matrix_size, setMatrixSize] = useState(3);
	const [matrix, setMatrix] = useState(new Array(matrix_size));
	const [b_vector, setBVector] = useState(new Array(matrix_size));
	const [a_title, setATitle] = useState(null);
	const [b_title, setBTitle] = useState(null);
	const [show_matrix, setShowMatrix] = useState(false);
	const [matrix_to_show, setMatrixToShow] = useState([]);
	const [show_matrix_result, setShowMatrixResult] = useState(false);
	const [vector_to_show, setVectorToShow] = useState([]);
	const [error, setError] = useState(null);
	const [showError, setShowError] = useState(false);
	const [sizeError, setSizeError] = useState(null);
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
		console.log(value);
		setMatrixSize(value);
	};

	const setOnesMatrix = (e) => {
		e.preventDefault();
		const regex = new RegExp('[0-9]+');
		setError(null);
		if (matrix_size < 2 || matrix_size === null) {
			setSizeError('Error performing matrix size, the value must be greater than 1');
			setShowError(true);
			return;
		} else if (!matrix_size.toString().match(regex)) {
			setSizeError('Only numbers are allowed in the matrix size');
			setShowError(true);
			return;
		} else if (matrix_size > 5) {
			setSizeError('The matrix size should be less than 6 for helping to perform operations');
			setShowError(true);
			return;
		} else {
			setSizeError(null);
		}
		setShowError(false);
		const matrix_size_aux = parseInt(matrix_size);
		const matrix_ones = new Array(matrix_size_aux);
		const vector_ones = new Array(matrix_size);

		for (let i = 0; i < matrix_size_aux; i++) {
			vector_ones[i] = Array(1).fill(1);
		}
		for (let i = 0; i < matrix_size_aux; i++) {
			matrix_ones[i] = Array(matrix_size_aux).fill(1);
		}
		// setMatrix(matrix_ones);
		setMatrix(matrix_ones);
		setBVector(vector_ones);
		setATitle('A');
		setBTitle('b');
		setShowMatrix(true);
	};
	const round = (value, decimals) => {
		return Number(Math.round(value + 'e' + decimals) + 'e-' + decimals);
	};
	const handleSubmit = async (event) => {
		event.preventDefault();
		const b_vector_selected = [...document.querySelectorAll('.b_vector')];
		console.log(b_vector_selected[1].value);
		let count = 0;
		for (let i = 0; i < matrix.length; i++) {
			for (let j = 0; j < matrix[0].length; j++) {
				// If the floating point number cannot be parsed, we set 0 for this value
				matrix[i][j] = !isNaN(parseFloat(event.target[count].value))
					? parseFloat(event.target[count].value)
					: 0;
				count += 1;
			}
		}
		count = 0;
		for (let i = 0; i < b_vector.length; i++) {
			for (let j = 0; j < b_vector[0].length; j++) {
				// If the floating point number cannot be parsed, we set 0 for this value
				b_vector[i][j] = !isNaN(parseFloat(b_vector_selected[count].value))
					? parseFloat(b_vector_selected[count].value)
					: 1;
				count += 1;
			}
		}
		setMatrix(matrix);
		setBVector(b_vector);
		console.log(typeof matrix[1][1]);
		const body = {
			matrix: matrix,
			vector: b_vector,
		};
		try {
			const result = await await axios.post(`https://euclid-api.herokuapp.com/${endpoint}`, body);
			console.log(result);
			const {PivotedMatrix, ValuesX} = result.data;
			// const matrix_result = array.filter((element) => typeof element === 'object');
			// const x_values = array.filter((element) => typeof element === 'number');
			// const matrix_result = result.filter(typeof Array);
			console.log(ValuesX);
			console.log(PivotedMatrix);
			setShowError(false);
			setShowMatrixResult(true);
			setMatrixToShow(PivotedMatrix);
			setVectorToShow(ValuesX);
		} catch (error) {
			const { message } = error.response.data;
			console.log(message);
			setError(message);
			setShowError(true);
		}
	};

	const showResults = () => {
		if (error && showError) {
			return (
				<div className="d-inline-flex p-2 m-3 text-danger font-weight-bold">
					<p>{error}</p>
				</div>
			);
		} else if (show_matrix_result) {
			const matrix_data = matrix_to_show;
			const vector_data = vector_to_show;
			return (
				<React.Fragment>
					<div className="d-inline-flex p-2 m-3">
						<div className="d-column-flex">
							<div>
								<p className="text-center font-weight-bold">Pivoted Matrix</p>
							</div>
							<div>
								{matrix_data.map((row, indexRow) => {
									return (
										<div className="d-flex-inline" key={indexRow}>
											{row.map((column, indexColumn) => {
												return (
													<MatrixInput
														defaultValue={round(matrix_data[indexRow][indexColumn], 4)}
														key={indexColumn}
														valueId={indexColumn}
														readOnly
													/>
												);
											})}
										</div>
									);
								})}
							</div>
						</div>
						<div className="d-flex flex-column ml-4">
							<div className="">
								<p className="text-center font-weight-bold">X values</p>
							</div>
							<div class="d-flex flex-column">
								{vector_data.map((row, indexRow) => {
									return (
										<div className="d-flex" key={indexRow}>
											<MatrixInput
												defaultValue={round(vector_data[indexRow], 4)}
												key={indexRow}
												className="b_vector"
												readOnly
											/>
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
				<form onSubmit={handleSubmit}>
					<div className="d-column-flex">
						<div className="d-inline-flex  mb-3 justify-content-center ">
							<div className="d-column-flex p-2 bd-highlight  m-3">
								<div>
									<p className="text-center">{a_title}</p>
								</div>
								<div>
									{matrix.map((row, indexRow) => {
										return (
											<div className="d-flex-inline" key={indexRow}>
												{row.map((column, indexColumn) => {
													return (
														<MatrixInput
															defaultValue={matrix[indexRow][indexColumn]}
															key={indexColumn}
															valueId={indexColumn}
														/>
													);
												})}
											</div>
										);
									})}
								</div>
							</div>
							<div className="d-flex flex-column p-2 m-3">
								<div className="">
									<p className="text-center">{b_title}</p>
								</div>
								<div class="d-flex flex-column">
									{b_vector.map((row, indexRow) => {
										return (
											<div className="d-flex-inline" key={indexRow}>
												{row.map((column, indexColumn) => {
													return (
														<MatrixInput
															defaultValue={b_vector[indexRow][indexColumn]}
															key={indexColumn}
															valueId={indexColumn}
															className="b_vector"
														/>
													);
												})}
											</div>
										);
									})}
								</div>
							</div>
						</div>
						<div className="d-flex justify-content-center">
							<button class="btn btn-primary">Calculate</button>
						</div>
					</div>
				</form>
			);
		}
		return null;
	};

	const HelpCard = () => {
		if (showHelp) {
			return (
				<div className="d-flex">
					<div className="card">
						<ul className="list-group list-group-flush">
							<li className="list-group-item">The input the methods input help you set the dimension of the matrix.</li>
							<li className="list-group-item">The determinant of the matrix cannot be 0.</li>
							<li className="list-group-item">The matrix can't have a 0 on the diagonal.</li>
						</ul>
					</div>
				</div>
			);
		}
		return null;
	};

	return (
		<div className="m-5">
			<h2 className="text-center mt-2">{matrix_method}</h2>
			<div className="d-flex justify-content-center">
				<div className="d-column-flex">
					<form onSubmit={setOnesMatrix}>
						<div className="d-flex justify-content-center">
							<input
								className="m-3"
								placeholder="Enter the matrix's size"
								name="matrix_size"
								type="number"
								onChange={handleChangeSizeMatrix}
							></input>
							<div className="d-flex justify-content-center m-3">
								<div className="d-flex">
									<button class="btn btn-primary" type="submit">
										Generate Matrix
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

export default MatrixMethod;
