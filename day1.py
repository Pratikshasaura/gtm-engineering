#Variable data type
#Variable
# String, int, float, booleadn
#functions Print(), Type(), Input()

#Variable
# GTM example: In a CRM, a contact record holds data like first_name, company, deal_value. 
# Variables in Python work exactly like CRM fields — each one is a named box holding a piece of information.
company_name = "ACME Corp" #str variable
Monthly_revenue = 42000 #Int
deal_value = 8560.50 # decimal which is float
is_enterprise = True #bool
print(company_name)


#String
"""A string is any piece of text. Always wrapped in quotes.
Strings hold text — names, emails, company names, lead sources, pipeline stages. Any value you see as text in a CRM is a string in Python. 
You can use single quotes 'hello' or double quotes "hello" — both work identically. The convention in GTM scripts is double quotes.
GTM example: A lead's email address, their job title, which channel they came from ("Google Ads", "LinkedIn", "Referral") — all strings.
 When you query a CRM API it returns strings for most fields."""
lead_email="alice@techcorp.com"
lead_stage="MQL"
lead_source="Linkedin"
lead_company_name="tech corp"
message=f"lead {lead_email} is at the stage of {lead_stage} from {lead_source}"
print(message)
messy_email= "Alice@techcorp.com"
clean_email= messy_email.strip().lower()
print(clean_email)

#integer

"""An integer is a whole number — no decimal point. No quotes.
Integers are used for counts, whole-number values, and anything that can't be a fraction — number of leads, number of deals, number of employees. 
No quotes around them — the moment you add quotes, Python sees it as text ("42" is not the same as 42).
GTM examples: Number of leads this month, number of open deals, company employee count, days since last activity, lead score (0-100). All are integers."""
lead_thismonth= 50
open_leads = 22
lead_employee_count=500
last_active = 10
lead_score= 78
conversion_rate= lead_thismonth - open_leads
doubled_leads= lead_thismonth *2
half_lead= open_leads//2

print(f"leads: {lead_thismonth} open leads are {open_leads} what is conversion rate {conversion_rate}")

#float decomal number
"""A float is a number with a decimal point. Used for money, percentages, and rates.
Any number that needs precision — money values, percentages, conversion rates, ratios — is a float. Python automatically uses float when you type a decimal. The word "float" comes from "floating point" — referring to the decimal point that can appear anywhere in the number.
GTM examples: Monthly Recurring Revenue (£8,500.00), conversion rate (0.23 = 23%), CAC/LTV ratio (3.5), average deal value (£12,400.75). Anything financial is usually a float."""





