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

from lead import leads

unsubscribed = [
    "alice@techcorp.com",
    "bob@startup.io"
]
outreach_query = []
for lead in leads:
   if lead["email"] not in unsubscribed:
      outreach_query.append(leads)
#block free email domain

block_domains = [
   "gmail.com",
   "yahoo.com",
   "hotmail.com"
]
sales_queue = []

for lead in leads:
   domain = lead["email"].split("@")[1]

if domain not in block_domains:
   sales_queue.append(lead)

#high schore leads shoud get calls
call_leads=[]

for lead in leads:
    if lead["score"]>=90:
        call_leads.append({
            "owner":"sales_team"
            "task_type":"call"
            "email":lead["email"]
        })
#gtm Thinking from CRM if score of lead in leads >=90
# call them
High_priority_leads = []

for lead in leads:
    if lead["score"] >=90:
        High_priority_leads.append(lead)

enterprise_leads = []

for lead in leads:
    if lead["employees"]>=500:
        enterprise_leads.append(lead)

qualified_leads = []

for lead in leads:
    if lead(["gdpr_ok"]=True) and lead(["score"]>=80):
        qualified_leads.append(lead)

call_task= []

for lead in leads:
    if lead["score"]>=90:
        call_task.append({
            "email":lead["email"],
            "task_type":"call"
        })



blocked_domain=[
    "gmail.com",
    "yahoo.com",
    "hotmail.com"
]
blocked_lead = []
business_leads = []
for lead in leads:
    domain = lead["email"].split("@")[1]

    if domain in blocked_domain:
        blocked_lead.append(lead)
    else:
        business_leads.append(lead)    

        






