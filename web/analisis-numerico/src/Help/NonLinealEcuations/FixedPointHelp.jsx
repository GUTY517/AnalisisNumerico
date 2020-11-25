import React, { useState, useEffect } from 'react';

const FixedPointHelp = () => {
	const [showHelp, setShowHelp] = useState(false);

	const showHelpCard = (e) => {
		if (showHelp) {
			setShowHelp(false);
		} else {
			setShowHelp(true);
		}
	};

	const HelpCard = () => {
		if (showHelp) {
			return (
				<div className="d-flex">
					<div className="card">
						<ul className="list-group list-group-flush">
							<li className="list-group-item">This method calculates the derivative automatically.</li>
							<li className="list-group-item">The functions must be continuous and differentiable.</li>
							<li className="list-group-item">Be sure that the function have a root.</li>
							<li className="list-group-item">The initial value is important for the method.</li>
							<li className="list-group-item">Tolerance must have a positive value.</li>
							<li className="list-group-item">x0 must be an aproximate root.</li>
							<li className="list-group-item">The iteration number must be positive.</li>
							<li className="list-group-item">g(x) = x - f(x)</li>
							<li className="list-group-item">You need to make sure that f(x) is continuous and g(x) is smooth and continuous on the interval.</li>
						</ul>
					</div>
				</div>
			);
		}
		return null;
	};

	return (
		<div className="d-flex justify-content-center">
			<button class="btn btn-primary" onClick={showHelpCard}>
				Help
			</button>
			{HelpCard()}
		</div>
	);
};

export default FixedPointHelp;
