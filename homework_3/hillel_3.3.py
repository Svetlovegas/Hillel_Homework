friends = ["John", "Marta", "James"]
enemies = ["John", "Jonatan", "Artur"]

for friend in friends:
    if friend == 'James':
        continue
    elif friend not in enemies:
        print(f'{friend} we are the best friends.')
    else:
        print(f'{friend} we are not the friends anymore.')
