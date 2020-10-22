from bs4 import BeautifulSoup
import requests

def scrape_poll_data():
    pollster_data_array = []

    URL = 'https://projects.fivethirtyeight.com/polls/president-general/'
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')

    rows = soup.find_all(class_='visible-row')
    for row in rows:
        date = row.find(class_='date-wrapper').text

        # The pollster container can have up to two links. One for the grade, if it exists,
        # and one for the pollster name. We want the latter.
        pollster_container = row.find(class_="pollster-container")
        pollster_links = pollster_container.find_all("a")
        pollster_name = pollster_links[-1].text # Accesses last element of the link array
        sample_size = row.find(class_="sample").text
        leader = row.find(class_="leader").text
        net = row.find(class_="net").text

        # Getting the percent favorable for Trump and Biden
        values = row.find_all(class_="value")
        # If the other value is hidden by the "more" button
        if len(values) == 1:
            next_sibling = row.findNext("tr")
            value = next_sibling.find(class_="value")
            values.append(value)
        biden_fav = values[0].find(class_="heat-map").text
        trump_fav = values[1].find(class_="heat-map").text
        
        pollster_data = {
            "date": date,
            "pollster_name": pollster_name,
            "sample_size": sample_size,
            "leader": leader,
            "net": net,
            "biden_fav": biden_fav,
            "trump_fav": trump_fav
        }

        pollster_data_array.append(pollster_data)

    return pollster_data_array



