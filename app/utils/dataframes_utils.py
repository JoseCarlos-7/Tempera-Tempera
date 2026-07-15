import pandas as pd
from pathlib import Path

class Dataframes:
    def __init__(self,
                 source:str|Path=None,
                 destination:str|Path=None,
                 sep:str=',',
                 encode:str='utf-8',
                 type:str='csv'):
        self.source = source
        self.destination = destination
        self.sep = sep
        self.encode = encode
        self.type = type

    def read(self):
        type = self.type

        setect_df = {'csv':pd.read_csv(self.source,
                    sep=self.sep,
                    encode=self.encode)}
        
        return setect_df[type]
    
    def write(self,dataframe:pd.DataFrame) -> None:
        type = self.type
        dataframe.to_csv(self.destination,
                         sep=self.sep,
                         encoding=self.encode)
    def writes_for(self,
                   dfs_to_save_dict:dict[str,pd.DataFrame]={}) -> None:
        
        for df in list(dfs_to_save_dict.keys())[:]:
            if type([dfs_to_save_dict[df]]) != pd.DataFrame:
                dfs_to_save_dict[df] = pd.DataFrame(dfs_to_save_dict[df])
            print(f'Salvando {df}:')
            iter_dataframe = dfs_to_save_dict[df]
            self.destination = Path(self.destination,f'{df}.csv')
            
            self.write(iter_dataframe)
            self.destination = Path(self.destination,f'{df}.csv').parents[1]
        
        