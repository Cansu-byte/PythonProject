a= float(input('islem yapmak istediginiz ilk sayiyi giriniz:'))
b= float(input('islem yapmak istediginiz ikinci sayiyi giriniz:'))
s= str(input('yapmak istediginiz islemi yaziniz(+,-,/,x):'))

if s == '+' :
    topla=a+b
    print(topla)
        
elif s == '-' :
    if a>b:    
      cikarma= a-b
      print(cikarma)
    elif b>=a: 
      cikarma=b-a
      print(cikarma)
    else:
        print("islem yapilamiyor.")
        
elif s == '/' :
    if b==0:
        print('Sifira bölme hatasi.')
    elif a<b or a>=b:
        bölme =a/b
        print(bölme)
    else:
        print('islem yapilamiyor.')
     
elif s == 'x' :
    carpma=a*b
    print(carpma)
    
else :
    print("Girdiniz islem yapilmamaktadir.")
    
    
