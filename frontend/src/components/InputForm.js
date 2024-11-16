import React, { useState, useContext } from 'react';
import { DataContext } from '../App';

function InputForm() {
    const [url, setUrl] = useState("");
    const { setQuestions, setOptions } = useContext(DataContext);

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const response = await fetch('http://127.0.0.1:5000/classify', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ url }),
            });
            const data = await response.json();
            setQuestions([data.questions]); // Wrap in array if single string
            setOptions(data.options); // Directly set options array
        } catch (error) {
            console.error("Error fetching classification:", error);
        }
    };

    return (
        <form onSubmit={handleSubmit}>
            <input
                type="text"
                value={url}
                onChange={(e) => setUrl(e.target.value)}
                placeholder="Enter website URL"
            />
            <button type="submit">Classify</button>
        </form>
    );
}

export default InputForm;


