# Author: Alyssa Feger
# Writing 

import re

def extraction():
    recipes_csv = open("recipe_csv.txt", "a")
    recipes_txt = open("recipes.txt")
    line_index = 0

    random_count = 0
    recipes_list = recipes_txt.readlines()
    recipe_regex = r"crafting"

    for line in recipes_list:
        crafting = re.search(recipe_regex, line)
        if crafting != None:
            recipes_dict = extraction_helper(recipes_list, {}, line_index)
            #recipes_csv.write(f"'{recipes_dict}'\n")
            if len(recipes_dict.keys()) > 3:
                random_count += 1
                print(f"{recipes_dict}\n")

        line_index += 1

    print(random_count)
    recipes_csv.close()
    recipes_txt.close()
            


def extraction_helper(recipes_txt: str, recipes_dict: dict[str, str], line_num) -> dict[str, str]:
    line_regex = r"count"
    exclude_regex = r'"{count:|,id:\"|\"|\n}"'
    end_regex = "stack_limit"
    component_regex = "minecraft:trim"

    for line in recipes_txt[line_num:]:
        count_line = re.search(line_regex, line)
        end_line = re.search(end_regex, line)
        component_check = re.search(component_regex, line)

        if component_check != None:
            pass
        elif count_line != None:
            line_split = re.split(exclude_regex, line)
            #print(line_split)
            #print("\n")
            count_num = line_split[1] 
            id_string = line_split[2]

            count_num_len = len(count_num)
            id_string_len = len(id_string)

            count_num2 = count_num[:count_num_len - 5]
            id_string2 = id_string[:id_string_len - 1]
            #print(count_num2)
            #print(id_string2)

            if id_string2 in recipes_dict.keys():
                upgraded_num = int(recipes_dict[id_string2]) + int(count_num2)
                recipes_dict[id_string2] = str(upgraded_num)
            else:
                recipes_dict[id_string2] = count_num2

        elif end_line != None:
            break


    return recipes_dict
                

