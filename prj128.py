import time 
import csv
from selenium import webdriver
from bs4 import BeautifulSoup

starturl = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browser = webdriver.Chrome(r"C:\Users\amogh_7war9uz\Downloads\chromedriver_win32")
browser.get(starturl)

time.sleep(10)

def scrap():
    headers = ["Name", "Distance", "Mass", "Radius"]
    planetData = []
    
    for i in range(0,213):
        soup = BeautifulSoup(browser.page_source, "html.parser")

        for ul_tag in soup.find_all("ul", attrs = {"class", "exoplanet"}):
            li_tags = ul_tag.find_all("li")
            tempList = []

            for index, li_tag in enumerate(li_tags):
                if index == 0:
                    tempList.append(li_tag.find_all("a")[0].contents[0])
                
                else:
                    try:
                        tempList.append(li_tag.contents[0])
                    except:
                        tempList.append("")
            
            planetData.append(tempList)
        
        browser.find_element_by_xpath('//*[@id="mw-panel-toc"]').click()
    
    with open("Exoplanets.csv", "w") as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerows(planetData)

scrap()