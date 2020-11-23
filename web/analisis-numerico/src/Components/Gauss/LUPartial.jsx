import React from 'react';
import LUMethod from './LUMethod';

const LUPartial = () => {
  return ( 
    <LUMethod
      matrix_method="Partial LU"
      endpoint="lu_pivoting"
    />
   );
}
 
export default LUPartial;