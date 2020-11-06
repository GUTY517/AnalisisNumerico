import React, { useState, useEffect } from "react";
import Geogebra from "../assets/Geogebra";
import axios from "axios";


const False_Rule = () => {
  const [data, setData] = useState([]);
  const [form_data, setFormData] = useState({
    func: "",
    initial_a: 0,
    initial_b: 0,
    tolerance: 1e-7,
    iterations: 100,
  });


  const handleInputChange = (e) => {

    setFormData({
      ...form_data,
      [e.target.name]: e.target.value,
    });
  };

  const handleSubtmit = async (e) => {
    e.preventDefault();


    const {func, initial_a, initial_b, tolerance, iterations} = form_data;
    const body = {
      function: func,
      initial_a: parseFloat(initial_a),
      initial_b: parseFloat(initial_b),
      tolerance: parseFloat(tolerance),
      iterations: parseFloat(iterations)
    }
    const result = await axios.post("http://127.0.0.1:5000/false_rule", body);
    setData(result.data);
    showData();
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
                {columns.map((column) => (
                  <th scope="col">{column}</th>
                ))}
              </tr>
            </thead>
            <tbody>
              {results.map((result, index) => (
                <tr id={index}>
                  <th>{result.Iteration}</th>
                  <th>{result.a}</th>
                  <th>{result.xm}</th>
                  <th>{result.b}</th>
                  <th>{result["f(xm)"]}</th>
                  <th>{result.Error}</th>
                </tr>
              ))}
            </tbody>
          </table>
        </React.Fragment>
      );
    }
    return null;
  };

  return (
    <div>
      <h2 className="text-center mt-2">False_Rule</h2>
      <div className="container mt-2">
        <div className="row">
          <div className="col-6 mt-3">
            <form className="m-auto" onSubmit={handleSubtmit}>
              <div className="form-group">
                <input
                  type="text"
                  className="form-control"
                  placeholder="f(x)="
                  name="func"
                  onChange={handleInputChange}
                ></input>
              </div>
              <div className="form-group">
                <input
                  type="text"
                  className="form-control"
                  placeholder="Initial a"
                  name="initial_a"
                  onChange={handleInputChange}
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
                  name="initial_b"
                  onChange={handleInputChange}
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
                  name="tolerance"
                  value={form_data.tolerance}
                  onChange={handleInputChange}
                ></input>
              </div>
              <div className="form-group">
                <input
                  type="text"
                  className="form-control"
                  placeholder="Iterations"
                  name="iterations"
                  value={form_data.iterations}
                  onChange={handleInputChange}
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

export default False_Rule;
  // "function": "ln(sin(x)^2 + 1) -1/2",
    // "g_function": "ln(sin(x)^2 + 1) -1/2",