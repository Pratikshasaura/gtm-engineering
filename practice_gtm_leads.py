#Suppression lead check
from lead import leads

unsubscribed = [
    "alice@techcorp.com",
    "bob@startup.io"
]
outreach_query = []

for lead in leads:
    if lead["email"] not in unsubscribed:
        outreach_query.append(leads)

from lead import leads

unsubscribed = [
    "alice@techcorp.com",
    "bob@startup.io"
]
outreach_query = []
for lead in leads:
    if lead["email"] not in unsubscribed:
        outreach_query.append(leads)





