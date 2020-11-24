import React, { useState, useEffect } from 'react';
import json_data from '../../json_data/total_pivoting.json';
import MatrixInput from '../assets/MartrixInput';
import axios from 'axios';
import '../../App.css';
const SORInput = ({ matrix_method, endpoint }) => {
	const [matrix_size, setMatrixSize] = useState(3);
	const [matrix, setMatrix] = useState(new Array(matrix_size));
	const [b_vector, setBVector] = useState(new Array(matrix_size));
	const [x0_vector, setX0Vector] = useState([]);
	const [tolerance_to_send, setToleranceToSend] = useState(null);
	const [iterations_to_send, setIterationsToSend] = useState(null);
	const [a_title, setATitle] = useState(null);
	const [b_title, setBTitle] = useState(null);
	const [show_matrix, setShowMatrix] = useState(false);
	const [table, setTable] = useState([]);
	const [w, setW] = useState(null);
	const [show_matrix_result, setShowMatrixResult] = useState(false);
	const [error, setError] = useState(null);
	const [showError, setShowError] = useState(false);
	const [sizeError, setSizeError] = useState(null);
	const [answers, setAnswers] = useState([]);
	const [spectral_values, setSpectralValues] = useState([]);

	const handleChangeSizeMatrix = (event) => {
		let value = event.target.value;
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
		const vector_ones = new Array(matrix_size_aux).fill(1);
		const x0_ones = new Array(matrix_size_aux).fill(0);
		for (let i = 0; i < matrix_size_aux; i++) {
			matrix_ones[i] = Array(matrix_size_aux).fill(1);
		}
		setMatrix(matrix_ones);
		// setMatrix([
		// 	[4, -1, 0, 3],
		// 	[1, 15.5, 3, 8],
		// 	[0, -1.3, -4, 1.1],
		// 	[14, 5, -2, 30],
		// ]);
		setBVector(vector_ones);
		setX0Vector(x0_ones);
		setATitle('A');
		setBTitle('b');
		setShowMatrix(true);
	};

	const handleSubmit = async (event) => {
		event.preventDefault();
		const b_vector_selected = [...document.querySelectorAll('.b_vector')];
		const x0_vector_selected = [...document.querySelectorAll('.x0_vector')];
		const tolerance_inputed = document.querySelector('.tolerance-input').value;
		const iterations_inputed = document.querySelector('.iterations-input').value;
		let w_inputed = document.querySelector('.w-input').value;
    const notation = new RegExp('[-+]?[0-9]*.?[0-9]+([eE][-+]?[0-9]+)?');
    const decimals = /^[0-9]+([,.][0-9]+)?$/g;
		if (!tolerance_inputed.match(notation)) {
      setError('Enter a correct tolerance format');
			setShowError(true);
			return;
    } else if(!decimals.test(w_inputed)) {
      setError('Enter a correct decimal number or number');
			setShowError(true);
      return;
    } 
    else {
			setShowError(false);
			setError(null);
		}
		setToleranceToSend(tolerance_inputed);
		setIterationsToSend(iterations_inputed);
		setW(w_inputed);
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
		for (let i = 0; i < b_vector.length; i++) {
			// If the floating point number cannot be parsed, we set 0 for this value
			b_vector[i] = !isNaN(parseFloat(b_vector_selected[i].value)) ? parseFloat(b_vector_selected[i].value) : 1;
		}

		for (let i = 0; i < x0_vector.length; i++) {
			// If the floating point number cannot be parsed, we set 0 for this value
			x0_vector[i] = !isNaN(parseFloat(x0_vector_selected[i].value))
				? parseFloat(x0_vector_selected[i].value)
				: 1;
		}
		// setX0(inputed_x0);

		setMatrix(matrix);
		setBVector(b_vector);
		setX0Vector(x0_vector);
    w_inputed = w_inputed.replace(",",".");
		const body = {
			matrix: matrix,
			vector: b_vector,
			x_0: x0_vector,
			w_value: parseFloat(w_inputed),
			tolerance: parseFloat(tolerance_inputed),
			iterations: parseInt(iterations_inputed),
		};
		try {
			const result = await await axios.post(`http://127.0.0.1:5000/${endpoint}`, body);
			console.log(result.data);
			const { Table, Answers, SpectralValues } = result.data;

			// const matrix_result = result.filter(typeof Array);
			setTable(Table);
			setAnswers(Answers);
			setSpectralValues(SpectralValues);
			setShowMatrixResult(true);
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
			const table_to_show = table;
			const spectral_values_to_show = spectral_values;
			const headers = Object.keys(table_to_show[0]);
			const answers_to_show = answers;
			return (
				<React.Fragment>
					<table class="table mt-4">
						<thead>
							<tr>
								{headers.map((header, index) => {
									return <th scope="col">{header}</th>;
								})}
							</tr>
						</thead>
						<tbody>
							{table_to_show.map((row, indexRow) => (
								<tr key={indexRow}>
									{headers.map((header, indexColumn) => {
										return <th key={indexColumn}>{row[header]}</th>;
									})}
								</tr>
							))}
						</tbody>
					</table>

					<div className="d-flex-column">
            <p className="font-weight-bold">Answers:</p>
						<div className="d-inline-flex justify-content-between">
							{answers_to_show.map((value, key) => {
								return (
									<div className="m-2">
										<p className="font-weight-bold">{value}</p>
									</div>
								);
							})}
						</div>
            <p className="font-weight-bold">Spectral value:</p>
						<div className="d-inline-flex justify-content-between">
							{spectral_values_to_show.map((value, key) => {
								return (
									<div className="m-2">
										<p className="font-weight-bold">{value}</p>
									</div>
								);
							})}
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
							<div className="d-inline-flex  mb-3 justify-content-center ">
								<div className="d-column-flex p-2 bd-highlight  m-3">
									<div>
										<p className="text-center font-weight-bold">{a_title}</p>
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
										<p className="text-center font-weight-bold">{b_title}</p>
									</div>
									<div class="d-flex flex-column">
										{b_vector.map((row, indexRow) => {
											return (
												<MatrixInput
													defaultValue={b_vector[indexRow]}
													key={indexRow}
													valueId={indexRow}
													className="b_vector"
												/>
											);
										})}
									</div>
								</div>
								<div className="d-flex flex-column p-2 m-3">
									<div className="">
										<p className="text-center font-weight-bold">x0</p>
									</div>
									<div class="d-flex flex-column">
										{x0_vector.map((row, indexRow) => {
											return (
												<MatrixInput
													defaultValue={x0_vector[indexRow]}
													key={indexRow}
													valueId={indexRow}
													className="x0_vector"
												/>
											);
										})}
									</div>
								</div>
							</div>
							<div className="form-group">
								<input
									type="text"
									className="form-control tolerance-input"
									placeholder="Tolerance"
									name="tolerance"
								/>
							</div>
							<div className="form-group">
								<input type="text" className="form-control w-input" placeholder="w" name="w" />
							</div>
							<div className="form-group">
								<input
									type="number"
									className="form-control iterations-input"
									placeholder="Iterations"
									name="iterations"
								/>
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
					{showMatrixInput()}
					{showResults()}
				</div>
			</div>
		</div>
	);
};

export default SORInput;
