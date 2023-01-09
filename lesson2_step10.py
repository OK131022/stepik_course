from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    
    link = "http://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
    import math
    def calc(x):
      return str(math.log(abs(12*math.sin(int(x)))))
    x_element = browser.find_element(By.CSS_SELECTOR, '[id="input_value"]')
    x = x_element.text
    print(x)
    y = calc(x)
    print(y)
    answ = browser.find_element(By.ID, "answer") 
    answ.send_keys(y)
    
    
    option1 = browser.find_element(By.CSS_SELECTOR, "[id='robotCheckbox']")
    option1.click()   
    browser.execute_script("window.scrollBy(0, 150);")
   # browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    option2 = browser.find_element(By.CSS_SELECTOR, "[id='robotsRule']")
    option2.click()
    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
  #  
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    time.sleep(2)

    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
	