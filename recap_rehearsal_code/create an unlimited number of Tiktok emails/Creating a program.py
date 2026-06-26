#Create a program for which I enter a valid number and it creates personal accounts for me with the same number as the valid number that I entered for it on Facebook, TikTok or Instagram.

# $ pip install selenium
# $ pip install webdriver-manager


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

# Open Instagram registration page
driver.get("https://www.instagram.com/accounts/emailsignup/")

# Wait for the page to load
time.sleep(30)

# Find the registration form fields
name_input = driver.find_element_by_name("Mobile Number or Email")
email_input = driver.find_element_by_name("Full Name")
username_input = driver.find_element_by_name("Username")
password_input = driver.find_element_by_name("password")

# Fill out the form (replace placeholders with actual data)
name_input.send_keys("Your Name335436")
email_input.send_keys("")
username_input.send_keys("YourUs355fg53dffername")
password_input.send_keys("YourPassword1csddf3545423")

# Submit the registration form
driver.find_element_by_css_selector("button[type='submit']").click()

# Wait for the registration process to complete
time.sleep(20)

# Now let's try logging in with the created account
driver.get("https://www.instagram.com/accounts/login/")

# Wait for the login page to load
time.sleep(30)

# Find the login form fields
username_login = driver.find_element_by_name("username")
password_login = driver.find_element_by_name("password")

# Fill out the login form (replace placeholders with actual data)
username_login.send_keys("YourUsername")
password_login.send_keys("YourPassword123")

# Submit the login form
password_login.send_keys(Keys.ENTER)

# Wait for the login process to complete
time.sleep(10)

# Close the webdriver
driver.quit()


















# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# import time

# driver = webdriver.Chrome()

# # Open Facebook registration page
# driver.get("https://www.facebook.com/r.php")

# # Wait for the page to load
# time.sleep(5)

# # Find the registration form fields
# first_name_input = driver.find_element_by_name("firstname")
# last_name_input = driver.find_element_by_name("lastname")
# mobile_or_email_input = driver.find_element_by_name("reg_email__")
# password_input = driver.find_element_by_name("reg_passwd__")
# birthday_day_input = driver.find_element_by_name("birthday_day")
# birthday_month_input = driver.find_element_by_name("birthday_month")
# birthday_year_input = driver.find_element_by_name("birthday_year")
# gender_radio = driver.find_element_by_xpath("//input[@type='radio' and @value='2']")  # Assuming 2 is for female, change if needed

# # Fill out the form (replace placeholders with actual data)
# first_name_input.send_keys("Name223")
# last_name_input.send_keys("Last22")
# mobile_or_email_input.send_keys("")
# password_input.send_keys("YourPassword123")
# birthday_day_input.send_keys("01")
# birthday_month_input.send_keys("Jan")
# birthday_year_input.send_keys("2000")

# # Select gender (in this case, Female)
# gender_radio.click()

# # Submit the registration form
# driver.find_element_by_name("websubmit").click()

# # Wait for the registration process to complete
# time.sleep(5)

# # Close the webdriver
# driver.quit()























# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# import time

# driver = webdriver.Firefox()

# # Open Facebook registration page
# driver.get("https://www.facebook.com/r.php")

# # Wait for the page to load
# time.sleep(3)

# # Find the registration form fields
# first_name_input = driver.find_element_by_name("firstname")
# last_name_input = driver.find_element_by_name("lastname")
# mobile_or_email_input = driver.find_element_by_name("reg_email__")
# password_input = driver.find_element_by_name("reg_passwd__")
# birthday_day_input = driver.find_element_by_name("birthday_day")
# birthday_month_input = driver.find_element_by_name("birthday_month")
# birthday_year_input = driver.find_element_by_name("birthday_year")
# gender_radio = driver.find_element_by_xpath("//input[@type='radio' and @value='2']")  # Assuming 2 is for female, change if needed

# # Fill out the form
# first_name_input.send_keys("Your First Name")
# last_name_input.send_keys("Your Last Name")
# mobile_or_email_input.send_keys("your_email@example.com")
# password_input.send_keys("YourPassword123")
# birthday_day_input.send_keys("01")
# birthday_month_input.send_keys("Jan")
# birthday_year_input.send_keys("2000")

# # Select gender (in this case, Female)
# gender_radio.click()

# # Submit the registration form
# driver.find_element_by_name("websubmit").click()

# # Wait for the registration process to complete
# time.sleep(5)

# # Close the webdriver
# driver.quit()



#///////
# import csv

# # Define the path to your CSV file
# csv_file = "path_to_your_csv_file.csv"

# # Read data from CSV file
# with open(csv_file, mode='r') as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         first_name = row['First Name']
#         last_name = row['Last Name']
#         email = row['Email']
#         password = row['Password']
#         birthday_day = row['Birthday Day']
#         birthday_month = row['Birthday Month']
#         birthday_year = row['Birthday Year']
#         gender = row['Gender']

#         # Now you can use this data to manually create a Facebook account
#         print(f"Creating Facebook account for {first_name} {last_name} ({email}) with password {password}, "
#               f"birthday: {birthday_day}/{birthday_month}/{birthday_year}, gender: {gender}")








# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from webdriver_manager.firefox import GeckoDriverManager
# import time

# driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

# class Bot:
#     def __init__(self, username, password, users, message):
#         self.username = username
#         self.password = password
#         self.users = users
#         self.message = message
#         self.bot = driver

#     def login(self):
#         self.bot.get('https://www.instagram.com/accounts/login/')
#         time.sleep(2)

#         username_field = WebDriverWait(self.bot, 10).until(
#             EC.presence_of_element_located((By.NAME, 'username'))
#         )
#         password_field = WebDriverWait(self.bot, 10).until(
#             EC.presence_of_element_located((By.NAME, 'password'))
#         )

#         username_field.send_keys(self.username)
#         password_field.send_keys(self.password)
#         password_field.submit()

#         time.sleep(5)

#         self.bot.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/button').click()
#         time.sleep(5)

#     def send_messages(self):
#         for user in self.users:
#             self.bot.get('https://www.instagram.com/direct/new/')
#             time.sleep(2)

#             search_box = WebDriverWait(self.bot, 10).until(
#                 EC.presence_of_element_located((By.CSS_SELECTOR, 'input[aria-label="Search"]'))
#             )
#             search_box.send_keys(user)
#             time.sleep(2)

#             search_result = WebDriverWait(self.bot, 10).until(
#                 EC.presence_of_element_located((By.CSS_SELECTOR, 'a[href="/' + user + '"]'))
#             )
#             search_result.click()

#             message_box = WebDriverWait(self.bot, 10).until(
#                 EC.presence_of_element_located((By.CSS_SELECTOR, 'textarea[aria-label="Message"]'))
#             )
#             message_box.send_keys(self.message)
#             message_box.send_keys(Keys.RETURN)

#             time.sleep(2)

# if __name__ == '__main__':
#     bot = Bot('your_username', 'your_password', ['user1', 'user2', 'user3'], 'Hello!')
#     bot.login()
#     bot.send_messages()














# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# import time

# # Initialize the Firefox WebDriver
# driver = webdriver.Firefox()

# def create_account(email, username, password):
#     # Navigate to the website's sign-up page
#     driver.get('https://www.facebook.com/r.php')

#     # Fill in the email field
#     email_field = driver.find_element(By.NAME, 'email')
#     email_field.send_keys(email)

#     # Fill in the username field
#     username_field = driver.find_element(By.NAME, 'username')
#     username_field.send_keys(username)

#     # Fill in the password field
#     password_field = driver.find_element(By.NAME, 'password')
#     password_field.send_keys(password)

#     # Submit the form
#     password_field.send_keys(Keys.RETURN)

#     # Wait for a few seconds to ensure the form is submitted
#     time.sleep(5)

# def post_comment(comment):
#     # Navigate to the website's post/comment page
#     driver.get('https://www.example.com/post')

#     # Fill in the comment field
#     comment_field = driver.find_element(By.NAME, 'comment')
#     comment_field.send_keys(comment)

#     # Submit the comment
#     comment_field.send_keys(Keys.RETURN)

#     # Wait for a few seconds to ensure the comment is posted
#     time.sleep(5)

# def create_accounts_and_post_comments(account_data, comments):
#     for data in account_data:
#         email = data['email']
#         username = data['username']
#         password = data['password']
#         create_account(email, username, password)
#         for comment in comments:
#             post_comment(comment)

# # Example usage
# account_data = [
#     {'email': 'test1@example.com', 'username': 'testuser1', 'password': 'YourSecurePassword'},
#     {'email': 'test2@example.com', 'username': 'testuser2', 'password': 'YourSecurePassword'},
#     {'email': 'test3@example.com', 'username': 'testuser3', 'password': 'YourSecurePassword'}
# ]

# comments = ['This is a test comment 1', 'This is a test comment 2', 'This is a test comment 3']

# # Create accounts and post comments
# create_accounts_and_post_comments(account_data, comments)

# # Close the driver
# driver.quit()















# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# import time

# # Initialize the Firefox WebDriver
# driver = webdriver.Firefox()

# def create_account(email, username, password):
#     # Navigate to the website's sign-up page
#     driver.get('https://www.tiktok.com/signup')

#     # Fill in the email field
#     email_field = driver.find_element(By.NAME, 'email')
#     email_field.send_keys(email)

#     # Fill in the username field
#     username_field = driver.find_element(By.NAME, 'username')
#     username_field.send_keys(username)

#     # Fill in the password field
#     password_field = driver.find_element(By.NAME, 'password')
#     password_field.send_keys(password)

#     # Submit the form
#     password_field.send_keys(Keys.RETURN)

#     # Wait for a few seconds to ensure the form is submitted
#     time.sleep(5)

# def post_comment(comment):
#     # Navigate to the website's post/comment page
#     driver.get('https://www.tiktok.com/')

#     # Fill in the comment field
#     comment_field = driver.find_element(By.NAME, 'comment')
#     comment_field.send_keys(comment)

#     # Submit the comment
#     comment_field.send_keys(Keys.RETURN)

#     # Wait for a few seconds to ensure the comment is posted
#     time.sleep(5)

# # Example usage
# emails = ['test1@example.com', 'test2@example.com', 'test3@example.com']
# usernames = ['testuser1', 'testuser2', 'testuser3']
# password = 'YourSecurePassword'
# comments = ['This is a test comment 1', 'This is a test comment 2', 'This is a test comment 3']

# # Create accounts and post comments
# for email, username in zip(emails, usernames):
#     create_account(email, username, password)
#     post_comment(comments.pop(0))

# # Close the driver
# driver.quit()

