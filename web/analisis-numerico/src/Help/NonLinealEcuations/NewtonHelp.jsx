import React from 'react';

const NewtonHelp = () => {
	return (
		<div className="">
			<ul>
				<li>You need to make sure that the function in continuous for the given interval.</li>
				<li>The derivative does not equal zero in any of the points of the interval being analyzed.</li>
				<li>If the derivative approaches zero, the method loses its speed because is possible to be a case of multiple root.</li>
				<li>Be sure that the function have a root.</li>
				<li>The initial value is very very important, 'cause this is an approximation to the root</li>
                <li>Tolerance must have a positive value.</li>
                <li>The iteration number must be positive.</li>
			</ul>
		</div>
	);
};

export default NewtonHelp;