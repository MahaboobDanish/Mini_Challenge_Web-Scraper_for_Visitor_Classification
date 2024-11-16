import React, { useContext, useState, useEffect } from 'react';
import { DataContext } from '../App';

function Questions() {
    const { questions, options } = useContext(DataContext);
    const [selectedOptions, setSelectedOptions] = useState({});
    const [submitted, setSubmitted] = useState(false);

    console.log("Questions state: ", questions); // Log questions state
    console.log("Options state: ", options); // Log options state

    // Reset selections and submission status whenever questions or options change
    useEffect(() => {
        setSelectedOptions({});
        setSubmitted(false);
    }, [questions, options]);

    // Check if questions exist and are in an array form
    if (!Array.isArray(questions) || questions.length === 0) {
        return <p>No questions available. Please enter a URL and click Classify.</p>;
    }

    // Handle option selection
    const handleOptionChange = (questionIndex, option) => {
        if (!submitted) {
            setSelectedOptions(prevState => {
                const selected = { ...prevState };
                if (!selected[questionIndex]) {
                    selected[questionIndex] = new Set();
                }
                if (selected[questionIndex].has(option)) {
                    selected[questionIndex].delete(option); // Deselect if already selected
                } else {
                    selected[questionIndex].add(option);
                }
                return selected;
            });
        }
    };

    // Handle form submission
    const handleSubmit = () => {
        setSubmitted(true);
    };

    return (
        <div className="questions">
            <h2>Generated Questions</h2>
            {questions.map((question, index) => (
                <div key={index} className="question-block">
                    <p><strong>{index + 1}. {question}</strong></p>
                    {Array.isArray(options) && options.length > 0 ? (
                        <ul style={{ listStyleType: 'none', paddingLeft: 0 }}>
                            {options.map((option, optIndex) => (
                                <li key={optIndex} style={{ display: 'flex', alignItems: 'center' }}>
                                    <input 
                                        type="checkbox" 
                                        id={`option-${index}-${optIndex}`} 
                                        name={`option-${index}`} 
                                        value={option} 
                                        onChange={() => handleOptionChange(index, option)}
                                        disabled={submitted} // Disable checkbox after submission
                                        style={{ marginRight: '8px' }}
                                    />
                                    <label htmlFor={`option-${index}-${optIndex}`}>{option}</label>
                                </li>
                            ))}
                        </ul>
                    ) : (
                        <p>No options available for this question.</p>
                    )}
                </div>
            ))}
            
            <button 
                onClick={handleSubmit} 
                style={{ marginTop: '20px', padding: '10px 20px', fontSize: '16px' }}
                disabled={submitted} // Disable submit button after submission
            >
                Submit
            </button>

            {submitted && (
                <div style={{ marginTop: '30px', padding: '10px', border: '1px solid #ccc', borderRadius: '5px' }}>
                    <h3>We are happy to help and assist with your choices selected:</h3>
                    {Object.entries(selectedOptions).map(([questionIndex, optionsSet]) => (
                        <div key={questionIndex}>
                            <p><strong>Question {parseInt(questionIndex) + 1}: {questions[questionIndex]}</strong></p>
                            <ul>
                                {[...optionsSet].map((option, i) => (
                                    <li key={i}>{option}</li>
                                ))}
                            </ul>
                        </div>
                    ))}
                </div>
            )}
        </div>
    );
}

export default Questions;


