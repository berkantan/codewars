def open_or_senior(data):
    output=[]
    for i,j in data:
            if i >= 55 and j >= 7:
                output.append('Senior')
            else:
                output.append('Open')
    return output