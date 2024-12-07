N=range
C=print
import requests as H,threading as G
from random_word import RandomWords as O
import time
from colorama import Fore as A,Style as B,init
from fake_useragent import UserAgent as P
init(autoreset=True)
J=set()
Q=G.Lock()
R=P()
def K(usernames):
	L='application/json';I=usernames;G='code';N='https://users.roblox.com/v1/usernames/users';M={'User-Agent':R.random,'accept':L,'Content-Type':L}
	try:
		O={'usernames':I,'excludeBannedUsers':False};D=H.post(N,headers=M,json=O,timeout=1)
		if D.status_code==200:
			F=D.json();P=[A['requestedUsername']for A in F['data']];S=[A for A in I if A not in P]
			for E in S:
				with Q:
					if E not in J:
						J.add(E);T=f"https://auth.roblox.com/v1/usernames/validate?birthday=2006-09-21T07:00:00.000Z&context=Signup&username={E}";D=H.get(T,headers=M)
						if D.status_code==200:
							F=D.json()
							if F[G]==0:
								C(f"[{A.YELLOW}name{B.RESET_ALL}-{A.CYAN}gen{B.RESET_ALL}] : {A.GREEN}pass{B.RESET_ALL}      : '{E}' is valid and available")
								with open('name-gen names.txt','a')as U:U.write(E+'\n')
							elif F[G]==1:C(f"[{A.YELLOW}name{B.RESET_ALL}-{A.CYAN}gen{B.RESET_ALL}] : {A.RED}error{B.RESET_ALL}     : '{E}' is already in use")
							elif F[G]==2:C(f"[{A.YELLOW}name{B.RESET_ALL}-{A.CYAN}gen{B.RESET_ALL}] : {A.RED}error{B.RESET_ALL}     : '{E}' is not appropriate for roblox")
							elif F[G]==10:C(f"[{A.YELLOW}name{B.RESET_ALL}-{A.CYAN}gen{B.RESET_ALL}] : {A.YELLOW}error{B.RESET_ALL}     : '{E}' might contain private info")
						else:C(f"[{A.YELLOW}name{B.RESET_ALL}-{A.CYAN}gen{B.RESET_ALL}] : {A.RED}error{B.RESET_ALL}     : unable to access api")
		elif D.status_code==429:C(f"[{A.YELLOW}name{B.RESET_ALL}-{A.CYAN}gen{B.RESET_ALL}] : {A.YELLOW}ratelimit{B.RESET_ALL} : rate limit reached, retrying in 15 sec.");time.sleep(15);K(I)
		else:C(f"[{A.YELLOW}name{B.RESET_ALL}-{A.CYAN}gen{B.RESET_ALL}] : {A.RED}error{B.RESET_ALL} - {D.status_code} - {D.text}")
	except H.exceptions.RequestException as V:C(f"[{A.YELLOW}name{B.RESET_ALL}-{A.CYAN}gen{B.RESET_ALL}] : {A.RED}error{B.RESET_ALL} - {V}")
if __name__=='__main__':
	I=O()
	while True:
		D=[]
		for T in N(500):
			E=I.get_random_word()
			while len(E)<6:E=I.get_random_word()
			D.append(E)
		L=125;S=[D[A:A+L]for A in N(0,len(D),L)];M=[G.Thread(target=K,args=(A,))for A in S]
		for F in M:F.start()
		for F in M:F.join()
