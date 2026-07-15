from app.utils.infra_utils import (
    Envs,
    Dirs)
from app.utils.yaml_utils import Yaml_metadata
from app.utils.create_files import (
    create_file_entities_dict    
)
from app.utils.fakedata_utils import (
    pessoas_columns,
    df_ready_to_use,
    get_calendar,
    get_join_ids,
    get_enderecos,
    get_clientes,
    get_transacoes
)
from app.utils.fakedataset_utils.fakedata_shapes import cria_contatos
from app.utils.dataframes_utils import Dataframes


ROWS = {'contatos':50}
table_metadata = Envs('YAML_METADATA').load_env()
tables = Envs('TABLES').load_env().split(',')
tables.remove('produtos')
tables = ['pessoas']
landing = Envs('LANDING').load_env()


pessoas_df = create_file_entities_dict(
                        Yaml_metadata,
                        Envs,
                        Dirs,
                        pessoas_columns,
                        tables,
                        700)

bairros_df = df_ready_to_use('bairros')
cidades_df = df_ready_to_use('cidades')
estados_df = df_ready_to_use('estados')
servicos_df = df_ready_to_use('servicos')
produtos_df = df_ready_to_use('produtos')
fornecedores_df = df_ready_to_use('fornecedores')
contatos_df = cria_contatos(50)
operacoes_df = df_ready_to_use('operacoes')
calendario_df = get_calendar(730,'2024-07-08')

enderecos_df = get_enderecos(
    Yaml_metadata,
    Dirs,
    get_join_ids,
    table_metadata,
    200,
    bairros_df,
    cidades_df,
    estados_df)


clientes_df = get_clientes(
    Yaml_metadata,
    Dirs,
    get_join_ids,
    table_metadata,
    500,
    pessoas_df,
    enderecos_df,
    contatos_df)

transacoes_df = get_transacoes(
    Yaml_metadata,
    Dirs,
    get_join_ids,
    table_metadata,
    1000,
    clientes_df,
    operacoes_df,
    produtos_df)


# ------------------------------------------------------------------------
# Writting at landing layer
# ------------------------------------------------------------------------
dfs_dict = {
    'pessoas':pessoas_df['pessoas'],
    'bairros':bairros_df,
    'cidades':cidades_df,
    'estados':estados_df,
    'servicos':servicos_df,
    'produtos':produtos_df,
    'fornecedores':fornecedores_df,
    'contatos':contatos_df,
    'operacoes':operacoes_df,
    'calendario':calendario_df,
    'enderecos':enderecos_df,
    'clientes':clientes_df,
    'transacoes':transacoes_df   
    }

Dataframes(destination=landing).writes_for(dfs_dict)





