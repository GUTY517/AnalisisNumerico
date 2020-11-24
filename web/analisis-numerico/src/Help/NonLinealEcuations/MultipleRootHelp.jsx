import React, { useState, useEffect } from 'react';

const MultipleRootHelp = () => {
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
							<li className="list-group-item">The convergence decreases or stops if there is any division by zero.</li>
							<li className="list-group-item">Be sure the derivatives of the function are correct.</li>
							<li className="list-group-item">The function must be continuous and differentiable.</li>
							<li className="list-group-item">Tolerance must have a positive value.</li>
							<li className="list-group-item">The iteration number must be positive.</li>
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

export default MultipleRootHelp;
