from lead import leads
entreprise_leads = []
for lead in leads:
    if lead["employees"] >= 500:
        entreprise_leads.append(lead)

print(entreprise_leads)


count = 0

for lead in leads:
    if lead["gdpr_ok"]:
        count += 1

print(count)
