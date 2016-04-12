import csv
import urllib
import io
import pandas as pd
data = urllib.request.urlopen("http://web.mta.info/developers/data/nyct/turnstile/turnstile_160326.txt")
data = list(csv.reader(io.TextIOWrapper(data)))
df = pd.DataFrame(columns=data[0],data=data[1:])