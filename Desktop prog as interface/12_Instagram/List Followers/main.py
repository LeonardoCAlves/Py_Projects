# Autor: Leonardo Alves

import instaloader as insta

logging = insta.Instaloader()
with open('./12_Instagram/dados/login e senha.txt') as arq : 
    dados = arq.readlines()
logging.login(dados[0], dados[1])

followers = insta.Profile.from_username(logging.context, 'username').get_followers()
followees = insta.Profile.from_username(logging.context, 'username').get_followees()

print(f'\nSeguidores: {str(followers._data['count'])}')
print(f'Seguindo: {str(followees._data['count'])}')

print(f'Lista e detalhes dos seguidores: \n{followers._data['edges']}')

