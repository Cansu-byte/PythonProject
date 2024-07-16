from googletrans import Translator

def Translate():
    translator = Translator()
    
    while True:
        TW = input("Çevirmek istediğiniz kelime veya cümleyi giriniz (q ile çıkış): ")
        
        if TW.lower() == 'q':
            print("Program sonlandırılıyor...")
            break
        
        result = translator.translate(TW, src='tr', dest='en')
        print("Çeviri:", result.text)
        

Translate()
    

    
