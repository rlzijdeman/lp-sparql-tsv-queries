
#import libraries
import pandas as pd
import requests
import io

# set info for retrieval
url = "http://grlc.io/api/rlzijdeman/lp-sparql-tsv-queries/lp-cshapes-query?endpoint=https%3A%2F%2Fapi.druid.datalegend.net%2Fdatasets%2Fnlgis%2Fcshapes%2Fservices%2Fcshapes%2Fsparql"
headers={'accept': 'text/csv'}

# retrieve and format data
resp = requests.get(url, headers = headers)
respClean = io.StringIO(resp.content.decode("utf-8"))
df = pd.read_csv(respClean, sep = ",")

# write to tsv file
df.to_csv("./cshapes-whgz.tsv", sep="\t", index = False)

# EOF
