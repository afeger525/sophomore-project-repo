# Author: Alyssa Feger

import ast 
import re

def check_keys(recipes_filename: str):
    recipes_txt = open(recipes_filename)
    random_count = 0
    index = 0
    for line in recipes_txt:
        line2 = line.strip("{}")
        recipes_dict = dict(item.split(": ") for item in line2.split(", "))
                
        '''
        concrete_regex = r"concrete"
        bed_regex = r"bed"
        piston_regex = r"piston"
        copper_regex = r"copper"
        rabbit_regex = r"rabbit"

    
        concrete_line = re.search(concrete_regex, line)
        bed_line = re.search(bed_regex, line)
        piston_line = re.search(piston_regex, line)
        copper_line = re.search(copper_regex, line)
        rabbit_line = re.search(rabbit_regex, line)

        '''

        key = list(recipes_dict.keys())[0]
        integer = (recipes_dict[key])[1]
        if int(integer) >= 10:
            print(f"{recipes_dict}\n")
            random_count += 1

        """"
        if len(recipes_dict.keys()) > 4:
            if concrete_line is None and bed_line is None and piston_line is None and copper_line is None and rabbit_line is None:
                random_count += 1
                print(f"{recipes_dict}\n")
        """

        index += 1
        #print(index)

    recipes_txt.close()
    print(f"{random_count}\n")