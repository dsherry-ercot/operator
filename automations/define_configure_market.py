if __name__ == "__main__":
    pass

def dcm(name):
    from selenium import webdriver
    # from selenium.webdriver.support.wait import WebDriverWait
    from selenium.webdriver.common.by import By
    from selenium.webdriver.edge.options import Options as EdgeOptions
    options = EdgeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_experimental_option("detach", True)
    driver = webdriver.Edge(options=options)

    driver.get('https://mis.ercot.com/moi-ercot-ihedge/#/market/auction/new')
    driver.maximize_window()
    driver.find_element(By.ID, 'marketName').send_keys(name)
    driver.find_element(By.ID, 'marketDescription').send_keys(name)
    auction_type = "MONTHLY" if "month" in str(name).lower() else "ANNUAL"
    driver.find_element(By.ID, 'termSelect').send_keys(auction_type)

    # --bid limit--
    bid_limit = driver.find_element(By.ID, 'auctionBidLimit')
    if auction_type == "MONTHLY":
        bid_limit.send_keys(10000)
    else:
        bid_limit.send_keys(4000)


    from data import df_activity_calendar

    # targetDateField
    six_days_ahead = df_activity_calendar.get_psadders_day_before(name)
    driver.find_element(By.ID, 'targetDateField').send_keys(six_days_ahead)

    # noticeDateField
    notice_date = df_activity_calendar.get_notice_date(name)
    driver.find_element(By.ID, 'noticeDateField').send_keys(notice_date)

    # openDateField
    open_date = df_activity_calendar.get_open_date(name)
    driver.find_element(By.ID, 'openDateField').send_keys(open_date)

    # closeDateField
    close_date = df_activity_calendar.get_close_date(name)
    driver.find_element(By.ID, 'closeDateField').send_keys(close_date)

  
    period_name = df_activity_calendar.get_period_name(name)
    # --constraint factor--
    cfactor_element = 'factor_' + period_name
    driver.find_element(By.ID, cfactor_element).clear()
    driver.find_element(By.ID, cfactor_element).send_keys(90)

    # Radio Button
    cb = 'radio_' + period_name
    driver.find_element(By.ID, cb).click()
    driver.find_element(By.ID, cb).click()

def attach_data_cases(name):
    from selenium import webdriver
    from selenium.webdriver import ActionChains, Keys
    from selenium.webdriver.common.by import By
    from selenium.webdriver.edge.options import Options as EdgeOptions
    from data import df_activity_calendar
    period_name = df_activity_calendar.get_period_name(name)
    print(period_name)
    options = EdgeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_experimental_option("detach", True)
    driver = webdriver.Edge(options=options)

    driver.get('https://mis.ercot.com/moi-ercot-ihedge/#/market/auction')
    driver.maximize_window()
    driver.implicitly_wait(2)
    driver.find_element(By.PARTIAL_LINK_TEXT, name).click()

    # Go to 'Grid'
    # UNFINISHED
    driver.get(driver.current_url.replace('edit', 'ngrid'))
    driver.find_elements(By.CSS_SELECTOR, "[id*=period_name]")

    peak_wd = driver.find_element(By.ID, "PeakWD::" + period_name)
    off_peak = driver.find_element(By.ID, "Off-peak::" + period_name)
    peak_we = driver.find_element(By.ID, "PeakWE::" + period_name)
    driver.implicitly_wait(2)
    elements = [peak_we, peak_wd, off_peak]
    action = ActionChains(driver)
    action.key_down(Keys.CONTROL)
    driver.implicitly_wait(2)
    for element in elements:
        element.click()
    action.key_up(Keys.CONTROL)
    


    
    


