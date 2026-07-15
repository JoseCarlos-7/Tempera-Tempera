import random
import uuid
ruas = [
"Rua das Flores","Rua do Sol","Rua da Esperança","Rua das Palmeiras","Rua das Acácias",
"Rua das Oliveiras","Rua dos Pinheiros","Rua das Orquídeas","Rua das Hortênsias","Rua das Violetas",
"Rua dos Lírios","Rua das Rosas","Rua das Tulipas","Rua das Magnólias","Rua dos Cravos",
"Rua das Margaridas","Rua das Azaleias","Rua dos Jasmins","Rua das Begônias","Rua das Camélias",
"Rua do Comércio","Rua da Liberdade","Rua da Paz","Rua da Alegria","Rua da Amizade",
"Rua da Harmonia","Rua da União","Rua da Saudade","Rua da Vitória","Rua da Glória",
"Rua do Progresso","Rua do Futuro","Rua da Felicidade","Rua do Horizonte","Rua do Amanhã",
"Rua Central","Rua Principal","Rua Nova","Rua Velha","Rua Alta",
"Rua Baixa","Rua Larga","Rua Estreita","Rua Direita","Rua Esquerda",
"Rua Norte","Rua Sul","Rua Leste","Rua Oeste","Rua Primeiro de Maio",
"Rua Sete de Setembro","Rua Quinze de Novembro","Rua Tiradentes","Rua Dom Pedro I","Rua Dom Pedro II",
"Rua Santos Dumont","Rua Rui Barbosa","Rua Castro Alves","Rua Machado de Assis","Rua Monteiro Lobato",
"Rua Carlos Gomes","Rua Heitor Villa-Lobos","Rua Anita Garibaldi","Rua Zumbi dos Palmares","Rua Chico Mendes",
"Rua Ayrton Senna","Rua Pelé","Rua Oscar Niemeyer","Rua Paulo Freire","Rua Darcy Ribeiro",
"Rua das Indústrias","Rua das Nações","Rua dos Estados","Rua dos Municípios","Rua das Capitais",
"Rua das Fronteiras","Rua das Colinas","Rua dos Lagos","Rua das Montanhas","Rua dos Rios",
"Rua das Praias","Rua das Ilhas","Rua do Bosque","Rua do Campo","Rua do Vale",
"Rua do Jardim","Rua da Serra","Rua do Planalto","Rua do Sertão","Rua da Floresta",
"Rua do Porto","Rua do Mercado","Rua da Estação","Rua do Aeroporto","Rua do Terminal",
"Rua do Hospital","Rua da Escola","Rua da Igreja","Rua da Prefeitura","Rua do Fórum",
"Rua das Oficinas","Rua dos Trabalhadores","Rua dos Comerciantes","Rua dos Estudantes","Rua dos Professores",
"Rua dos Médicos","Rua dos Engenheiros","Rua dos Advogados","Rua dos Artistas","Rua dos Escritores",
"Rua das Crianças","Rua dos Jovens","Rua dos Idosos","Rua da Família","Rua do Lar",
"Rua da Colônia","Rua do Distrito","Rua da Vila","Rua do Bairro","Rua da Cidade",
"Rua da República","Rua do Império","Rua da Constituição","Rua da Democracia","Rua da Justiça",
"Rua da Igualdade","Rua da Fraternidade","Rua da Solidariedade","Rua da Cidadania","Rua da Cultura",
"Rua da Educação","Rua da Saúde","Rua do Esporte","Rua do Lazer","Rua do Turismo",
"Rua da Tecnologia","Rua da Inovação","Rua da Ciência","Rua da Pesquisa","Rua do Conhecimento",
"Rua das Energias","Rua do Petróleo","Rua do Gás","Rua da Água","Rua do Ar",
"Rua do Fogo","Rua da Terra","Rua dos Ventos","Rua das Chuvas","Rua do Clima",
"Rua do Tempo","Rua da História","Rua da Memória","Rua da Tradição","Rua do Patrimônio",
"Rua das Artes","Rua da Música","Rua do Teatro","Rua do Cinema","Rua da Dança",
"Rua da Fotografia","Rua da Pintura","Rua da Escultura","Rua do Design","Rua da Moda",
"Rua do Ouro","Rua da Prata","Rua do Bronze","Rua do Ferro","Rua do Aço",
"Rua do Cobre","Rua do Alumínio","Rua do Cristal","Rua do Diamante","Rua da Esmeralda",
"Rua do Rubi","Rua da Safira","Rua da Pérola","Rua do Topázio","Rua da Turquesa",
"Rua das Estrelas","Rua da Lua","Rua do Sol Nascente","Rua do Sol Poente","Rua do Eclipse",
"Rua do Universo","Rua da Galáxia","Rua do Cometa","Rua do Planeta","Rua da Constelação"
]

male_names = [
'José','Mário','João','Pedro','Lucas','Gabriel','Rafael','Carlos','Marcos','Paulo',
'Bruno','Eduardo','Felipe','Gustavo','Diego','André','Fernando','Ricardo','Rodrigo','Leandro',
'Vinícius','Thiago','Daniel','Leonardo','Henrique','Matheus','Alexandre','Fábio','Caio','Samuel',
'Igor','Renato','Marcelo','Vitor','Adriano','Jorge','Roberto','César','Danilo','Elias',
'Márcio','Cláudio','Otávio','Cristiano','Alessandro','Valdir','Rogério','Gilberto','Sérgio','Wesley'
]

female_names = [
'Maria','Ana','Juliana','Fernanda','Patrícia','Camila','Amanda','Aline','Bruna','Carla',
'Daniela','Eduarda','Fabiana','Gabriela','Helena','Isabela','Jéssica','Larissa','Letícia','Luciana',
'Mariana','Natália','Paula','Priscila','Renata','Simone','Tatiane','Vanessa','Sílvia','Bianca',
'Beatriz','Cláudia','Cristiane','Débora','Elaine','Flávia','Geovana','Ingrid','Jaqueline','Karen',
'Lorena','Michele','Nayara','Olívia','Raquel','Sabrina','Tainá','Yasmin','Zilda','Evelyn'
]

surnames = [
'Silva','Santos','Oliveira','Souza','Rodrigues','Ferreira','Alves','Pereira','Lima','Gomes',
'Costa','Ribeiro','Martins','Carvalho','Almeida','Lopes','Soares','Fernandes','Vieira','Barbosa',
'Rocha','Dias','Monteiro','Cardoso','Reis','Araújo','Nascimento','Freitas','Cavalcanti','Teixeira',
'Correia','Mendes','Batista','Ramos','Moreira','Azevedo','Nogueira','Moura','Campos','Duarte',
'Pinto','Machado','Freire','Borges','Farias','Peixoto','Coelho','Leite','Sales','Castro'
]

universal_names = [
'Ariel','Yves','Alex','Dani','Fran','Sam','Noel','Kim','Lee','Luca',
'Jo','Cris','Biel','Duda','Jaci','Ari','Nani','Rene','Val','Eli',
'Isa','Gabi','Tay','Kai','Jan','Luan','Mika','Sacha','Noa','Zion',
'Ryan','Tony','Gael','Andy','Beni','Lori','Mari','Cadu','Jade','Rael',
'Joade','Sol','Lua','Ciel','Ayo','Dani','Ariel','Yuri','Acyr','Eden'
]


estados  = {
    'cod_estado':[1,2],
    'nome':['SP','MG'],
    'habitantes':[46000000,21000000],
    'renda_percapita':[2300,2600]    
}

cidades = {
'cod_cidade': list(range(1,21)),
'nome': [
    'Campo Limpo Paulista',
    'Jundiaí',
    'Campinas',
    'São Paulo',
    'Santos',
    'Sorocaba',
    'Ribeirão Preto',
    'São José dos Campos',
    'Piracicaba',
    'Bauru',
    'Belo Horizonte',
    'Uberlândia',
    'Contagem',
    'Juiz de Fora',
    'Betim',
    'Montes Claros',
    'Uberaba',
    'Governador Valadares',
    'Ipatinga',
    'Sete Lagoas'
],
'habitantes': [
    77000,
    430000,
    1210000,
    12300000,
    430000,
    720000,
    720000,
    730000,
    410000,
    380000,
    2400000,
    700000,
    670000,
    570000,
    450000,
    420000,
    340000,
    280000,
    270000,
    240000
],
'renda_percapita': [
    1200,
    2900,
    3000,
    3200,
    2800,
    2500,
    2600,
    2800,
    2500,
    2400,
    2700,
    2500,
    2300,
    2400,
    2300,
    2000,
    2400,
    1900,
    2200,
    2100
],
'cod_estado': [
    1,1,1,1,1,1,1,1,1,1,
    2,2,2,2,2,2,2,2,2,2
]
}

bairros = {
    'cod_bairro': list(range(1, 41)),
    'nome': [
        'Centro', 'Jardim América',                  # Campo Limpo Paulista
        'Vila Arens', 'Anhangabaú',                  # Jundiaí
        'Cambuí', 'Taquaral',                        # Campinas
        'Moema', 'Pinheiros',                        # São Paulo
        'Gonzaga', 'Ponta da Praia',                 # Santos
        'Centro', 'Campolim',                        # Sorocaba
        'Jardim Botânico', 'Centro',                 # Ribeirão Preto
        'Jardim Aquarius', 'Centro',                 # São José dos Campos
        'Centro', 'Piracicamirim',                   # Piracicaba
        'Centro', 'Vila Falcão',                     # Bauru
        'Savassi', 'Pampulha',                       # Belo Horizonte
        'Santa Mônica', 'Centro',                    # Uberlândia
        'Eldorado', 'Industrial',                    # Contagem
        'Centro', 'São Mateus',                      # Juiz de Fora
        'Centro', 'Alterosas',                       # Betim
        'Centro', 'Major Prates',                    # Montes Claros
        'Centro', 'Abadia',                          # Uberaba
        'Centro', 'Grã-Duquesa',                     # Governador Valadares
        'Centro', 'Canaã',                           # Ipatinga
        'Centro', 'Boa Vista'                        # Sete Lagoas
    ],
    'habitantes': [
        5000, 7000,
        8000, 6000,
        15000, 12000,
        20000, 18000,
        9000, 8500,
        10000, 11000,
        9500, 9000,
        12000, 11000,
        8000, 7500,
        7000, 6500,
        13000, 14000,
        9000, 8500,
        10000, 9500,
        11000, 10500,
        9500, 9000,
        8500, 8000,
        8000, 7500,
        7000, 6800,
        7200, 7000,
        6800, 6500
    ],
    'renda_percapita': [
        1800, 2200,
        2500, 2400,
        4000, 3500,
        4500, 4200,
        3000, 2900,
        2600, 2800,
        2700, 2600,
        3200, 3000,
        2400, 2300,
        2300, 2200,
        3800, 3600,
        2600, 2500,
        2400, 2300,
        2500, 2400,
        2300, 2200,
        2100, 2000,
        2400, 2300,
        2000, 1900,
        2200, 2100,
        2100, 2000
    ],
    'cod_cidade': [
        1,1,
        2,2,
        3,3,
        4,4,
        5,5,
        6,6,
        7,7,
        8,8,
        9,9,
        10,10,
        11,11,
        12,12,
        13,13,
        14,14,
        15,15,
        16,16,
        17,17,
        18,18,
        19,19,
        20,20
    ]
}


fornecedores = {
    'cod_fornecedor':[i for i in range(1,8)],	
    'nome':['Alpes Atacado','Loja do trol','Três irmãos','Piratininga Variedades','Lombriqueta','Ponto do empreendedor','Loja do Zé'],		
    'data_fundacao':['1991-08-15','1954-11-15','2001-01-20','2005-09-15','1990-05-15','1980-01-15','1978-01-08'],		
    'cod_endereco':[random.randint(1,100) for i in range(7)],	
    'cod_contato':[random.randint(1,100) for i in range(7)]
    
}

servicos  = {'psicologia':
                {
                    'cod_servico':[1,2,3,4,5],
                    'nome':['Avaliação presencial','Tratamento presencial',\
                        'Consultoria empresarial','Avaliação on-line',\
                            'Tratamento on-line'],
                    'custo':[100.0,100.0,200.0,30.0,30.0],
                    'preco':[300.0,300.0,600.0,150.0,150.0]                            
                            }
                            
                            }

# produtos  = {'sobremesas':
#                 {
#                     'cod_produto':[1,2,3,4,5],
#                     'nome':['Bolo','Pudim de leite',\
#                         'amendoim doce','torta',\
#                             'trufa'],
#                     'custo':[4.0,2.0,3.0,1.0,1.0],
#                     'preco':[6.0,6.0,7.0,8.0,5.0]                            
#                             }                            
#                             }
produtos = {
    'salgados': {
        'cod_produto': [101, 102, 103, 104, 105],
        'nome': [
            'Feijoada no pote', 
            'Feijão tropeiro artesanal', 
            'Bobó de cogumelos com dendê',  # Opção vegana afetiva
            'Pastel de angu com ora-pro-nóbis', 
            'Arrubadinho de feijão verde'
        ],
        'custo': [12.0, 10.0, 14.0, 5.0, 9.0],
        'preco': [28.0, 24.0, 32.0, 14.0, 22.0]
    },
    'sobremesas': {
        'cod_produto': [201, 202, 203, 204, 205],
        'nome': [
            'Pudim de leite com calda de gergelim', 
            'Banana da terra flambada na cachaça', 
            'Cocada cremosa com raspas de limão cravo', 
            'Bolo de rolo com geleia de umbu', 
            'Quindim de colher com baunilha do cerrado'
        ],
        'custo': [6.0, 5.0, 4.5, 7.0, 5.5],
        'preco': [16.0, 14.0, 12.0, 18.0, 15.0]
    }
}

enderecos_vazia = {
    'cod_endereco':[],
    'cep':[],
    'logradouro':[],
    'numero':[],
    'cod_estado':[],
    'cod_cidade':[],
    'cod_bairro':[]
}

clientes_vazia = {
    'cod_cliente':[],
    'cod_endereco':[],
    'cod_contato':[],		
    'data_primeira_compra':[]
}

operacoes = {
    'cod_operacao' : [1,2,3,4,5,6,7],
    'tipo' : ['agendamento','compra','venda','devolucao','troca','voucher','cancelamento']
}

transacoes_vazia = {
    'cod_transacao':[],
    'cod_calendario':[],
    'cod_operacoes':[],
    'cod_produto':[],
    'quantidade_produto':[],
    'cod_cliente':[],
    'cod_servico':[],
    'quantidade_servico':[]
}


def cria_contatos(rows_limit:int=10):
    em_pt1 = random.choice(['caramelo','cuei','aguia','tartaruga','_','foguete'])
    em_pt2 = random.choice(['potencia','flamejante','doce','azedinha','_','ratoeira'])
    em_pt3 = str(random.randint(1982,2026))
    em_pt4 = random.choice(['brasi','daquebrada','dopiratininga','nacopa','_',f'{random.randint(1000,5000)}_fitas'])
    em_pt5 = random.choice(['canela_de_fogo','sem_re','_camisa10_','joelho_ungido','_',f'{random.randint(1000,5000)}_cairaodomeulado'])
    
    def compose(*args):
        apelido:str = ''
        for _ in range(1,4):
            apelido+= str(random.choice([*args]))
        return apelido
    
    apelido = [compose(em_pt1,em_pt2,em_pt3,em_pt4,em_pt5) for i in range(rows_limit)]
    # apelido = f'{}{}{}{}'
    # telefone = f"11 9{random.randint(1000,2000)}-{random.randint(5000,6000)}"
    output_dict = {'cod_contato' : [random.choice([uuid.uuid4().hex[:8],uuid.uuid4().hex[:8]]) for i in range(rows_limit)],
    'telefone' : [random.choice(['nao_informado',f"11 9{random.randint(1000,2000)}-{random.randint(5000,6000)}"])  for i in range(rows_limit)],
    'email' : [random.choice(['nao_informado',f"{apelido[i]}@email.com.br"]) for i in range(rows_limit)],
    'instagram' : [random.choice(['nao_informado',f"@{apelido[i]}"]) for i in range(rows_limit)],
    'facebook' : [random.choice(['nao_informado',f"@{apelido[i]}"]) for i in range(rows_limit)],
    'linkedin' : [random.choice(['nao_informado',apelido[i]]) for i in range(rows_limit)],
    'kuwei' : [random.choice(['nao_informado',apelido[i]]) for i in range(rows_limit)],
    'whatsapp' : [random.choice(['nao_informado',f"11 9{random.randint(1000,2000)}-{random.randint(5000,6000)}"]) for i in range(rows_limit)],}

    return output_dict

programa_de_fidelidade = {
    'cod_fidelidade':[1,2],
    'nome_fidelidade':['padrao','premium'],
    'desconto_seg_sex':[0.08,0.20],
    'desconto_fim_de_semana':[0.05,0.08]
}