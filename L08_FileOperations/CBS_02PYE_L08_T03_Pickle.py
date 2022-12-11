import json
import pickle

products = """{
    "items": {
        "4857650475": {
            "manufacturer": "apple",
            "vendor code": "MLK03",
            "model": "iphone 13 mini",
            "color": "midnight",
            "built-in memory": "128"
        },
        "3559660371": {
            "manufacturer": "apple",
            "vendor code": "MJQG3",
            "model": "iphone 13 mini",
            "color": "purple",
            "built-in memory": "128"
        },
        "2523655384": {
            "manufacturer": "apple",
            "vendor code": "MPVN3",
            "model": "iphone 14",
            "color": "blue",
            "built-in memory": "128"
        }
    }
}"""

n = pickle.dumps(products)
print(n)

with open('CBS_02PYE_L08_T03_Pickle.txt', 'wb') as file_to_write:
    pickle.dump(products, file_to_write)

with open('CBS_02PYE_L08_T03_Pickle.txt', 'rb') as file_to_read:
    items = pickle.load(file_to_read)

print(items)
print(type(items))

data = json.loads(items)
with open('CBS_02PYE_L08_T03_Pickle.json', 'w', encoding='utf-8') as json_to_write:
    json.dump(data, json_to_write, indent=4)
