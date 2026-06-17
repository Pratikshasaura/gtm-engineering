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

        
free_domains = [
    "gmail.com",
    "yahoo.com",
    "hotmail.com"
]
enterprise_queue=[]
mid_market_queue=[]
smb_queue=[]
rejected_queue=[]
crm_update=[]
owner_assistant=[]
call_tasks=[]
entrichment_jobs=[]
campaign_assignments=[]
workflow_action=[]

for lead in leads:

    domain = lead["email"].split("@")[1]
    #GDPR gate
    if not lead["gdpr_ok"]:
        rejected_queue.append(lead)
        continue

    #free email rejection

    if domain in free_domains:
        rejected_queue.append(lead)
        continue
    #segment routing
    if lead["employees"]>=1000:

        segment = "Enterprise"
        enterprise_queue.append(lead)
    elif lead["employees"]>=100:
        segment="Mid-Market"
        enterprise_queue.append(lead)
    else:
        segment="SMB"
        smb_queue.append(lead)

    #Priority
    priority="high" if lead["score"]>=90 else "Normal"

    crm_update.append({
        "email": lead["email"],
        "field": "priority",
        "value": priority
    })

    #lead status
    if lead["score"] >= 90:
        lead_status = "Hot Lead"

    elif lead["score"] >= 80:
        lead_status = "Warm Lead"

    else:
        lead_status = "Cold Lead"

    crm_update.append({
        "email": lead["email"],
        "field": "lead_status",
        "value": lead_status
    })
    #owner assigned

    if segment == "Enterprise":
        owner =(
        "Strategic AE"
        if lead("score") >=90
        else "Enterprise SDR"
        )
    else:
        owner = "SMB SDR"

    owner_assistant.append({
        "email": lead["email"],
        "owner":owner
    })
#call task

    if lead["score"]>=90:
        call_task.append({
            "email": lead["email"],
            "task_type": "Call",
            "owner": owner
        })
    #enrichment
    if segment =="Enterprise" and lead["score"]>=90:
        entrichment_jobs.append({
            "email": lead["email"],
            "provider": "Clay"
        })

    #campain Assignment
    if ".ai" in domain:
        campain = "AI Campain"
    elif "bank" in domain:
        campain="Finance Campain"
    else:
        campain = "General Campain"
    
    campaign_assignments.append({
        "email": lead["email"],
        "campaign": campain

    })
    workflow_action.append({
        "email": lead["email"],
        "segment": segment,
        "priority": priority,
        "owner": owner,
        "campaign": campain
    })

    #continue
    














