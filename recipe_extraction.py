# Author: Alyssa Feger
# Writing 

import re

# Function that helps to extract all recipes into dictionaries and inputs them as dictionary strings into a txt file
def extraction():
    recipes_csv = open("recipe_csv.txt", "a")  # File to put recipe dictionaries into
    recipes_txt = open("recipes.txt")  # File that has all of the recipe code in it (now as text)
    line_index = 0  # Indicates what line to start at when using extraction_helper

    #random_count = 0  # Used to debug
    recipes_list = recipes_txt.readlines()
    recipe_regex = r"crafting"  # To find what line to start reading recipes from

    for line in recipes_list:
        crafting = re.search(recipe_regex, line)  # Returns None if line does not have crafting in it, returns match object if it does
        if crafting != None:
            recipes_dict = extraction_helper(recipes_list, {}, line_index)  # Actually creating dictionaries
            recipes_csv.write(f"'{recipes_dict}'\n")


            # All used to debug 
            #if len(recipes_dict.keys()) > 3:
                #random_count += 1
                #print(f"{recipes_dict}\n")

        line_index += 1  # Incrementing each time


    recipes_csv.close()
    recipes_txt.close()
            




# Function that actually makes the dictionaries of the recipes
# Parameters: the file to read from, empty dictionary to put recipes in, line_num to start at
# Returns: Dictionary of recipes; first key and value is what is crafted, rest is the recipe
def extraction_helper(recipes_txt: str, recipes_dict: dict[str, str], line_num: int) -> dict[str, str]:
    line_regex = r"count"
    exclude_regex = r'"{count:|,id:\"|\"|\n}"'
    end_regex = "stack_limit"
    component_regex = "minecraft:trim"

    for line in recipes_txt[line_num:]:
        count_line = re.search(line_regex, line)  # Checking where an item in recipe is found
        end_line = re.search(end_regex, line)  # Checking where to end for loop
        component_check = re.search(component_regex, line)  # This was to relieve me of the stress of trims and their stupidness

        if component_check != None:
            pass
        elif count_line != None:
            line_split = re.split(exclude_regex, line)  # Splits line on the things that are in the exclude_regex


            # Except re.split() didn't work as I intended so II improvised - line_split would return string with unneccessary characters
            count_num = line_split[1]
            id_string = line_split[2]

            count_num_len = len(count_num)
            id_string_len = len(id_string)

            count_num2 = count_num[:count_num_len - 5]
            id_string2 = id_string[:id_string_len - 1]

            # All of above got rid of unneccessary characters at beginning and end of the items in the list line_split


            if id_string2 in recipes_dict.keys():  # Checks if item is already in keys so it can add to it's value - messed up on those with like five million recipes
                upgraded_num = int(recipes_dict[id_string2]) + int(count_num2)
                recipes_dict[id_string2] = str(upgraded_num)
            else:
                recipes_dict[id_string2] = count_num2  # Adds item and it's value to the dictionary

        elif end_line != None:  # Ends for loop when "stack_limit" is found in the line
            break


    return recipes_dict
                

