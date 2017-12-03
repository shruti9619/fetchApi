def fetch_notifics(limit=10):
    # by default top ten notifications will be fetched
    # returns list of dictionary with date and notification text
    notif_dict = list([])



    import requests
    # specify the url
    url = "http://www.ipu.ac.in/notices.php"

    page = requests.get(url)

    # import the Beautiful soup functions to parse the data returned from the website
    from bs4 import BeautifulSoup

    soup = BeautifulSoup(page.content, 'html.parser')

    import re

    tds = soup.find_all('td')


    i = 0
    j = 0
    while j < limit and i < len(tds):
        td = tds[i].find('a', attrs={'href': re.compile('/pubinfo/')})
        if td is not None:
            # storing in dictionary in list
            notif_dict.append({'date':tds[i + 1].string, 'notification_text':td.string })
            j += 1
        i += 1



    return notif_dict



#print(fetch_notifics(4))