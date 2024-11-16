// This manages the state of the questtions, optins and any errors

import {
    FETCH_CLASSIFICATION_RQUEST,
    FETCH_CLASSIFICATION_SUCSESS,
    FETCH_CLASSIFICATION_FAILURE,
}from './actions';

const initialState = {
    loading: false,
    questions: null,
    options: [],
    error: null,
};

function classificationReducer(state = initialState,action){
    switch(action.type){
        case FETCH_CLASSIFICATION_RQUEST:
            return { ...state, loading: true, error: null};
        case FETCH_CLASSIFICATION_SUCSESS:
            return{
                ...state,
                loading:false,
                questions: action.payload.questions,
                options: action.payload.options,
            };
        case FETCH_CLASSIFICATION_FAILURE:
            return {...state, loading:false, error: action.payload};
        default:
            return state;
    }
}

export default classificationReducer;