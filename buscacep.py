#    _   _                        			SOBRE O SCRIPT
#  _/ \|/ \_
# /\\/   \//\       Autor: lucas-Dk | Whatsapp, copie e cole no navegador > wa.me/5531986802198
# \|/<\ />\|/		Script: Busca-Cep
# /\   _   /\
# \|/\ Y /\|/
#  \/|v-v|\/
#   \/\_/\/

import sys
import os
import requests
import json
import urllib.request

sistema = sys.platform

if sistema == "linux" or sistema == "linux2":
	conectar = urllib.request.urlopen("https://www.google.com")
	if conectar:
		while True:
			os.system("clear")
			print("""\033[1;33m
  _                                              
 | |__  _   _ ___  ___ __ _        ___ ___ _ __  
 | '_ \| | | / __|/ __/ _` |_____ / __/ _ \ '_ \ 
 | |_) | |_| \__ \ (_| (_| |_____| (_|  __/ |_) |
 |_.__/ \__,_|___/\___\__,_|      \___\___| .__/ 
                                          |_|
                            {lucas-Dk} 
				\n\033[m""")
			cep_user = str(input("\033[1;32m[+]\033[m Informe o CEP para busca: "))
			if "-" not in cep_user:
				print("\n\033[1;32m[ERROR] Você não colocou o - no seu cep. tente novamente!\033[m")
				print()
				sys.exit()
			else:
				url = "https://viacep.com.br/ws/{}/json/".format(cep_user)
				requisitar = requests.get(url)
				if requisitar.status_code == 200:
					dados = json.loads(requisitar.text)
					for k,v in dados.items():
						if k == "erro":
							print("\033[1;31m[ERROR]\033[m Esse cep {} é inválido!".format(cep_user))
							sys.exit()
					print()
					print("==========================")
					print("  \033[1;32m>>> CEP ENCONTRADO <<<\033[m")
					print("==========================\n")
					for key,value in dados.items():
						if key and value:
							print("\033[1;32m[INFO]\033[m \033[1;33m{}\033[m: {}".format(key,value))
					print()
					print("S > Sair")
					print("C > Buscar novo CEP\n")
					sair = str(input("\033[1;32m[*]\033[m Deseja pesquisar outro CEP ou deseja sair? [S/C]: ")).upper()
					while sair not in "S" and sair not in "C":
						sair = str(input("\033[1;32m[*]\033[m Deseja pesquisar outro CEP ou deseja sair? [S/C]: ")).upper()
					if sair == "S":
						print("\n\033[1;31m[*]\033[m Saindo...\n")
						sys.exit()
					elif sair == "C":
						pass
	else:
		print("\033[1;31m[ERROR]\033[m Parece que você não está conectado na internet! :(\n")

elif sistema == "win32":
	os.system("cls")
	conectar = urllib.request.urlopen("https://www.google.com")
	if conectar:
		while True:
			os.system("cls")
			print("""
  _                                              
 | |__  _   _ ___  ___ __ _        ___ ___ _ __  
 | '_ \| | | / __|/ __/ _` |_____ / __/ _ \ '_ \ 
 | |_) | |_| \__ \ (_| (_| |_____| (_|  __/ |_) |
 |_.__/ \__,_|___/\___\__,_|      \___\___| .__/ 
                                          |_|
                            {lucas-Dk}  
				\n""")
			cep_user = str(input("[*] Informe o CEP para busca: "))
			if "-" not in cep_user:
				print("\n[ERROR] Você não colocou o - no seu cep. tente novamente!\n")
				sys.exit()
			else:
				url = "https://viacep.com.br/ws/{}/json/".format(cep_user)
				requisitar = requests.get(url)
				if requisitar.status_code == 200:
					dados = json.loads(requisitar.text)
					for k,v in dados.items():
						if k == "erro":
							print("[ERROR] Esse CEP {} é inválido!".format(cep_user))
							sys.exit()
					print()
					print("==========================")
					print("  >>> CEP ENCONTRADO <<<")
					print("==========================")
					print()
					for key,value in dados.items():
						if key and value:
							print("[*] {}: {}".format(key,value))
					print()
					print("S > Sair")
					print("C > Buscar novo CEP\n")
					sair = str(input("[*] Deseja sair ou buscar outro cep? [S/C]: ")).upper()
					while sair not in "S" and sair not in "C":
						sair = str(input("[*] Deseja sair ou buscar outro cep? [S/C]: ")).upper()
					if sair == "S":
						print("\n[*] Saindo...\n")
						sys.exit()
					elif sair == "C":
						pass
	else:
		print("[ERROR] Parece que você não está conectado na internet! :(\n")
else:
	print("\033[1;31m[ERROR] Esse script não te versão para esse sistema! :(\n\033[m")
#Fim
