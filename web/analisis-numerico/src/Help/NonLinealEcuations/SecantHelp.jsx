import React from 'react';

const SecantHelp = () => {
	return (
		<div className="">
			<ul>
				<li>You need to make sure that the function in continuous for the given interval.</li>
				<li>The method requires two initial values which should be chosen to lie close to the root, to be more fast.</li>
				<li>Be sure that the function have a root.</li>
				<li>The function must be continuous and differentiable.</li>
                <li>Tolerance must have a positive value.</li>
                <li>The iteration number must be positive.</li>
			</ul>
		</div>
	);
};

export default SecantHelp;