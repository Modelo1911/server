name = "Guillermo"
print(name)


def say_hello():
    print("Hello")
    print('IM inside')


print("I'm outside")

say_hello()


prices = [4, 8, 12, 3, 5, 9]

prices.append(9)

print(prices)

total = 0
for price in prices:
    total += price

print(total)

me = {
    "name": "Guillermo",
    "age": "25",
    "hobbies": [],
    "address": {
        "street": "Mariposa",
        "city": "Huston",
    }
}

print(me)

print(me["name"])

if "last" in me:
    print(me["last"])

me["age"] = 99

me["last"] = "escobar"

print("THE END!")