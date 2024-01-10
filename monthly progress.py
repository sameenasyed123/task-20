from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set the path to your webdriver executable
webdriver_path = '/path/to/chromedriver'  # Replace with the actual path

# Create a new instance of the Chrome driver
driver = webdriver.Chrome(executable_path=webdriver_path)

# Open the URL
url = "https://labour.gov.in/"
driver.get(url)

try:
    # Locate and click on the "Documents" menu
    documents_menu = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Documents"))
    )
    documents_menu.click()

    # Locate and click on the "Monthly Progress Report" link
    progress_report_link = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Monthly Progress Report"))
    )
    progress_report_link.click()

    # The above code assumes that clicking the link will initiate the download.
    # If not, you may need to handle the download dialog based on your browser.

except Exception as e:
    print(f"An error occurred: {str(e)}")

finally:
    # Close the browser after completion
    driver.quit()
