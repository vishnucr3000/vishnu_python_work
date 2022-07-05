import json

with open("country.json",encoding="utf-8") as stream:
    countrylist=json.load(stream)

# print total number of country detials

number_of_country=len([country for country in countrylist])
print(number_of_country)

# print languages of Ukrane

country_details=[country["languages"] for country in countrylist if country["name"]=="Ukraine"]
for lang in country_details[0]:
    print(lang["name"])


# print currency of China

currency_details=[country["currencies"] for country in countrylist if country["name"].startswith("Palestine")][0]
currency=[currency["name"] for currency in currency_details]

print(currency)

# print population of India

population=[country["population"] for country in countrylist if country["name"]=="India"]
print(population)

# print neibouring of Australia

neibouring=[country["name"] for country in countrylist if country["alpha3Code"] in [country["borders"] for country in countrylist if country["name"]=="Ukraine"][0]]

print(neibouring)
#


print(max(countrylist,key=lambda c:c.get("population"))["name"])

print(min(countrylist,key=lambda m:m.get("population"))["name"])