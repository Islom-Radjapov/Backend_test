import wikipedia

wikipedia.set_lang("uz")
a = wikipedia.page("toshkent")

print(a.content[:146])