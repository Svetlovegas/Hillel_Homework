john = {'full_name': 'John King', 'age': 25, 'salary': 15000,
        'gender': True,'friends': ['Adam', 'Bruno', 'Calvin', 'Dan', 'Edgar'],
        'coordinates': (50.4536, 30.5164)}
dan_friend_john = {'full_name': 'Dan Don', 'age': 30, 'salary': 20000,
        'gender': True,'friends': ['Adam', 'Bruno', 'Calvin', 'Dan', 'Edgar'],
        'coordinates': (50.4536, 30.5164)}
rick_friend_john = {'full_name': 'Rick Wong', 'age': 27, 'salary': 15500,
        'gender': True,'friends': ['Adam', 'Bruno', 'Calvin', 'Dan', 'Edgar'],
        'coordinates': (50.4536, 30.5164)}
marta = {'full_name': 'Marta Kong', 'age': 21, 'salary': 10000,
         'gender': False, 'friends': ['Olivia', 'Emma', 'Sophia', 'Amelia', 'Mia'],
         'coordinates': (50.4536, 30.5164)}
sarah_friend_marta = {'full_name': 'Sarah Connor', 'age': 23, 'salary': 90000,
         'gender': False, 'friends': ['Olivia', 'Emma', 'Sophia', 'Amelia', 'Mia'],
         'coordinates': (50.4536, 30.5164)}
sveta_friend_marta = {'full_name': 'Sveta Bublik', 'age': 22, 'salary': 40000,
         'gender': False, 'friends': ['Olivia', 'Emma', 'Sophia', 'Amelia', 'Mia'],
         'coordinates': (50.4536, 30.5164)}

john['friends'] = (dan_friend_john, rick_friend_john)
marta['friends'] = (sarah_friend_marta, sveta_friend_marta)

for key, value in john.items():
    print(key, value)

for key, value in marta.items():
    print(key, value)