import axios from 'axios';
//import Questions from '../components/Questions';

export const FETCH_CLASSIFICATION_RQUEST = 'FETCH_CLASSIFICATION_RQUEST';
export const FETCH_CLASSIFICATION_SUCSESS = 'FETCH_CLASSIFICATION_SUCSESS';
export const FETCH_CLASSIFICATION_FAILURE = 'FETCH_CLASSIFICATION_FAILURE';

export const fetchClassification = (url) =>async (dispatch) => {
    dispatch({type: FETCH_CLASSIFICATION_RQUEST});

    try{
        const response = await axios.post('http://127.0.0.1:5000/classify', { url });
        dispatch({
            type: FETCH_CLASSIFICATION_SUCSESS,
            payload: {
                questions: response.data.questions,
                options: response.data.options,
            },
        });
    } catch(error){
        dispatch({
            type: FETCH_CLASSIFICATION_FAILURE,
            payload: error.message || 'Something went wrong',
        });
    }
};