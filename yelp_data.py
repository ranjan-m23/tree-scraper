import requests,os
import util
from dotenv import load_dotenv

load_dotenv()

# wrap in function
""" Calls the Yelp API and gets information for each city """
def get_yelp_data(city_name:str):
    try:
        yelp_key = os.getenv("YELP_KEY")
        auth_token = f"Bearer {yelp_key}"
        offset = 0
        total_businesses = []
        yelp_data = []
        headers={"Authorization":auth_token}


        r1 = requests.get("https://api.yelp.com/v3/businesses/search",params = {
            "term":f"tree services in {city_name}",
            "location":city_name,
            "categories":"treeservices",
            "limit":50,},headers=headers)

        data = r1.json()
        total = data['total']
        total_businesses += data['businesses']

        n = util.yelp_api_iteration_count(total)

        # get all data from api
        for i in range(n):
            offset = offset + 50

            params = {
                "term":f"tree services in {city_name}",
                "location":f"{city_name}",
                "categories":"treeservices",
                "limit":50,
                "offset":offset
            }

            r2 = requests.get("https://api.yelp.com/v3/businesses/search",params=params,headers=headers)

            data = r2.json()
            total_businesses += data['businesses']

        # iterate over total_businesses
        # total = len(total_businesses)
        total_businesses = iter(total_businesses)

        while True:
            try:
                business = next(total_businesses)
                obj = util.scrape_yelp_api_data(business,total)

                if obj != "Next":
                    yelp_data.append(obj)

            except StopIteration:
                break
    
        return yelp_data
    
    except KeyError:
        return "Invalid City"