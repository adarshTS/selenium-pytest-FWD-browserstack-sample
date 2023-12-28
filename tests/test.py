import json
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options as ChromeOptions

options= ChromeOptions()
options.set_capability('sessionName', 'BStack Sample Test')
driver= webdriver.Chrome(options=options)

try:
    driver.get('https://uat-www.fwd.com.sg')
    time.sleep(2)

    travel_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//span[text()='Travel']"))
    )
    time.sleep(2)

    driver.execute_script("arguments[0].click();", travel_element)
    time.sleep(2)

    driver.execute_script("window.scrollTo(0, 1100)") 
    time.sleep(10)

    price1_element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='Single']"))
    )

    driver.execute_script("arguments[0].click();", price1_element)
    time.sleep(5)

    price2_element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[text()='who']"))
    )

    driver.execute_script("arguments[0].click();", price2_element)
    time.sleep(2)

    myself_element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[text()='myself']"))
    )
    
    driver.execute_script("arguments[0].click();", myself_element)
    time.sleep(5)

    region_element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[text()='region']"))
    )
    
    driver.execute_script("arguments[0].click();", region_element)
    time.sleep(2)

    region_ASEAN = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[text()='ASEAN']"))
    )
    
    driver.execute_script("arguments[0].click();", region_ASEAN)
    time.sleep(2)

    travel_date_element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@name='travelEndDate']"))
    )
    
    driver.execute_script("arguments[0].click();", travel_date_element)
    time.sleep(5)

    day_element = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//div[@aria-label='Choose Thursday, December 28th, 2023']"))
    )
    driver.execute_script("arguments[0].click();", day_element)
    time.sleep(10)

    calculate_premium_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CLASS_NAME, "btn.premium_button_home"))
    )
    driver.execute_script("arguments[0].click();", calculate_premium_button)
    time.sleep(5)

    apply_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@class='btn btn-primary' and @id='planApply']"))
    )

    driver.execute_script("arguments[0].click();", apply_button)
    time.sleep(2)

    skip_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@class='btn rgtCovidBtnUnSel' and text()='Skip']"))
    )

    driver.execute_script("arguments[0].click();", skip_button)
    time.sleep(10)

    WebDriverWait(driver, 30).until(
    lambda x: x.execute_script("return document.readyState === 'complete'")
)

    confirm_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="nav-next-button"]'))
    )

    driver.execute_script("arguments[0].click();", confirm_button)
    time.sleep(5)

    skip_for_now_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="nav-next-alt-button"]'))
    )

    driver.execute_script("arguments[0].click();", skip_for_now_button)
    time.sleep(10)    

    complete_manually_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="manual_button"]/span'))
    )

    driver.execute_script("arguments[0].click();", complete_manually_button)
    time.sleep(5)

    name_element =  WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//input[@placeholder="as per your NRIC/FIN"]'))
    )
    driver.execute_script("arguments[0].click();", name_element)
    name_element.send_keys("Test")
    
    phone_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "(//input[@id='phone'])[2]"))
    )
    driver.execute_script("arguments[0].click();", phone_element)
    phone_element.send_keys("90100037")
    
    email_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "(//input[@id='email'])[2]"))
    )   
    driver.execute_script("arguments[0].click();", email_element)
    email_element.send_keys("test@fwd.com")
    
    select_gender = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="gender_div_1"]'))
    )
    driver.execute_script("arguments[0].click();", select_gender)
    
    dob = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@id='dob']"))
    )
    driver.execute_script("arguments[0].click();", dob)
    dob.send_keys("20091998")

    nric = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "(//input[@id='nric'])[2]"))
    )
    driver.execute_script("arguments[0].click();", nric)
    nric.send_keys("S5542707J")

    postalCode = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@id='postalCode']"))
    )
    driver.execute_script("arguments[0].click();", postalCode)
    postalCode.send_keys("550325")
    time.sleep(10)

    driver.execute_script("arguments[0].blur();", postalCode)
    time.sleep(5)
    
    personalDetailsTermsCheck = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@id='personalDetailsTermsCheck']"))
    )
    driver.execute_script("arguments[0].click();", personalDetailsTermsCheck)
    time.sleep(5)

    nextButton = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "(//button[text()='Next'])[1]"))
    )
    driver.execute_script("arguments[0].click();", nextButton)
    time.sleep(10)

    nextButton2 = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="nav-next-button"]'))
    )
    driver.execute_script("arguments[0].click();", nextButton2)
    time.sleep(5)

    confirmProceed = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "(//button[text()='Confirm & proceed'])[1]"))
    )
    driver.execute_script("arguments[0].click();", confirmProceed)
    time.sleep(5)


    checkmark_checkbox = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//span[@class='checkmark_checkbox']"))
    )
    driver.execute_script("arguments[0].click();", checkmark_checkbox)
    time.sleep(5)


    confirmProceed2 = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="nav-next-button"]'))
    )
    driver.execute_script("arguments[0].click();", confirmProceed2)
    time.sleep(5)

    paymentOption = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, "(//div[@class='payment-option-button'])[1]"))
    )
    driver.execute_script("arguments[0].click();", paymentOption)
    time.sleep(20)

    cardNumber = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="cardNumber"]'))
    )
    driver.execute_script("arguments[0].click();", cardNumber)
    time.sleep(10)
    cardNumber.send_keys("550325")
    time.sleep(20)




except NoSuchElementException as err:
    message = 'Exception: ' + str(err.__class__) + str(err.msg)
    driver.execute_script(
        'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": ' + json.dumps(message) + '}}')

except Exception as err:
    message = 'Exception: ' + str(err.__class__) + str(err.msg)
    driver.execute_script(
        'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": ' + json.dumps(message) + '}}')

finally:
    driver.quit();

