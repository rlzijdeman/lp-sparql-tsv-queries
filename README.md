# lp-sparql-tsv-queries

In order to help find datasets with (historical) geo-data across The Web and link them the World Historical Gazetteer suggests the [Linked Places format](https://github.com/LinkedPasts/linked-places/blob/master/tsv.md) with a minimum number of required and recommend fields (columns). This repository contains sparql queries that retrieve the required info from sparql endpoints.
The queries are powered via [grlc](http://grlc.io) and thus contain executable API's. To see the grlc-api's goto 'http://grlc.io/api/<name-of-github-repo-owner>/<name-of-github-query-repo/>'. So for this repo, all queries are found at [http://grlc.io/api/rlzijdeman/lp-sparql-tsv-queries/](http://grlc.io/api/rlzijdeman/lp-sparql-tsv-queries/).

To execute a query, click on the query and the 'try it out' button below the expanded query. Next scroll down and hit the blue 'execute' bar.

To download the results, click the download button in the lower right corner of the results section.

To change the format of the results into json or text/html, set the appropriate response type and hit 'execute' again.

Obviously, all of this can automatically be retrieved via CURL or REQUEST, in this case respectively:
'''curl -X GET "http://grlc.io/api/rlzijdeman/lp-sparql-tsv-queries/lp-cshapes-query?endpoint=https%3A%2F%2Fapi.druid.datalegend.net%2Fdatasets%2Fnlgis%2Fcshapes%2Fservices%2Fcshapes%2Fsparql" -H "accept: text/csv"'''

'''http://grlc.io/api/rlzijdeman/lp-sparql-tsv-queries/lp-cshapes-query?endpoint=https%3A%2F%2Fapi.druid.datalegend.net%2Fdatasets%2Fnlgis%2Fcshapes%2Fservices%2Fcshapes%2Fsparql'''

For more info on grlc, visit the [website](http://grlc.io) or github [repo](https://github.com/CLARIAH/grlc).
