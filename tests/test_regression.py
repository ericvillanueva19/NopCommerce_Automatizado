import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

t=2
from Funciones import Funciones_Globales

class flujo_completo(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        # options.add_argument("--headless=new")  # opcional

        self.driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=options
        )
        self.driver.maximize_window()


    def test1(self): # NC-SM-01 - Registro válido (nuevo usuario)
        driver= self.driver
        f  = Funciones_Globales(driver)
        f.Navegar("https://demo.nopcommerce.com/",t)
        f.Click_Mixto("xpath","//a[@class='ico-register']",4)
        f.Check_Xpath("//span[@class='male']",3)
        f.Texto_Mixto("xpath", "//input[@id='FirstName']", "Eric",3)
        f.Texto_Mixto("xpath", "//input[@id='LastName']", "Villanueva",3)
        f.Texto_Mixto("xpath", "//input[@id='Email']", "david0880@yopmail.com",3)
        f.Texto_Mixto("xpath", "//input[@id='Password']", "Evv1234*",3)
        f.Texto_Mixto("xpath", "//input[@id='ConfirmPassword']", "Evv1234*",3)
        f.Click_Mixto("xpath", "//button[@id='register-button']", 4)

    def test2(self): # NC-SM-01 - Registro válido (nuevo usuario)
        driver= self.driver
        f  = Funciones_Globales(driver)
        f.Navegar("https://demo.nopcommerce.com/",t)
        f.Click_Mixto("xpath","//a[@class='ico-register']",4)
        f.Check_Xpath("//span[@class='male']",3)

        f.Texto_Mixto("xpath", "//input[@id='Email']", "david0880@yopmail.com",3)
        f.Texto_Mixto("xpath", "//input[@id='Password']", "Evv1234*",3)
        f.Texto_Mixto("xpath", "//input[@id='ConfirmPassword']", "Evv1234*",3)
        f.Click_Mixto("xpath", "//button[@id='register-button']", 4)
    def test3(self): # NC-SM-01 - Registro válido (nuevo usuario)
        driver = self.driver
        f = Funciones_Globales(driver)
        f.Navegar("https://demo.nopcommerce.com/", t)
        f.Click_Mixto("xpath", "//a[@class='ico-login']", 4)
        f.Texto_Mixto("xpath", "//input[@id='Email']", "david0880@yopmail.com", 3)
        f.Texto_Mixto("xpath", "//input[@id='Password']", "Ericdavid", 3)
        f.Click_Mixto("xpath", "//button[normalize-space()='Log in']", 7)
    def test4(self): # NC-SM-01 - Registro válido (nuevo usuario)
        driver = self.driver
        f = Funciones_Globales(driver)
        f.Navegar("https://demo.nopcommerce.com/", t)
        f.Click_Mixto("xpath", "//a[@class='ico-login']", 4)
        f.Texto_Mixto("xpath", "//input[@id='Email']", "david0880yopmail.com", 3)
        f.Texto_Mixto("xpath", "//input[@id='Password']", "Evv1234*", 3)
        f.Click_Mixto("xpath", "//button[normalize-space()='Log in']", 7)
    def test5(self):
        driver = self.driver
        f = Funciones_Globales(driver)
        f.Navegar("https://demo.nopcommerce.com/", t)