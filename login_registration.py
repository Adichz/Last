from selenium import webdriver
driver = webdriver.Chrome()
driver.get("http://practice.automationtesting.in/")
driver.maximize_window()
acc_men = driver.find_element_by_id("menu-item-50")
acc_men.click()
reg_milo = driver.find_element_by_id("reg_email")
reg_milo.send_keys("Velikolepnoe_Milo@bk.ru")
reg_pass = driver.find_element_by_id("reg_password")
reg_pass.send_keys("Velik0lep")
rega = driver.find_element_by_id("woocommerce-register-nonce")
rega.click()