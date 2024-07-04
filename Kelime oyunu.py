import random

def Kelime_sec():
    kelimeliste = ["araba", "muz", "aile", "çilek", "oyun", "adam","yazilim","telefon","anne","çita","beyin","görgü","kural","kuzen","vergi","yasak"]
    return random.choice(kelimeliste)

def play_game():
    gizli_kelime = Kelime_sec()
    Tahmin_Listesi = []
    deneme = 5  # Toplam tahmin hakkı

    print("Adam asmaca oyununa hosgeldiniz!")
    print("Gizli kelimeyi tahmin edin.")
    print("Kelimenin harf sayisi:", len(gizli_kelime))
    print()

    while deneme > 0:
        dogru_tahmin = ""
        for harf in gizli_kelime:
            if harf in Tahmin_Listesi:
                dogru_tahmin += harf + " "
            else:
                dogru_tahmin += "_ "

        print("Gizli kelime:", dogru_tahmin)
        print("Kalan deneme sayisi:", deneme)
        print()

        if "_" not in dogru_tahmin:
            print("Tebrikler! Kelimeyi tahmin ettiniz", gizli_kelime)
            break

        tahmin = input("Bir harf girin veya kelimenin tamamini tahmin ediniz. ").lower()

        if len(tahmin) == 1:  # Tek harf tahmini
            if tahmin in Tahmin_Listesi:
                print("Bu harf daha önce denenmisdir.")
            elif tahmin in gizli_kelime:
                print("iyi tahmin!")
                Tahmin_Listesi.append(tahmin)
            else:
                print("Yanlis tahmin ettiniz.")
                deneme -= 1
                Tahmin_Listesi.append(tahmin)
        else:  # Kelime tahmini
            if tahmin == gizli_kelime:
                print("Tebrikler kelimeyi buldunuz:", gizli_kelime)
                break
            else:
                print("Yanlis tahmin!")
                deneme -= 1

    if deneme == 0:
        print("Tüm deneme haklariniz bitmistir. Kelimeniz:", gizli_kelime)

play_game()    
