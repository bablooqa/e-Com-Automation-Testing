import softest
from selenium import webdriver
from selenium.webdriver.common.by import By

class AssertionsTest(softest.TestCase):
    pass

def test_lambdatest_radio_button_demo_value(self):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.lambdatest.com/selenium-playground/radiobutton-demo")
    driver.find_element(By.XPATH,'//h4[contains(text(),"Gender")]').click()
    driver.find_element(By.XPATH, "//div//div//div//div//div//div//div//div//label[normalize-space()='Male']//input[1]").click()
 
    driver.find_element(By.XPATH,
                        '//h4[contains(text(),"Age")]'
                        "//following::input[@value='5 - 15']").click()
    
    driver.find_element(By.XPATH,
        '//button[text()="Get values"]').click()
    
    gender = driver.find_element(By.CSS_SELECTOR, ".genderbutton").text
    # gender1="Female"
    # print(gender)
    # Gender = Male
        
    age_group = driver.find_element(By.CSS_SELECTOR, ".groupradiobutton")
    
    self.soft_assert(self.assertIs,
    "Male", gender, "Gender Is Not Correct" )
    self.soft_assert(self.assertTrue,
      driver.title.__contains__("Selenium Grid Online"))
    self.soft_assert(self.assertIn,
     "51", age_group, "Age Group Is Not Correct")
    
    self.assert_all()
   
    # assert gender is "Male", "Gender Is Not Correct"
    # assert driver.title.__contains__("Selenium Grid Online")
    # assert "51" in age_group, "Age Group Is Not Correct"
    
    
    
    
