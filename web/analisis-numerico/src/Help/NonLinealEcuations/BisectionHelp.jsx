import React from 'react';

const BisectionHelp = () => {
	return (
		<div className="">
			<ul>
				<li>The function must be continuous and differentiable.</li>
				<li>The value of A must be minor than b.</li>
				<li>the specific function evaluated at the interval ends must have a different sign.</li>
				<li>The value of A represents the lower limit.</li>
				<li>The value of B represents the upper limit.</li>
				<li>Tolerance must have a positive value.</li>
				<li>Both values, a and b must exist in the function.</li>
				<li>The iteration number must be positive.</li>
			</ul>
		</div>
	);
};

export default BisectionHelp;
