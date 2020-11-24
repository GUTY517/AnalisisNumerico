import React, { useState, useEffect } from 'react';

const DirectMethodInput = () => {
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
						<li className="list-group-item">The input in the methods help you to be sure in the dimension of the matrix.</li>
						<li className="list-group-item">The determinant of the matrix cannot be 0.</li>
						<li className="list-group-item">The matrix can´t have a 0 on the diagonal.</li>
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

export default DirectMethodInput;
