// // The main application component, which renders the InputForm and Questions components

import React, { useState, createContext } from 'react';
import InputForm from './components/InputForm';
import Questions from './components/Questions';

// Create DataContext to manage questions and options globally
export const DataContext = createContext();

function App() {
    const [questions, setQuestions] = useState([]);
    const [options, setOptions] = useState([]);

    return (
        <DataContext.Provider value={{ questions, setQuestions, options, setOptions }}>
            <div className="app">
                <h1>Website Visitor Classification</h1>
                <InputForm />
                <Questions />
            </div>
        </DataContext.Provider>
    );
}

export default App;

