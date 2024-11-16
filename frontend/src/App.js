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


// import React, { useState, createContext } from "react";
// import InputForm from './components/InputForm';
// import Questions from './components/Questions';

// export const DataContext = createContext();

// function App() {
//     const [questions, setQuestions] = useState([]);
//     const [options, setOptions] = useState([]);

//     return (
//         <DataContext.Provider value={{ questions, setQuestions, options, setOptions }}>
//             <div className="app">
//                 <h1>Website Visitor Classification</h1>
//                 <InputForm />
//                 <Questions />
//             </div>
//         </DataContext.Provider>
//     );
// }
// export default App;




// src/App.js
// import React, { useState } from 'react';
// import axios from 'axios';

// const App = () => {
//   const [url, setUrl] = useState('');
//   const [classificationData, setClassificationData] = useState([]);
//   const [loading, setLoading] = useState(false);
//   const [error, setError] = useState('');

//   // Handle URL input change
//   const handleInputChange = (e) => {
//     setUrl(e.target.value);
//   };

//   // Handle classify button click
//   const handleClassify = async () => {
//     if (!url) {
//       alert("Please enter a website URL.");
//       return;
//     }

//     setLoading(true);
//     setError('');

//     try {
//       // Make the API call to the backend for classification
//       const response = await axios.post('http://127.0.0.1:5000/classify', { url });

//       // Update the classification data
//       setClassificationData(response.data);
//     } catch (err) {
//       setError('Error fetching classification data');
//     } finally {
//       setLoading(false);
//     }
//   };

//   return (
//     <div>
//       <h1>Visitor Classification</h1>
//       <input
//         type="text"
//         value={url}
//         onChange={handleInputChange}
//         placeholder="Enter website URL"
//       />
//       <button onClick={handleClassify} disabled={loading}>
//         {loading ? 'Classifying...' : 'Classify'}
//       </button>

//       {error && <p>{error}</p>}

//       {classificationData.length > 0 && (
//         <ul>
//           {classificationData.map((item, index) => (
//             <li key={index}>{item.question}</li>
//           ))}
//         </ul>
//       )}
//     </div>
//   );
// };

// export default App;


// import React from "react";
// import InputForm from './components/InputForm';
// import Questions from './components/Questions';

// function App(){
//     return (
//         <div className="app">
//             <h1>Website Visitor Classification</h1>
//             <InputForm />
//             <Questions />
//         </div>
//     );
// }

// export default App;



// import React from 'react';

// const App = () => {
//   return (
//     <div>
//       <h1>Hello, React App!</h1>
//     </div>
//   );
// };

// export default App;
