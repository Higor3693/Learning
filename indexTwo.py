from seleniumabsxy import set_show_hotkey_coords, coordsclicker
import undetected_chromedriver as uc
from time import sleep

if __name__=="__main__":
    set_show_hotkey_coords(hotkey='ctrl+alt+k')
    driver = uc.Chrome()
    coordsclicker.driver = driver
    sleep(5)
    driver.get("https://jurisprudencia.trt15.jus.br/")
    driver.maximize_window()