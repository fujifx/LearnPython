import json

# JSON represents data as nested "lists" and "dictionaries"

data = '''{
    "name" : "Chuck",
    "phone" : {
        "type" : "intl",
        "number" : "+1 734 303 4456"
    },
    "email" : {
        "hide" : "yes"
    }
}'''

info = json.loads(data)     # loads stands for Load From String
print('Name: ', info["name"])
print("Hide: ", info["email"]["hide"])

# Slightly complex JSON (which is a list)

comp_data = '''[
    { "id" : "001",
     "x" : "2",
     "name" : "Chuck"
     } ,
     { "id" : "009",
      "x" : "7",
      "name" : "Chuck"     
     }
]'''

info = json.loads(comp_data)
print('User count: ', len(info))
for item in info:
    print('Name:', item['name'])
    print('Id:', item['id'])
    print('Attribute:', item['x'])
