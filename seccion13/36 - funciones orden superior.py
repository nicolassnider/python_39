def saludar(lang):
    def saludar_es():
        print("hola")
    def saludar_en():
        print("helo")
    def saludar_fr():
        print("salut")
    
    lang_func ={
        "es":saludar_es,
        "en":saludar_en,
        "fr":saludar_fr
    }
    return lang_func[lang]

f = saludar("es")
f()
    
saludar("fr")()