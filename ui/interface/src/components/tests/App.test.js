import { shallow } from "enzyme";
import App from "../App";

describe("App", () => {
  it("renders without crashing", () => {
    let mountedApp = shallow(<App />);
  });
});
