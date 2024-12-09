from selenium import webdriver

def test_lambdatest_playground():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.lambdatest.com/selenium-playground/")
    print("Title:",driver.title)
    
def test2_lambdatest_ecomerce():
    driver = webdriver.Chrome() #to create instance
    driver.maximize_window() #to maximise window
    driver.get("https://ecommerce-playground.lambdatest.io")
    print("Title", driver.title)
    
def testResxWebsite():
    driver = webdriver.Chrome() #to create instance
    driver.maximize_window() #to maximise window
    driver.get("https://rexjones2.com")
    print("Title", driver.title)
    
def google_test():
    driver = webdriver.Chrome() #to create instance
    driver.maximize_window() #to maximise window
    driver.get("https://google.com")
    print("Title", driver.title)