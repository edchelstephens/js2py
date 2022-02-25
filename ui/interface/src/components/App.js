import { useState } from "react";

import axios from "axios";

const App = () => {
  const [input, setInput] = useState("");
  const [output, setOutput] = useState("");

  const handleInputChange = (event) => {
    setInput(event.target.value);
  };

  const handleConvertClick = async (event) => {
    event.preventDefault();
    let data = {
      data: input,
    };
    let response = await axios.post("/conversions/js-to-python/", data);
    setOutput(response.data.prettified_conversion);
  };

  return (
    <div className="app">
      <textarea
        type="text"
        value={input}
        onChange={handleInputChange}
        rows="40"
        cols="100"
      ></textarea>
      <button onClick={handleConvertClick}>Convert</button>
      <textarea
        readOnly
        type="text"
        value={output}
        rows="40"
        cols="100"
      ></textarea>
    </div>
  );
};

export default App;
