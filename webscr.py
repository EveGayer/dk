import bs4 as bs
import urllib.request

# Lieber Coder Gott vergieb mir das
host = "http://www.deutschlands-brauereien.de/"
indexscript = "brauerei.php?ID=16"

# Definieren der Funktion um die "Hauptwebsite" aufzurufen
def scrap_main_website(website):
    requested_website = urllib.request.urlopen(website).read()
    soup = bs.BeautifulSoup(requested_website, 'html.parser')
    links = []
    for entry in soup.find_all('a', 'braun'):
        links.append(entry.get('href'))

    # entfernen von nicht aufrufbaren oder unnötigen links
    try:
        links.remove('javascript:history.back()')
        links.remove('#top')
    except ValueError:
        pass  # or scream: thing not in some_list!
    except AttributeError:
        print("some_list not quacking like a list!")

    return links

# Funktion um die in der oberen gefundenen subsiten ( nur der Teil nach dem / ) aufzurufen
def scrap_subsite(website, subsites_array):
    for subsite in subsites_array:
        # website/subsite
        print(website + subsite)
        requested_website = urllib.request.urlopen(website + subsite).read()
        soup = bs.BeautifulSoup(requested_website, 'html.parser')
        tbody = soup.find_all('table')
#        soup.find_all("div", class_="stylelistrowone stylelistrowtwo")

        all_braun_td = soup.find_all('td', "braun")
        print (all_braun_td)


# website/subsite
subsites = scrap_main_website(host + indexscript)
print(subsites)

scrap_subsite(host, subsites)