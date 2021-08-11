import requests, os, ctypes

ctypes.windll.kernel32.SetConsoleTitleW('Token Checker | Angelus#0999')

print('[>] Account token', end='')
token = input('  :  ')
os.system('cls')

headers = {
    'Authorization': token,
    'Content-Type': 'application/json'
}

r = requests.get('https://discord.com/api/v6/users/@me', headers=headers)
try:
    if r.status_code == 200:
        userName = r.json()['username'] + '#' + r.json()['discriminator']
        userId = r.json()['id']
        phone = r.json()['phone']
        email = r.json()['email']
        twoFactor = r.json()['mfa_enabled']
        print(f"\n                          [User Name]      :       {userName}\n")
        print(f"\n                          [User ID]      :       {userId}\n")
        print(f"\n                          [Phone Number]      :       {phone if phone else ''}\n")
        print(f"\n                          [Email]      :       {email}\n")
        print(f"\n                          [2 Factor]      :       {twoFactor}\n")
        print('\n')
        input=()
        os.system('pause')
    else:
        print('Invalid token!')
        os.system('pause')
except Exception:
    print('Cant contact with discordapp.com')