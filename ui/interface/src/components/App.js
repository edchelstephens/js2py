import { useState } from "react";

import axios from "axios";

const App = () => {
  const [input, setInput] = useState("");
  const [output, setOutput] = useState("");
  const [hasError, setHasError] = useState(false);

  const handleInputChange = (event) => {
    setInput(event.target.value);
  };

  const handleConvertClick = async (event) => {
    event.preventDefault();
    let data = {
      data: input,
    };
    try {
      let response = await axios.post("/conversions/js-to-python/", data);
      setOutput(response.data.prettified_conversion);
      setHasError(false);
    } catch (error) {
      setHasError(true);
      setOutput(error.response.data.error);
    }
  };

  return (
    <div className="app">
      <textarea
        type="text"
        style={{ color: "cadetblue" }}
        value={input}
        onChange={handleInputChange}
        rows="40"
        cols="100"
      ></textarea>
      <button onClick={handleConvertClick}>Convert</button>
      <textarea
        readOnly
        style={{ color: hasError ? "red" : "green" }}
        type="text"
        value={output}
        rows="40"
        cols="100"
      ></textarea>
    </div>
  );
};

export default App;
