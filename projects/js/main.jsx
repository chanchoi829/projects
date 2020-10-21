import React from 'react';
import ReactDOM from 'react-dom';
import Simulation from './simulation';
import Manager from './manager';


if (document.getElementById('reactEntry') === null) {
  ReactDOM.render(
    <Manager />,
    document.getElementById('reactEntryManager'),
  );
}
else {
  ReactDOM.render(
    <Simulation />,
    document.getElementById('reactEntry'),
  );
}

