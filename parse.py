from bs4 import BeautifulSoup
import requests

with open("urls.txt", "w") as txt:
    next_url = "https://www.theonion.com/c/american-voices"
    while next_url is not None:
        print ("Processing " + next_url)
        req = requests.get(next_url)
        if req.status_code == requests.codes.ok:
            soup = BeautifulSoup(req.text, "html.parser")
            load_more_button = soup.find("div", {"class": "load-more__button"})
            next_url = (
                "https://www.theonion.com/c/american-voices" + \
                load_more_button.find("a")["href"]
                if load_more_button is not None else
                None
            )
            headlines = soup.find_all("h1", {"class": "headline entry-title"})
            for headline in headlines:
                url = headline.find("a")["href"]
                txt.write(url + "\n")
        else:
            print ("Bad status code for " + next_url)

print ("Finished")
