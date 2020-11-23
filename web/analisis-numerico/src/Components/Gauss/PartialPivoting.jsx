import React from 'react';
import MatrixInput from '../assets/MartrixInput';
import MatrixMethod from "./MatrixMethod";
const PartialPivoting = () => {
  return ( 
    <MatrixMethod
      endpoint="partial_pivoting"
      matrix_method="Partial Pivoting"
    />
   );
}
 
export default PartialPivoting;