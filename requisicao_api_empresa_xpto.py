import pandas as pd
import requests
import json
import os
from datetime import date
today = str(date.today())

credential = {"username": "email.com.br", "password": "senha"}
credentialLogin = requests.post("https://siteOnddeEstaOsDados.com/especifica_em_q_parte_do_site_vc_quer_buscar", json=credential)
credentialLoginJson = credentialLogin.json()
credentialTokenValue = credentialLoginJson['token']

________________________________________________________________________________________________________________________________________________

import pandas as pd
import requests
import json
import os
from datetime import date
today = str(date.today())

credential = {"username": "email.com.br", "password": "senha"}
credentialLogin = requests.post("https://siteOnddeEstaOsDados.com/especifica_em_q_parte_do_site_vc_quer_buscar", json=credential)
credentialLoginJson = credentialLogin.json()
credentialTokenValue = credentialLoginJson['token']
headers = {'Authorization':'JWT '+credentialTokenValue}

requests = requests.get("https://siteOnddeEstaOsDados.com/especifica_em_q_parte_do_site_vc_quer_buscar?Credencial_q_tavez_precise", headers=headers)
requests

#saída: 
response 200 # no meu caso significa q deu tudo certo :)

requests_Jason = requests.json()
requests_Text = json.dumps(requests_Jason, sort_keys=True, indent=4)
print(requests_Text)