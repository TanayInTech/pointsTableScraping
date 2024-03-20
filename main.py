from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import json

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

url = "https://en.wikipedia.org/wiki/2023_Cricket_World_Cup"
driver.get(url)

team_names = driver.find_elements("xpath", '//table[@class="wikitable"][3]/tbody/tr/th/a')
points = driver.find_elements("xpath", '//table[@class="wikitable"][3]/tbody/tr/td[7]')

data = []

for team, point in zip(team_names, points):
    data.append({
        "team": team.text,
        "points": point.text
    })

json_data = json.dumps(data, indent=4)

print(json_data)

# Close the webdriver
driver.quit()
