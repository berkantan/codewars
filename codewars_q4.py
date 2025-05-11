#QUESTION-4
# Implement the function unique_in_order which takes as argument a sequence and returns a list of items 
# without any elements with the same value next to each other and preserving the original order of elements.

def unique_in_order(sequence):
    new_list = []
    lenght = len(sequence) - 1
    if len(sequence) == 0:
        return new_list
    elif len(sequence) == 1:
        new_list.append(sequence[0])
    else:
        for i in range(0, len(sequence)):
            if i+1 <=  lenght:
                if sequence[i] != sequence[i+1]:
                    new_list.append(sequence[i])

        new_list.append(sequence[lenght])
    return new_list