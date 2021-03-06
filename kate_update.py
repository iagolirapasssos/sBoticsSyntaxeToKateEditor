##﻿#Authors: Francisco Iago Lira Passo (iagolirapassos@gmail.com)
### and Vinicios Lugli (vinicioslugli@gmail.com)
### Data de criação: 19/04/2021
### Data de modificação: 22/04/2021

import json, requests, os, sys, pip
from classes.Manager import *

## VARIAVEIS --------------------------------------------------------------------
#LINKS API WEDUC
api_reduc = {
	"ptbr": 'https://sbotics.weduc.natalnet.br/api/snippet/reduc_ptbr',
	"en":'https://sbotics.weduc.natalnet.br/api/snippet/reduc_en'
}

api_csharp = {
	"ptbr": 'https://sbotics.weduc.natalnet.br/api/snippet/csharp_ptbr',
	"en": 'https://sbotics.weduc.natalnet.br/api/snippet/csharp_en'
}

#LOCAIS DAS PASTAS
try:
	HOME = os.path.expanduser('~')
except:
	HOME = None

paths = {
	"linux": f'{HOME}/.local/share/org.kde.syntax-highlighting/',
	"windows": f'{HOME}/AppData/Local/org.kde.syntax-highlighting/',
	"darwin": f'{HOME}/Library/Application/Support/org.kde.syntax-highlighting/'
}

#GIT LINKS
themes_to_update = "https://raw.githubusercontent.com/iagolirapasssos/sBoticsThemesToKateEditor/main/to_auto_update.json"
themes_link = "https://raw.githubusercontent.com/iagolirapasssos/sBoticsThemesToKateEditor/main/"

#UTILIZAÇÕES GLOBAIS
local_system = "windows"
language = "en"
language_data = None

## VERIFICAR OS MÓDULOS
class verificarModulos():
	def verificar(self):
		if not 'requests' in sys.modules.keys():
			pip.main(['install', 'requests'])
		

## CLASSES PRINCIPAIS
class Checks():
	def language(self):
		global language
		global language_data
		language_data = Json.read("./translation.json")[language]

		if(len(sys.argv) == 1):
			language = str(input("ptbr / en ?\n")).lower()
			if(language != "ptbr" and language != "en"):
				print(language_data["global"]["language_not_found"])
				exit()

		elif(sys.argv[1].lower() == "ptbr"):
			language = "ptbr"

		language_data = Json.read("./translation.json")[language]

	def system(self):
		global local_system
		_platform = sys.platform
		if _platform == "linux" or _platform == "linux2":# linux
			local_system = "linux"
			print(language_data["system_detected"]["linux"])
		elif _platform == "win32" or _platform == "win64":# Windows
			local_system = "windows"
			print(language_data["system_detected"]["windows"])
		elif _platform == "darwin":# MAC OS X
			local_system = "darwin"
			print(language_data["system_detected"]["darwin"])
		else:
			print(language_data["system_detected"]["not_found"])

	def directory(self):
		global paths
		global local_system
		if(HOME == None):
			print(language_data["path_not_found"])
			exit()

		path = paths[local_system]
		to_check = ["syntax", "themes"]

		for folder in to_check:
			if not os.path.exists(path+folder):
				os.makedirs(path+folder, exist_ok=True)

class Snippets():
	def __init__(self, language_name, language_api):
		self.language_name = language_name
		self.language_api = language_api
		self.filename = f'{self.language_name}_{language}.xml'
		self.functions_xml = ""

	def update(self):
		response = requests.get(self.language_api)
		functions = response.json()["functions"]
		self.functions_xml = "<list name=\"keywords\">\n"
		for function in functions:
			self.functions_xml+=f'    <item>{function["code"]}</item>\n'
		self.functions_xml+="    </list>"

	def save(self):
		xml_base = File.read(f'./dataFiles/base_syntax/base_{self.language_name}_{language}.xml')
		File.write(paths[local_system]+f'syntax/{self.filename}', xml_base.replace("<PART2></PART2>", self.functions_xml))
		print(language_data["syntax"], self.filename)

class Themes():
	def update(self):
		self.themes_names = requests.get(themes_to_update).json()

	def save(self):
		for name_reduc in self.themes_names["reduc"]:
			file_to_save = requests.get(f'{themes_link}/R-EDUC/{name_reduc}').json()
			Json.write(paths[local_system]+f'themes/{name_reduc}', file_to_save)
			print(language_data["theme"], name_reduc)

		for name_csharp in self.themes_names["csharp"]:
			file_to_save = requests.get(f'{themes_link}/CSHARP/{name_csharp}').json()
			Json.write(paths[local_system]+f'themes/{name_csharp}', file_to_save)
			print(language_data["theme"], name_csharp)

checks = Checks()
try:
	checks.language()
	checks.system()
	checks.directory()
except Exception as ex:
	print(ex)

themesUpdater = Themes()
reducSnippets = Snippets("reduc", api_reduc[language])
csharpSnippets = Snippets("csharp", api_csharp[language])

modulo = verificarModulos()

#MAIN
try:

	print(language_data["await"])
	#Verificar módulo
	modulo.verificar()

	#snippets/syntax
	reducSnippets.update()
	csharpSnippets.update()

	reducSnippets.save()
	csharpSnippets.save()

	#temas
	themesUpdater.update()
	themesUpdater.save()

except Exception as ex:
	print(language_data["error"], ex)

else:
	print(language_data["sucess"])
