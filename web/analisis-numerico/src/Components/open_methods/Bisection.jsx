import React, { useState, useEffect } from "react";
import Geogebra from "../assets/Geogebra";
import json_data from "../../json_data/bisection.json";
const Bisection = () => {
  const [data, setData] = useState([]);
  const calculate = (event) => {
    event.preventDefault();
    setData(json_data);
  };
  const showData = () => {
    if (data.length > 0) {
      let columns = data[0];
      let results = data.slice(1);

      console.log(results);
      return (
        <React.Fragment>
          <table class="table">
            <thead>
              <tr>
                {
                  columns.map(column => (
                  <th scope="col">{column}</th>
                  ))
                }
              </tr>
            </thead>
            <tbody>
              {
                results.map((result, index) => (
                  <tr id={index}>
                    <th>{result.Iteration}</th>
                <th>{result.a}</th>
                <th>{result.xm}</th>
                    <th>{result.b}</th>
                    <th>{result["f(xm)"]}</th>
                    <th>{result.Error}</th>
                  </tr>
                ))
              }
            </tbody>
          </table>
        </React.Fragment>
      );
    }
    return null;
  };

  return (
    <div>
      <h2 className="text-center mt-2">Bisection</h2>
      <div className="container mt-2">
        <div className="row">
          <div className="col-6 mt-3">
            <form className="m-auto" onSubmit={calculate}>
              <div className="form-group">
                <input
                  type="text"
                  className="form-control"
                  placeholder="Function"
                ></input>
              </div>
              <div className="form-group">
                <input
                  type="text"
                  className="form-control"
                  placeholder="Initial a"
                ></input>
                <small id="initialAHelp" class="form-text text-muted">
                  First element included in a range
                </small>
              </div>
              <div className="form-group">
                <input
                  type="text"
                  className="form-control"
                  placeholder="Initial b"
                ></input>
                <small id="initialAHelp" class="form-text text-muted">
                  Last element included in a range
                </small>
              </div>
              <div className="form-group">
                <input
                  type="text"
                  className="form-control"
                  placeholder="Tolerance"
                ></input>
              </div>
              <div className="form-group">
                <input
                  type="text"
                  className="form-control"
                  placeholder="Iterations"
                ></input>
              </div>
              <div className="form-group">
                <button type="submit" class="btn btn-primary">
                  Calculate
                </button>
              </div>
            </form>
          </div>
          <div>
            <Geogebra />
          </div>
        </div>
        <div className="row">
          <div className="col">
            <h3>Results</h3>
            {showData()}
          </div>
        </div>
      </div>
    </div>
  );
};

export default Bisection;
