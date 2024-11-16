// src/redux/store.js
import { configureStore } from '@reduxjs/toolkit';

// Define your initial state
const initialState = {
  classificationData: [],
};

// Define your reducer
const classificationReducer = (state = initialState, action) => {
  switch (action.type) {
    case 'SET_CLASSIFICATION_DATA':
      return { ...state, classificationData: action.payload };
    default:
      return state;
  }
};

// Create the Redux store using configureStore
const store = configureStore({
  reducer: {
    classification: classificationReducer,
  },
});

export default store;
