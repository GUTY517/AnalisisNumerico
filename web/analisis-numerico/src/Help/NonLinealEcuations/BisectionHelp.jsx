import React, { useState, useEffect } from 'react';

const BisectionHelp = () => {
	const [showHelp, setShowHelp] = useState(false);

	const showHelpCard = (e) => {
		if (showHelp) {
			setShowHelp(false);
		} else {
			setShowHelp(true);
		}
		// HelpCard();
	};

	const HelpCard = () => {
		if (showHelp) {
			return (
				<div className="d-flex">
					<div className="card">
						<ul className="list-group list-group-flush">
							<li className="list-group-item">The function must be continuous and differentiable.</li>
							<li className="list-group-item">The value of A must be minor than b.</li>
							<li className="list-group-item">
								the specific function evaluated at the interval ends must have a different sign.
							</li>
							<li className="list-group-item">The value of A represents the lower limit.</li>
							<li className="list-group-item">The value of B represents the upper limit.</li>
							<li className="list-group-item">Tolerance must have a positive value.</li>
							<li className="list-group-item">Both values, a and b must exist in the function.</li>
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

export default BisectionHelp;
