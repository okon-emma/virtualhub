from portal.models import Leaque, Week, Match
from bs4 import BeautifulSoup
import datetime
#exec(open('port.py').read())

count = 0
now = str(datetime.datetime.now())
soup = BeautifulSoup(open('page.html'), 'html.parser')
weeks = soup.findAll('td', {'style':'width: 33%; text-align:center; background-color: #E1E3E6; padding: 7px'})

h = weeks[0].findAll('tr')[1].findAll('td')[0].text
w = weeks[0].findAll('tr')[1].findAll('td')[2].text
leaque_identifier = h + w
l = Leaque(leaque_id=leaque_identifier, date=now)
l.save()

#f = open("results.csv", "w")
#f.write("home, score, away \n")

for week in weeks:
    weekn = week.findAll('tr')
    count = count +1
    w = Week(position=str(count), leaque=l)
    w.save()
    print("Week " + str(count) + " Inserted")

    for match in weekn:
        match1 = match.findAll('td')
        if len(match1) == 3:
            home = match1[0].text
            score = match1[1].text
            away = match1[2].text
            match_id = home + away
            #f.write(home + "," + score + "," + away + "\n")
            m = Match(match_id=match_id, home=home, score=score, away=away, week=w)
            m.save()
#f.close()
print(" Data Porting Completed Sucessfully...")
