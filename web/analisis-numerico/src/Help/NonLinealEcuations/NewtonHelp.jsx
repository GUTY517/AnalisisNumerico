import React, { useState, useEffect } from 'react';

const NewtonHelp = () => {
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
							<li className="list-group-item">You need to make sure that the function in continuous for the given interval.</li>
							<li className="list-group-item">The derivative does not equal zero in any of the points of the interval being analyzed.</li>
							<li className="list-group-item">If the derivative approaches zero, the method loses its speed because is possible to be a case of multiple root.</li>
							<li className="list-group-item">Be sure that the function have a root.</li>
							<li className="list-group-item">The initial value is very very important, because this is an approximation to the root.</li>
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
export default NewtonHelp;
