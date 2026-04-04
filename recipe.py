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
    recipe_df = pd.read_tsv("recipes.tsv")
    return raw_materials_helper(materials, recipe_df)


def raw_materials_helper(materials_dict: dict[str, int], recipe_df): #should probably add another parameter
    mat_dict: dict[str, int] = {}
    for material in materials_dict.keys():
        thing_dict: dict[str, int] = {}
        materials_mask = recipe_df.loc[:, "Craftable"] == material
        
        if materials_mask.empty:
            print(f"{material} does not exist in recipe list")
        else:
            material_num = materials_dict[material]
            count = int(materials_mask.loc[0, "Count"])
            recipe = materials_mask.loc[0, "Recipe"]

            
            if material_num % count != 0:
                num_count = (material_num // count) + 1
            else:
                num_count = material_num / count

            
            if recipe == "NA":
                return materials_dict
            else:
                recipe_list = recipe.split(",")
                for thing in recipe_list:
                    thing_split = thing.split()
                    mat_count = int(thing_split[0]) * num_count
                    thing_dict[thing] = mat_count

                raw_dict = raw_materials_helper(thing_dict, recipe_df)

                for raw in raw_dict.keys():
                    if raw in mat_dict.keys():
                        mat_dict[raw] = mat_dict[raw] + raw_dict[raw]
                    else:
                        mat_dict[raw] = raw_dict[raw]
                    

            
            
        