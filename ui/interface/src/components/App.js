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
      <input type="text" value={input} onChange={handleInputChange}></input>
      <button onClick={handleConvertClick}>Convert</button>
      <input type="text" value={output}></input>
    </div>
  );
};

export default App;
