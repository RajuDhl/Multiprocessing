import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


def main():
    done = ""
    while done != 'y':
        service = Service("chromedriver.exe")
        driver = webdriver.Chrome(service=service)

        driver.get("https://app.apollo.io/#/login")
        driver.maximize_window()
        time.sleep(5)

        uid = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div[1]/div/div[2]/div/div[2]/div/form/div['
                                           '3]/div/div/input').send_keys("anu.t@primeaxistech.com")
        pw = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div[1]/div/div[2]/div/div[2]/div/form/div[4]/div/div['
            '1]/div/input').send_keys("Dallas2022!")

        driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div[1]/div/div[2]/div/div[2]/div/form/div[5]/div').click()

        ready = input("are you ready?? Y/N")

        no_of_items = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div/div[1]/div/div[2]/div/div[2]/div/div/div/div/div[2]/div/div[3]/div/div/div/div/div[3]/div/div[1]/span').text

        print(no_of_items)
        no_of_items = no_of_items.replace(',', '')
        print(no_of_items)
        total_pages = int(int(no_of_items[10:len(no_of_items)]) / 25) + 1
        try:
            if_extra = int(int(no_of_items[14:len(no_of_items)]) / 25) + 1
            total = total_pages + if_extra
        except:
            total = total_pages
        i = 0
        url = driver.current_url
        print("total ==>", total, "Url ===>", url)
        if ready == 'Y':
            while i in range(0, total + 1):
                driver.get(url)
                time.sleep(2)
                main = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div/div[1]/div/div[2]/div/div[2]/div/div/div/div/div[2]/div/div[2]/div/div[1]/div[1]/div/div/div').click()
                time.sleep(2)
                option = driver.find_element(By.XPATH, '/html/body/div[4]/div/div/div/a[1]')
                print(option)
                option.click()
                try:
                    try:
                        save = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div/div[1]/div/div[2]/div/div[2]/div/div/div/div/div[2]/div/div[2]/div/div[1]/div[3]/div[1]/i').click()
                        print("1")
                    except:
                        try:
                            save = driver.find_element(By.CSS_SELECTOR,
                                                       '#provider-mounter > div > div:nth-child(2) > div:nth-child(2) > div > div.zp_1DSCs > div > div.zp_3Lzj1 > div > div.zp_p7Ra4 > div > div > div > div > div.zp_1ybjt > div > div.zp_mtt5S.zp_2xQfh.zp_vXURL > div > div:nth-child(1) > div.zp_1Gu3n > div.zp-button.zp_1X3NK.zp_2NNaJ.zp_2T3rz.zp_awepE').click()
                            print("2")
                        except:
                            try:
                                save = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div/div[1]/div/div[2]/div/div[2]/div/div/div/div/div[2]/div/div[2]/div/div[1]/div[3]/div[1]')
                                print("3")
                                save.send_keys('ENTER')
                            except:
                                try:
                                    save = driver.find_element(By.XPATH, '//*[@id="provider-mounter"]/div/div[2]/div[2]/div/div[1]/div/div[2]/div/div[2]/div/div/div/div/div[2]/div/div[2]/div/div[1]/div[3]/div[1]/i')
                                    print("4")
                                except:
                                    print("unclicable")

                    print("save clicked")
                    time.sleep(0.4)
                    save.send_keys('ENTER')
                except:
                    pass
                try:
                    driver.find_element(By.XPATH, '/html/body/div[5]/div[2]/div/div/div[3]/div[1]').click()
                except:
                    print("some error")
                try:
                    next_page = driver.find_element(By.CSS_SELECTOR, '#provider-mounter > div > div:nth-child(2) > div:nth-child(2) > div > div.zp_1DSCs > div > div.zp_3Lzj1 > div > div.zp_p7Ra4 > div > div > div > div > div.zp_1ybjt > div > div.zp_p7Ra4 > div > div > div > div > div.zp_3Lry3 > div > div.zp-button-group.zp_3tokH.zp_3HFM6 > div:nth-child(3)').click()
                    time.sleep(3)
                except:
                    current_url = driver.current_url
                    driver.get(current_url)
                    time.sleep(6)
                    next_page = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div/div[1]/div/div[2]/div/div[2]/div/div/div/div/div[2]/div/div[3]/div/div/div/div/div[3]/div/div[2]/div[3]').click()
                    # error = input("Continue??")
                    # if error == 'Y':

                    # else:
                    #     pass

                i += 1
            print("end")
            zz = input("done??")
            if zz == 'y':
                done = 'y'
            else:
                pass


main()
