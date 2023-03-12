import requests 
import csv
from bs4 import BeautifulSoup

BASE_URL = "https://mtgtop8.com/topcards?f=PAU&meta=145&current_page="

card_list = []
data = []
in_progress = True
x = 1
while in_progress == True:
    current_card = None
    r = requests.get(BASE_URL + str(x))
    soup = BeautifulSoup(r.content, 'html.parser')

    cards = soup.find_all('td', class_ = 'L14')

    for card in cards:
        if card.text.isalpha() or ' ' in card.text and '%' not in card.text:
            current_card = card.text
        elif '%' in card.text:
            if float(card.text.translate({ord(i):None for i in '!@#$ %'})) > 5:
                card_list.append(current_card)
                data.append(current_card)
            else:
                in_progress = False
            

    x+=1

print(card_list)

# create a CSV file in write mode
with open('output.csv', 'w', newline='') as file:

    # create a CSV writer object
    writer = csv.DictWriter(file, fieldnames=["Card Name"])

    # write the header row to the CSV file
    writer.writeheader()

    # write data to the CSV file in a loop
    write.writerows(data)