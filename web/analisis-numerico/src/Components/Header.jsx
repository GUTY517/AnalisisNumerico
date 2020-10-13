import React from "react";
import { Link } from "react-router-dom";
const Header = () => {
  return (
    <div>
      <nav className="navbar navbar-expand-lg navbar-light bg-secondary">
        <Link className="navbar-brand" to="#">
          Numeric Methods
        </Link>
        <div className="collapse navbar-collapse" id="navbarNavDropdown">
          <ul className="navbar-nav">
            <li className="nav-item dropdown">
              <Link
                className="nav-link dropdown-toggle"
                
                id="navbarDropdownMenuLink"
                role="button"
                data-toggle="dropdown"
                aria-haspopup="true"
                aria-expanded="false"
              >
                One Variable Ecuations
              </Link>
              <div
                className="dropdown-menu"
                aria-labelledby="navbarDropdownMenuLink"
              >
                <Link className="dropdown-item" to="#">
                  Incremental Search
                </Link>
                <Link className="dropdown-item" to="/Bisection">
                  Bisection
                </Link>
                <Link className="dropdown-item" to="#">
                  Newton
                </Link>
                <Link className="dropdown-item" to="#">
                  Fixed Point
                </Link>
                <Link className="dropdown-item" to="#">
                  Multiple Roots
                </Link>
                <Link className="dropdown-item" to="#">
                  False Rule
                </Link>
                <Link className="dropdown-item" to="#">
                  Secant
                </Link>
              </div>
            </li>
            <li className="nav-item dropdown">
              <Link
                className="nav-link dropdown-toggle"
                to="#"
                id="navbarDropdownMenuLink"
                role="button"
                data-toggle="dropdown"
                aria-haspopup="true"
                aria-expanded="false"
              >
                Equations Systems
              </Link>
              <div
                className="dropdown-menu"
                aria-labelledby="navbarDropdownMenuLink"
              >
                <Link className="dropdown-item" to="#">
                  Parcial Pivoting
                </Link>
                <Link className="dropdown-item" to="total-pivoting">
                  Total Pivoting
                </Link>
                {/* <Link className="dropdown-item" to="#">
                  Something else here
                </Link> */}
              </div>
            </li>
          </ul>
        </div>
      </nav>
    </div>
  );
};

export default Header;
