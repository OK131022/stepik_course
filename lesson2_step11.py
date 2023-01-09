from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try: 
    link = "http://suninjuly.github.io/file_input.html"

    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    labels = browser.find_elements(By.TAG_NAME,"label") # Список лэйблов над текстовыми полями
    inputs = browser.find_elements(By.TAG_NAME,"input") # Список текстовых полей

    for i, label in enumerate(labels):          # Если последний символ
        if label.text == 'Email *':               # лейбла над текстовым полем равен "*",
            inputs[i].send_keys('Email@ya.ru')   # то в поле ввода печатаем "Обязалово!"
        elif label.text == 'First name*':               # лейбла над текстовым полем равен "*",
            inputs[i].send_keys('Иван')
        elif label.text == 'Last name*':               # лейбла над текстовым полем равен "*",
            inputs[i].send_keys('Олегович')
  #      else:     inputs[i].send_keys('необязательно')
    
  
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    print(os.path.abspath(os.path.dirname(__file__))) 
    file_path = os.path.join(current_dir, 'file_example.txt')           # добавляем к этому пути имя файла 
    print(file_path)
    element = browser.find_element(By.CSS_SELECTOR, "[type='file']")
 #   browser.find_element_by_css_selector("#file").send_keys(file_path)

    element.send_keys(file_path)
    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
	
	