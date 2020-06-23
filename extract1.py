import makecsv
from multiprocessing import Pool

cities = [
    "Bakersfield"
]

with Pool(2) as p:
    p.map(makecsv.makecsv,cities)