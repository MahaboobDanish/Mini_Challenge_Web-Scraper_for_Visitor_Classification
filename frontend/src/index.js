import React from 'react';
import ReactDOM from 'react-dom/client'; // Updated import
import { Provider } from 'react-redux';
import App from './App';
import store from './redux/store';
import './styles.css';

// Create the root element using ReactDOM.createRoot()
const root = ReactDOM.createRoot(document.getElementById('root'));

// Render the App component inside the root element
root.render(
  <Provider store={store}>
    <App />
  </Provider>
);
