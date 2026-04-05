# Author: Alyssa Feger
from recipe_extraction import extraction
from csvimport import check_keys
from csvimports import turn_into_csv, add_raw_materials
from recipe.py import raw_materials
import re


def main():
    #extraction()
    #check_keys("recipe_csv.txt")
    #turn_into_csv()
    #add_raw_materials()
    raw_materials(["4 cartography table"])
    x =  0
    #print(type(x), x)



if __name__ == "__main__":
    main()