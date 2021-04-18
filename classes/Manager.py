import json

class JsonManager():
	def read(self, _file):
		with open(_file, "r", encoding="utf8") as jf:
			return json.load(jf)

	def write(self, _file, _data):
		with open(_file, "w", encoding="utf8") as jf:
			json.dump(_data, jf, ensure_ascii=False, indent=4)

class FileManager():
	def read(self, _file):
		with open(_file, "r", encoding="utf8") as f:
			return f.read()

	def write(self, _file, _data):
		with open(_file, 'w', encoding='utf-8') as f:
			f.write(_data)
		f.close()

Json = JsonManager()
File = FileManager()