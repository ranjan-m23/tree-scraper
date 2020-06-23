"""
Generates the csv file for a given city. Calls the Yelp API , scrapes results from google and saves data to a csv file made with pandas
"""
import yelp_data,scraper
from operator import itemgetter
import pandas as pd

def makecsv(city_name):
    file_name = "_".join(city_name.split(' '))
    data = yelp_data.get_yelp_data(city_name)

    # reverse sort city_names
    yelp_data_sorted = sorted(data, key=itemgetter('yelp_review_count'), reverse=True)

    if len(yelp_data_sorted) > 50:
        data = yelp_data_sorted[:50]
    else:
        data = yelp_data_sorted

    ar = scraper.return_ratings_object(data)

    df = pd.DataFrame(ar)

    df.fillna(0,inplace=True)
    df.to_csv(f"{file_name}.csv")