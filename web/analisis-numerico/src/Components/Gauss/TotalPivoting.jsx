import React, { useState, useEffect } from 'react';
import json_data from '../../json_data/total_pivoting.json';
import MatrixInput from '../assets/MartrixInput';
import '../../App.css';
const TotalPivoting = () => {
	const [matrix_size, setMatrixSize] = useState(3);
	const [matrix, setMatrix] = useState(new Array(matrix_size));
	const [b_vector, setBVector] = useState(new Array(matrix_size));
	const [a_title, setATitle] = useState(null);
	const [b_title, setBTitle] = useState(null);
	const [show_matrix, setShowMatrix] = useState(false);
	// let ones_matrix = new Array(matrix_size);
	// for (let i = 0; i < ones_matrix; i ++) {
	// 	ones_matrix[i] = new Array(matrix_size)
	// 	for (let j = 0; j < ones_matrix.length; j++) {
	// 		ones_matrix[i][j] = 1;
	// 	}
	// }
	// console.log(ones_matrix)
	useEffect(() => {
		// console.log(matrix_size);
		// setMatrix([]);
		// setBVector([[1], [1], [1]]);
	}, [matrix_size, matrix]);

	const handleChangeSizeMatrix = (event) => {
		let value = event.target.value;
		console.log(value);
		setMatrixSize(value);
	};

	const setOnesMatrix = (e) => {
		e.preventDefault();
		const matrix_size_aux = parseInt(matrix_size);
		const matrix_ones = new Array(matrix_size_aux);
		const vector_ones = new Array(matrix_size);

		for (let i = 0; i < matrix_size_aux; i++) {
			vector_ones[i] = Array(1).fill(1);
		}
		for (let i = 0; i < matrix_size_aux; i++) {
			matrix_ones[i] = Array(matrix_size_aux).fill(1);
		}
		setMatrix(matrix_ones);
		setBVector(vector_ones);
		setATitle('A');
		setBTitle('b');
		setShowMatrix(true);
	};

	const handleSubmit = (event) => {
		event.preventDefault();
		const b_vector_selected = [...document.querySelectorAll(".b_vector")]
		console.log(b_vector_selected[1].value)
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
		console.log(b_vector);
		console.log(matrix)
	};

	const hanldeMatrixInput = (event) => {

	};

	const showMatrix = () => {
		if (show_matrix) {
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
											<div className="d-flex-inline" key={indexRow} onChange={hanldeMatrixInput}
											>
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
															valueId = {indexColumn}
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
							<button>Calculate</button>
						</div>
					</div>
				</form>
			);
		}
	};

	return (
		<div className="m-5">
			<h2 className="text-center mt-2">Total Pivoting</h2>
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
									<button type="submit">Generate Matrix</button>
								</div>
							</div>
						</div>
					</form>
					{showMatrix()}
				</div>
			</div>
			{/* <div className="d-flex justify-content-center">
					<button clas>Calculate</button>
				</div>				 */}
		</div>
	);
};

export default TotalPivoting;
