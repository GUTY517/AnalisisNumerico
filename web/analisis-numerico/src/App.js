import React from "react";
import Header from "./Components/Header";
import useScript from 'react-script-hook';

import { BrowserRouter as Router, Switch, Route, Link } from "react-router-dom";
import Bisection from "./Components/open_methods/Bisection";
import TotalPivoting from "./Components/Gauss/TotalPivoting"; 
import Newton from "./Components/open_methods/Newton";
import False_Rule from "./Components/open_methods/False_Rule";
import Fixed_Point from "./Components/open_methods/Fixed_Point";
function App() {
  return (
    <div className="App">
      <Router>
        <Header />

        <Switch>
          <Route path="/bisection">
            <Bisection/>

          </Route>
          <Route path="/newton">
            <Newton/>

          </Route>
          <Route path="/total-pivoting">
            <TotalPivoting/>

          </Route>
          <Route path="/false_rule">
            <False_Rule/>

          </Route>
          <Route path="/fixed_point">
            <Fixed_Point/>

          </Route>
        </Switch>
      </Router>
    </div>
  );
}

export default App;
