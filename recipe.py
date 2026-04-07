#this is where i'm gonna write these stupid ass functions
# Prepare for the worst explanations eve

def transform_list(change: list[str]) -> dict[str, int]:
    change_dict = {} # Dictionary to return
    
    for string in change:
        materails = string.split()  # splits string into both the number assigned to materials and the material
        num = materails[0]
        materials = materails[1:] # If more than one word takes list of rest of words then joins them together with _
        string = "_".join(materials)

        string = "minecraft:" + string.lower()  # Adding minecraft to material name because that's the thingy in the thingy
        change_dict[string] = int(num)

    return change_dict


def trans_string(change: dict[str, int]):
    change_str = ""
    for mat in change.keys():
        material = mat[9:]
        string = f"{change[mat]} {material} "
        change_str = change_str + string

    change_str = change_str[:-1]

    return change_str



    