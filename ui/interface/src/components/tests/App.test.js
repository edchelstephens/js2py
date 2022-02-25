import { shallow } from "enzyme";
import App from "../App";

describe("App", () => {
  let mountedApp;
  beforeEach(() => {
    mountedApp = shallow(<App />);
  });
  it("renders without crashing", () => {});
  it("renders two textareas", () => {
    const textInputs = mountedApp.find("textarea");
    expect(textInputs.length).toBe(2);
  });

  it("renders one button with name 'Convert'", () => {
    const button = mountedApp.find("button");
    expect(button.length).toBe(1);
    expect(button.text()).toEqual("Convert");
  });
});
