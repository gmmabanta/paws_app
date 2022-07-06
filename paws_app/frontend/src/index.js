import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
// import Login from './components/login';
import RootView from './components/RootView';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <RootView />
  </React.StrictMode>
);
