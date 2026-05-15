"""
Fraud Detection in Banking
Action:
    A credit card company processes billions of transactions.
Inference:
    When a transaction occurs, the engine compares it against user behavior patterns
    (time, location, amount).
Outcome:
    If card belongs to one country(user_country) and user is making purchase in other country(sale_country),
    abort transaction.
    However, if user_country and sale_country belongs to eu, allow transaction
    If user_country and sale_country are same, allow transaction

"""

# FACTS
db = {
    "countries": ["US", "UK", "INDIA", "GERMANY", "SPAIN", "SUDAN", "AUSTRALIA"],
    "eu": ["UK", "GERMANY", "SPAIN"],
}


# RULE 1 : Check If country-1 and country-2 are valid
def rule_are_valid_countries(country1, country2):
    countries = db.get("countries")
    result = country1 in countries and country2 in countries
    return result


# RULE 2 : If both countries are same, allow purchase
def rule_are_countries_same(country1, country2):
    result = False
    if country1 == country2:
        result = True
    print(f"Calling rule_are_countries_same for {country1},{country2}: {result}")
    return result


# RULE 3: If both countries are EU countries , allow purchase
def rule_are_eu_countries(country1, country2):
    eu = db.get("eu")
    result = country1 in eu and country2 in eu
    print(f"Calling rule_are_eu_countries for {country1},{country2}: {result}")
    return result


# RULE 4: OR of RULE2 and RULE3 : i.e. Either Countries are same or both countries are in EU
def rule_are_same_or_eu(country1, country2):
    return rule_are_countries_same(
        country1=country1, country2=country2
    ) or rule_are_eu_countries(country1=country1, country2=country2)


'''
RULE 1 and RULE 4 only, (If it is a valid country then check for other conditions) 
RULE 4 is OR of RULE 2 and RULE 3
'''
rules = [rule_are_valid_countries, rule_are_same_or_eu]
def infer(user_country, sale_country):
    for rule in rules:
        if rule(user_country, sale_country) == False:
            return False
    return True


# Run Inference
print("Starting Inference...")
user_country = "UK"
sale_country = "GERMANY"
result = infer(user_country=user_country, sale_country=sale_country)
print(f"Final Facts for ({user_country},{sale_country}): {result}")
