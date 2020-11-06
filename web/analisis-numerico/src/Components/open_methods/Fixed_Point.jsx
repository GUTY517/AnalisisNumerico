import React, { useState, useEffect } from "react";
import Geogebra from "../assets/Geogebra";
import axios from "axios";


const Fixed_Point = () => {
  const [data, setData] = useState([]);
  const [form_data, setFormData] = useState({
    funct: "",
    g_function: "",
    initial_ax: 0,
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


    const {funct, g_function, initial_ax,  tolerance, iterations} = form_data;
    const body = {
      function: funct,
      g_function: g_function,
      initial_ax: parseFloat(initial_ax),
      tolerance: parseFloat(tolerance),
      iterations: parseFloat(iterations)
    }
    console.log(body);
    const result = await axios.post("http://127.0.0.1:5000/fixed_point", body);
    console.log(result);
    setData(result.data);
    showData()
  };
  const showData = () => {
    if (data.length > 0) {
      let results = data;

      console.log(results);
      return (
        <React.Fragment>
          <table class="table">
            <thead>
              <tr>

                  <th scope="col">Iteration</th>
                  <th scope="col">xi</th>
                  <th scope="col">g(xi)</th>
                  <th scope="col">f(xi)</th>
                  <th scope="col">Error</th>
        
              </tr>
            </thead>
            <tbody>
              {results.map((result, index) => (
                <tr id={index}>
                  <th>{result.Iteration}</th>
                  <th>{result.xi}</th>
                  <th>{result["f(xi)"]}</th>
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
      <h2 className="text-center mt-2">Fixed Point</h2>
      <div className="container mt-2">
        <div className="row">
          <div className="col-6 mt-3">
            <form className="m-auto" onSubmit={handleSubtmit}>
              <div className="form-group">
                <input
                  type="text"
                  className="form-control"
                  placeholder="f(x)="
                  name="funct"
                  onChange={handleInputChange}
                ></input>
              </div>
              <div className="form-group">
                <input
                  type="text"
                  className="form-control"
                  placeholder="g(x)="
                  name="g_function"
                  onChange={handleInputChange}
                ></input>
              </div>
              <div className="form-group">
                <input
                  type="text"
                  className="form-control"
                  placeholder="Initial ax"
                  name="initial_ax"
                  onChange={handleInputChange}
                ></input>
                <small id="initialAHelp" class="form-text text-muted">
                  First aproximation
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

export default Fixed_Point;

