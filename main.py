parts = input().split()
name = parts[0]
while name != '-1':
    try:
        age = int(parts[1]) + 1
        print(f'{name} {age}')
    except ValueError:
        age = 0
        print(f'{name} {age}')
    # Get next line
    parts = input().split()
    name = parts[0]

