import React, { useState, useEffect } from 'react';

const IncrementalSearchHelp = () => {
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
						<li className="list-group-item">You need to make sure that there is no discontinuity in the function with the numbers that are going to be tested</li>
						<li className="list-group-item">The delta should not be too small because it can slow down the method.</li>
						<li className="list-group-item">The initial value must exist in the function.</li>
						<li className="list-group-item">The functionTolerance must have a positive value.</li>
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

export default IncrementalSearchHelp;