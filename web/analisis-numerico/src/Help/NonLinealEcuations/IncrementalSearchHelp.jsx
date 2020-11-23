import React from 'react';

const IncrementalSearchHelp = () => {
	return (
		<div className="">
			<ul>
				<li>You need to make sure that there is no discontinuity in the function with the numbers that are going to be tested</li>
				<li>The delta should not be too small because it can slow down the method.</li>
				<li>The initial value must exist in the function.</li>
				<li>The function must be continuous and differentiable.</li>
				<li>Tolerance must have a positive value.</li>
				<li>The iteration number must be positive.</li>
			</ul>
		</div>
	);
};

export default IncrementalSearchHelp;