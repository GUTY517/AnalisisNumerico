import React from 'react';
import SplineInput from './SplineInput';

const CuadraticSpline = () => {
  return ( 
    <SplineInput
      spline_method="Cuadratic Spline"
      endpoint="cuadratic_spline"
    />
   );
}
 
export default CuadraticSpline;