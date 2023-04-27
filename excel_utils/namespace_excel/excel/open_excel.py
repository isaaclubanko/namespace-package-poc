import pandas as pd

def concat_excel(file_name):
    df = pd.concat(
            pd.read_excel(
                file_name,
                sheet_name=None,
                engine='openpyxl'
            ), 
            ignore_index=True
        )
    
def dict_to_dataframe(dict, keys=[]):
    df = pd.DataFrame(dict)
    if keys:
        return df[keys]
    return df
