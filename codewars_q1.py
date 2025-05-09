def open_or_senior(data):
    output = []
    for i,j in data:
        if i >= 55 and j >= 7:
            output.append('Senior')
        else:
            output.append('Open')
    print(output)
    

data = [(45, 12),(55,21),(19, -2),(104, 20)]
result = open_or_senior(data)
print(result)