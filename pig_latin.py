#!/usr/bin/env python3
#
# Created by Marcus A. Mosley
# Created on December 2020
# This program translates text into Pig Latin


def translator(word_list):
    # This function translates text into Pig Latin

    latin_list = []
    counter = 0
    length = len(word_list)
    while counter < length:
        temp_string = word_list[counter]
        if (temp_string[0] == 'a' or temp_string[0] == 'e' or
                temp_string[0] == 'i' or temp_string[0] == 'o' or
                temp_string[0] == 'u'):
            temp_string = temp_string + "yay"
        else:
            temp_string = temp_string + temp_string[0] + "ay"
            temp_string = temp_string[1:]
        counter += 1
        latin_list.append(temp_string)
    pig_latin = ' '.join(latin_list)
    pig_latin = pig_latin.capitalize()

    return pig_latin


def main():
    # This function receives input

    word_list = []

    # Input
    string = input("Enter the text that is to be translated: ")
    string = string.lower()
    word_list = string.split()
    print(" ")

    # Call Functions
    pig_latin = translator(word_list)

    print(pig_latin)


if __name__ == "__main__":
    main()
