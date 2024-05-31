
import time
from seleniumabsxy import coordsclicker, click_on_coords
import undetected_chromedriver as uc
from mousekey import MouseKey
from selenium.webdriver.common.alert import Alert

driver = uc.Chrome()
Alerta = Alert(driver)
mkey = MouseKey()


def captcha():
    mkey.left_click_xy_natural(
        849,
        678,
        delay=.3,
        min_variation=-10,
        max_variation=10,
        use_every=4,
        sleeptime=(0.005, 0.009),
        print_coords=True,
        percent=90,
    )

def pesquisar():
    mkey.left_click_xy_natural(
        996,
        683,
        delay=2,
        min_variation=-10,
        max_variation=10,
        use_every=4,
        sleeptime=(0.005, 0.009),
        print_coords=True,
        percent=90,
    )

def passarCaptcha():

    coordsclicker.driver = driver
    driver.get("https://jurisprudencia.trt15.jus.br/")
    driver.maximize_window()

    time.sleep(2)
    captcha()

    time.sleep(10)
    pesquisar()

    time.sleep(5)

    driver.close()

passarCaptcha()