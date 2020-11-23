import React from 'react';

const SORHelp = () => {
	return (
		<div className="">
			<ul>
				<li>In sor if w = 1 we is like Gauss-Seidel method.</li>
				<li>
					In sor if 0 minus w minus 1 we got sub-relaxation methods (used in non-convergent Gauss-Seidel
					systems).
				</li>
				<li>
					In sor if 1 minus w minus 2 we got over-relaxation methods (used to "increase" the speed of some
					methods).
				</li>
				<li>In sor if w = 1 we is like Gauss-Seidel method.</li>
				<li>The initial vector isn´t too important.</li>
				<li>The determinant of the matrix cannot be 0.</li>
				<li>The matrix cannot have a 0 on the main diagonal</li>
				<li>The number of iterations mus be positive.</li>
				<li>The tolerance must be positive.</li>
			</ul>
		</div>
	);
};

export default SORHelp;
