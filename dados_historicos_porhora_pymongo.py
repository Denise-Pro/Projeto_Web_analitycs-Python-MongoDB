import pymongo
from bson.objectid import ObjectId
import numpy as np
import datetime
import time

# crio uma conexão com o mongo passando o localhost, usuario e senha
clientMongo = pymongo.MongoClient('"mongodb://localhost:27017/"',username='root', password='xpto123') # fake

db = clientMongo["Banco"] # especifico com qual banco quero trabalhar dentro do mongo
collection1 =db["collection1"] #especifico as collections - nomes fake
collection2 =db['collection2'] 
sensors_input = list(collection1.find())
sensors_out = list(collection2.find())

# contruo uma função so pra calcular as medias das variáveis da collectio1
def media(L):
    if type(L) != list:
        return L
    if len(L) ==0:
         return 0
    if type(L) == list and len(L) > 0:
        return np.mean(L)

# essa função calcula a media dos valores das variáveis a seguir referentes as últimas 24 horas
#ex: se agora são 9:00 a função calcula as medias dos valores dessas variáveis entre 9 horas de hoje e 9 hrs de hj
def etl_collection2():
    now = time.mktime(datetime.datetime.now().timetuple()) # timpestamp hora atual 
    t0 = datetime.datetime.fromtimestamp(now) #timestamp de 24 h atrás # t0 vai ser sempre o limite inferior
    t0= t0.replace(second=0, microsecond=0, minute=0, hour=t0.hour)-datetime.timedelta(hours=t0.minute//30)# essa linha pega so
    # as 'horas zero' ex: 14:00, 12:00, 9:00,
    t0_fixo = t0
    t = t0 - datetime.timedelta(hours=24) # se t0 é 22/04 ás 22 -> t é 21/04 ás 22
    for sensor in sensors_input: # para cada snsor na coll collection1
        data=[]
        add_sensor={} 
        t0=t0_fixo
        while t0.timestamp() >= t.timestamp():
            hora = str(int(t0.timestamp()*1000)) # multiplico o timestamp por mil pra igualar as casas decimais
            dados_sensor = {hora: [{'id':sensor['sensor_id'],'sensor_id':[],'last_seen':[],'update_d_time':[],'rpm': [], 'aceleracao_x': [], 'aceleracao_y': [], 'aceleracao_z': [], 'aceleracao_local': [], 'frequencia': [], 'amplitude_x': [],'amplitude_y': [],'amplitude_local': [],'constante': [], 'amplitude_z': [],'angulo_mov': [], 'temperature_sensor': [],'displacement_x': [], 'displacement_y': [], 'displacement_z': [],'phase_angle': [],'delta_temperature': [],'rms': [],'sensor_on_off':[]}]}
            #data.append({hora: [{'rpm': [], 'aceleracao_x': [], 'aceleracao_y': [], 'aceleracao_z': [], 'aceleracao_local': [], 'frequencia': [], 'amplitude_x': [],'amplitude_y': [],'amplitude_local': [],'constante': [], 'amplitude_z': [],'angulo_mov': [], 'temperature_sensor': [],'displacement_x': [], 'displacement_y': [], 'displacement_z': [],'phase_angle': [],'delta_temperature': [],'rms': []}]})
            for sensor_timestamp in sensor['data']: # se ja tiver dados pra tal horário
                if list(sensor_timestamp.keys())[0] > hora: # se tal timestamp for menor q o horário de agora
                    for key, value in sensor_timestamp[list(sensor_timestamp.keys())[0]][0].items():
                        dados_sensor[hora][0][key].append(value) 
                    sensor['data'].remove(sensor_timestamp) # remove os timestamps q ja foram incluídos na coll1
            if len(dados_sensor[hora][0]['sensor_id']) > 1:  
                dados_sensor[hora][0]['sensor_id'] = dados_sensor[hora][0]['sensor_id'][0]
            # aqui calculo as medias dessas variáveis e arredondo o resultado para 2 casas decimasis pos vírgula
            dados_sensor[hora][0]['rpm'] = round(media(dados_sensor[hora][0]['rpm']),2)
            dados_sensor[hora][0]['aceleracao_x'] = round(media(dados_sensor[hora][0]['aceleracao_x']),2)
            dados_sensor[hora][0]['aceleracao_y'] = round(media(dados_sensor[hora][0]['aceleracao_y']),2)
            dados_sensor[hora][0]['aceleracao_z'] = round(media(dados_sensor[hora][0]['aceleracao_z']),2)
            dados_sensor[hora][0]['aceleracao_local'] = round(media(dados_sensor[hora][0]['aceleracao_local']),2)
            dados_sensor[hora][0]['aceleracao_local'] = round(media(dados_sensor[hora][0]['aceleracao_local']),2)
            dados_sensor[hora][0]['frequencia'] = round(media(dados_sensor[hora][0]['frequencia']),2)
            dados_sensor[hora][0]['amplitude_x'] = round(media(dados_sensor[hora][0]['amplitude_x']),2)
            dados_sensor[hora][0]['amplitude_y'] = round(media(dados_sensor[hora][0]['amplitude_y']),2)
            dados_sensor[hora][0]['amplitude_local'] = round(media(dados_sensor[hora][0]['amplitude_local']),2)
            dados_sensor[hora][0]['constante'] = round(media(dados_sensor[hora][0]['constante']),2)
            dados_sensor[hora][0]['amplitude_z'] = round(media(dados_sensor[hora][0]['amplitude_z']),2)
            dados_sensor[hora][0]['angulo_mov'] = round(media(dados_sensor[hora][0]['angulo_mov']),2)
            dados_sensor[hora][0]['temperature_sensor'] = round(media(dados_sensor[hora][0]['temperature_sensor']),2)
            dados_sensor[hora][0]['displacement_x'] = round(media(dados_sensor[hora][0]['displacement_x']),2)
            dados_sensor[hora][0]['displacement_y'] = round(media(dados_sensor[hora][0]['displacement_y']),2)
            dados_sensor[hora][0]['displacement_z'] = round(media(dados_sensor[hora][0]['displacement_z']),2)
            dados_sensor[hora][0]['phase_angle'] = round(media(dados_sensor[hora][0]['phase_angle']),2)
            dados_sensor[hora][0]['delta_temperature'] = round(media(dados_sensor[hora][0]['delta_temperature']),2)
            dados_sensor[hora][0]['rms'] = dados_sensor[hora][0]['rms']
            # aqui eu excluo as chave:valor q não me interessam nessa análise
            dados_sensor[hora][0].pop('last_seen', None)
            dados_sensor[hora][0].pop('update_d_time', None)
            dados_sensor[hora][0].pop('sensor_on_off', None)
            #salvo os dados separados por hora em uma lista
            data.append(dados_sensor)
            #persisto a lista em um dicionario - estrutura q me foi requisitada na especificação funcional
            add_sensor.update({'sensor_id': sensor['sensor_id'], 'data': data})
            #atualizo o timestamp
            t0 = t0 - datetime.timedelta(hours=1)
            #adiciono os sensores ja existentes na coll collection2 nessa lista
        sensor_existente=[]   
        if len(sensors_out) > 0:
            for e in sensors_out:
                sensor_existente.append(e['sensor_id'])
        # se a coll estiver vazia ou se o sensor ainda n exiistir nela faço insert
        if len(sensors_out) == 0 or sensor['sensor_id'] not in sensor_existente:
            collection2.insert_one(add_sensor)
        if sensor['sensor_id'] in sensor_existente: # se o sensor ja existir na coll
            times_new =[]
            for s in sensors_out: #pra cada sensor existente
                for d in add_sensor['data']: # em cada dicionario onde a chave é um timestamp - cada d é um dict 
                    if d not in s['data'] and add_sensor['sensor_id'] == s['sensor_id']: #se d n existir e o sensor for o mesmo
                        id = s['_id'] #pego o id do documento da collection collection2
                        if d not in times_new: #evito appends duplicados
                            times_new.append(d)# salvo nessa lista os timestamps novos
            for i in times_new:
                collection2.update_one({'_id': id}, {"$push": {'data': i}}) # upsert de timestamps novos
                        


len(sensors_out) #verifica a quantidade de sensores na collection
len(sensors_out[0]['data']) #verifica quantos timestamps foram inseridos a cada execução no primeiro sensor
sensors_out[0]['data'][24] 

