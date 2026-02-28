# Author: Alyssa Feger
from recipe_extraction import extraction
from csvimport import check_keys
from csvimports import turn_into_csv
import re


def main():
    #extraction()
    #check_keys("recipe_csv.txt")
    turn_into_csv()
    x =  0
    #print(type(x), x)



if __name__ == "__main__":
    main()