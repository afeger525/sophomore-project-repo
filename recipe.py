#this is where i'm gonna write these stupid ass functions
import pandas as pd

def transform_list(change: list[str]):
    change_dict = {}
    for string in change:
        materails = string.split()
        num = materails[0]
        string = materails[1]

        string = "minecraft:" + string
        change_dict[string] = int(num)

    return change_dict



def raw_materials(materials_list: list[str]):
    materials = transform_list(materials_list)
    return raw_materials_helper(materials)


def raw_materials_helper(materials_list: list[str]): #should probably add another parameter
    x = 2