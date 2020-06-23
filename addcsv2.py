import pandas as pd

df1 = pd.read_csv('El_Paso.csv')
print(df1)

data = [
    {'name':'El Paso Tree Services','google_rating': 4.0, 'google_review_count': 4, 'facebook_rating': 5.0, 'facebook_review_count': 1, 'website_name': 'https://www.elpasotrees.com/'},
    {'name':"john's Tree and Lawn Services",'google_rating': 3.5, 'google_review_count': 4, 'angieslist_rating': 4.6, 'angieslist_review_count': 10, 'yellowpages_rating': 1.0,'yellowpages_review_count': 1, 'website': 'not claimed on google'},
    {'name':'Growing Concern','google_rating': 4.7, 'google_review_count': 9, 'facebook_rating': 5.0, 'facebook_review_count': 3, 'angieslist_rating': 4.8, 'angieslist_review_count': 44, 'website_name': 'http://www.growingconcerntexas.com/'}
]

df2 = pd.DataFrame(data)

df1.append(df2)
print(df1)

df1.fillna(0,inplace=True)

df1.to_csv("El_PasoF.csv")