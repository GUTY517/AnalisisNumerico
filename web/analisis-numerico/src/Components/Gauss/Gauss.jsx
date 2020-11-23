import React from 'react';
import MatrixInput from '../assets/MartrixInput';
import MatrixMethod from "./MatrixMethod";
const Gauss = () => {
  return ( 
    <MatrixMethod
      endpoint="gauss"
      matrix_method="Gauss"
    />
   );
}
 
export default Gauss;