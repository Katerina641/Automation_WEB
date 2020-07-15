import pytest # preinstalled with "pip install pytest-dependency"
from selenium import webdriver
import unittest
import time
import json # text format for storing and exchanging data.
import requests # preinstalled with "pip install requests" for interacting with HTTP
from selenium.webdriver.common.keys import Keys
import smtplib, ssl # Sending emails from Python using smtplib module
from email.mime.text import MIMEText # used to work with mail
from email.mime.multipart import MIMEMultipart # to send email automatically

#Declare dependencies
def pytest_namespace():
    return {'email': None}
def pytest_namespace():
    return {'data_f': None}
def pytest_namespace():
    return {'data_c': None}
def pytest_namespace():
    return {'data_d': None}


class search_site (unittest.TestCase):

    @pytest.mark.dependency() # creating dependency
    def test_01(self): # Open the browser, go to https://getnada.com. Remember the generated email address

        self.driver = webdriver.Chrome(executable_path="C:/Users/Katerina/Documents/drivers/chromedriver.exe")
        self.driver.get("https://getnada.com")
        driver = self.driver
        pytest.email = driver.find_element_by_xpath('.//span[@class="address what_to_copy"]').text

        if pytest.email==pytest.email.find('@'):
            assert True
        driver.implicitly_wait(1000.0) # the tab remains open

    @pytest.mark.dependency() # creating dependency
    def test_02(self): # Request random links in API and convert to links

        self.driver = webdriver.Chrome(executable_path="C:/Users/Katerina/Documents/drivers/chromedriver.exe")
        self.driver.get("https://aws.random.cat/meow")
        driver = self.driver
        time.sleep(0.2)
        link_1= driver.find_element_by_xpath("//pre")
        data = json.loads(link_1.text)
        pytest.data_f = data['file']
        if requests.get("https://aws.random.cat/meow"):
            assert True
        driver.close()

    @pytest.mark.dependency()
    def test_03(self): # Request random links in API and convert to links

        self.driver = webdriver.Chrome(executable_path="C:/Users/Katerina/Documents/drivers/chromedriver.exe")
        self.driver.get("https://random.dog/woof.json")
        driver = self.driver
        time.sleep(0.2)
        link_1 = driver.find_element_by_xpath("//pre")
        data = json.loads(link_1.text)
        pytest.data_c = data['url']
        if requests.get("https://random.dog/woof.json"):
            assert True
        driver.close()

    @pytest.mark.dependency()
    def test_04(self): # Request random links in API and convert to links

        self.driver = webdriver.Chrome(executable_path="C:/Users/Katerina/Documents/drivers/chromedriver.exe")
        self.driver.get("https://randomfox.ca/floof/")
        driver = self.driver
        time.sleep(0.2)
        link_1 = driver.find_element_by_xpath("//pre")
        data = json.loads(link_1.text)
        pytest.data_d = data['image']
        if requests.get("https://randomfox.ca/floof/"):
            assert True
        driver.close()

    @pytest.mark.dependency(depends=["search_site::test_01"]) # dependency links
    @pytest.mark.dependency(depends=["search_site::test_02"])
    @pytest.mark.dependency(depends=["search_site::test_03"])
    @pytest.mark.dependency(depends=["search_site::test_04"])

    def test_05(self): # sending a letter that contains received links to the images

        self.driver = webdriver.Chrome(executable_path="C:/Users/Katerina/Documents/drivers/chromedriver.exe")
        self.driver.get("https://mail.google.com/mail/u/2/?pli=1#inbox")
        driver = self.driver
        sender_email = "terentevakaterina641@gmail.com"
        receiver_email = pytest.email
        password = "1P2P3P4P5P"

        message = MIMEMultipart("alternative")
        message["Subject"] = "multipart test"
        message["From"] = sender_email
        message["To"] = receiver_email

        # Create the  HTML version of your message
        html = '''\
        <html>
          <body>
            <p>Hi,<br>
               Your link №1 is<br>
             ''' + str(pytest.data_f) + '''
            </p>
            <p><br>
               Your link №2 is<br>
             ''' + str(pytest.data_c) + '''
            </p>
            <p><br>
               Your link №3 is<br>
             ''' + str(pytest.data_d) + '''
            </p>
          </body>
        </html>
        '''


        # Add HTMLto MIMEMultipart message
        # The email client will try to render the last part first
        message.attach(MIMEText(html, 'html'))

        # Create secure connection with server and send email
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(
                sender_email, receiver_email, message.as_string()
            )

        if receiver_email==receiver_email.find('@'):
            assert True
        driver.close()
        time.sleep(90)



if __name__ == "__main__":
    unittest.main()