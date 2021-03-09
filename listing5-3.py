planets = { "Mercury": ["The smallest planet, nearest yo the Sun", False, 0],
            "Venus": ["Venus takes 243 days to rotate", False, 0],
            "Earth": ["The only planet known to have native life", False, 1],
            "Mars": ["The second smallest planet", False, 2],
            "Jupiter": ["The largest planet, a gas giant", True, 67],
            "Satern": ["the secound largest planet is a gas giant", True, 62],
            "Uranus": ["An ice giant with a ring system", True, 27],
            "Neptune": ["An ice giant and farthest frome the Sun", True, 14],
            "Pluto": ["Largest dwarf planet in the Solar System", False, 5]
            }

while True:
    query = input("Which planet would you like information on? ")
    if query in planets.keys():
        print(planets[query])
    else:
        print("No data available! Sorry!")