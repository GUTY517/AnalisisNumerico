import React from 'react';
import LUMethod from './LUMethod';

const LUGauss = () => {
  return ( 
    <LUMethod
      matrix_method="Gauss LU"
      endpoint="lu_gauss"
    />
   );
}
 
export default LUGauss;