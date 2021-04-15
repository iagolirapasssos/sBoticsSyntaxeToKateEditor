import json
import requests
import os
from classes.languages import Linguagens

####USANDO AS APIS SBOTICS

def cpxml(file):
	paths = [
			'$HOME/.local/share/org.kde.syntax-highlighting/syntax',
			'%USERPROFILE%\\AppData\\Local\\org.kde.syntax-highlighting\\syntax',
			'$HOME/Library/Application\ Support/org.kde.syntax-highlighting/syntax'
			]
	msg = "Atenção! Copiar os arquivos .xml para os seguintes diretórios\nAttention! Copy the .xml files to the following directories\n\n".upper()
	msg +="LINUX: $HOME/.local/share/org.kde.syntax-highlighting/syntax/\n"
	msg +="WINDOWS: %USERPROFILE%\\AppData\\Local\\org.kde.syntax-highlighting\\syntax\\\n\n"
	msg +="macOS: $HOME/Library/Application\\ Support/org.kde.syntax-highlighting/syntax/\n\n\n"
	msg +="Atenção! Se os diretórios acima não existirem, então crie-os manualmente!\n"
	msg +="Attention! If the above directories do not exist, then create them manually!\n\n\n"
	msg +="PT_BR:Os arquivos .kateschema com os temas, podem ser importados no próprio KATE\nAcesse o menu Configurações > Configurações do Kate > Fontes e cores.\nEscolha R-EDUC em \"Eschema\", depois \"importar\".\n\n"
	msg +="EN_US:The .kateschema files with the themes can be imported into KATE itself \nAccess the Settings menu> Kate Settings> Fonts and colors. \nChoose R-EDUC in \"Eschema\", then \"import\"."

	try:
		os.system(f'cp {file} {str(paths[0])}')
	except:
		try:
			os.system(f'cp {file} {str(paths[0])}')
		except:
			print(msg)

api_link_reduc = [
	 		'https://sbotics.weduc.natalnet.br/api/snippet/reduc_ptbr',
			'https://sbotics.weduc.natalnet.br/api/snippet/reduc_en'
		   ]
arquivoXML_reduc = ['reduc_ptbr.xml', 'reduc_en.xml']


api_link_csharp = [
			'https://sbotics.weduc.natalnet.br/api/snippet/csharp_ptbr',
			'https://sbotics.weduc.natalnet.br/api/snippet/csharp_en'
		   ]
arquivoXML_csharp = ['csharp_ptbr.xml', 'csharp_en.xml']

try:
	print("\nAguarde/Wait...\n")

	partes = Linguagens("reduc", "pt_BR")
	for link in api_link_reduc:
		indice = api_link_reduc.index(link)
		resp = requests.get(link)

		if indice == 0:
			parte1_ = partes.reduc_ptbr_parte1()
			parte3_ = partes.reduc_ptbr_parte3()
			
		elif indice == 1:
			parte1_ = partes.reduc_en_parte1()
			parte3_ = partes.reduc_en_parte3()

		parte2 = "<list name=\"keywords\">\n"
		for todo_item in resp.json()['functions']:
			parte2+='      <item>{}</item>\n'.format(todo_item['name'])
		parte2+="      </list>"

		total = parte1_+parte2+parte3_
		
		filename = "LANGUAGES/"+arquivoXML_reduc[indice]
		with open(filename, 'w', encoding='utf-8') as arquivo:
			arquivo.write(total)
		arquivo.close()
		cpxml(filename)

	print("\nSucesso!/Sucess!...\n")
	try:
		os.system('ls')
	except:
		try:
			os.system('dir')
		except:
			print("\nError!...\n")
except:
	print("Alert! Error!")
