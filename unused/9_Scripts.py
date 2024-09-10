import streamlit as st

st.markdown('### Here are some scripts you can run:')
st.markdown('______')
st.markdown('##### This script will open the MOI to the 2026.2nd6.AnnualAuction.Seq6 auction')

def run_selenium():
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.edge.options import Options as EdgeOptions
    import time

    options = EdgeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Edge(options=options)

    # Popup message
    # messagebox.showinfo(title='Cert verification', message='Press on your certification and click OK')

    driver.get('https://mis.ercot.com/moi-ercot-ihedge/#/market/auction')
    driver.maximize_window()

    element = driver.find_element(By.LINK_TEXT, '2026.2nd6.AnnualAuction.Seq6').click()
    driver.implicitly_wait(3)
    market_report = driver.find_element(By.LINK_TEXT, 'Market Report').click()

    # wait = webdriver(driver, 30);
    # driver element = wait.until(ExpectedConditions.elementToBeClickable(By.linkText("some_link")));
    # element.click();

    # element = driver.find_element(By.ID, 'sb_form_q')
    # element.send_keys('Why is Dan so awesome')
    # element.submit()

    time.sleep(5)
    driver.quit()
        # perform a task
        # modify or add to session state

st.button('Run Script!', on_click=run_selenium)