import React, { useState, useEffect } from "react";
import json_data from "../../json_data/total_pivoting.json";
const TotalPivoting = () => {
  const [data, setData] = useState([]);
  const calculate = (event) => {
    event.preventDefault();
    setData(json_data);
  };
  const showData = () => {
    if (data.length > 0) {
      let matrix = data;
      return (
        <React.Fragment>
          <table class="table">

            <tbody>
              {matrix.map((row,index) =>(
                <tr>
                  {row.map(column => (
                    <td>{column}</td>
                  ))}
                </tr>
              ))}
              <tr></tr>
            </tbody>
          </table>
        </React.Fragment>
      );
    }
    return null;
  };

  return (
    <div>
      <h2 className="text-center mt-2">Total Pivoting</h2>
      <div className="container mt-2">
        <div className="row">
          <div className="col-6 m-auto">
            <form className="mt-3" onSubmit={calculate}>
              <div className="form-group">
                <input
                  type="text"
                  className="form-control"
                  placeholder="Number of Rows"
                ></input>
              </div>
              <div className="form-group">
                <input
                  type="text"
                  className="form-control"
                  placeholder="Number of Columns"
                ></input>
              </div>
              <div className="form-group">
                <input
                  type="text"
                  className="form-control"
                  placeholder="Matrix A"
                ></input>
                <small id="matrixAHelp" class="form-text text-muted">
                  Matrix Format eg: [[2,3],[3,4]]
                </small>
              </div>
              <div className="form-group">
                <input
                  type="text"
                  className="form-control"
                  placeholder="Vector b"
                ></input>
                <small id="VectorBHelp" class="form-text text-muted">
                  Vector Format eg: [1,2,3]
                </small>
              </div>
              <div className="form-group">
                <button type="submit" class="btn btn-primary">
                  Calculate
                </button>
              </div>
            </form>
          </div>
          <div></div>
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

export default TotalPivoting;
