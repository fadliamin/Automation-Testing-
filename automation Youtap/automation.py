from atexit import register
import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestLogin(unittest.TestCase): 

    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        
    def test_a_success_login(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("https://portal.youtap.id/auth/sign-in") # buka situs
        time.sleep(3)
        browser.find_element(By.ID,"inputEmail").send_keys("085156873908") # isi email
        time.sleep(1)
        browser.find_element(By.ID,"inputPassword").send_keys("Harahap12!") # isi password
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[2]/div/div/div/div[2]/div/div/form/button").click() # klik tombol sign in
        time.sleep(1)

        

    def test_a_failed_login_non_register(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("https://portal.youtap.id/auth/sign-in") # buka situs
        time.sleep(3)
        browser.find_element(By.ID,"inputEmail").send_keys("085156873909") # isi email
        time.sleep(1)
        browser.find_element(By.ID,"inputPassword").send_keys("Harahap12!") # isi password
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[2]/div/div/div/div[2]/div/div/form/button").click() # klik tombol sign in
        time.sleep(1)

        # validasi
        response_data = browser.find_element(By.XPATH,"/html/body/div/div[2]/div/div/div/div[2]/div/div[2]/div").text
        

        self.assertEqual('User Tidak Ditemukan', response_data)
       

    def test_a_failed_login_without_password(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("https://portal.youtap.id/auth/sign-in") # buka situs
        time.sleep(3)
        browser.find_element(By.ID,"inputEmail").send_keys("085156873908") # isi email
        time.sleep(1)
        browser.find_element(By.ID,"inputPassword").send_keys("") # isi password
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[2]/div/div/div/div[2]/div/div/form/button").click() # klik tombol sign in
        time.sleep(1)

        # validasi
        response_data = browser.find_element(By.XPATH,"/html/body/div/div[2]/div/div/div/div[2]/div/div[2]/div").text
        

        self.assertIn('Password yang anda masukkan tidak sesuai', response_data)
        # self.assertEqual(response_message, 'Cek kembali email anda')

    def test_a_failed_login_without_email_and_without_password(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("https://portal.youtap.id/auth/sign-in") # buka situs
        time.sleep(3)
        browser.find_element(By.ID,"inputEmail").send_keys("") # isi email
        time.sleep(1)
        browser.find_element(By.ID,"inputPassword").send_keys("") # isi password
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[2]/div/div/div/div[2]/div/div/form/button").click() # klik tombol sign in
        time.sleep(1)

        # validasi
        response_data = browser.find_element(By.XPATH,"/html/body/div/div[2]/div/div/div/div[2]/div/div[2]/div").text
        

        self.assertEqual('User Tidak Ditemukan', response_data)

    def test_b_Forgot_password(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("https://portal.youtap.id/auth/sign-in") # buka situs
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div/div[2]/div/div/div/div[2]/div/div/form/div[3]/a").click() 
        time.sleep(1)
        browser.find_element(By.ID,"email").send_keys("085156873908") # masukkan email / no HP
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[2]/div/div/form/input[2]").click() # klik tombol submit
        time.sleep(1)

      

    def tearDown(self): 
        self.browser.close() 

if __name__ == "__main__": 
    unittest.main()