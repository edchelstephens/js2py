from selenium import webdriver

firefox_path = "/home/ed/.drivers/geckodriver"
browser = webdriver.Firefox(executable_path=firefox_path)
browser.get("http://localhost:8000")

assert "Js2Py" in browser.title