import React from 'react';

const GaussSeidelHelp = () => {
	return (
		<div className="">
			<ul>
				<li>The initial vector isn´t too important.</li>
				<li>The determinant of the matrix cannot be 0.</li>
				<li>The matrix cannot have a 0 on the main diagonal</li>
				<li>The number of iterations mus be positive.</li>
				<li>The tolerance must be positive.</li>
			</ul>
		</div>
	);
};

export default GaussSeidelHelp;
