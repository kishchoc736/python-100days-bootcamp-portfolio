capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

# Nested List in Dictionary

# travel_log = {
#     "France": ["Paris", "Lille", "Dijon"],
#     "Germany": ["Stuttgart", "Berlin"]
# }
#Pause 1
# print lille
# print(travel_log["France"][1])

nested_list = ["A", "B", ["C", "D"]]

#Pause 2
print(nested_list[2][1])

#Pause 3
travel_log = {
  "France": {
    "cities_visited": ["Paris", "Lille", "Dijon"],
    "total_visits": 12
   },
  "Germany": {
    "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
    "total_visits": 5
   },
}

# Print Stuttgart
print(travel_log["Germany"]["cities_visited"][2])
