import React, { useState, useEffect } from 'react';
import json_data from '../../json_data/total_pivoting.json';
import MatrixInput from '../assets/MartrixInput';
import '../../App.css';
const TotalPivoting = () => {
	const [data, setData] = useState([]);
	const calculate = (event) => {
		event.preventDefault();
		setData(json_data);
	};
	const showData = () => {
		if (data.length > 0) {
			let matrix = data;
			return (
				<React.Fragment>
					<table class="table">
						<tbody>
							{matrix.map((row, index) => (
								<tr>
									{row.map((column) => (
										<td>{column}</td>
									))}
								</tr>
							))}
							<tr></tr>
						</tbody>
					</table>
				</React.Fragment>
			);
		}
		return null;
	};

	return (
		<div>
			<h2 className="text-center mt-2">Total Pivoting</h2>
			<div className="d-flex flex-column container justify-content-center">
				<input className="w-25 " placeholder="hola"></input>
				<div className="d-flex flex-inline  mb-3 justify-content-center ">
					<div class="d-flex flex-column  p-2 bd-highlight  m-3">
						<div className="d-flex flex-inline">
							<MatrixInput />
							<MatrixInput />
							<MatrixInput />
							<MatrixInput />
						</div>
						<div className="d-flex flex-inline">
							<MatrixInput />
							<MatrixInput />
							<MatrixInput />
							<MatrixInput />
						</div>
					</div>
					<div class="p-2 bd-highlight p-5 m-3">Flex item 2</div>
				</div>
			</div>
		</div>
	);
};

export default TotalPivoting;
