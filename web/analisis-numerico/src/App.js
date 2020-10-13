import React from "react";
import Header from "./Components/Header";
import useScript from 'react-script-hook';

import { BrowserRouter as Router, Switch, Route, Link } from "react-router-dom";
import Bisection from "./Components/open_methods/Bisection";
import TotalPivoting from "./Components/Gauss/TotalPivoting"; 
function App() {
  return (
    <div className="App">
      <Router>
        <Header />

        <Switch>
          <Route path="/bisection">
            <Bisection/>

          </Route>
          <Route path="/total-pivoting">
            <TotalPivoting/>

          </Route>
        </Switch>
      </Router>
    </div>
  );
}

export default App;
