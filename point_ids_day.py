import pymongo
from bson.objectid import ObjectId
# crio uma conexão com o mongo passando o localhost, usuario e senha
clientMongo = pymongo.MongoClient('"mongodb://localhost:27017/"',username='root', password='xpto123') # fake
db = clientMongo["Banco"] # especifico com qual banco quero trabalhar dentro do mongo
coll =db["point_ids"] #especifico as collections - nomes fake
coll1 =db['point_ids_day'] 
x=coll.find_one(sort=[('_id', -1)]) #pegando o ultimo documento da collection1
y= coll1.find_one(sort=[('_id', -1)])


def point_ids_day():
    
     # salvando os point_ids de todas as máquinas em lista
    j=1
    point_ids=[]
    while(j<len(x['machines'])): # esse primeiro laço passa por todas as maquinas
        for i in range(len(x['machines'][j]['point'])):#esse segundo imprime cada point id de cada maquina
            point_ids.append(x['machines'][j]['point'][i]['sensor_id']) 
        j=j+1
        
    #pegando todas as máquinas existentes para esse doc da point_ids
    i=1
    machines=[]
    while(i<len(x['machines'])):
        machines.append(x['machines'][i]['name'])
        i=i+1
    try:    
        # se a collection point_ids-day ja tiver algum doc:
        if len(list(y.keys())) > 0:
            existente=list(y.keys()) # cada posição dessa lista 'existente' é um point_id da collection point_ids_day

            # pegando os point_ids que não estão na collection point_ids_day
            n_tem=[]
            for i in point_ids: # para cada point id dessa lista 'point_ids' verifique se todos os point-ids estão nessa collection
                if i not in existente: # os que não estiverem nessa colection ainda serão adicionados em n_tem
                    n_tem.append(i)

            # sensor ainda não existente na collection point_ids_day
            if len(n_tem) != 0:
                for sensor in n_tem:
                     for j in range(1,len(machines)+1): 
                        for i in x['machines'][j]['point']:
                            if sensor == i['sensor_id']: # se um sensor id de alguma maquina ainda n estiver na collection
                                y.update({i['sensor_id']:[{str(i['point_id'][0]['last_seen']):i['point_id']}]}) #crio um dict novo

            # codigo pra sensor ja existente
            for p in point_ids: 
                if p in existente:# se tal poit_id de alguma maquina ja existir na colection point_ids_day 
                    for j in range(1,len(machines)+1): # olhe em cada maquina
                         for i in x['machines'][j]['point']: # se achar o point id e se o timestamp n for repetido pra esse sensor
                                if p == i['sensor_id'] and list(y[p][-1].keys())[0] != str(i['point_id'][0]['last_seen']):
                                    y[p].append({str(i['point_id'][0]['last_seen']):i['point_id']})#appenda essa informação
                                    #na lista ja existente de timestamps para esse sensor
            y.pop('_id', None)
            coll1.insert_one(y)
            return y
    except:
        # primeiro insert na collection point_ids_day
        a=0
        hist={}
        while(a<len(point_ids)): # pra cada point id de cada maquina
            for j in range(1,len(machines)+1): # pro numero de maquinas q tem
                for i in x['machines'][j]['point']: # pra cada quantidade de sensor que existe em cada maquina
                    if point_ids[a]== i['sensor_id']: # se achar o point id dentro de alguma maquina
                        hist.update({i['sensor_id']:[{str(i['point_id'][0]['last_seen']):i['point_id']}]})# se n converter o timestamp pra string o banco n consegue isenrir o doc
            a=a+1
        coll1.insert_one(hist)
        return 'primeiro insert realizado'

point_ids_day()