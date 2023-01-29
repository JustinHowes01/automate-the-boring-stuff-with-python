import bs4
import requests


def getEtsyPrice(productUrl):
    res = requests.get(productUrl)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.select(
        '#listing-page-cart > div.wt-mb-xs-6.wt-mb-lg-0 > div:nth-child(1) > div.wt-mb-xs-3 > div.wt-mb-xs-3 > div:nth-child(1) > div > div.wt-display-flex-xs.wt-align-items-center.wt-flex-wrap > p')
    return elems[0].text.strip()


price = getEtsyPrice(
    'https://www.etsy.com/listing/1336771386/python-cheat-sheet-coaster-made-of-a?ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=westartfactory&ref=sr_gallery-1-3&bes=1&organic_search_click=1')
print('The price is ' + price)
