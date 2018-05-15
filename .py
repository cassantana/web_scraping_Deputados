

import requests 
import csv

url = 'https://dadosabertos.camara.leg.br/api/v2/deputados'
deputados = []
arquivo = open("deputados.csv", mode="w", encoding = "utf8")
arquivo_deputados = csv.writer(arquivo, lineterminator = "\n")
arquivo_deputados.writerow(["uri", "nomeCivil", "nomeEleitoral", "siglaPartido", "siglaUf", "telefone", "email", "sexo", "dataNascimento"])


for pagina in [1,2,3,4,5,6]:
    parametros = {'formato': 'json', 'itens': 100, 'pagina': pagina} 
    resposta = requests.get(url, parametros) 
    for deputado in resposta.json()['dados']:
        deputados_uri = deputado['uri'] 
        parametros = {'formato': 'json'}
        response = requests.get(deputados_uri, parametros)
        dados = response.json()['dados'] 
        uri = dados['uri']
        nome_civil = dados['nomeCivil'].title()
        sexo = dados['sexo']
        data_de_nascimento = dados['dataNascimento']
        escolaridade = dados['escolaridade']
        status = dados['ultimoStatus']
        nome_eleitoral = status['nomeEleitoral'].title()
        sigla_do_partido = status['siglaPartido']
        sigla_da_uf = status['siglaUf']
        url_foto = status['urlFoto']      
        gabinete = status['gabinete']
        numero = gabinete['telefone']
        email = gabinete['email']
        arquivo_deputados.writerow([uri, nome_civil, nome_eleitoral, sigla_do_partido, sigla_da_uf, numero, email, sexo, data_de_nascimento])
    
arquivo.close()
