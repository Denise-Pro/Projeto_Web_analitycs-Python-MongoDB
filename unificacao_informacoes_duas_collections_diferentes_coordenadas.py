import pymongo
clientMongo = pymongo.MongoClient("mongodb://localhost:27017/")# conectando com o servidor e passando a porta
db = clientMongo["test"]# passando o nome do bancco
coll = db["user_get"]# passando o nome da collection
coll1= db["sites"]# passando o nome da collection

user_get= coll.find_one()#pega o json la do mongo
sites = coll1.find_one()#pega o json la do mongo

def f_tela1(username):#estou declarando uma função e passando um parametro
    if username == user_get['user']['username']:# se esse username for valido a função sera executada
        sites_name = user_get['user']['sites']# sites_name vai receber o nome dos sites
        i = 0 #inicio a variável pra poder iterar 
        coordinates_sites ={} # declarando o dicionario que vai receber o nome do site e a coordenada do mesmo
        while(i<len(sites['sites'])):#a quantidade de vezes q esse laço vai executar depende do numero sites do json sites
            for site in sites_name:#para cada site de site_name
                if site == sites['sites'][i]['site_name']:#verifico se um nome de site está no json sites
                    coordinates_sites.update({site : sites['sites'][i]['coordinates']})#se ele encontrar esse nome ele pega a coordenada referente a esse site
                    #e salva nesse dicionario
            i = i+1
        return coordinates_sites #retorna os nomes dos sites com suas cordenadas
    else: 
        return 'username invalido'#se o parametro passado n for encontrado no json de user

f_tela1('email@gmail.com.br')#chamando a funçaõ e passando um username valido

# saida da função:
{site: cordenada, site2:cordenada2}