#Creating a dictionary to hold rappers 
rappers = {}

#Creating attributes for each rapper
attributes = {'ig_follows': 96800000, 'feuds': ['Cardi, B', 'Lil Kim', 'Iggy Azalea']}
rappers['Nicki Minaj'] = attributes
rappers['Cardi B'] = {'ig_follows': 38300000, 'feuds': ['Lil Kim', 'Remy Ma', 'Azalea Banks']}
rappers['Lil Kim'] = {'ig_follows': 2400000, 'feuds': ['Foxy Brown', ' Nicki Minaj', 'Remy Ma']}
rappers['Remy Ma'] = {'ig_follows': 6400000, 'feuds': ['Nicki Minaj', 'Lady Luck', 'Lil Kim']}
rappers['Foxy Brown'] = {'ig_follows': 378000, 'feuds': ['Lil Kim', 'Queen Latifah', 'Jackie-O']}
rappers['Azalea Banks'] = {'ig_follows': 615000, 'feuds': ['Angel Haze', 'Iggy Azalea', 'Nicki Minaj', 'Kreayshawn']}
rappers['Iggy Azalea'] = {'ig_follows': 12800000, 'feuds': ['Azalea Banks', 'Nicki Minaj']}
rappers['Khia'] = {'ig_follows': 20600, 'feuds': ['Trina']}
rappers['Trina'] = {'ig_follows': 3100000, 'feuds': ['Khia']}
rappers['Queen Latifah'] = {'ig_follows': 4400000, 'feuds': ['Foxy Brown']}
rappers['Jackie-O'] = {'ig_follows': 17585, 'feuds': ['Foxy Brown']}
rappers['Angel Haze'] = {'ig_follows': 111000, 'feuds': ['Azalea Banks']}
rappers['Kreayshawn'] = {'ig_follows': 308000, 'feuds': ['Azalea Banks']}


#Finds the rapper with the least feuds
max = 1000
for name in rappers:
    user = rappers[name]
    feuds = user['feuds']
    if len(feuds) < max:
        least_feuds = name
        max = len(feuds)

print('The rapper with the least feuds is', least_feuds)
#print(least_feuds, 'has feuds with these rappers', rappers[feuds])

#Finds the rapper with the most feuds
min = 1
for name in rappers:
    user = rappers[name]
    feuds = user['feuds']
    if len(feuds) > min:
        most_feuds = name
        min = len(feuds)

print('The rapper with the most feuds is', most_feuds)
