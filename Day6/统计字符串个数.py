def character_number(character):
    char_count = {}
    for char in character:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

input_string = input("请输入字符串")
request = character_number(input_string)
print(request)