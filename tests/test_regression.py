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



    def test1(self): #Prueba de buscador
        driver= self.driver
        f  = Funciones_Globales(driver)
        f.Navegar("https://demo.nopcommerce.com/",t)
        f.Texto_Mixto("xpath","//input[@id='small-searchterms']","Iphone")
        f.Click_Mixto("xpath","//button[@type='submit']",4)