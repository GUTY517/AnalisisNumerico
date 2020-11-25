import React, { useState, useEffect } from 'react';

const SpecialInputHelp = () => {
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
						<li className="list-group-item">exp(5) = e^5</li>
							<li className="list-group-item">sin(exp(3)*ln(x)) = sin(e^3*log(x))</li>
							<li className="list-group-item">ln(x) = log(x)</li>
							<li className="list-group-item">use ** instead of ^ eg: 2*x^2 = 2*x**2 </li>
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
				Input Help
			</button>
			{HelpCard()}
		</div>
	);
};


export default SpecialInputHelp;
