from .dv_utils import (
    Schema, 
    MetadataPipeline,
    Yaml_metadata,
    Envs,
    Path_handler
)

def get_env_entities():
    # Lista nomes das tabelas do projeto
    TABLES = Envs('TABLES').load_env()
    # Define o caminho raiz do projeto
    ROOT = Envs('ROOT').load_env()
    # Define o caminho do arquivo do dicionario yaml
    YAML_METADATA = Envs('YAML_METADATA').load_env()
    # Define o caminho do arquivo do dicionario yaml
    BRONZE = Envs('BRONZE').load_env()
    # Define o caminho do arquivo do dicionario yaml
    SILVER = Envs('SILVER').load_env()
    return {
        'TABLES':TABLES,
        'ROOT':ROOT,
        'YAML_METADATA':YAML_METADATA,
        'BRONZE':BRONZE,
        'SILVER':SILVER}

# define o dicionario yaml
def get_metadata(filename:str,yamlmetada:dict):
    entity_metadata = Yaml_metadata(
        Path_handler(yamlmetada)
        .build(filename)
        ).read_yaml()
    return entity_metadata


