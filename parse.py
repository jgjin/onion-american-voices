from bs4 import BeautifulSoup
import requests

with open("urls.txt", "w") as txt:
    page_index = 1
    valid = True
    while valid:
        print ("Processing page " + str(page_index))
        req = requests.get("http://www.theonion.com/search?feature-type=american-voices&page=" + str(page_index))
        page_index += 1
        if req.status_code == requests.codes.ok:
            soup = BeautifulSoup(req.text, "html.parser")
            headlines = soup.find_all("h2")
            for headline in headlines:
                try:
                    url = headline.find("a")["href"]
                    if "americanvoices" in url:
                        txt.write(url + "\n")
                except TypeError:
                    continue
        else:
            valid = False

print ("Finished")
