import util
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# city_name = input("Enter city name: ")
# cty_name = "+".join(city_name.split(' '))

services = [
    'El Paso Tree Service','El Paso Tree Removal',"Johns Tree and Lawn Services","American Tree Trimming","R&M Tree Service","Growing Concern","El Paso Landscaping and Tree Service"
]

for service in services:
    print(service)
    string = "+".join(service.split(" "))
    driver = webdriver.Chrome('./chromedriver')

    driver.get(f"https://www.google.com/search?q={string}+El+Paso")

    main_object = {}

    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.ID, "cnt"))
        )
    except:
        print("Failed to load. Execute script again")

    driver.execute_script(
        """
        let list = document.getElementsByClassName("dhIWPd f")
        let aside = document.querySelector(".rhsvw.kno-kp.mnr-c.g-blk")
        if(aside != null){
            document.output = "aside present"
            let google_review = document.querySelector(".Ob2kfd")
            let website_button = document.querySelector(".ab_button")

            try {
                document.google_review = google_review.textContent
                if(website_button != null && website_button.textContent == "Website"){
                document.website = website_button.getAttribute("href")
            }

            }

            catch(err){ }
        }
        try {
            results = document.querySelectorAll(".r")
            document.top = results[0].getElementsByTagName("a")[0].getAttribute("href")
        }
        catch(err){ }


        document.obj = []

        for(let i = 0 ; i < list.length;i++){
        let a = list[i].textContent
        if (a.search("Rating:") != -1){
            a = String(a)
        let b = list[i].parentElement.parentElement.parentElement.firstElementChild.getElementsByTagName("cite")[0].textContent
        result = b.slice(0,b.search(" "))

        if(result !="www.yelp.com" && result !="https://www.yelp.com" && result != "www.yelp.com.mx"){
        details = {
            "rating":a,
            website:result
        }

        document.obj.push(details)
        }
        }
        }
        """
    )

    web_ratings = driver.execute_script("return document.obj")
    google_ratings = driver.execute_script("return document.google_review")
    website_name = driver.execute_script("return document.website")
    top_website = driver.execute_script("return document.top")

    # debug
    # print(web_ratings)

    # ________________________________________________________
    # skip insertion if both ratings are non

    # ________________________________________________________

    # if google rating insert into main_object
    if google_ratings != None:
        google_rating,google_count = util.google_rating_and_count(google_ratings)
        g_r = {
            "google_rating":google_rating,
            "google_review_count":google_count
        }

        main_object.update(g_r)


    # ________________________________________________________

    # if ratings insert into object
    web_ratings_obj = {}

    if web_ratings != None:
        for obj in web_ratings:
            website = util.retrive_domain(obj['website'])
            rating,review_count = util.website_rating_and_count(obj['rating'])
            web_ratings_obj[f'{website}_rating'] = rating
            web_ratings_obj[f'{website}_review_count'] = review_count

        main_object.update(web_ratings_obj)


    # ________________________________________________________

    # insert website
    if website_name != None and top_website != None:
        main_object['website_name'] = website_name

    elif website_name == None and top_website != None:
        main_object['website'] = "not claimed on google"

    elif website_name != None and top_website == None:
        main_object['website'] = website_name


    # ________________________________________________________
    driver.close()
    print(main_object)
