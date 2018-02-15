import bs4 as bs
import urllib.request


class Sitescraper:
    def __init__(self, host, soup):
        self.host = host
        self.soup = soup

    def scrapWebsite(self, path, element, printelement):
        print(self.host + path)
        website = urllib.request.urlopen(self.host + path).read()
        soup = self.soup.BeautifulSoup(website, 'html.parser')
        for entry in soup.find_all(element):
            print(entry)
            print(entry.get(printelement))
            return entry.get(printelement)


indexscript = "brauerei.php"
params = "?ID=16"

sitescraper = Sitescraper("http://www.deutschlands-brauereien.de/", bs)

sitescraper.scrapWebsite(indexscript + params, 'a', 'href')



