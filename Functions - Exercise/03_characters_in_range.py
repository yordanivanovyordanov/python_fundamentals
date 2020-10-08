# CHARACTERS IN RANGE
# Write a function that receives two characters and returns a single string with all the characters
# in between them according to the ASCII code.

# SOLUTION
char_1 = input()
char_2 = input()


def characters_in_range(character_1, character_2):
    start = ord(character_1)
    end = ord(character_2)

    for char in range(start + 1, end):
        if not char == end - 1:
            print(chr(char), end=" ")
        else:
            print(chr(char))


characters_in_range(char_1, char_2)
