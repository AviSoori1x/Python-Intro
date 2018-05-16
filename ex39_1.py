states= {
'Western Australia': 'WA',
'South Australia':'SA',
'Australian Capital Territory': 'ACT',
'New South Wales': 'NSW',
'Tazmania': 'TA'
}
cities = {
 'WA' : 'Perth',
 'TA' : 'Hobart',
 'NSW': 'Sydney',
 'ACT' : 'Canberra',
 'SA' : 'Melbourne'
}
cities['NA']='Darwin'
states['Northern Australia']='NA'
print(cities)
print(states)
for state, abbr in list(states.items()):
    print(f"The state {state} has abbreviation {abbr}")
    print(f"{cities[abbr]} is in the state of {state}")
print(list(cities.keys()))
print(sorted(list(cities.keys())))
print('Colombo' in cities)
print('Melbourne' in cities)
us_cities=dict([('New York','NYC'),('Los Angeles','LA'),('Chicago','CHI'),('Charlotte','CH')])
for city, abbr in list(us_cities.items()):
    print(f"{city} has the abbreviation {abbr}")
    print(f"{city} is awesome,")
    print(f"But {abbr} is easier to type, saves ink.")
