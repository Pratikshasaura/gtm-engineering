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
