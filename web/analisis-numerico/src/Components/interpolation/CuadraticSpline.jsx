import React from 'react';
import SplineInput from './SplineInput';

const CuadraticSpline = () => {
  return ( 
    <SplineInput
      spline_method="Quadratic Spline"
      endpoint="cuadratic_spline"
    />
   );
}
 
export default CuadraticSpline;