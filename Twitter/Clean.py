import pandas as pd

twitter = pd.read_csv("Raw_Data/Twitter_Transparency-Information_Requests_Jul-Dec-2020.csv", header=1)
twitter = twitter[twitter.Country == "United States"][
    ["Time period start", "Combined requests", "Combined accounts specified", "Country"]
].dropna()

twitter["half"] = ["Jul-Dec" if "07" in t else "Jan-Jun" for t in twitter["Time period start"]]
twitter["year"] = [t[0:4] for t in twitter["Time period start"]]

twitter.columns = ['Time period start', "total_requests", "total_requests_accounts", "country", 'half', 'year']

twitter["time"] = twitter.apply(lambda y: y.half + " " + y.year, axis=1)
twitter["accounts_per_request"] = twitter.total_requests_accounts / twitter.total_requests.map(lambda t: int(t))
twitter["site"] = "Twitter"

twitter = twitter[twitter.year != "2012"]
twitter = twitter[twitter.time != "Jan-Jun 2013"]

twitter = twitter.sort_values(["year", "half"], ascending=True)

twitter.to_csv("../Clean_Data/Twitter.csv")