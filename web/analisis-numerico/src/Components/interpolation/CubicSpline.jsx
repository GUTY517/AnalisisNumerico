import React from 'react';
import SplineInput from './SplineInput';

const CubicSpline = () => {
  return ( 
    <SplineInput
      spline_method="Cubic Spline"
      endpoint="cubic_spline"
    />
   );
}
 
export default CubicSpline;