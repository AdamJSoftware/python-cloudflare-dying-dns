import requests
import json

import os

cloudflare_url = 'https://api.cloudflare.com/client/v4/zones'

def log_write(message):
    if(os.path.isfile('./log.txt')):
        pass
    else:
        with open('./log.txt', 'w') as f:
            f.write('')
    with open('./log.txt', 'a') as f:
        f.write(message+"\n")
    print(message)


def main():
    current_ip = requests.get('https://ifconfig.me').text

    with open('./config.json', 'r') as f:
        data = f.read()
        credentials = json.loads(data)
        token = credentials['cloudflare_token']


        for item in credentials['sites']:
            cloudflare_zone_identifier = item['cloudflare_zone_identifier']
            domain = item['domain']
            cloudflare_token = f'Bearer {token}'
            headers={"Content-Type": "application/json","Authorization": cloudflare_token}


            r = requests.get(f'{cloudflare_url}/{cloudflare_zone_identifier}/dns_records', headers=headers)
            if(r.ok):
                results = json.loads(r.text)
                for i in results['result']:
                    name = i['name']
                    if(name == domain):
                        content = i['content']
                        if(current_ip != content):
                            log_write('IP HAS CHANGED')
                            log_write(f'CURRENT IP {current_ip}')
                            log_write(f'OLD IP {content}')
                            identifier = i['id']

                            url =f'{cloudflare_url}/{cloudflare_zone_identifier}/dns_records/{identifier}'

                            r = requests.patch(url=url,headers=headers, data=json.dumps({'content': str(current_ip)}))
                            if(r.ok):
                                log_write('IP CHANGED SUCCESSFULY')

                            else:
                                log_write('ERROR CHANGING IP')
            else:
                log_write('ERROR AUTHENTICATING WITH CLOUDFLARE! PLEASE CHECK TOKEN')

if __name__ == "__main__":
    main()