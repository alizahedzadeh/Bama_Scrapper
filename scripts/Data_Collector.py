from bs4 import BeautifulSoup
from selenium import webdriver
from Const import all_brands
import pymongo


json_field = {
    "Brand_Name_eng": "",
    "Brand_Name_per": "",
    "Brand_Models_eng": [],
    "Brand_Models_per": [],
}

#Function
#For Collect data from bama website(Models and brands)
def get_brands(model):
    options = webdriver.FirefoxOptions()
    options.add_argument("--headless")
    path = r'D:\Projects\Bama_Scrapper\geckodriver.exe'
    driver = webdriver.Firefox(executable_path=path, options=options)
    driver.get("https://bama.ir/car/" + model)
    element = driver.find_element_by_id("selectedTopModel")
    element.click()
    page_src = driver.page_source
    driver.close()
    driver.quit()
    soup = BeautifulSoup(page_src, 'html.parser')
    cb4 = soup.find_all("div", {"class": "cb4"})[1]
    # print(type(cb4))
    drop_down = cb4.find(id="model-dropdown-span")
    options = drop_down.find_all("option")[1:]
    # print(options)

    per = []
    eng = []
    for data in options:
        eng.append(data['value'].split(',')[1])
        per.append(data.text)
    return eng, per



myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["Bama"]
mycol = mydb["Brands_and_Models_2"]




#INSERT DATA TO MONGODB
c = 1
for data in all_brands:
    new_json = json_field.copy()
    new_json["Brand_Name_eng"] = data[0]
    new_json["Brand_Name_per"] = data[1]
    eng, per = get_brands(data[0])
    new_json["Brand_Models_eng"] = eng
    new_json["Brand_Models_per"] = per
    # json_object = json.dumps(json_field, indent=4, ensure_ascii=False)

    mycol.insert_one(new_json)
    print(c)
    print(new_json)
    c += 1

