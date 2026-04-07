# Author: Alyssa Feger
from recipe_extraction import extraction
from csvimport import check_keys
from csvimports import turn_into_csv, add_raw_materials, add_concrete
import re


def main():
    #extraction()
    #check_keys("recipe_csv.txt")
    #turn_into_csv()
    #add_raw_materials()
    #raw_materials(["4 cartography table"])
    x =  0
    #print(type(x), x)
    add_concrete()



if __name__ == "__main__":
    main()