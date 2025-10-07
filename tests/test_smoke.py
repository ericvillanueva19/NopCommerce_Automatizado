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
    def test2(self): #NC-SM-02 - Login válido (usuario registrado)
        driver = self.driver
        f = Funciones_Globales(driver)
        f.Navegar("https://demo.nopcommerce.com/", t)
        f.Click_Mixto("xpath", "//a[@class='ico-login']", 4)
        f.Texto_Mixto("xpath", "//input[@id='Email']", "david0880@yopmail.com", 3)
        f.Texto_Mixto("xpath", "//input[@id='Password']", "Evv1234*", 3)
        f.Click_Mixto("xpath", "//button[normalize-space()='Log in']", 7)

    def test3(self):  # NC-SM-03 - Navegar categoría y aplicar filtro (Notebooks)
        driver = self.driver
        f = Funciones_Globales(driver)
        f.Navegar("https://demo.nopcommerce.com/", t)
        f.HoverYClick_Mixto(
            "xpath", "//ul[@class='top-menu notmobile']//a[normalize-space()='Computers']",
            "xpath", "//ul[@class='top-menu notmobile']//a[normalize-space()='Notebooks']",
            tiempo=3
        )
        f.Click_Mixto("xpath", "//input[@id='attribute-option-6']", 4)
    def test4(self):# NC-SM-04 - Ordenar por precio (Low → High)
        driver = self.driver
        f = Funciones_Globales(driver)
        f.Navegar("https://demo.nopcommerce.com/", t)
        f.HoverYClick_Mixto(
            "xpath", "//ul[@class='top-menu notmobile']//a[normalize-space()='Computers']",
            "xpath", "//ul[@class='top-menu notmobile']//a[normalize-space()='Notebooks']",
            tiempo=7
        )
        f.Select_Xpath_Type(xpath="//select[@id='products-orderby']",
                            tipo="text",
                            dato="Price: Low to High",tiempo=10)
        f.Tiempo(7)

    def test5(self):# NC-SM-05 - Detalle de producto
        driver = self.driver
        f = Funciones_Globales(driver)
        f.Navegar("https://demo.nopcommerce.com/", t)
        f.Click_Mixto("xpath", "//a[normalize-space()='Apple MacBook Pro']", 4)
        f.Scroll(cantidad=300, tiempo=2)
        f.Tiempo(10)
    def test6(self):#  NC-SM-06 - Agregar al carrito (qty=2) y validar totales
        driver = self.driver
        f = Funciones_Globales(driver)
        f.Navegar("https://demo.nopcommerce.com/", t)
        f.Click_Mixto("xpath", "//div[@class='item-grid']//div[2]//div[1]//div[2]//div[3]//div[2]//button[1]", 4)
        f.Click_Mixto("xpath", "//button[@id='add-to-cart-button-4']", 4)
        f.Click_Mixto("xpath", "//a[normalize-space()='shopping cart']", 4)
        f.Tiempo(5)
    def test7(self):#  NC-SM-07 - Actualizar cantidad y remover en carrito
        driver = self.driver
        f = Funciones_Globales(driver)
        f.Navegar("https://demo.nopcommerce.com/", t)
        f.Click_Mixto("xpath", "//div[@id='main']//div[3]//div[1]//div[2]//div[3]//div[2]//button[1]", 4)
        f.Click_Mixto("xpath", "//div[@id='main']//div[3]//div[1]//div[2]//div[3]//div[2]//button[1]", 4)
        f.Click_Mixto("xpath", "//a[normalize-space()='shopping cart']", 4)
        f.Tiempo(4)
        f.Click_Mixto("xpath", "//button[@class='remove-btn']", 4)
    def test8(self):#NC-SM-08 - Wishlist: agregar y mover al carrito
        driver = self.driver
        f = Funciones_Globales(driver)
        f.Navegar("https://demo.nopcommerce.com/", t)
        f.HoverYClick_Mixto(
            "xpath", "//ul[@class='top-menu notmobile']//a[normalize-space()='Electronics']",
            "xpath", "//ul[@class='top-menu notmobile']//a[normalize-space()='Cell phones']",
            tiempo=4
        )
        f.Click_Mixto("xpath", "//div[@class='item-grid']//div[1]//div[1]//div[2]//div[3]//div[2]//button[3]", 4)
        f.Click_Mixto("xpath","//a[normalize-space()='wishlist']",3)
        f.Click_Mixto("xpath","//input[@name='addtocart']",3)
        f.Click_Mixto("xpath","//button[@name='addtocartbutton']",3)
    def test9(self):#NC-SM-09 - Checkout como invitado (Guest)
        driver = self.driver
        f = Funciones_Globales(driver)
        f.Navegar("https://demo.nopcommerce.com/", t)
        f.Click_Mixto("xpath", "//div[@id='main']//div[3]//div[1]//div[2]//div[3]//div[2]//button[1]", 4)
        f.Click_Mixto("xpath", "//a[normalize-space()='shopping cart']", 4)
        f.Click_Mixto("xpath", "//input[@id='termsofservice']", 4)
        f.Click_Mixto("xpath", "//button[@id='checkout']", 4)
    def test10(self):
        driver = self.driver
        f = Funciones_Globales(driver)
        f.Navegar("https://demo.nopcommerce.com/", t)
        f.Click_Mixto("xpath", "//a[@class='ico-login']", 4)
        f.Texto_Mixto("xpath", "//input[@id='Email']", "david0880@yopmail.com", 3)
        f.Texto_Mixto("xpath", "//input[@id='Password']", "Evv1234*", 3)
        f.Click_Mixto("xpath", "//button[normalize-space()='Log in']", 7)
        f.Click_Mixto("xpath", "//div[@id='main']//div[3]//div[1]//div[2]//div[3]//div[2]//button[1]", 4)
        f.Click_Mixto("xpath", "//a[normalize-space()='shopping cart']", 4)
        f.Click_Mixto("xpath", "//input[@id='termsofservice']", 4)
        f.Click_Mixto("xpath", "//button[@id='checkout']", 4)
