from selenium import webdriver
from selenium.webdriver.common.keys import Keys
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

    # Navigate to the Partners page
    partners_url = "https://www.cowin.gov.in/partners"
    driver.get(partners_url)

except Exception as e:
    print(f"An error occurred: {str(e)}")

finally:
    # Close the original window
    driver.close()

    # Switch back to the first window
    driver.switch_to.window(driver.window_handles[0])

# Close the main window after completion
driver.quit()
