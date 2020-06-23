def yelp_api_iteration_count(total_count:int):
    return (total_count//50)


def scrape_yelp_api_data(business_object,total):
    name = business_object['name']
    rating = business_object['rating']
    review_count = business_object['review_count']
    phone = business_object["phone"]
    city = business_object["location"]["city"]

    # conditonals
    if review_count < 2 and total > 20:
        return "Next"

    yelp_obj = {
            "name":name,
            "phone":phone,
            "city":city,
            "yelp_rating":rating,
            "yelp_review_count":review_count,
    }
    return yelp_obj

def google_rating_and_count(google_review:str):
    rating_and_count = google_review.strip("Google reviews")
    rating = float(rating_and_count[:3])
    count = int(rating_and_count[3:])
    
    return (rating,count)

def website_rating_and_count(rating:str):
    rating = rating.split(":")[1]
    # stipping whitespace
    rating = rating.rstrip().lstrip().strip('\u2003')

    # extract position of suffix
    if "review" in rating:
        string = rating.find("review")

    if "reviews" in rating:
        string = rating.find("reviews")

    if "vote" in rating:
        string = rating.find("vote")
    
    if "votes" in rating:
        string = rating.find("votes")
    

    # remove suffix
    numbers = rating[0:string].split('- \u200e')

    # make rating and rating_count
    rating = float(numbers[0].lstrip().rstrip())
    rating_count = int(numbers[1].lstrip().rstrip())

    # return rating and rating_count
    return (rating,rating_count)


def retrive_domain(url):
    a = url.split('.')
    return a[1]

def split_list(l, n:int):
    k, m = divmod(len(l), n)
    return (l[i * k + min(i, m):(i + 1) * k + min(i + 1, m)] for i in range(n))