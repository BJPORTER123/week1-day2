users = {
  "Jonathan": {
    "twitter": "jonnyt",
    "lottery_numbers": [6, 12, 49, 33, 45, 20],
    "home_town": "Stirling",
    "pets": [
    {
      "name": "fluffy",
      "species": "cat"
    },
    {
      "name": "fido",
      "species": "dog"
    },
    {
      "name": "spike",
      "species": "dog"
    }
  ]
  },
  "Erik": {
    "twitter": "eriksf",
    "lottery_numbers": [18, 34, 8, 11, 24],
    "home_town": "Linlithgow",
    "pets": [
    {
      "name": "nemo",
      "species": "fish"
    },
    {
      "name": "kevin",
      "species": "fish"
    },
    {
      "name": "spike",
      "species": "dog"
    },
    {
      "name": "rupert",
      "species": "parrot"
    }
  ]
  },
  "Avril": {
    "twitter": "bridgpally",
    "lottery_numbers": [12, 14, 33, 38, 9, 25],
    "home_town": "Dunbar",
    "pets": [
      {
        "name": "monty",
        "species": "snake"
      }
    ]
  }
}

# 1. Get Jonathan's Twitter handle (i.e. the string `"jonnyt"`)
john_twitterhandle = users["Jonathan"]["twitter"]
# 2. Get Erik's hometown
erik_hometown = users["Erik"]["home_town"]
# 3. Get the list of Erik's lottery numbers
erik_lottery = users["Erik"]["lottery_numbers"]
# 4. Get the species of Avril's pet Monty
avril_species = users["Avril"]["pets"][0]
# 5. Get the smallest of Erik's lottery numbers
smallest_lottery = min(erik_lottery)
# 6. Return an list of Avril's lottery numbers that are even
avril_lottery = users["Avril"]["lottery_numbers"]
for num in avril_lottery:
  if num % 2 == 0:
      print(num)
# 7. Erik is one lottery number short! Add the number `7` to be included in his lottery numbers
avril_lottery.append(7)
# 8. Change Erik's hometown to Edinburgh
users["Erik"]["home_town"] = "edinburgh"
print(users["Erik"]["home_town"])
# 9. Add a pet dog to Erik called "fluffy"
users["Erik"]["pets"].append({"name" : "fluffy", "species" : "dog"})

# 10. Add another person to the users dictionary
users["john"] = {
  "twitter" : "twitter name",
  "lottery number" : 1236734,
  "hometown" : "edinburgh"
}
