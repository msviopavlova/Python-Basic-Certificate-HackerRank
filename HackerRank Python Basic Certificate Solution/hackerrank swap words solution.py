def reverse_my_sentence(sentence):

    new_list = list(sentence.split())
    reversed_list = []
    reversed_list.append(new_list[::-1])
    reversed_string = ""
    for inner_list in reversed_list:
        for word in inner_list:
            reversed_string+=word
            reversed_string+=" "

    ready_string = ""
    for char in reversed_string:
        if char.islower():
            ready_string+=char.upper()
        elif char.isupper():
            ready_string+=char.lower()
        elif char == " ":
            ready_string+= " "

    return ready_string

print(reverse_my_sentence(sentence="HeLlO How aRe yOu"))





