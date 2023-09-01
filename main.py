import requests
import warnings
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pystyle import Center, Colors, Colorate
import os
import time
import random

warnings.filterwarnings("ignore", category=DeprecationWarning)

# Function to select a random proxy server from the provided dictionary
def selectRandom(proxy_servers):
    return random.choice(list(proxy_servers.values()))

# Main function
def main():
    print('')

    # Dictionary containing proxy server options
    proxy_servers = {
        1: "https://www.blockaway.net",
        2: "https://www.croxyproxy.com",
        3: "https://www.croxyproxy.rocks",
        4: "https://www.croxy.network",
        5: "https://www.croxy.org",
        6: "https://www.youtubeunblocked.live",
        7: "https://www.croxyproxy.net",
    }

    # Prompting the user to select a proxy server
    print(Colorate.Vertical(Colors.green_to_cyan, Center.XCenter("""
           
██████╗ ███████╗██╗   ██╗ ██████╗██╗  ██╗███████╗    ██████╗  ██████╗ ████████╗███████╗
██╔══██╗██╔════╝╚██╗ ██╔╝██╔════╝██║  ██║██╔════╝    ██╔══██╗██╔═══██╗╚══██╔══╝██╔════╝
██████╔╝███████╗ ╚████╔╝ ██║     ███████║█████╗      ██████╔╝██║   ██║   ██║   ███████╗
██╔═══╝ ╚════██║  ╚██╔╝  ██║     ██╔══██║██╔══╝      ██╔══██╗██║   ██║   ██║   ╚════██║
██║     ███████║   ██║   ╚██████╗██║  ██║███████╗    ██████╔╝╚██████╔╝   ██║   ███████║
╚═╝     ╚══════╝   ╚═╝    ╚═════╝╚═╝  ╚═╝╚══════╝    ╚═════╝  ╚═════╝    ╚═╝   ╚══════╝
                                                                                       
                                                 
""")))
    print("Vyber proxy server pičo (1-7):")
    proxy_choice = int(input("> "))  # User selects a proxy server by entering a number
    proxy_url = proxy_servers.get(proxy_choice)  # Retrieve the URL of the selected proxy server

    twitch_username = input("Doplň pičo https://twitch.tv/:")  # User enters their Twitch channel name
    proxy_count = int(input("Kolik chceš čekovatelů: "))  # User specifies the number of proxy sites to open

    print("Chceš snížit kvalitu na 160p? (y/n):")
    quality_choice = input("> ")

    if quality_choice.lower() == "y":
        reduce_quality = True
    else:
        reduce_quality = False

    os.system("cls")  # Clear the console screen

    print("Vytvářím fejkové čekovatele")
    print("Ujisti se, že jde stream nastavit na 160p jinak appka dropne")

    chrome_path = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'
    driver_path = 'chromedriver.exe'

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    chrome_options.add_argument('--disable-logging')
    chrome_options.add_argument("--lang=en")
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--log-level=3')
    chrome_options.add_argument('--disable-extensions')
    chrome_options.add_argument("--mute-audio")
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(options=chrome_options)

    driver.get(proxy_url)  # Open the selected proxy server in Chrome

    counter = 0  # Counter variable to keep track of the number of drivers created

    # Loop to create virtual viewers using different proxy servers
    for i in range(proxy_count):
        try:
            random_proxy_url = selectRandom(proxy_servers)  # Select a random proxy server for this tab
            driver.execute_script("window.open('" + random_proxy_url + "')")
            driver.switch_to.window(driver.window_handles[-1])
            driver.get(random_proxy_url)

            text_box = driver.find_element(By.ID, 'url')
            text_box.send_keys(f'www.twitch.tv/{twitch_username}')
            text_box.send_keys(Keys.RETURN)


            if reduce_quality:
                time.sleep(20)

                element_xpath = "//div[@data-a-target='player-overlay-click-handler']"

                element = driver.find_element(By.XPATH, element_xpath)

                actions = ActionChains(driver)

                actions.move_to_element(element).perform()

                time.sleep(20)  ## If you get errors in these parts, extend this time

                ## 160P Settings
                settings_button = driver.find_element(By.XPATH, "//button[@aria-label='Settings']")
                settings_button.click()

                wait = WebDriverWait(driver, 10)
                quality_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[text()='Quality']")))
                quality_option.click()

                time.sleep(10)  ## If you get errors in these parts, extend this time

                resolution_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(), '160p')]")))
                resolution_option.click()

            counter += 1  # Increment the counter for each driver created
            print(f"Fejkovej čekovatel {counter}/{proxy_count} spawned.")  # Print the counter and total count

        except WebDriverException as e:
            print("An error occurred while spawning a virtual viewer (Chrome driver):")
            print(e)
            break  # Exit the loop if an exception occurs

    input(Colorate.Vertical(Colors.green, Center.XCenter('Všechny fejk čekovatele byly vytvořeny, pro ukončení znásilňuj klávesu <CTRL+C>..\n')))
    print(Colorate.Vertical(Colors.green_to_cyan, Center.XCenter("""
           
    ██████╗ ███████╗██╗   ██╗ ██████╗██╗  ██╗███████╗
    ██╔══██╗██╔════╝╚██╗ ██╔╝██╔════╝██║  ██║██╔════╝
    ██████╔╝███████╗ ╚████╔╝ ██║     ███████║█████╗  
    ██╔═══╝ ╚════██║  ╚██╔╝  ██║     ██╔══██║██╔══╝  
    ██║     ███████║   ██║   ╚██████╗██║  ██║███████╗
    ╚═╝     ╚══════╝   ╚═╝    ╚═════╝╚═╝  ╚═╝╚══════╝
                                                 
""")))
    
    driver.quit()  # Close the Chrome webdriver

if __name__ == '__main__':
    main()
