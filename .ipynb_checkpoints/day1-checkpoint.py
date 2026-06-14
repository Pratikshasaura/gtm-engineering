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
mrr = 8500.00
conversion_rate = 0.23
avg_deal_value = 12400.75
ltv_cac_ratio = 3.5 # LTV:CAC — healthy is above 3; Float arithmetic — THE core GTM calculation
arr = mrr * 12
print(f"MRR: £{mrr}") 
print(f"ARR: £{arr}")
messy_result = 102000.000000001
clean_result = round(arr, 2)
print(f"Clean ARR: £{clean_result}")

#booleans
"""A boolean holds exactly one of two values: True or False. Capital T and F.
Booleans are on/off switches. They answer yes/no questions. In Python they must be capitalised: True and False. They're the result of any comparison — "is this lead's score above 70?" returns True or False. This is how Python makes decisions.
GTM examples: is_enterprise (True/False), is_gdpr_compliant (True/False), has_been_contacted (True/False), is_duplicate (True/False). Boolean fields are common in CRMs and in data quality checks."""
is_enterprise = True 
has_been_contacted = False 
is_gdpr_compliant = True 
is_duplicate = False
lead_score = 85 
is_hot_lead = lead_score > 70
is_cold_lead = lead_score < 30
print(is_hot_lead)
print(is_cold_lead)
mrr = 8500 
healthy_arr = (mrr * 12) > 50000
print(f"Is ARR healthy? {healthy_arr}")

#input() — Accept Data from the User
"""input() pauses the script and waits for the user to type something. Always returns a string.
input() lets you build interactive scripts — instead of hardcoding values, the user can type them in when the script runs. Critical rule: input() ALWAYS returns a string, no matter what the user types. If they type 8500, Python receives the string "8500" not the number 8500. You must convert it.
GTM use case: A quick interactive calculator you run at the start of a sales meeting: "Enter this month's MRR" → script calculates ARR, pipeline coverage, CAC payback live. This is exactly what you'll build today."""
company_name = input("Enter company name: ")
print(f"Company: {company_name}")
mrr_input = input("Enter MRR (£): ")
mrr = float(mrr_input)
arr = mrr * 12 
print(f"Your ARR is: £{arr:,.2f}")
mrr = float(input("Enter MRR (£): "))

#Putting It Together — The ARR Calculator Script
"""A GTM revenue calculator using every concept from today."""
company_name = input("Enter company name: ")
rep_name = input("entre sales rep name: ")
mrr= float(input("entre Monthly recurring revenue($): "))
Monthly_churn = float(input("Enter monthly churn: "))
cac = float(input("entre monthly cac: "))
arr=mrr*12
net_mrr = mrr*(1-Monthly_churn)
ltv = (mrr/Monthly_churn)
ltv_cac_ratio= ltv/cac
cac_payback_mo = cac/mrr
is_arr_healthy = arr>100000
is_ltv_cac_good = ltv_cac_ratio>=3
is_churn_low = Monthly_churn<0.03
print() 
print("=" * 45) 
print(f" GTM REVENUE REPORT — {company_name.upper()}")
print(f"CAC: £{cac:>10,.2f}")
print(f" LTV:CAC Ratio: {ltv_cac_ratio:>10.1f}x")
print(f" CAC Payback: {cac_payback_mo:>9.1f} months") 
print("=" * 45) 
print(f" ARR Healthy (>£100k)? {is_arr_healthy}") 
print(f" LTV:CAC Good (>=3x)? {is_ltv_cac_good}") 
print(f" Churn Low (<3%/mo)? {is_churn_low}") 
print("=" * 45)



