if __name__ == "__main__":
    pass

def draft_operator_message(msg):
    from selenium import webdriver
    import streamlit as st
    # from selenium.webdriver.support.wait import WebDriverWait
    from selenium.webdriver.common.by import By
    from selenium.webdriver.edge.options import Options as EdgeOptions
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    options = EdgeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_experimental_option("detach", True)
    driver = webdriver.Edge(options=options)

    driver.get("https://mis.ercot.com/moi-ercot-ihedge/#/message")
    driver.maximize_window()
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[2]/form[1]/div[2]/div[1]/textarea[1]"))
    )
    driver.find_element(By.XPATH,("/html[1]/body[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[2]/form[1]/div[2]/div[1]/textarea[1]")).clear()
    driver.implicitly_wait(1)
    driver.find_element(By.XPATH,("/html[1]/body[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[2]/form[1]/div[2]/div[1]/textarea[1]")).send_keys(msg)
    # st.session_state.moi = False
    
def draft_email(msg):
    import webbrowser
    import urllib.parse
    parsed_msg = urllib.parse.quote(msg)
    # used https://mailtolinkgenerator.com/ to generate this link
    webbrowser.open('mailto:ERCOTCRR@ercot.com?cc=James.LaWare@ercot.com&subject=Posted%20Operator%20Message%20for%20MIS%20Failover%20(01%2F18%2F2024%2C%2017%3A00-20%3A00)&body=' + parsed_msg)
    print(parsed_msg)



