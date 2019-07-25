import pandas as pd
import requests
url = "http://grlc.io/api/rlzijdeman/lp-sparql-tsv-queries/lp-cshapes-query?endpoint=https%3A%2F%2Fapi.druid.datalegend.net%2Fdatasets%2Fnlgis%2Fcshapes%2Fservices%2Fcshapes%2Fsparql"
headers={'accept': 'text/csv'}
resp = requests.get(url, headers = headers)
# print(resp.status_code) # 200
print(resp.content) # start with: b'"id", ...
# df = pd.read_(resp.content)
