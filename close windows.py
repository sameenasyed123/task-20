from selenium import webdriver
from selenium.webdriver.common.by import By

# Set the path to your webdriver executable
webdriver_path = '/path/to/chromedriver'  # Replace with the actual path

# Create a new instance of the Chrome driver
driver = webdriver.Chrome(executable_path=webdriver_path)

# Open the URL
url = "https://www.cowin.gov.in/"
driver.get(url)

try:
    # Locate and click the "Create FAQ" link
    create_faq_link = driver.find_element(By.LINK_TEXT, "Create FAQ")
    create_faq_link.click()

    # Open a new window/tab (using JavaScript)
    driver.execute_script("window.open('', '_blank');")

    # Switch to the new window
    driver.switch_to.window(driver.window_handles[1])

    # Display the window ID
    print(f"Window 1 ID: {driver.current_window_handle}")

    # Navigate to the FAQ page
    faq_url = "https://www.cowin.gov.in/faq"
    driver.get(faq_url)

    # Locate and click the "Partners" link
    partners_link = driver.find_element(By.LINK_TEXT, "Partners")
    partners_link.click()

    # Open another new window/tab
    driver.execute_script("window.open('', '_blank');")

    # Switch to the new window
    driver.switch_to.window(driver.window_handles[2])

    # Display the window ID
    print(f"Window 2 ID: {driver.current_window_handle}")

    # Navigate to the Partners page
    partners_url = "https://www.cowin.gov.in/partners"
    driver.get(partners_url)

finally:
    # Close the additional windows
    for handle in driver.window_handles[1:]:
        driver.switch_to.window(handle)
        driver.close()

    # Switch back to the main window
    driver.switch_to.window(driver.window_handles[0])
    print(f"Switched back to Window 0 ID: {driver.current_window_handle}")

# Close the main window after completion
driver.quit()
