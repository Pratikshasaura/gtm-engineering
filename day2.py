# What Is a List? Many Values, One Variable.
"""GTM example: You don't have 47 separate variables for 47 lead emails. You have one list called lead_emails that contains all 47.
 When you pull contacts from HubSpot API, the response comes back as a list. Every CSV file becomes a list of rows.
   Lists are everywhere in GTM data work."""
lead_emails = ["alice@techcorp.com","bob@startup.io","carol@enterprise.co.io","dave@scaleup.com"]
lead_scores = [85,42,91,67]
deal_value = [8500.55,4566.85,4526.00,15000.00]
is_enterprise = [True, False, True, False]
hot_lead = []

#Indexing
"""count starts with zero python also supports -ve indexing
-ve indexing means count from back ex. in above variable lead_score"""

"""
Slicing — Getting a Portion of a List
Sub-lists
Use [start:stop] to get a section of a list. Stop index is excluded.
Slicing gives you a new list made from part of the original. The syntax is [start:stop] where start is included and stop is excluded. If you leave start empty, it means "from the beginning". If you leave stop empty, it means "to the end".
GTM use case: API pagination — you pulled 100 leads but only want to process the first 10 to test. Or you have a ranked list of accounts and want only the top 5. Slicing does this in one line."""

"""len() — How Many Items Are in the List?
Built-in Function
len() returns the number of items in a list. You'll use this constantly.
len() works on lists, strings, and other collections. For a list of 4 items, len() returns 4. This is essential for reporting ("processed 247 leads"), for checking if a list is empty before processing it, and for calculating rates."""
print(len(lead_emails))

"""Checking Membership + Sorting
The in operator & sorted()
in checks if something is in a list (returns a boolean). sorted() returns a sorted version.
The in operator is how you ask "is this email already in the unsubscribe list?" or "is this company in my target account list?" It returns True or False — making it a boolean check you'll pair with if statements on Day 4."""
target_accounts = ["TechCorp", "StartupIO", "EnterpriseCoUK"] 
unsubscribed = ["bob@startup.io", "frank@old.com"]
print("TechCorp" in target_accounts)
lead_scores = [85, 42, 91, 67, 55]
ranked = sorted(lead_scores, reverse=True)
print(ranked)
companies = ["Zeta Corp", "Acme", "Beta Inc"] 
print(sorted(companies))

"""Lists of Lists — A Preview of Real GTM Data
Nested Structure
A list can contain other lists. This is how CSV rows work — a table is a list of rows, each row is a list.
Real GTM data is rarely a flat list of single values. A CSV file becomes a list of rows, where each row is itself a list of column values. Understanding this structure is the bridge from "toy examples" to real data work. Tomorrow (Day 3) you'll upgrade this to a list of dictionaries, which is how APIs actually return data."""
leads = [ ["alice@techcorp.com", 85, "MQL"], ["bob@startup.io", 42, "Lead"], ["carol@enterprise.co.uk", 91, "SQL"], ["dave@scaleup.com", 67, "MQL"] ]
print(f"Total leads: {len(leads)}")
print(leads[0])
print(leads[0][0])
print(leads[0][1])
print(leads[2][2])
leads = [ ["alice@techcorp.com", 85, "MQL", True], ["bob@startup.io", 42, "Lead", False], ["carol@enterprise.co.uk", 91, "SQL", True], ["dave@scaleup.com", 67, "MQL", False], ["eve@bigco.com", 78, "MQL", True], ["frank@tiny.io", 31, "Lead", False], ] 
unsubscribed = ["frank@tiny.io", "old@gone.com"]
emails = []
scores = []
stages = []
emails.append(leads[0][0]); 
scores.append(leads[0][1]); 
stages.append(leads[0][2]) 
emails.append(leads[1][0]); 
scores.append(leads[1][1]); 
stages.append(leads[1][2]) 
emails.append(leads[2][0]); 
scores.append(leads[2][1]); 
stages.append(leads[2][2]) 
emails.append(leads[3][0]); 
scores.append(leads[3][1]); 
stages.append(leads[3][2]) 
emails.append(leads[4][0]); 
scores.append(leads[4][1]); 
stages.append(leads[4][2]) 
emails.append(leads[5][0]); 
scores.append(leads[5][1]); 
stages.append(leads[5][2])
total_leads= len(leads) 
top_lead_email= leads[0][0]
last_lead_email= leads[-1][0]
ranked_scores = sorted(scores, reverse=True)
highest_score = ranked_scores[0]
lowest_score = ranked_scores[-1]
top3scores= ranked_scores[:3]
avg_score = sum(scores) / len(scores)
frank_unsub = "frank@tiny.io" in unsubscribed
alice_unsub = "alice@techcorp.com" in unsubscribed
print() 
print("━" * 50) 
print(" LEAD PROCESSOR REPORT") 
print("━" * 50) 
print(f" Total leads: {total_leads}") 
print(f" Highest score: {highest_score}") 
print(f" Lowest score: {lowest_score}") 
print(f" Average score: {avg_score:.1f}") 
print(f" Top 3 scores: {top3scores}") 
print(f" First lead: {top_lead_email}") 
print(f" Last lead: {last_lead_email}") 
print("━" * 50) 
print(" UNSUBSCRIBE CHECKS") 
print(f" frank@tiny.io in unsub list? {frank_unsub}") 
print(f" alice@techcorp.com in unsub? {alice_unsub}") 
print("━" * 50) 
print(" STAGES BREAKDOWN") 
print(f" All stages: {stages}") 
print(f" First 3 emails: {emails[:3]}") 
print("━" * 50)

"""What Is a Dictionary? A CRM Record in Python.
The Mental Model
A dictionary stores data as key: value pairs inside curly braces. Every value has a name.
you stored a lead as ["alice@techcorp.com", 85, "MQL", True] — 
a list where position meant everything. To get the score you wrote lead[1]. 
A dictionary gives every piece of data a name. Instead of lead[1] you write lead["score"]. 
Much clearer. Much safer.
GTM example: Every HubSpot contact, every Salesforce lead, every row returned from a CRM API is a 
dictionary in Python — a collection of named fields and their values. 
When you call the HubSpot API to get a contact, the response looks exactly like a 
Python dictionary: {"email": "alice@techcorp.com", "score": 85, "stage": "MQL"}."""
contact = {"email": "alice@google.com", "score" : 85, "Stage": "MQL", "is_enterprise": True, "mrr": 8500.55,}
print(contact)
print(type(contact))
#cannot do slicing in dict
email = contact["email"]
mrr = contact["mrr"]
print(email, mrr)
"""Accessing Values — Square Brackets vs .get()
Two Ways to Read Data
Use dict["key"] when the key must exist. Use dict.get("key") when it might not.
Square bracket access crashes with a KeyError if the key doesn't exist. .get() 
returns None (or a default you choose) if the key is missing — no crash. In GTM data work, 
API responses often have missing fields. A contact might have no phone number, no company size, 
no industry. .get() is how you handle that safely.
GTM rule: Use square brackets for fields you know will always exist (email, contact ID). Use .get() 
for optional enrichment fields (phone, LinkedIn URL, company revenue) that might be missing."""
print(contact.get("phone"))
print(contact.get("score"))
phone= contact.get("phone","N/A")
industry = contact.get("industry", "unknown")
print(f"Phone: {phone}, Industry: {industry}")
"""Adding & Updating Values
Mutating a Dictionary
Assign to a key to add or update it. If the key exists, it updates. If it doesn't, it's created.
Dictionaries are mutable — you can add new fields and update existing ones after creation. 
The syntax is the same whether you're adding a new key or updating an existing one: dict["key"] = value. 
This mirrors what happens in a CRM when you enrich a contact — you add new fields or update existing ones.
GTM pattern: You pull a raw contact from HubSpot (no enrichment), run it through Clearbit to get company data,
 then add the enriched fields to the dictionary before writing it back. 
 This add-then-update pattern is everywhere in GTM pipelines."""
contact = {"email": "alice@gmail.com", "Score":85}
contact["Stage"] = "MQL"
contact["company"] = "google"
contact["enriched"] = True
print(contact)
del contact["company"]

""".keys(), .values(), .items() — Looping Over a Dict
Dict Views
Three methods let you see all keys, all values, or both at once as key-value pairs.
These three methods return views of the dictionary — live snapshots you can iterate over. .items() is the most useful — it gives you both the key and value together, 
which is how you loop over a dictionary to build reports or process fields. You will use .items() constantly from Day 5 onwards."""
contact = { "email": "alice@techcorp.com", "score": 85, "stage": "MQL", "company": "TechCorp" }
print(contact.keys())
print(contact.values())
print(contact.items())
print("score" in contact)
print("phone" in contact)
print("phone" in contact.keys())
"""
Method	                 Returns	                                              GTM Use Case
.keys()	                 All key names	                                     Check which fields a contact has before processing
.values()	               All values	                                         Collect all scores from a contact for averaging
.items()	               Key-value pairs	                                   Loop over every field to print a contact report
.get(k, d)	             Value or default	                                   Safe field access when fields may be missing
.update(d)	             Merges another dict in	                             Merge enrichment data into a base contact record
"k" in d	               True/False	                                         Check if a field exists before accessing it
"""

"""Nested Dictionaries — A Dict Inside a Dict
Nested Structure
A dictionary value can itself be a dictionary. This is how real API responses are structured.
Real-world data is never flat. A HubSpot contact doesn't just have an email — it has a company with its own fields (name, size, industry, domain). 
A deal has an associated contact which has its own fields. These nested relationships are represented as dictionaries inside dictionaries.
You access them by chaining keys: contact["company"]["name"]. GTM API reality: HubSpot's API returns contacts like: {"id": "123", "properties": {"email": "alice@...", "score": "85"}}.
The actual fields are nested inside a "properties" dictionary. You'll navigate this exact structure on Day 15 when you call real APIs."""
contact = { "email": "alice@techcorp.com", "score": 85, "stage": "MQL", "company": {"name": "TechCorp", "employees": 450, "industry": "SaaS", "mrr": 42000.0 } }
print(contact["company"])
print(contact["company"]["name"])
revenue = contact.get("company",{}).get("mrr",0)
print(revenue)
hubspot_contact = { "id": "123456", "properties": { "email": "alice@techcorp.com", "score": "85","lifecyclestage": "marketingqualifiedlead" } }
email = hubspot_contact["properties"]["email"]
score = int(hubspot_contact["properties"]["score"])
print(f"ID: {hubspot_contact['id']}, Email: {email}, Score: {score}")
"""List of Dictionaries — The Shape of Real GTM Data
The Real Data Shape
A list of dictionaries is a list where every item is a dictionary. This is how APIs return multiple records.
This is the most important data structure in GTM engineering. A HubSpot API call for 100 contacts returns a list of 100 dictionaries. A database query returns a list of dictionaries (one per row). A CSV loaded with pandas gives you a list of dictionaries. If you master one structure, master this one.
This is the Day 2 upgrade: Yesterday you had leads[0][1] to get a score. Today you write leads[0]["score"]. Same idea, but now every field has a name instead of a position number. This is how all real GTM data looks."""
leads = [ {"email": "alice@techcorp.com", "score": 85, "stage": "MQL", "is_enterprise": True}, {"email": "bob@startup.io", "score": 42, "stage": "Lead", "is_enterprise": False}, {"email": "carol@enterprise.co.uk", "score": 91, "stage": "SQL", "is_enterprise": True}, {"email": "dave@scaleup.com", "score": 67, "stage": "MQL", "is_enterprise": False}, ]
print(leads[0])
print(leads[0]["email"])
print(leads[0]["score"])
print(leads[2]["stage"])
print(leads[-1]["is_enterprise"])
print(f"Total leads: {len(leads)}")
""".update() — Merging Data Into a Dictionary
Data Enrichment Pattern
dict.update(another_dict) merges all key-value pairs from another dict in. Existing keys are overwritten.
This is the Python equivalent of enriching a CRM record. You start with base contact data from HubSpot, then enrich it with company data from Clearbit, then add scoring fields from your own model. Each enrichment step is a .update() call that merges new fields into the contact dictionary.
GTM pipeline pattern: Pull contact → enrich with firmographic data → add scoring → update CRM. Each arrow is a .update()."""
contact = { "email": "alice@techcorp.com", "score": 85 }
clearbit_data = { "company": "TechCorp", "employees": 450, "industry": "SaaS", "country": "UK" }
contact.update(clearbit_data)
scoring_data = { "score": 92, "is_icp": True, "routing_queue": "enterprise" }
contact.update(scoring_data)
print(contact["score"])

"""A script that builds a list of contact dictionaries, enriches them, and prints a formatted CRM report.
This script is the Day 2 lead processor — completely rewritten using dictionaries instead of lists of lists. Compare them side by side: the logic is identical, but the dictionary version is dramatically more readable. Every field has a name. Every value is clear. This is what production GTM scripts look like."""
contacts = [ { "email": "alice@techcorp.com", "score": 85, "stage": "MQL", "is_enterprise": True, "company": {"name": "TechCorp", "employees": 450, "mrr": 42000} }, { "email": "bob@startup.io", "score": 42, "stage": "Lead", "is_enterprise": False, "company": {"name": "StartupIO", "employees": 12, "mrr": 800} }, { "email": "carol@enterprise.co.uk", "score": 91, "stage": "SQL", "is_enterprise": True, "company": {"name": "EnterpriseCo", "employees": 2100, "mrr": 95000} }, { "email": "dave@scaleup.com", "score": 67, "stage": "MQL", "is_enterprise": False, "company": {"name": "ScaleUp", "employees": 85, "mrr": 6200} }, { "email": "eve@bigco.com", "score": 78, "stage": "MQL", "is_enterprise": True, "company": {"name": "BigCo", "employees": 900, "mrr": 28000} }, ]
contacts[0].update({"routing": "enterprise-ae", "gdpr_ok": True})
contacts[1].update({"routing": "sdr-outbound", "gdpr_ok": False})
contacts[2].update({"routing": "enterprise-ae", "gdpr_ok": True})
contacts[3].update({"routing": "sdr-outbound", "gdpr_ok": True})
contacts[4].update({"routing": "enterprise-ae", "gdpr_ok": True})
total = len(contacts) 
scores = [c["score"] for c in contacts]
avg_score = sum(scores) / len(scores) 
top_contact = contacts[0]
last_contact = contacts[-1]
top_company = top_contact.get("company", {}).get("name", "Unknown")
top_mrr = top_contact.get("company", {}).get("mrr", 0)
top_routing = top_contact.get("routing", "unassigned")
print()
print("━" * 55)
print(" CRM CONTACT PROCESSOR REPORT")
print(f" Total contacts: {total}")
print(f" Average score: {avg_score:.1f}")
print("━" * 55)
print(" CONTACT DETAILS")
print(f" First contact email: {top_contact['email']}")
print(f" Company: {top_company}")
print(f" Company MRR: £{top_mrr:,}")
print(f" Score: {top_contact['score']}")
print(f" Stage: {top_contact['stage']}")
print(f" Enterprise: {top_contact['is_enterprise']}")
print(f" Routed to: {top_routing}")
print("━" * 55)
print(" GDPR SAFETY")
print(f" Bob GDPR ok? {contacts[1].get('gdpr_ok', False)}")
print(f" Alice GDPR ok? {contacts[0].get('gdpr_ok', False)}")
print("━" * 55)
print(" KEYS IN FIRST CONTACT")
print(f" {list(contacts[0].keys())}")
print("━" * 55)
