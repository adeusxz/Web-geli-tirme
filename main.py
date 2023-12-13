from flask import Flask
import random
app = Flask(__name__)

liste1 = ["Teknolojik bağımlılıktan mustarip olan çoğu kişi, kendilerini şebeke kapsama alanı dışında bulduklarında veya cihazlarını kullanamadıkları zaman yoğun stres yaşarlar.",
         "2018 yılında yapılan bir araştırmaya göre 18-34 yaş arası kişilerin %50'den fazlası kendilerini akıllı telefonlarına bağımlı olarak görüyor.",
         "Teknolojik bağımlılık çalışması, modern bilimsel araştırmanın en ilgili alanlarından biridir.",
         "2019'da yapılan bir araştırmaya göre, insanların %60'ından fazlası akıllı telefonlarındaki iş mesajlarına işten ayrıldıktan sonraki 15 dakika içinde yanıt veriyor.",
         "Teknolojik bağımlılıkla mücadele etmenin bir yolu, zevk veren ve ruh halini iyileştiren faaliyetler aramaktır.",
         "Elon Musk, sosyal ağların içeriği görüntülemek için mümkün olduğunca fazla zaman harcamamız için bizi platformun içinde tutmak üzere tasarlandığını iddia ediyor.",
         "Elon Musk sosyal ağların düzenlenmesini ve kullanıcıların kişisel verilerinin korunmasını savunmaktadır. Sosyal ağların hakkımızda büyük miktarda bilgi topladığını ve bu bilgilerin daha sonra düşüncelerimizi ve davranışlarımızı manipüle etmek için kullanılabileceğini iddia ediyor.",
         "Sosyal ağların olumlu ve olumsuz yanları vardır ve bu platformları kullanırken her ikisinin de farkında olmalıyız."         ]

liste2 = ["yazı","tura"]

@app.route("/")
def ilk():
    return f'<h1 style = " color:purple;font-size:80px;">Teknoloji Dünyasına Hoşgeldiniz.</h1> <p> <a href="/yaziTura">Yazı mı Tura mı?</a> </p><p> <a href="/rastgele_gercek">Teknolojinin farkında mısınız?</a> </p>'

@app.route("/rastgele_gercek")
def gelgit1():
    return f'<p>{random.choice(liste1)}</p> <a href="/">Geri git</a>'

@app.route("/yaziTura")
def gelgit2():
    if random.choice(liste2)=="tura":
        sonuc="<img width=100 src=https://scontent.fist7-1.fna.fbcdn.net/v/t39.30808-6/301298342_366452402361608_3534797641160948806_n.jpg?_nc_cat=106&ccb=1-7&_nc_sid=efb6e6&_nc_ohc=1XUsTvkSHg4AX_eWRel&_nc_ht=scontent.fist7-1.fna&oh=00_AfCTlsTMmXCu5eUTh5t1AO5opD5k5xmgKT0NNyUVVCQ0Zg&oe=657EC15C>";
    else:
        sonuc="<img width=100 src=https://d35fbhjemrkr2a.cloudfront.net/Images/Shop/5/Product/12163/400/fc281a0ccbb3428d8359605e3ff41fa6.jpg>"
    
    return f'<p>{sonuc}</p> <a href="/">Geri git</a>'
    
app.run(debug=True)