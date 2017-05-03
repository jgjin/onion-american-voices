from bs4 import BeautifulSoup as bs
import requests

with open("urls.txt", "w") as txt:
    page_index = 1
    while True:
        print "Processing page " + str(page_index)
        r = requests.get("http://www.theonion.com/search?feature-type=american-voices&page=" + str(page_index))
        page_index += 1
        if "The page you were seeking burned down." not in r.text:
            soup = bs(r.text, "html")
            headlines = soup.find_all("h2")
            for headline in headlines:
                try:
                    url = headline.find("a")["href"]
                    if "americanvoices" in url:
                        txt.write(url + "\n")
                except TypeError:
                    continue
        else:
            break
print "Finished."
