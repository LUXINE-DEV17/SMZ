import os,sys,requests,re

def menu():
	print(f'->  PILIH MENU 3 UNTUK LOGIN KE DALAM MENU SMZ')
	print(f"""[01] Login Cookie V1\n[02] Login Cookie V2\n[03] Login Cookie V3""")
	menu = input('\n[?] Pilih : ')
	if menu in ['1']:
		os.system('rm -rf .tokenku.txt')
		os.system('rm -rf .cokieku.txt')
		token1()
	elif menu in ['2']:
		os.system('rm -rf .token.txt')
		os.system('rm -rf .cok.txt')
		token2()
	elif menu in ['3']:
		os.system('rm -rf .token.txt')
		os.system('rm -rf cok.txt')
		token3()
	else:
		exit()

def token1():
	try:
		ses = requests.Session()
		cookie = input('\n[?] MASUKAN COOKIE : ')
		cookies = {'cookie':cookie}
		url = 'https://www.facebook.com/adsmanager/manage/campaigns'
		req = ses.get(url,cookies=cookies)
		set = re.search('act=(.*?)&nav_source',str(req.content)).group(1)
		nek = '%s?act=%s&nav_source=no_referrer'%(url,set)
		roq = ses.get(nek,cookies=cookies)
		tok = re.search('accessToken="(.*?)"',str(roq.content)).group(1)
		tokenw = open(".tokenku.txt", "w").write(tok)
		cokiew = open(".cokieku.txt", "w").write(cookie)
		print('[✓] LOGIN BERHASIL')
		os.system('python runx.py')
	except Exception as e:
		os.system('rm -rf .cok.txt && rm -rf .tok.txt')
		print(e)
		exit()


def token2():
	try:
		ses = requests.Session()
		print(f' LOGIN COKIE V2')
		cookie = input('\n[?] Cookie : ')
		cookies = {'cookie':cookie}
		url = 'https://www.facebook.com/adsmanager/manage/campaigns'
		req = ses.get(url,cookies=cookies)
		set = re.search('act=(.*?)&nav_source',str(req.content)).group(1)
		nek = '%s?act=%s&nav_source=no_referrer'%(url,set)
		roq = ses.get(nek,cookies=cookies)
		tok = re.search('accessToken="(.*?)"',str(roq.content)).group(1)
		tokenw = open(".token.txt", "w").write(tok)
		cokiew = open(".cok.txt", "w").write(cookie)
		os.system('python runx.py')
	except Exception as e:
		os.system('rm -rf c.txt && rm -rf t.txt')
		print(e)
		exit()

def token3():
	try:
		ses = requests.Session()
		print(f'LOGIN COOKIE V3')
		cookie = input('\nCOKIE : ')
		cookies = {'cookie':cookie}
		url = 'https://www.facebook.com/adsmanager/manage/campaigns'
		req = ses.get(url,cookies=cookies)
		set = re.search('act=(.*?)&nav_source',str(req.content)).group(1)
		nek = '%s?act=%s&nav_source=no_referrer'%(url,set)
		roq = ses.get(nek,cookies=cookies)
		tok = re.search('accessToken="(.*?)"',str(roq.content)).group(1)
		tokenw = open(".token.txt", "w").write(tok)
		cokiew = open(".cok.txt", "w").write(cookie)
		os.system('python smz.py')
		#print('\nLogin Berhasil , file tersimpan di token.txt & cok.txt')
	except Exception as e:
		os.system('rm -rf cok.txt && rm -rf token.txt')
		print(e)
		exit()

if __name__=='__main__':
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	os.system('clear')
	menu()
