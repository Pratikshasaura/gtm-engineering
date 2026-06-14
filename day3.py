"""if / elif / else — The Decision Tree
The Mental Model
Python reads your conditions top to bottom and runs the first block that is True. Everything else is skipped.
An if statement tests a condition. If it's True, that block runs and all others are skipped. elif (else-if) is tested only if the if was False. else runs when nothing above matched. You can have one if, any number of elifs, and at most one else. The colon : and indentation (4 spaces) are mandatory — Python uses indentation to define what's inside each block.
GTM example: Lead routing. If the lead is enterprise and score > 80 → route to Senior AE. Elif score > 60 → route to Mid-Market AE. Elif score > 30 → route to SDR. Else → mark as unqualified. That is a real lead router — written as if/elif/else."""

score = 85

if score >= 90:
    print("Hot lead — route to Senior AE immediately")
elif score >= 70:
    print("Warm lead — route to Mid-Market AE")
elif score >= 40:
    print("Cool lead — assign to SDR for nurturing")
else:
    print("Cold lead — add to long-term nurture sequence")

print("━" * 55)
temperature = -50

if temperature <=0:
    print("Freezing")
elif temperature <=30:
    print("worm")
elif temperature <= 60:
    print ("Hot")
else:
    print("Feels like I am cooking")

"""Comparison Operators — The Six Ways to Compare
Operators
Six operators that compare two values and return True or False.
Every condition in an if statement uses at least one comparison. These six operators are the building blocks. The one that catches everyone is == vs =: one equals sign assigns a value, two equals signs test equality."""

"""Operator	Meaning	GTM Example	Result
==	Equal to	stage == "MQL"	True if stage is exactly "MQL"
!=	Not equal to	stage != "Closed Lost"	True if stage is anything but "Closed Lost"
>	Greater than	score > 70	True if score is 71 or higher
>=	Greater or equal	score >= 70	True if score is 70 or higher
<	Less than	churn < 0.03	True if churn is below 3%
<=	Less or equal	days_stale <= 14	True if stale for 14 days or fewer"""

"""and / or / not — Combining Conditions
Logical Operators
Combine multiple comparisons into one condition. Real GTM decisions always have multiple criteria.
Single comparisons rarely capture real business logic. A lead isn't hot just because their score is high — they also need to be in your ICP, not already a customer, and not GDPR-blocked. and requires ALL conditions to be True. or requires ANY condition to be True. not flips True to False and False to True.
GTM rule of thumb: Lead qualification criteria use and (must meet ALL criteria). Disqualification/suppression uses or (fail any one criterion → skip). GDPR checks use not."""
contact = {
    "email": "alice@techcorp.com",
    "score": 85,
    "is_enterprise": True,
    "gdpr_ok": True,
    "is_customer": False,
    "employees": 450
}

# and — ALL conditions must be True
is_hot_lead = (
    contact["score"] >= 80
    and contact["is_enterprise"]
    and contact["gdpr_ok"]
)

print(is_hot_lead)

# or — ANY condition True is enough
needs_review = (
    contact["score"] > 90
    or contact["employees"] > 1000
)

print(needs_review)

# not — flips the boolean
safe_to_email = not contact["is_customer"]

print(safe_to_email)

# Real GTM routing decision
if (
    contact["score"] >= 80
    and contact["is_enterprise"]
    and not contact["is_customer"]
):
    routing = "enterprise-ae"
elif (
    contact["score"] >= 50
    and contact["gdpr_ok"]
):
    routing = "mid-market-ae"
else:
    routing = "sdr-nurture"

print(f"Routing: {routing}")

"""Truthy & Falsy — What Counts as True Without ==
Implicit Booleans
In Python, values are "truthy" or "falsy" — you can use them directly in if without comparing to True/False.
Python evaluates almost anything as a boolean when used in a condition. This lets you write clean, readable conditions without redundant comparisons. The falsy values are: False, None, 0, 0.0, "" (empty string), [] (empty list), {} (empty dict). Everything else is truthy.
GTM use: Check if a field has data before using it. if contact.get("phone") is True only if phone has a non-empty value — skips contacts where phone is None or "". This is cleaner than if contact.get("phone") != None and contact.get("phone") != ""."""

# Examples of falsy values

if False:
    print("never runs")

if None:
    print("never runs")  # None is what .get() returns when missing

if 0:
    print("never runs")

if "":
    print("never runs")  # empty string

if []:
    print("never runs")  # empty list

if {}:
    print("never runs")  # empty dict


# GTM pattern: check if a field has a real value

contact = {
    "email": "alice@techcorp.com",
    "phone": "",
    "linkedin": None
}

phone = contact.get("phone")
linkedin = contact.get("linkedin")

if phone:
    print(f"Call: {phone}")
else:
    print("No phone — try email only")  # runs: "" is falsy

if linkedin:
    print(f"LinkedIn: {linkedin}")
else:
    print("No LinkedIn data — skip enrichment")  # runs: None is falsy


# Check if a list has items before processing

hot_leads = []

if hot_leads:
    print("Processing hot leads...")
else:
    print("No hot leads today")

"""Nested Conditionals — Decisions Inside Decisions
Nesting
You can put an if inside another if. Each level is indented 4 more spaces.
Nested conditionals let you make a first decision, then a more specific decision inside it. In GTM routing, you might first check GDPR compliance (outer), then check lead score for routing tier (inner). The rule: never go deeper than 3 levels of nesting — it becomes unreadable. Tomorrow you'll learn functions, which is the clean way to handle complex multi-level logic.
GTM pattern: GDPR gate (outer) → routing tier (inner). Check compliance first. Only if compliant, decide where to route. Never route a non-compliant lead regardless of score."""
contact = {
    "email": "alice@techcorp.com",
    "score": 92,
    "gdpr_ok": True
}

if contact["gdpr_ok"]:
    print("GDPR check passed")

    if contact["score"] >= 90:
        print("Route to Enterprise Sales Team")
    else:
        print("Route to Standard Sales Team")

else:
    print("Do not route lead")

contact = {
    "score": 95,
    "gdpr_ok": True,
    "is_enterprise": True
}

if contact["gdpr_ok"]:

    if contact["is_enterprise"]:

        if contact["score"] >= 90:
            print("Assign to Senior Account Executive")
        else:
            print("Assign to Enterprise SDR")

    else:
        print("Assign to SMB Team")

else:
    print("Reject lead - GDPR not approved")


"""in with Conditionals — List and String Membership
Membership Tests in Conditions
The in operator from Day 2 pairs naturally with if to check suppression lists, ICP tiers, and blocked domains.
You learned in on Day 2 as a standalone boolean check. Today it slots into if conditions. This combination — if email in unsubscribed — is one of the most common GTM patterns you'll write."""


