import React from 'react';

const FixedPointHelp = () => {
	return (
		<div className="">
			<ul>
				<li>The functions must be continuous and differentiable.</li>
				<li>Be sure that the function have a root.</li>
				<li>The initial value is important for the method.</li>
				<li>Tolerance must have a positive value.</li>
				<li>The iteration number must be positive.</li>
				<li>You need to make sure that f(X) is continuous and g(X) is smooth and continuous on the interval.</li>
			</ul>
		</div>
	);
};

export default FixedPointHelp;
