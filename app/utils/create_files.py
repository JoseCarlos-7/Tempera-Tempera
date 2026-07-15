from typing import Callable
from .fakedata_utils import (
    person_name
    )

def dummy(table_name:str,column_name:str):
    return f'{table_name}-{column_name}'


def create_file_entities_dict(fn_Yaml_metadata:Callable,
                              fn_Envs:Callable,
                              fn_Dirs:Callable,
                              fn_create_random:Callable,
                              tables_list:list,
                              rows_limit:int=5
                              ) -> dict:
    
    dict_:dict[str,dict[str,list]] = {}
    table_metadata = fn_Envs('YAML_METADATA').load_env()
    for table in tables_list:

        yaml = fn_Yaml_metadata(fn_Dirs(table_metadata).defines(f'{table}.yaml')).read_yaml()

        dict_[table] = {}
        n = 1
        for k in list(yaml[table]['columns'].keys())[:]:
            print(f'interação {n}\n table:{table}\n column: {k}')
            dict_[table][k] = []
            # item = fn_create_random(table,k)
            [dict_[table][k].append(fn_create_random(table,k)) for i in range(rows_limit)]
            # del item
            n+=1
    if table == 'pessoas':
        for _ in range(rows_limit):
            gender,name = person_name()
            
            dict_[table]['genero'].append(gender)
            dict_[table]['nome'].append(name)
            dict_[table]['genero'].remove(None)
            dict_[table]['nome'].remove(None)


    return dict_


