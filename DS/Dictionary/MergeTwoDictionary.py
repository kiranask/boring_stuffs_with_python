countries = {
"contry1": {
"name": "india",
"population": 23213,
"GDP": [1, 2, 3]
},
"contry2": {
"name": "USA",
"population": 3232,
"GDP": [1, 2, 3]
},
"contry3": {
"name": "UK",
"population": 1313,
"GDP": [1, 2, 3]},
"contry4": {
"name": "IRAN",
"population": 9999,
"GDP": [10]}
}

additional_info = {
"contry1": {
"Continent": "XYZ",
"GDP": [1, 100]
},
"contry2": {
"Continent": "ABC",
"GDP": [1, 200]
},
"contry3": {
"Continent": "DFF",
"GDP": [1, 300]}
}




final = {}
#loop over all the keys in dic1
for country in countries.keys():
    #check same keys are there in dic2
    if country in additional_info:
        final[country] = countries[country]
        for ad_info in additional_info[country].keys():
            if ad_info in final[country]:
                common_details=additional_info[country][ad_info]
                print("Common Details", common_details)
                if type(common_details) is list:
                    final[country][ad_info]=list(set(final[country][ad_info]+common_details))

            else:
                final[country].update({ad_info:additional_info[country][ad_info]})
    else:
        final[country] = countries[country]

print(final)

# Common keys set and add
# New keys update.

