import random
import uuid
import datetime as dt
from .global_utils import get_date
import pandas as pd
from typing import Callable
from datetime import datetime, timedelta
from .fakedataset_utils.fakedata_shapes import (
    male_names,
    female_names,
    universal_names,
    surnames,
    bairros,
    cidades,
    estados,
    fornecedores,
    produtos,
    servicos,
    operacoes,
    ruas
)

def get_random_gender() -> str:
    return random.choice(['M','F','U'])

def person_name():
    gender = get_random_gender()
    n_names = random.randint(2,4)
    select = {'F':female_names,'M':male_names,'U':universal_names}
    p_name:str = ''
    for name in list(range(n_names - 1) )[:]:
        p_name = p_name +' '+ random.choice(select[gender])
    p_name = p_name.strip()
    p_name = p_name +' '+ random.choice(surnames)
    p_name = p_name.strip()
    return [gender,p_name]

def pessoas_creates_cpf():
    return f'{random.randint(100,900)}.{random.randint(100,900)}.{random.randint(100,900)}-{random.randint(10,99)}'

def pessoas_columns(
        table_name:str='pessoas',
        column_name:str=None,
        apelido:str='cuei'):
    
    assert column_name in [
        'cod_pessoa', 'cpf', 'genero',
        'nome', 'data_nascimento', 'cor_da_pele',
        'data_criacao', 'data_alteracao'] , f'column name: {column_name} não encontrado'
    if column_name not in ['genero','nome']:
        cod_pessoa=uuid.uuid4().hex[:8]
        cpf=pessoas_creates_cpf()

        data_nascimento=get_date('random')	
        cor_da_pele=random.choice(['Branca','Preta','Parda','Amarela'])
        data_criacao=get_date('today')
        data_alteracao=get_date('today')

        col_dict = {
        'cod_pessoa':cod_pessoa,
        'cpf':cpf,

        'data_nascimento':data_nascimento,	
        'cor_da_pele':cor_da_pele,
        'data_criacao':data_criacao,
        'data_alteracao':data_alteracao,
        }

        return col_dict[column_name]
# ---------------------------------------
# Methods that return dataframe as output
# ---------------------------------------
def df_ready_to_use(table_name:str='bairros') :
    df_dict = {'bairros':bairros,
               'cidades':cidades,
               'estados':estados,
               'fornecedores':fornecedores,
               'produtos':produtos['sobremesas'],
               'servicos':servicos['psicologia'],
               'operacoes':operacoes}

    return pd.DataFrame(df_dict[table_name])
def get_calendar(dias, data_inicio, feriados=None):
    # Dias da semana em português
    dias_semana = [
        "segunda-feira", "terça-feira", "quarta-feira",
        "quinta-feira", "sexta-feira", "sábado", "domingo"
    ]
    
    # Feriados nacionais fixos (Brasil)
    feriados_nacionais = {
        "01-01": "Confraternização Universal",
        "04-21": "Tiradentes",
        "05-01": "Dia do Trabalhador",
        "09-07": "Independência do Brasil",
        "10-12": "Nossa Senhora Aparecida",
        "11-02": "Finados",
        "11-15": "Proclamação da República",
        "12-25": "Natal"
    }
    
    # Inicializa dicionário de saída
    calendario = {
        "cod_calendario": [],
        "data": [],
        "dia_da_semana": [],
        "feriado": [],
        "data_especial": []
    }
    
    # Converte data inicial
    data_atual = datetime.strptime(data_inicio, "%Y-%m-%d")
    
    for i in range(dias):
        data_str = data_atual.strftime("%Y-%m-%d")
        dia_semana = dias_semana[data_atual.weekday()]
        
        # Verifica feriado nacional
        chave_mes_dia = data_atual.strftime("%m-%d")
        nome_feriado = feriados_nacionais.get(chave_mes_dia, None)
        
        # Verifica datas especiais customizadas
        nome_especial = None
        if feriados:
            nome_especial = feriados.get(data_str, None)
        
        # Preenche estrutura
        calendario["cod_calendario"].append(i + 1)
        calendario["data"].append(data_str)
        calendario["dia_da_semana"].append(dia_semana)
        calendario["feriado"].append(nome_feriado)
        calendario["data_especial"].append(nome_especial)
        
        # Próximo dia
        data_atual += timedelta(days=1)
    
    return pd.DataFrame(calendario)


def contatos_columns(
        table_name:str='contatos',
        column_name:str=None) :
    return None

def operacoes_columns(
        table_name:str='operacoes',
        column_name:str=None) :
    return None

def servicos_columns(
        table_name:str='servicos',
        column_name:str=None) :
    return None

def fornecedores_columns(
        table_name:str='fornecedores',
        column_name:str=None) :
    return None


def get_join_ids(
        bairros_df:pd.DataFrame, 
        cidades_df:pd.DataFrame, 
        estados_df:pd.DataFrame, ) -> pd.DataFrame:

    relation_ids = pd.merge(
        bairros_df,
        cidades_df,
        how='inner',
        on='cod_cidade',
        suffixes=['_bairro','_cidade']
        ).merge(
            estados_df,
            how='inner',
            on='cod_estado',
            suffixes=['_cidade_del','_estado'])[['cod_bairro','cod_cidade','cod_estado']]
    return relation_ids

def get_enderecos(
        fn_Yaml_metadata:Callable,
        fn_Dirs:Callable,
        fn_get_join_ids:Callable,
        table_metadata:dict,
        rows_limit:int=10,
        bairros_df:pd.DataFrame=None, 
        cidades_df:pd.DataFrame=None, 
        estados_df:pd.DataFrame=None):

    # ---------------------------------------------
    # ------ get columns list from yaml -----------
    # ---------------------------------------------
    table = 'enderecos'
    yaml_columns = fn_Yaml_metadata(fn_Dirs(table_metadata).defines(f'{table}.yaml')).read_yaml()[table]['columns'].keys()
    yaml_columns = list(yaml_columns)[:]
    # ---------------------------------------------
    # ------ set dictionary -----------------------
    # ---------------------------------------------
    enderecos_dict:dict[str,list] = {}
    for col in yaml_columns:
        enderecos_dict[col] = []
    # ---------------------------------------------
    # ------ set dictionary -----------------------
    # ---------------------------------------------
    
    for row in range(rows_limit):
        nn = random.randint(1,39)
        cod_bairro,cod_cidade,cod_estado = list(fn_get_join_ids(bairros_df, cidades_df, estados_df).iloc[nn].values)
        cod_endereco = uuid.uuid4().hex[:8]
        cep = f'{random.randint(10,99)}.{random.randint(100,999)}.{random.randint(100,999)}-{random.randint(100,999)}'
        logradouro = random.choice(ruas)
        numero = random.randint(1,1000)
        data_criacao = '2000-01-12'
        data_alteracao = '2000-01-12'

        inner_dict = {'cod_endereco': cod_endereco,
        'cep': cep,
        'logradouro': logradouro,
        'numero': numero,
        'cod_estado': cod_estado,
        'cod_cidade': cod_cidade,
        'cod_bairro': cod_bairro,
        'data_criacao': data_criacao,
        'data_alteracao': data_alteracao}

        for col in yaml_columns[:]:
            enderecos_dict[col].append(inner_dict[col])
    # ---------------------------------------------
    # ------ set dataframe -----------------------
    # ---------------------------------------------
    return pd.DataFrame(enderecos_dict)

def remove_dups_from_series(serie:pd.Series) -> list:
    return random.choice(list(set(serie)))

def get_clientes(
        fn_Yaml_metadata:Callable,
        fn_Dirs:Callable,
        fn_get_join_ids:Callable,
        table_metadata:dict,
        rows_limit:int=10,
        pessoas_df:pd.DataFrame=None,
        enderecos_df:pd.DataFrame=None,
        contatos_df:pd.DataFrame=None
        ):

    # ---------------------------------------------
    # ------ get columns list from yaml -----------
    # ---------------------------------------------
    table = 'clientes'
    yaml_columns = fn_Yaml_metadata(fn_Dirs(table_metadata).defines(f'{table}.yaml')).read_yaml()[table]['columns'].keys()
    yaml_columns = list(yaml_columns)[:]
    # ---------------------------------------------
    # ------ set dictionary -----------------------
    # ---------------------------------------------
    clientes_dict:dict[str,list] = {}
    for col in yaml_columns:
        clientes_dict[col] = []
    # ---------------------------------------------
    # ------ set dictionary -----------------------
    # ---------------------------------------------
    pessoas_df = pd.DataFrame(pessoas_df['pessoas'])
    print(pessoas_df.head(3))
    contatos_df = pd.DataFrame(contatos_df)
    # inner_cod_cliente  = []
    for row in range(rows_limit):
        cod_cliente = remove_dups_from_series(pessoas_df['cod_pessoa'])
        cod_endereco = remove_dups_from_series(enderecos_df['cod_endereco'])
        cod_contato = remove_dups_from_series(contatos_df['cod_contato'])

        data_primeira_compra = get_date('random')
        data_criacao = get_date('today')
        data_alteracao = get_date('today')

        inner_dict = {
            'cod_cliente':cod_cliente,
            'cod_endereco':cod_endereco,
            'cod_contato':cod_contato,		
            'data_primeira_compra':data_primeira_compra,
            'data_criacao':data_criacao,
            'data_alteracao':data_alteracao}

        for col in yaml_columns[:]:
            clientes_dict[col].append(inner_dict[col])
    # ---------------------------------------------
    # ------ set dataframe -----------------------
    # ---------------------------------------------
    clientes_dataframe = pd.DataFrame(clientes_dict)
    clientes_dataframe = clientes_dataframe.drop_duplicates(subset=['cod_cliente'],keep='first')
    return clientes_dataframe

def get_transacoes(
        fn_Yaml_metadata:Callable,
        fn_Dirs:Callable,
        fn_get_join_ids:Callable,
        table_metadata:dict,
        rows_limit:int=10,
        clientes_df:pd.DataFrame=None,
        operacoes_df:pd.DataFrame=None,
        produtos_df:pd.DataFrame=None
        ):

    # ---------------------------------------------
    # ------ get columns list from yaml -----------
    # ---------------------------------------------
    table = 'transacoes'
    yaml_columns = fn_Yaml_metadata(fn_Dirs(table_metadata).defines(f'{table}.yaml')).read_yaml()[table]['columns'].keys()
    yaml_columns = list(yaml_columns)[:]
    # ---------------------------------------------
    # ------ set dictionary -----------------------
    # ---------------------------------------------
    transacoes_dict:dict[str,list] = {}
    for col in yaml_columns:
        transacoes_dict[col] = []
    # ---------------------------------------------
    # ------ set dictionary -----------------------
    # ---------------------------------------------
    # pessoas_df = pessoas_df
    # contatos_df = pd.DataFrame(contatos_df)
    for row in range(rows_limit):

        inner_dict = {
    'cod_transacao':uuid.uuid4().hex[:8],
    'cod_calendario':random.randint(1,730),
    'cod_operacoes':random.choice(list(operacoes_df['cod_operacao'])),
    'cod_produto':random.choice(list(produtos_df['cod_produto'])),
    'quantidade_produto':random.randint(1,5),
    'cod_cliente':random.choice(list(clientes_df['cod_cliente'])),
    'cod_servico':None,
    'quantidade_servico':None,
    'data_criacao':get_date('today'),
    'data_alteracao':get_date('today')
}

        for col in yaml_columns[:]:
            transacoes_dict[col].append(inner_dict[col])
    # ---------------------------------------------
    # ------ set dataframe -----------------------
    # ---------------------------------------------
    return pd.DataFrame(transacoes_dict)