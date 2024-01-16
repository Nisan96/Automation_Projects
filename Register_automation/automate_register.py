import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from Name_Validation import name_validate
from phone_validation import phone_validate
from password_validation import password_validate
from email_validation import char1_validate,char2_validate,position_validate


# Screenshot File Path
screenshot_file_path = "D:\\Automation_testing\\Automation_Projects\\Register_automation\\Screenshots"

# Valid Test automation
def valid_RegisterTest():
    '''# Configure Logging settings
    logging.basicConfig(filename="Test_Log/RegisterTest_Valid.log", level=logging.INFO,
                        format='%(asctime)s - %(levelname)s: %(message)s')'''

    # Logging configuration
    LOGGING_LEVEL = logging.INFO
    LOGGING_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    LOGGING_FILENAME_invalid = os.path.join(os.getcwd(), 'Test_Log', 'RegisterTest_Valid.log')
    # Implement Logging interface
    logger = logging.getLogger(__name__)
    logger.setLevel(LOGGING_LEVEL)

    # Create a file handler and set the logging level
    file_handler = logging.FileHandler(LOGGING_FILENAME_invalid)
    file_handler.setLevel(LOGGING_LEVEL)

    # Create a formatter and add it to the file handler
    formatter = logging.Formatter(LOGGING_FORMAT)
    file_handler.setFormatter(formatter)

    # Add the file handler to the logger
    logger.addHandler(file_handler)

    # step 1: Launch browser
    logging.info("valid Register Test execution start...")
    control = webdriver.Edge()
    logging.info("Edge launch successfully")
    control.maximize_window()
    control.implicitly_wait(10)

    # step 2: Open URL
    control.get("https://tutorialsninja.com/demo/index.php?route=account/register")
    control.implicitly_wait(10)
    logging.info("Register page open Successful.")

    # step 3: Find location of First Name
    firstName_field = WebDriverWait(control,5).until(ec.visibility_of_element_located((By.ID,"input-firstname")))
    firstName_field_enable_state = firstName_field.is_enabled()
    print("firstName_field is enable:", firstName_field_enable_state)

    # step 4: verify First Name field is enabled or not and enter First Name
    if firstName_field_enable_state == True:
        firstName_field.clear()
        with open ('Testing_Text_files/valid_Register_test.txt', 'r') as f:
            content = f.readlines()
            f.close()
        firstName_field.send_keys(content[0])

        logging.info("Enter First Name Successfully.")
    else:
        logging.error("First name field isn't enable.....Test Fail")

    # step 5: Find location of Last Name
    lastName_field = WebDriverWait(control, 5).until(ec.visibility_of_element_located((By.ID, "input-lastname")))
    lastName_field_enable_state = lastName_field.is_enabled()
    print("lastName_field is enable:", lastName_field_enable_state)

    # step 6: verify Last Name field is enabled or not and enter Last Name
    if lastName_field_enable_state == True:
        lastName_field.clear()
        with open ('Testing_Text_files/valid_Register_test.txt', 'r') as f:
            content = f.readlines()
            f.close()
        lastName_field.send_keys(content[1])
        logging.info("Enter Last Name Successfully")
    else:
        logging.error("Last Name field isn't enable....Test fail")

    # step 7: Find location of E-Mail
    email_field = WebDriverWait(control, 5).until(ec.visibility_of_element_located((By.ID, "input-email")))
    email_field_enable_state = email_field.is_enabled()
    print("email_field is enable:", email_field_enable_state)

    # step 8: verify E-Mail field is enabled or not and enter E-Mail
    if email_field_enable_state == True:
        email_field.clear()
        with open ('Testing_Text_files/valid_Register_test.txt', 'r') as f:
            content = f.readlines()
            f.close()
        email_field.send_keys(content[2])
        logging.info("Enter E-mail Successfully")
    else:
        logging.error("email field isn't enable....Test fail")

    # step 9: Find location of Telephone
    telephone_field = WebDriverWait(control, 5).until(ec.visibility_of_element_located((By.ID, "input-telephone")))
    telephone_field_enable_state = telephone_field.is_enabled()
    print("telephone_field is enable:", telephone_field_enable_state)

    # step 10: verify Telephone field is enabled or not and enter Telephone
    if telephone_field_enable_state == True:
        telephone_field.clear()
        with open ('Testing_Text_files/valid_Register_test.txt', 'r') as f:
            content = f.readlines()
            f.close()
        telephone_field.send_keys(content[3])
        logging.info("Enter phone number Successfully")
    else:
        logging.error("telephone field isn't enable....Test fail")

    # step 11: Find location of Password
    password_field = WebDriverWait(control, 5).until(ec.visibility_of_element_located((By.ID, "input-password")))
    password_field_enable_state = password_field.is_enabled()
    print("password_field is enable:", password_field_enable_state)

    # step 12: verify Password field is enabled or not and enter Password
    if password_field_enable_state == True:
        password_field.clear()
        with open ('Testing_Text_files/valid_Register_test.txt', 'r') as f:
            content = f.readlines()
            f.close()
        password_field.send_keys(content[4])
        logging.info("Enter password Successfully")
    else:
        logging.error("password field isn't enable....Test fail")

    # step 13: Find location of Password Confirm
    confirm_password_field = WebDriverWait(control, 5).until(ec.visibility_of_element_located((By.ID, "input-confirm")))
    confirm_password_field_enable_state = confirm_password_field.is_enabled()
    print("confirm_password_field is enable:", confirm_password_field_enable_state)

    # step 14: verify Password Confirm field is enabled or not and enter Password Confirm
    if confirm_password_field_enable_state == True:
        confirm_password_field.clear()
        with open ('Testing_Text_files/valid_Register_test.txt', 'r') as f:
            content = f.readlines()
            f.close()
        confirm_password_field.send_keys(content[4])
        logging.info("Enter confirm password Successfully")
    else:
        logging.error("Password Confirm field isn't enable....Test fail")

    # Find location of newsletter subscribe button "Yes"
    subscribe_radio_button = WebDriverWait(control, 5).until(ec.visibility_of_element_located((By.NAME, "newsletter")))
    subscribe_radio_button_enable_state = subscribe_radio_button.is_enabled()
    print("subscribe_radio_button is enable:", subscribe_radio_button_enable_state)

    # step 16: verify Newsletter Subscribe Radio Button "Yes" is enabled or not and click on this
    if subscribe_radio_button_enable_state == True:
        #subscribe_radio_button.clear()
        subscribe_radio_button.click()
        logging.info("Subscribe Radio Button clicked Successfully")
        time.sleep(3)
    else:
        logging.error("Subscribe Radio Button isn't enable....Test fail")

    # step 17: Find location of agree policy checkbox
    agree_checkbox = WebDriverWait(control, 5).until(ec.visibility_of_element_located((By.NAME, "agree")))
    agree_checkbox_enable_state = agree_checkbox.is_enabled()
    print("agree police checkbox is enable:", agree_checkbox_enable_state)

    # step 18: verify agree policy checkbox is enabled or not and click on this
    if agree_checkbox_enable_state == True:
        #agree_checkbox.clear()
        agree_checkbox.click()
        logging.info("agree checkbox checked Successfully")
        time.sleep(3)
    else:
        logging.error("agree checkbox isn't enable....Test fail")

    # step 19: Find location of continue button
    continue_button = WebDriverWait(control, 5).until(ec.visibility_of_element_located((By.CLASS_NAME, "btn-primary")))
    continue_button_enable_state = continue_button.is_enabled()
    print("continue_button_enable_state is enable:", continue_button_enable_state)

    # step 20: verify continue button is enabled or not and click on this
    if continue_button_enable_state == True:
        continue_button.click()
        logging.info("continue button clicked successfully")
        #time.sleep(5)
    else:
        logging.error("continue button isn't enable...Test Fail")

    # step 21: verify continue button work or not by checking url
    expected_url = "https://tutorialsninja.com/demo/index.php?route=account/success"
    time.sleep(5)
    actual_url = control.current_url
    if expected_url == actual_url:
        logging.info("Test passed. Register successfully")
        control.get_screenshot_as_file(screenshot_file_path + "\\Register_ValidTest_passed.png")
    else:
        logging.info("Test failed. Can't Register")
        control.get_screenshot_as_file(screenshot_file_path + "\\Register_ValidTest_failed.png")

    logger.removeHandler(file_handler)
    control.quit()

# Invalid Name Test automation
def Invalid_Name_RegisterTest():
    '''# Configure Logging settings
    logging.basicConfig(filename="Test_Log/RegisterTest_Invalid_Name.log", level=logging.INFO,
                        format='%(asctime)s - %(levelname)s: %(message)s')'''

    # Logging configuration
    LOGGING_LEVEL = logging.INFO
    LOGGING_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    LOGGING_FILENAME_invalid = os.path.join(os.getcwd(), 'Test_Log', 'RegisterTest_invalid_Name.log')
    # Implement Logging interface
    logger = logging.getLogger(__name__)
    logger.setLevel(LOGGING_LEVEL)

    # Create a file handler and set the logging level
    file_handler = logging.FileHandler(LOGGING_FILENAME_invalid)
    file_handler.setLevel(LOGGING_LEVEL)

    # Create a formatter and add it to the file handler
    formatter = logging.Formatter(LOGGING_FORMAT)
    file_handler.setFormatter(formatter)

    # Add the file handler to the logger
    logger.addHandler(file_handler)

    # step 1: Launch browser
    logging.info("Invalid Name Register Test execution start...")
    control = webdriver.Edge()
    logging.info("Edge launch successfully")
    control.maximize_window()
    control.implicitly_wait(10)

    # step 2: Open URL
    control.get("https://tutorialsninja.com/demo/index.php?route=account/register")
    control.implicitly_wait(10)
    logging.info("Register page open Successful.")

    # step 3: Find location of First Name
    firstName_field = WebDriverWait(control, 5).until(ec.visibility_of_element_located((By.ID, "input-firstname")))
    firstName_field_enable_state = firstName_field.is_enabled()
    print("firstName_field is enable:", firstName_field_enable_state)

    # step 4: verify First Name field is enabled or not and enter First Name
    if firstName_field_enable_state == True:
        firstName_field.clear()
        with open('Testing_Text_files/Invalid_Name_Register_test.txt', 'r') as f:
            content = f.readlines()
            f.close()
        firstName_field.send_keys(content[0])
        logging.info("Enter First Name Successfully.")
        if len(content[0]) > 33:
            logging.error("First Name must be between 1 and 32 characters!")
        elif len(content[1]) <= 1:
            logging.error("First Name field is empty")
        else:
            firstName = name_validate(content[0])
            logging.info(firstName)
    else:
        logging.error("First name field isn't enable.....Test Fail")

    # step 5: Find location of Last Name
    lastName_field = WebDriverWait(control, 5).until(ec.visibility_of_element_located((By.ID, "input-lastname")))
    lastName_field_enable_state = lastName_field.is_enabled()
    print("lastName_field is enable:", lastName_field_enable_state)

    # step 6: verify Last Name field is enabled or not and enter Last Name
    if lastName_field_enable_state == True:
        lastName_field.clear()
        with open('Testing_Text_files/Invalid_Name_Register_test.txt', 'r') as f:
            content = f.readlines()
            f.close()
        lastName_field.send_keys(content[1])
        logging.info("Enter Last Name Successfully")
        if len(content[1]) > 32:
            logging.error("Last Name must be between 1 and 32 characters!")
        elif len(content[1]) < 1:
            logging.error("Last Name field is empty")
        else:
            lastName = name_validate(content[1])
            logging.info(lastName)
    else:
        logging.error("Last Name field isn't enable....Test fail")

    # step 7: Find location of E-Mail
    email_field = WebDriverWait(control, 5).until(ec.visibility_of_element_located((By.ID, "input-email")))
    email_field_enable_state = email_field.is_enabled()
    print("email_field is enable:", email_field_enable_state)

    # step 8: verify E-Mail field is enabled or not and enter E-Mail
    if email_field_enable_state == True:
        email_field.clear()
        with open('Testing_Text_files/valid_Register_test.txt', 'r') as f:
            content = f.readlines()
            f.close()
        email_field.send_keys(content[2])
        logging.info("Enter E-mail Successfully")
    else:
        logging.error("email field isn't enable....Test fail")

    # step 9: Find location of Telephone
    telephone_field = WebDriverWait(control, 5).until(ec.visibility_of_element_located((By.ID, "input-telephone")))
    telephone_field_enable_state = telephone_field.is_enabled()
    print("telephone_field is enable:", telephone_field_enable_state)

    # step 10: verify Telephone field is enabled or not and enter Telephone
    if telephone_field_enable_state == True:
        telephone_field.clear()
        with open('Testing_Text_files/valid_Register_test.txt', 'r') as f:
            content = f.readlines()
            f.close()
        telephone_field.send_keys(content[3])
        logging.info("Enter phone number Successfully")
    else:
        logging.error("telephone field isn't enable....Test fail")

    # step 11: Find location of Password
    password_field = WebDriverWait(control, 5).until(ec.visibility_of_element_located((By.ID, "input-password")))
    password_field_enable_state = password_field.is_enabled()
    print("password_field is enable:", password_field_enable_state)

    # step 12: verify Password field is enabled or not and enter Password
    if password_field_enable_state == True:
        password_field.clear()
        with open('Testing_Text_files/valid_Register_test.txt', 'r') as f:
            content = f.readlines()
            f.close()
        password_field.send_keys(content[4])
        logging.info("Enter password Successfully")
    else:
        logging.error("password field isn't enable....Test fail")

    # step 13: Find location of Password Confirm
    confirm_password_field = WebDriverWait(control, 5).until(ec.visibility_of_element_located((By.ID, "input-confirm")))
    confirm_password_field_enable_state = confirm_password_field.is_enabled()
    print("confirm_password_field is enable:", confirm_password_field_enable_state)

    # step 14: verify Password Confirm field is enabled or not and enter Password Confirm
    if confirm_password_field_enable_state == True:
        confirm_password_field.clear()
        with open('Testing_Text_files/valid_Register_test.txt', 'r') as f:
            content = f.readlines()
            f.close()
        confirm_password_field.send_keys(content[4])
        logging.info("Enter confirm password Successfully")
    else:
        logging.error("Password Confirm field isn't enable....Test fail")

    # Find location of newsletter subscribe button "Yes"
    subscribe_radio_button = WebDriverWait(control, 5).until(ec.visibility_of_element_located((By.NAME, "newsletter")))
    subscribe_radio_button_enable_state = subscribe_radio_button.is_enabled()
    print("subscribe_radio_button is enable:", subscribe_radio_button_enable_state)

    # step 16: verify Newsletter Subscribe Radio Button "Yes" is enabled or not and click on this
    if subscribe_radio_button_enable_state == True:
        # subscribe_radio_button.clear()
        subscribe_radio_button.click()
        logging.info("Subscribe Radio Button clicked Successfully")
        time.sleep(3)
    else:
        logging.error("Subscribe Radio Button isn't enable....Test fail")

    # step 17: Find location of agree policy checkbox
    agree_checkbox = WebDriverWait(control, 5).until(ec.visibility_of_element_located((By.NAME, "agree")))
    agree_checkbox_enable_state = agree_checkbox.is_enabled()
    print("agree police checkbox is enable:", agree_checkbox_enable_state)

    # step 18: verify agree policy checkbox is enabled or not and click on this
    if agree_checkbox_enable_state == True:
        # agree_checkbox.clear()
        agree_checkbox.click()
        logging.info("agree checkbox checked Successfully")
        time.sleep(3)
    else:
        logging.error("agree checkbox isn't enable....Test fail")

    # step 19: Find location of continue button
    continue_button = WebDriverWait(control, 5).until(ec.visibility_of_element_located((By.CLASS_NAME, "btn-primary")))
    continue_button_enable_state = continue_button.is_enabled()
    print("continue_button_enable_state is enable:", continue_button_enable_state)

    # step 20: verify continue button is enabled or not and click on this
    if continue_button_enable_state == True:
        continue_button.click()
        logging.info("continue button clicked successfully")
        time.sleep(5)
    else:
        logging.error("continue button isn't enable...Test Fail")

    # step 21: verify InvalidTest pass or fail by checking url
    expected_url = "https://tutorialsninja.com/demo/index.php?route=account/register"
    actual_url = control.current_url
    if expected_url == actual_url:
        logging.info("Test passed. can't Register")
        control.get_screenshot_as_file(screenshot_file_path + "\\Register_Invalid_Name_Test_passed.png")
    else:
        logging.info("Test failed. Account Created")
        control.get_screenshot_as_file(screenshot_file_path + "\\Register_Invalid_Name_Test_failed.png")

    logger.removeHandler(file_handler)
    control.quit()

# Invalid phone number test automation
def Invalid_Phone_RegisterTest():
    '''# Configure Logging settings
    logging.basicConfig(filename="Test_Log/RegisterTest_Invalid_Phone.log", level=logging.INFO,
                        format='%(asctime)s - %(levelname)s: %(message)s')'''

    # Logging configuration
    LOGGING_LEVEL = logging.INFO
    LOGGING_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    LOGGING_FILENAME_invalid = os.path.join(os.getcwd(), 'Test_Log', 'RegisterTest_invalid_Phone.log')
    # Implement Logging interface
    logger = logging.getLogger(__name__)
    logger.setLevel(LOGGING_LEVEL)

    # Create a file handler and set the logging level
    file_handler = logging.FileHandler(LOGGING_FILENAME_invalid)
    file_handler.setLevel(LOGGING_LEVEL)

    # Create a formatter and add it to the file handler
    formatter = logging.Formatter(LOGGING_FORMAT)
    file_handler.setFormatter(formatter)

    # Add the file handler to the logger
    logger.addHandler(file_handler)

    # step 1: Launch browser
    logging.info("Invalid Phone Register Test execution start...")
    control = webdriver.Edge()
    logging.info("Edge launch successfully")
    control.maximize_window()
    control.implicitly_wait(10)

    # step 2: Open URL
    control.get("https://tutorialsninja.com/demo/index.php?route=account/register")
    control.implicitly_wait(10)
    logging.info("Register page open Successful.")

    # step 3: Find location of First Name
    firstName_field = WebDriverWait(control, 5).until(ec.visibility_of_element_located((By.ID, "input-firstname")))
    firstName_field_enable_state = firstName_field.is_enabled()
    print("firstName_field is enable:", firstName_field_enable_state)

    # step 4: verify First Name field is enabled or not and enter First Name
    if firstName_field_enable_state == True:
        firstName_field.clear()
        with open('Testing_Text_files/valid_Register_test.txt', 'r') as f:
            content = f.readlines()
            f.close()
        firstName_field.send_keys(content[0])

        logging.info("Enter First Name Successfully.")
    else:
        logging.error("First name field isn't enable.....Test Fail")

    # step 5: Find location of Last Name
    lastName_field = WebDriverWait(control, 5).until(ec.visibility_of_element_located((By.ID, "input-lastname")))
    lastName_field_enable_state = lastName_field.is_enabled()
    print("lastName_field is enable:", lastName_field_enable_state)

    # step 6: verify Last Name field is enabled or not and enter Last Name
    if lastName_field_enable_state == True:
        lastName_field.clear()
        with open('Testing_Text_files/valid_Register_test.txt', 'r') as f:
            content = f.readlines()
            f.close()
        lastName_field.send_keys(content[1])
        logging.info("Enter Last Name Successfully")
    else:
        logging.error("Last Name field isn't enable....Test fail")

    # step 7: Find location of E-Mail
    email_field = WebDriverWait(control, 5).until(ec.visibility_of_element_located((By.ID, "input-email")))
    email_field_enable_state = email_field.is_enabled()
    print("email_field is enable:", email_field_enable_state)

    # step 8: verify E-Mail field is enabled or not and enter E-Mail
    if email_field_enable_state == True:
        email_field.clear()
        with open('Testing_Text_files/valid_Register_test.txt', 'r') as f:
            content = f.readlines()
            f.close()
        email_field.send_keys(content[2])
        logging.info("Enter E-mail Successfully")
    else:
        logging.error("email field isn't enable....Test fail")

    # step 9: Find location of Telephone
    telephone_field = WebDriverWait(control, 5).until(ec.visibility_of_element_located((By.ID, "input-telephone")))
    telephone_field_enable_state = telephone_field.is_enabled()
    print("telephone_field is enable:", telephone_field_enable_state)

    # step 10: verify Telephone field is enabled or not and enter Telephone
    if telephone_field_enable_state == True:
        telephone_field.clear()
        with open('Testing_Text_files/Invalid_phone_Register_test.txt', 'r') as f:
            content = f.readlines()
            f.close()
        telephone_field.send_keys(content[0])
        logging.info("Enter phone number Successfully")
        telephone = phone_validate(content[0])
        logging.info(telephone)

    else:
        logging.error("telephone field isn't enable....Test fail")

    # step 11: Find location of Password
    password_field = WebDriverWait(control, 5).until(ec.visibility_of_element_located((By.ID, "input-password")))
    password_field_enable_state = password_field.is_enabled()
    print("password_field is enable:", password_field_enable_state)

    # step 12: verify Password field is enabled or not and enter Password
    if password_field_enable_state == True:
        password_field.clear()
        with open('Testing_Text_files/valid_Register_test.txt', 'r') as f:
            content = f.readlines()
            f.close()
        password_field.send_keys(content[4])
        logging.info("Enter password Successfully")
    else:
        logging.error("password field isn't enable....Test fail")

    # step 13: Find location of Password Confirm
    confirm_password_field = WebDriverWait(control, 5).until(ec.visibility_of_element_located((By.ID, "input-confirm")))
    confirm_password_field_enable_state = confirm_password_field.is_enabled()
    print("confirm_password_field is enable:", confirm_password_field_enable_state)

    # step 14: verify Password Confirm field is enabled or not and enter Password Confirm
    if confirm_password_field_enable_state == True:
        confirm_password_field.clear()
        with open('Testing_Text_files/valid_Register_test.txt', 'r') as f:
            content = f.readlines()
            f.close()
        confirm_password_field.send_keys(content[4])
        logging.info("Enter confirm password Successfully")
    else:
        logging.error("Password Confirm field isn't enable....Test fail")

    # Find location of newsletter subscribe button "Yes"
    subscribe_radio_button = WebDriverWait(control, 5).until(ec.visibility_of_element_located((By.NAME, "newsletter")))
    subscribe_radio_button_enable_state = subscribe_radio_button.is_enabled()
    print("subscribe_radio_button is enable:", subscribe_radio_button_enable_state)

    # step 16: verify Newsletter Subscribe Radio Button "Yes" is enabled or not and click on this
    if subscribe_radio_button_enable_state == True:
        # subscribe_radio_button.clear()
        subscribe_radio_button.click()
        logging.info("Subscribe Radio Button clicked Successfully")
        time.sleep(3)
    else:
        logging.error("Subscribe Radio Button isn't enable....Test fail")

    # step 17: Find location of agree policy checkbox
    agree_checkbox = WebDriverWait(control, 5).until(ec.visibility_of_element_located((By.NAME, "agree")))
    agree_checkbox_enable_state = agree_checkbox.is_enabled()
    print("agree police checkbox is enable:", agree_checkbox_enable_state)

    # step 18: verify agree policy checkbox is enabled or not and click on this
    if agree_checkbox_enable_state == True:
        # agree_checkbox.clear()
        agree_checkbox.click()
        logging.info("agree checkbox checked Successfully")
        time.sleep(3)
    else:
        logging.error("agree checkbox isn't enable....Test fail")

    # step 19: Find location of continue button
    continue_button = WebDriverWait(control, 5).until(ec.visibility_of_element_located((By.CLASS_NAME, "btn-primary")))
    continue_button_enable_state = continue_button.is_enabled()
    print("continue_button_enable_state is enable:", continue_button_enable_state)

    # step 20: verify continue button is enabled or not and click on this
    if continue_button_enable_state == True:
        continue_button.click()
        logging.info("continue button clicked successfully")
        time.sleep(5)
    else:
        logging.error("continue button isn't enable...Test Fail")

    # step 21: verify InvalidTest pass or fail by checking url
    expected_url = "https://tutorialsninja.com/demo/index.php?route=account/register"
    actual_url = control.current_url
    if expected_url == actual_url:
        logging.info("Test passed. can't Register")
        control.get_screenshot_as_file(screenshot_file_path + "\\Register_Inalid_phone_Test_passed.png")
    else:
        logging.info("Test failed. Account Created!")
        control.get_screenshot_as_file(screenshot_file_path + "\\Register_Inalid_phone_Test_failed.png")

    logger.removeHandler(file_handler)
    control.quit()

# Invalid password test automation
def Invalid_Password_RegisterTest():
    '''# Configure Logging settings
    logging.basicConfig(filename="Test_Log/RegisterTest_Invalid_Password.log", level=logging.INFO,
                        format='%(asctime)s - %(levelname)s: %(message)s')'''

    # Logging configuration
    LOGGING_LEVEL = logging.INFO
    LOGGING_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    LOGGING_FILENAME_invalid = os.path.join(os.getcwd(), 'Test_Log', 'RegisterTest_invalid_Password.log')
    # Implement Logging interface
    logger = logging.getLogger(__name__)
    logger.setLevel(LOGGING_LEVEL)

    # Create a file handler and set the logging level
    file_handler = logging.FileHandler(LOGGING_FILENAME_invalid)
    file_handler.setLevel(LOGGING_LEVEL)

    # Create a formatter and add it to the file handler
    formatter = logging.Formatter(LOGGING_FORMAT)
    file_handler.setFormatter(formatter)

    # Add the file handler to the logger
    logger.addHandler(file_handler)

    # step 1: Launch browser
    logging.info("Invalid password Register Test execution start...")
    control = webdriver.Edge()
    logging.info("Edge launch successfully")
    control.maximize_window()
    control.implicitly_wait(10)

    # step 2: Open URL
    control.get("https://tutorialsninja.com/demo/index.php?route=account/register")
    control.implicitly_wait(10)
    logging.info("Register page open Successful.")

    # step 3: Find location of First Name
    firstName_field = WebDriverWait(control, 5).until(ec.visibility_of_element_located((By.ID, "input-firstname")))
    firstName_field_enable_state = firstName_field.is_enabled()
    print("firstName_field is enable:", firstName_field_enable_state)

    # step 4: verify First Name field is enabled or not and enter First Name
    if firstName_field_enable_state == True:
        firstName_field.clear()
        with open('Testing_Text_files/valid_Register_test.txt', 'r') as f:
            content = f.readlines()
            f.close()
        firstName_field.send_keys(content[0])

        logging.info("Enter First Name Successfully.")
    else:
        logging.error("First name field isn't enable.....Test Fail")

    # step 5: Find location of Last Name
    lastName_field = WebDriverWait(control, 5).until(ec.visibility_of_element_located((By.ID, "input-lastname")))
    lastName_field_enable_state = lastName_field.is_enabled()
    print("lastName_field is enable:", lastName_field_enable_state)

    # step 6: verify Last Name field is enabled or not and enter Last Name
    if lastName_field_enable_state == True:
        lastName_field.clear()
        with open('Testing_Text_files/valid_Register_test.txt', 'r') as f:
            content = f.readlines()
            f.close()
        lastName_field.send_keys(content[1])
        logging.info("Enter Last Name Successfully")
    else:
        logging.error("Last Name field isn't enable....Test fail")

    # step 7: Find location of E-Mail
    email_field = WebDriverWait(control, 5).until(ec.visibility_of_element_located((By.ID, "input-email")))
    email_field_enable_state = email_field.is_enabled()
    print("email_field is enable:", email_field_enable_state)

    # step 8: verify E-Mail field is enabled or not and enter E-Mail
    if email_field_enable_state == True:
        email_field.clear()
        with open('Testing_Text_files/valid_Register_test.txt', 'r') as f:
            content = f.readlines()
            f.close()
        email_field.send_keys(content[2])
        logging.info("Enter E-mail Successfully")
    else:
        logging.error("email field isn't enable....Test fail")

    # step 9: Find location of Telephone
    telephone_field = WebDriverWait(control, 5).until(ec.visibility_of_element_located((By.ID, "input-telephone")))
    telephone_field_enable_state = telephone_field.is_enabled()
    print("telephone_field is enable:", telephone_field_enable_state)

    # step 10: verify Telephone field is enabled or not and enter Telephone
    if telephone_field_enable_state == True:
        telephone_field.clear()
        with open('Testing_Text_files/valid_Register_test.txt', 'r') as f:
            content = f.readlines()
            f.close()
        telephone_field.send_keys(content[3])
        logging.info("Enter phone number Successfully")
    else:
        logging.error("telephone field isn't enable....Test fail")

    # step 11: Find location of Password
    password_field = WebDriverWait(control, 5).until(ec.visibility_of_element_located((By.ID, "input-password")))
    password_field_enable_state = password_field.is_enabled()
    print("password_field is enable:", password_field_enable_state)

    # step 12: verify Password field is enabled or not and enter Password
    if password_field_enable_state == True:
        password_field.clear()
        with open('Testing_Text_files/valid_Register_test.txt', 'r') as f:
            content = f.readlines()
            f.close()
        password_field.send_keys(content[4])
        logging.info("Enter password Successfully")
        password = password_validate(content[4])
        logging.info(password)
    else:
        logging.error("password field isn't enable....Test fail")

    # step 13: Find location of Password Confirm
    confirm_password_field = WebDriverWait(control, 5).until(ec.visibility_of_element_located((By.ID, "input-confirm")))
    confirm_password_field_enable_state = confirm_password_field.is_enabled()
    print("confirm_password_field is enable:", confirm_password_field_enable_state)

    # step 14: verify Password Confirm field is enabled or not and enter Password Confirm
    if confirm_password_field_enable_state == True:
        confirm_password_field.clear()
        with open('Testing_Text_files/Invalid_password_Register_test.txt', 'r') as f:
            content = f.readlines()
            f.close()
        confirm_password_field.send_keys(content[0])
        logging.info("Enter confirm password Successfully")
        with open('Testing_Text_files/valid_Register_test.txt', 'r') as f:
            content1 = f.readlines()
            f.close()
        if content[0] == content1[4]:
            logging.info("Password matches with confirm password")
        else:
            logging.error("Password confirmation does not match password")
    else:
        logging.error("Password Confirm field isn't enable....Test fail")

    # Find location of newsletter subscribe button "Yes"
    subscribe_radio_button = WebDriverWait(control, 5).until(ec.visibility_of_element_located((By.NAME, "newsletter")))
    subscribe_radio_button_enable_state = subscribe_radio_button.is_enabled()
    print("subscribe_radio_button is enable:", subscribe_radio_button_enable_state)

    # step 16: verify Newsletter Subscribe Radio Button "Yes" is enabled or not and click on this
    if subscribe_radio_button_enable_state == True:
        # subscribe_radio_button.clear()
        subscribe_radio_button.click()
        logging.info("Subscribe Radio Button clicked Successfully")
        time.sleep(3)
    else:
        logging.error("Subscribe Radio Button isn't enable....Test fail")

    # step 17: Find location of agree policy checkbox
    agree_checkbox = WebDriverWait(control, 5).until(ec.visibility_of_element_located((By.NAME, "agree")))
    agree_checkbox_enable_state = agree_checkbox.is_enabled()
    print("agree police checkbox is enable:", agree_checkbox_enable_state)

    # step 18: verify agree policy checkbox is enabled or not and click on this
    if agree_checkbox_enable_state == True:
        # agree_checkbox.clear()
        agree_checkbox.click()
        logging.info("agree checkbox checked Successfully")
        time.sleep(3)
    else:
        logging.error("agree checkbox isn't enable....Test fail")

    # step 19: Find location of continue button
    continue_button = WebDriverWait(control, 5).until(ec.visibility_of_element_located((By.CLASS_NAME, "btn-primary")))
    continue_button_enable_state = continue_button.is_enabled()
    print("continue_button_enable_state is enable:", continue_button_enable_state)

    # step 20: verify continue button is enabled or not and click on this
    if continue_button_enable_state == True:
        continue_button.click()
        logging.info("continue button clicked successfully")
        time.sleep(5)
    else:
        logging.error("continue button isn't enable...Test Fail")

    # step 21: verify InvalidTest pass or fail by checking url
    expected_url = "https://tutorialsninja.com/demo/index.php?route=account/register"
    actual_url = control.current_url
    if expected_url == actual_url:
        logging.info("Test passed. Can't Register")
        control.get_screenshot_as_file(screenshot_file_path + "\\Register_Invalid_password_Test_passed.png")
    else:
        logging.info("Test failed. Account Created!")
        control.get_screenshot_as_file(screenshot_file_path + "\\Register_Invalid_password_Test_failed.png")

    logger.removeHandler(file_handler)
    control.quit()

# Invalid email test automation
def Invalid_Email_RegisterTest():
    '''# Configure Logging settings
    logging.basicConfig(filename="Test_Log/RegisterTest_Invalid_Email.log", level=logging.INFO,
                        format='%(asctime)s - %(levelname)s: %(message)s')'''

    # Logging configuration
    LOGGING_LEVEL = logging.INFO
    LOGGING_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    LOGGING_FILENAME_invalid = os.path.join(os.getcwd(), 'Test_Log', 'RegisterTest_invalid_Email.log')
    # Implement Logging interface
    logger = logging.getLogger(__name__)
    logger.setLevel(LOGGING_LEVEL)

    # Create a file handler and set the logging level
    file_handler = logging.FileHandler(LOGGING_FILENAME_invalid)
    file_handler.setLevel(LOGGING_LEVEL)

    # Create a formatter and add it to the file handler
    formatter = logging.Formatter(LOGGING_FORMAT)
    file_handler.setFormatter(formatter)

    # Add the file handler to the logger
    logger.addHandler(file_handler)

    # step 1: Launch browser
    logging.info("Invalid Email Register Test execution start...")
    control = webdriver.Edge()
    logging.info("Edge launch successfully")
    control.maximize_window()
    control.implicitly_wait(10)

    # step 2: Open URL
    control.get("https://tutorialsninja.com/demo/index.php?route=account/register")
    control.implicitly_wait(10)
    logging.info("Register page open Successful.")

    # step 3: Find location of First Name
    firstName_field = WebDriverWait(control, 5).until(ec.visibility_of_element_located((By.ID, "input-firstname")))
    firstName_field_enable_state = firstName_field.is_enabled()
    print("firstName_field is enable:", firstName_field_enable_state)

    # step 4: verify First Name field is enabled or not and enter First Name
    if firstName_field_enable_state == True:
        firstName_field.clear()
        with open('Testing_Text_files/valid_Register_test.txt', 'r') as f:
            content = f.readlines()
            f.close()
        firstName_field.send_keys(content[0])

        logging.info("Enter First Name Successfully.")
    else:
        logging.error("First name field isn't enable.....Test Fail")

    # step 5: Find location of Last Name
    lastName_field = WebDriverWait(control, 5).until(ec.visibility_of_element_located((By.ID, "input-lastname")))
    lastName_field_enable_state = lastName_field.is_enabled()
    print("lastName_field is enable:", lastName_field_enable_state)

    # step 6: verify Last Name field is enabled or not and enter Last Name
    if lastName_field_enable_state == True:
        lastName_field.clear()
        with open('Testing_Text_files/valid_Register_test.txt', 'r') as f:
            content = f.readlines()
            f.close()
        lastName_field.send_keys(content[1])
        logging.info("Enter Last Name Successfully")
    else:
        logging.error("Last Name field isn't enable....Test fail")

    # step 7: Find location of E-Mail
    email_field = WebDriverWait(control, 5).until(ec.visibility_of_element_located((By.ID, "input-email")))
    email_field_enable_state = email_field.is_enabled()
    print("email_field is enable:", email_field_enable_state)

    # step 8: verify E-Mail field is enabled or not and enter E-Mail
    if email_field_enable_state == True:
        email_field.clear()
        with open('Testing_Text_files/Invalid_email_Register_test.txt', 'r') as f:
            content = f.readlines()
            f.close()
        email_field.send_keys(content[0])
        logging.info("Enter E-mail Successfully")

        special_symbol = [';',':','<','>','"','(',')','[',']',',']
        if len(content[0]) > 96:
            logging.error("E-Mail Address does not appear to be valid!")
        else:
            for w in content[0]:
                if w in special_symbol:
                    logging.error("E-mail shouldn't contain this symbol")
                    break
                else:
                    continue
            else:
                # validation of invalid email
                ar = char1_validate('@', content[0])
                dot = char2_validate('.', content[0])
                print("index of '@' :", ar)
                print("index of '.' :", dot)
                print(content[0])
                print(len(content[0]))

                if len(ar) > 1:
                    if ar[0] == 0:
                        logging.error("Please Enter a part followed by '@'. this email is Incomplete")
                    else:
                        logging.error("a part following '@' should not contain the symbol of '@'")
                elif len(ar) == 1:
                    if ar[0] == 0:
                        logging.error("Please Enter a part followed by '@'. this email is Incomplete")
                    elif ar[0] == len(content[0]) - 1:
                        logging.error("Please Enter a part following '@'. this email is Incomplete")
                    else:
                        if len(dot) == 1:
                            if dot[0] == 0:
                                logging.error("E-Mail Address does not appear to be valid!")
                            elif dot[0] == len(content[0]) - 1:
                                logging.error("'.' used at a wrong position")
                            else:
                                p = position_validate(content[0], ar, dot)
                                logging.info(p)
                        elif len(dot) == 0:
                            logging.error("this email missing an '.'")
                        else:
                            p = position_validate(content[0], ar, dot)
                            logging.info(p)
                else:
                    logging.error("this email missing an '@'")

    else:
        logging.error("email field isn't enable....Test fail")

    # step 9: Find location of Telephone
    telephone_field = WebDriverWait(control, 5).until(ec.visibility_of_element_located((By.ID, "input-telephone")))
    telephone_field_enable_state = telephone_field.is_enabled()
    print("telephone_field is enable:", telephone_field_enable_state)

    # step 10: verify Telephone field is enabled or not and enter Telephone
    if telephone_field_enable_state == True:
        telephone_field.clear()
        with open('Testing_Text_files/valid_Register_test.txt', 'r') as f:
            content = f.readlines()
            f.close()
        telephone_field.send_keys(content[3])
        logging.info("Enter phone number Successfully")
    else:
        logging.error("telephone field isn't enable....Test fail")

    # step 11: Find location of Password
    password_field = WebDriverWait(control, 5).until(ec.visibility_of_element_located((By.ID, "input-password")))
    password_field_enable_state = password_field.is_enabled()
    print("password_field is enable:", password_field_enable_state)

    # step 12: verify Password field is enabled or not and enter Password
    if password_field_enable_state == True:
        password_field.clear()
        with open('Testing_Text_files/valid_Register_test.txt', 'r') as f:
            content = f.readlines()
            f.close()
        password_field.send_keys(content[4])
        logging.info("Enter password Successfully")
    else:
        logging.error("password field isn't enable....Test fail")

    # step 13: Find location of Password Confirm
    confirm_password_field = WebDriverWait(control, 5).until(ec.visibility_of_element_located((By.ID, "input-confirm")))
    confirm_password_field_enable_state = confirm_password_field.is_enabled()
    print("confirm_password_field is enable:", confirm_password_field_enable_state)

    # step 14: verify Password Confirm field is enabled or not and enter Password Confirm
    if confirm_password_field_enable_state == True:
        confirm_password_field.clear()
        with open('Testing_Text_files/valid_Register_test.txt', 'r') as f:
            content = f.readlines()
            f.close()
        confirm_password_field.send_keys(content[4])
        logging.info("Enter confirm password Successfully")
    else:
        logging.error("Password Confirm field isn't enable....Test fail")

    # Find location of newsletter subscribe button "Yes"
    subscribe_radio_button = WebDriverWait(control, 5).until(ec.visibility_of_element_located((By.XPATH, "/html//div[@id='content']/form[@action='https://tutorialsninja.com/demo/index.php?route=account/register']//div[@class='form-group']/div[@class='col-sm-10']/label[1]/input[@name='newsletter']")))
    subscribe_radio_button_enable_state = subscribe_radio_button.is_enabled()
    print("subscribe_radio_button is enable:", subscribe_radio_button_enable_state)

    # step 16: verify Newsletter Subscribe Radio Button "Yes" is enabled or not and click on this
    if subscribe_radio_button_enable_state == True:
        # subscribe_radio_button.clear()
        subscribe_radio_button.click()
        logging.info("Subscribe Radio Button clicked Successfully")
        time.sleep(3)
    else:
        logging.error("Subscribe Radio Button isn't enable....Test fail")

    # step 17: Find location of agree policy checkbox
    agree_checkbox = WebDriverWait(control, 5).until(ec.visibility_of_element_located((By.NAME, "agree")))
    agree_checkbox_enable_state = agree_checkbox.is_enabled()
    print("agree police checkbox is enable:", agree_checkbox_enable_state)

    # step 18: verify agree policy checkbox is enabled or not and click on this
    if agree_checkbox_enable_state == True:
        # agree_checkbox.clear()
        agree_checkbox.click()
        logging.info("agree checkbox checked Successfully")
        time.sleep(3)
    else:
        logging.error("agree checkbox isn't enable....Test fail")

    # step 19: Find location of continue button
    continue_button = WebDriverWait(control, 5).until(ec.visibility_of_element_located((By.CLASS_NAME, "btn-primary")))
    continue_button_enable_state = continue_button.is_enabled()
    print("continue_button_enable_state is enable:", continue_button_enable_state)

    # step 20: verify continue button is enabled or not and click on this
    if continue_button_enable_state == True:
        continue_button.click()
        logging.info("continue button clicked successfully")
        time.sleep(5)
    else:
        logging.error("continue button isn't enable...Test Fail")

    # step 21: verify InvalidTest pass or fail by checking url
    expected_url = "https://tutorialsninja.com/demo/index.php?route=account/register"
    actual_url = control.current_url
    if expected_url == actual_url:
        logging.info("Test passed. Can't Register")
        control.get_screenshot_as_file(screenshot_file_path + "\\Register_Invalid_Email_Test_passed.png")
    else:
        logging.info("Test failed. Account Created!")
        control.get_screenshot_as_file(screenshot_file_path + "\\Register_Invalid_Email_Test_failed.png")

    logger.removeHandler(file_handler)
    control.quit()

# Invalid test (uncheck agree box)
def Invalid_checkbox_RegisterTest():
    '''# Configure Logging settings
    logging.basicConfig(filename="Test_Log/RegisterTest_Invalid_checkbox.log", level=logging.INFO,
                        format='%(asctime)s - %(levelname)s: %(message)s')'''

    # Logging configuration
    LOGGING_LEVEL = logging.INFO
    LOGGING_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    LOGGING_FILENAME_invalid = os.path.join(os.getcwd(), 'Test_Log', 'RegisterTest_invalid_checkbox.log')
    # Implement Logging interface
    logger = logging.getLogger(__name__)
    logger.setLevel(LOGGING_LEVEL)

    # Create a file handler and set the logging level
    file_handler = logging.FileHandler(LOGGING_FILENAME_invalid)
    file_handler.setLevel(LOGGING_LEVEL)

    # Create a formatter and add it to the file handler
    formatter = logging.Formatter(LOGGING_FORMAT)
    file_handler.setFormatter(formatter)

    # Add the file handler to the logger
    logger.addHandler(file_handler)

    # step 1: Launch browser
    logging.info("Invalid checkbox Register Test execution start...")
    control = webdriver.Edge()
    logging.info("Edge launch successfully")
    control.maximize_window()
    control.implicitly_wait(5)

    # step 2: Open URL
    control.get("https://tutorialsninja.com/demo/index.php?route=account/register")
    control.implicitly_wait(10)
    logging.info("Register page open Successful.")

    # step 3: Find location of First Name
    firstName_field = WebDriverWait(control, 5).until(ec.visibility_of_element_located((By.ID, "input-firstname")))
    firstName_field_enable_state = firstName_field.is_enabled()
    print("firstName_field is enable:", firstName_field_enable_state)

    # step 4: verify First Name field is enabled or not and enter First Name
    if firstName_field_enable_state == True:
        firstName_field.clear()
        with open('Testing_Text_files/valid_Register_test.txt', 'r') as f:
            content = f.readlines()
            f.close()
        firstName_field.send_keys(content[0])

        logging.info("Enter First Name Successfully.")
    else:
        logging.error("First name field isn't enable.....Test Fail")

    # step 5: Find location of Last Name
    lastName_field = WebDriverWait(control, 5).until(ec.visibility_of_element_located((By.ID, "input-lastname")))
    lastName_field_enable_state = lastName_field.is_enabled()
    print("lastName_field is enable:", lastName_field_enable_state)

    # step 6: verify Last Name field is enabled or not and enter Last Name
    if lastName_field_enable_state == True:
        lastName_field.clear()
        with open('Testing_Text_files/valid_Register_test.txt', 'r') as f:
            content = f.readlines()
            f.close()
        lastName_field.send_keys(content[1])
        logging.info("Enter Last Name Successfully")
    else:
        logging.error("Last Name field isn't enable....Test fail")

    # step 7: Find location of E-Mail
    email_field = WebDriverWait(control, 5).until(ec.visibility_of_element_located((By.ID, "input-email")))
    email_field_enable_state = email_field.is_enabled()
    print("email_field is enable:", email_field_enable_state)

    # step 8: verify E-Mail field is enabled or not and enter E-Mail
    if email_field_enable_state == True:
        email_field.clear()
        with open('Testing_Text_files/valid_Register_test.txt', 'r') as f:
            content = f.readlines()
            f.close()
        email_field.send_keys(content[2])
        logging.info("Enter E-mail Successfully")
    else:
        logging.error("email field isn't enable....Test fail")

    # step 9: Find location of Telephone
    telephone_field = WebDriverWait(control, 5).until(ec.visibility_of_element_located((By.ID, "input-telephone")))
    telephone_field_enable_state = telephone_field.is_enabled()
    print("telephone_field is enable:", telephone_field_enable_state)

    # step 10: verify Telephone field is enabled or not and enter Telephone
    if telephone_field_enable_state == True:
        telephone_field.clear()
        with open('Testing_Text_files/valid_Register_test.txt', 'r') as f:
            content = f.readlines()
            f.close()
        telephone_field.send_keys(content[3])
        logging.info("Enter phone number Successfully")
    else:
        logging.error("telephone field isn't enable....Test fail")

    # step 11: Find location of Password
    password_field = WebDriverWait(control, 5).until(ec.visibility_of_element_located((By.ID, "input-password")))
    password_field_enable_state = password_field.is_enabled()
    print("password_field is enable:", password_field_enable_state)

    # step 12: verify Password field is enabled or not and enter Password
    if password_field_enable_state == True:
        password_field.clear()
        with open('Testing_Text_files/valid_Register_test.txt', 'r') as f:
            content = f.readlines()
            f.close()
        password_field.send_keys(content[4])
        logging.info("Enter password Successfully")
    else:
        logging.error("password field isn't enable....Test fail")

    # step 13: Find location of Password Confirm
    confirm_password_field = WebDriverWait(control, 5).until(ec.visibility_of_element_located((By.ID, "input-confirm")))
    confirm_password_field_enable_state = confirm_password_field.is_enabled()
    print("confirm_password_field is enable:", confirm_password_field_enable_state)

    # step 14: verify Password Confirm field is enabled or not and enter Password Confirm
    if confirm_password_field_enable_state == True:
        confirm_password_field.clear()
        with open('Testing_Text_files/valid_Register_test.txt', 'r') as f:
            content = f.readlines()
            f.close()
        confirm_password_field.send_keys(content[4])
        logging.info("Enter confirm password Successfully")
    else:
        logging.error("Password Confirm field isn't enable....Test fail")

    # step 15: Find location of newsletter subscribe button "NO"
    subscribe_radio_button = WebDriverWait(control, 5).until(ec.visibility_of_element_located((By.XPATH, "/html//div[@id='content']/form[@action='https://tutorialsninja.com/demo/index.php?route=account/register']//div[@class='form-group']/div[@class='col-sm-10']/label[2]/input[@name='newsletter']")))
    subscribe_radio_button_enable_state = subscribe_radio_button.is_enabled()
    print("subscribe_radio_button is enable:", subscribe_radio_button_enable_state)

    # step 16: verify Newsletter Subscribe Radio Button "NO" is enabled or not and click on this
    if subscribe_radio_button_enable_state == True:
        # subscribe_radio_button.clear()
        subscribe_radio_button.click()
        logging.info("Subscribe Radio Button clicked Successfully")
        time.sleep(3)
    else:
        logging.error("Subscribe Radio Button isn't enable....Test fail")

    # step 17: Find location of agree policy checkbox
    agree_checkbox = WebDriverWait(control, 5).until(ec.visibility_of_element_located((By.NAME, "agree")))
    agree_checkbox_enable_state = agree_checkbox.is_enabled()
    print("agree police checkbox is enable:", agree_checkbox_enable_state)

    # step 18: verify agree policy checkbox is enabled or not and click on this
    if agree_checkbox_enable_state == True:
        # agree_checkbox.clear()
        #agree_checkbox.click()
        logging.error("agree checkbox Unchecked!")
        time.sleep(3)
    else:
        logging.error("agree checkbox isn't enable....Test fail")

    # step 19: Find location of continue button
    continue_button = WebDriverWait(control, 5).until(ec.visibility_of_element_located((By.CLASS_NAME, "btn-primary")))
    continue_button_enable_state = continue_button.is_enabled()
    print("continue_button_enable_state is enable:", continue_button_enable_state)

    # step 20: verify continue button is enabled or not and click on this
    if continue_button_enable_state == True:
        continue_button.click()
        logging.info("continue button clicked successfully")
        time.sleep(5)
    else:
        logging.error("continue button isn't enable...Test Fail")

    # step 21: verify InvalidTest Pass or Fail by checking error message
    expected_error_message = "Warning: You must agree to the Privacy Policy!"
    actual_error = control.find_element(By.CSS_SELECTOR,".alert-dismissible").text
    actual_error_message = actual_error
    print("actual error message:", actual_error)
    if expected_error_message == actual_error_message:
        logging.info("Test passed. Can't Register")
        control.get_screenshot_as_file(screenshot_file_path + "\\Register_Invalid_checkbox_Test_passed.png")
    else:
        logging.info("Test failed. Account Created!")
        control.get_screenshot_as_file(screenshot_file_path + "\\Register_Invalid_checkbox_Test_failed.png")

    logger.removeHandler(file_handler)
    control.quit()


# Main Function
if __name__=="__main__":
    #valid_RegisterTest()
    #Invalid_Name_RegisterTest()
    #Invalid_Phone_RegisterTest()
    #Invalid_Password_RegisterTest()
    #Invalid_Email_RegisterTest()
    Invalid_checkbox_RegisterTest()



