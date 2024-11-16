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


// import React, { useState, useContext } from 'react';
// import axios from 'axios';
// import { DataContext } from '../App';

// function InputForm() {
//     const [url, setUrl] = useState('');
//     const { setQuestions, setOptions } = useContext(DataContext);

//     const handleUrlChange = (e) => {
//         setUrl(e.target.value);
//     };

//     const handleSubmit = async (e) => {
//         e.preventDefault();
//         try {
//             const response = await axios.post('http://127.0.0.1:5000/classify', { url });
//             console.log("API Response:", response.data);  // Log for debugging

//             const { questions, options } = response.data;
//             // Validate the structure before setting state
//             if (Array.isArray(questions) && Array.isArray(options)) {
//                 setQuestions(questions);
//                 setOptions(options);
//             } else {
//                 console.error("Invalid data structure:", response.data);
//                 setQuestions([]);
//                 setOptions([]);
//             }

//             // setQuestions(Array.isArray(questions) ? questions : []);
//             // setOptions(Array.isArray(options) ? options : []);

//         } catch (error) {
//             console.error("Error fetching classification:", error);
//             setQuestions([]);
//             setOptions([]);
//         }
//     };

//     return (
//         <form onSubmit={handleSubmit}>
//             <label>
//                 Website URL:
//                 <input type="text" value={url} onChange={handleUrlChange} />
//             </label>
//             <button type="submit">Classify</button>
//         </form>
//     );
// }

// export default InputForm;
