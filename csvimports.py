# Author: Alyssa Feger


def turn_into_csv():
    '''
    Function that puts the information in the dictionaries in recipe_csv.txt in csv (not true it's a tsv just cause it's a bit easier to work with in this case)
    so it can be later used for the extraction of raw materials function
    '''

    recipe_csvtxt = open("recipe_csv.txt")
    recipe_tsv = open("recipes.tsv", 'a')  # tsv that all recipe information will be stored in

    title = "Craftable\tCount\tRecipe\n"  # title of tsv
    recipe_tsv.write(title)
    #line_num = 1


    for line in recipe_csvtxt:
        index = 0
        new_string = ''  # String to be concatenate all recipe informatino
        materials_str = ""  # String to concatenate all the recipe materials


        # Dictionaries in recipe_csv are all strings so they need to be converted into dictionaries again

        new_line = new_line.strip("{}")  # Gets rid of the {} at beginning and end of strings
        new_line = new_line.replace("'", "")  # Gets rid of unneccessary quotations
        new_dict = dict(item.split(': ') for item in new_line.split(", "))  # Compiles line into dictionary
        


        # Now we get to the big guns
        for key in new_dict.keys():
            if index == 0:  # First key in new_dict is the craftable item
                craftable_string = f"{key}\t{new_dict[key]}\t"  # Separates item name and how many can be crafted by tab characters so they are in separate columns
                index += 1
                new_string = new_string + craftable_string  # Adding craftable_string to new_string to concatenate it with rest of materials

            else:
                materials = f"{new_dict[key]} {key}, "
                new_string = new_string + materials  # Note: Materials are not separated by tab character because they all must be in same column


        new_string = new_string[:-2]  # Getting rid of the ", " at end of new_string 
        new_string = new_string + "\n"
        recipe_tsv.write(new_string)  # Writes all the information into the tsv



    recipe_csvtxt.close()


# Adds raw materials to tsv
def add_raw_materials():
    recipe_raw = open("raw_materials.txt")
    recipe_tsv = open("recipes.tsv", 'a')

    for line in recipe_raw:
        line_split = line.split()
        line_join = "_".join(line_split)
        minecraft_data = "minecraft:" + line_join

        recipe = f"{minecraft_data}\t1\t0\n"

        recipe_tsv.write(recipe)
