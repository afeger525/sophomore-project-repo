# Author: Alyssa Feger

def turn_into_csv():
    recipe_csvtxt = open("recipe_csv.txt")
    recipe_tsv = open("recipes.tsv", 'a')

    title = "Craftable\tCount\tRecipe\n"
    recipe_tsv.write(title)
    random_count = 0
    line_num = 1

    for line in recipe_csvtxt:
        index = 0
        new_string = ''
        materials_str = ""
        
        print(line_num)
        line_length = len(line)
        new_line = line[1:line_length - 2]


        new_line = new_line.strip("{}")
        new_line = new_line.replace("'", "")
        print(f"line before: {new_line}")
        new_dict = dict(item.split(': ') for item in new_line.split(", "))
        
        print(type(new_dict), new_dict)

        line_num += 1

        for key in new_dict.keys():
            if index == 0:
                craftable_string = f"{key}\t{new_dict[key]}\t"
                index += 1
                new_string = new_string + craftable_string

            else:
                materials = f"{new_dict[key]} {key}, "
                new_string = new_string + materials


        new_string = new_string[:-2]
        new_string = new_string + "\n"
        recipe_tsv.write(new_string)



    recipe_csvtxt.close()
