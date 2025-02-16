import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_data():
    url = "https://en.wikipedia.org/wiki/List_of_municipal_corporations_in_India"  # Replace with the actual URL
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Print the HTML content to verify
    print(soup.prettify())
    
    # Example: Scraping table data
    table = soup.find('table')
    if table is None:
        print("No table found in the HTML content.")
        return
    
    rows = table.find_all('tr')
    
    data = []
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        data.append([ele for ele in cols if ele])
    
    df = pd.DataFrame(data[1:], columns=data[0])
    df.to_csv('../data/scraped_data.csv', index=False)

if __name__ == "__main__":
    scrape_data()