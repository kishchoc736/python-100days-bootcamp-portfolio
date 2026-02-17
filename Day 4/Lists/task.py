states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]
#print the first item
print(states_of_america[0])
#in order to print the last item, do [-1]
print(states_of_america[-1])
# todo: reassign pennsylvania
states_of_america[1]= "pencil"
print(states_of_america[1])

states_of_america.append("Kishoreland")
print(states_of_america[-1])
# extend functions needs another iterable to be added, in this case a list of more countries extends the states of America
states_of_america.extend(["AkshayLand", "RamkumarLand"])
# to print the ;ast 4 items in the list
print(states_of_america[-4:])

