import React, { useState, useEffect } from 'react';

const Geogebra = () => {
  const style = {}
  useEffect(() => {
  });
  return (
      <div className="col mt-3">
        <script src="https://www.geogebra.org/apps/deployggb.js"></script>
        
        <div id="ggb-element"></div> 
        {/* <div className="emdeb-responsive">
          <iframe
            src="https://www.geogebra.org/calculator/"
            // style="border:0px #ffffff none;"
            name=""
            scrolling="no"
            // style={{}}
            frameborder="1"
            height="500px"
            width="500px"
            // showMenuBar={false}
            // showToolBar={false}
            customToolBar={2}
            playButton={true}
            allowfullscreen
          ></iframe>
        </div> */}
      </div>
  );
};

export default Geogebra;
