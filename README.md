# FACTORYINSIGHTS


Uygulamanın deploy edilmiş linki-> 

### Sistem Hakkında:

* Sistem hangi kullanıcının giriş yaptığını anlar ve ismi giriş ekranına yazdırır.
* Admin olmayan kullanıcı,kullanıcı tablosunu görüntüleyemez,kullanıcı ekleyemez ve değişiklik yapamaz.
* Admin olan kullanıcı,kullanıcı tablosunu görüntüler,kullanıcı ekler ve değişiklik yapabilir.
* Kullanıcı makinelere özellikler ekleyebilir ve güncelleyebilir.



#### Admin kullanıcısı oluşturmak için örnek proje komut satırı:

* from myapp.models.user import CustomUser
* CustomUser.objects.create_user(email="admin@admin.com", password="1234",is_admin=True)

## VIEWS

### LOGIN VIEW
1. [x] POST isteği durumunda,POST isteğinin içindeki email ve password alanlarını alınır.
2. [x] Veritabanındaki kullanıcıyı e-posta adresine göre filtrele. 
3. [x] Burada 2 ihtimal var.Kullanıcı veritabanında bulunmazsa hata mesajıyla birlikte login.html sayfasına yönlendirir.
4. [x] Girilen şifre,kullanıcının kayıtlı şifresiyle uyuşmazsa hata mesajıyla birlikte login.html'e gönderir.
5. [x] Her kullanıcıya özel token oluşturulması. (token_payload)
6. [x] Token oluşturulurken, bu bilgiler içeriğe eklenir ve ardından bu içerik, gizli bir anahtar (settings.SECRET_KEY içinde saklanan) kullanılarak imzalanır. İmzalanmış token, kullanıcıya verilir ve daha sonra gelen isteklerde token doğrulama için kullanılır. Bu, kullanıcının kimliğini doğrulamak ve belirli işlemleri gerçekleştirmesine izin vermek için güvenli bir yöntemdir. 
7. [x] Access token cookie alanına set edilir.
8. [x] GET isteği durumunda veya başarılı giriş olmadığında login.html sayfasına yönlendirir.
 

###  LOGIN REQUIRED DEKORATÖRÜ

1. [x] <span style="color:pink;">access_token=request.COOKIES.get.("access_token")=GELEN HTTP isteğinin cookielerinden "access_token " adlı çerezi
   alır.
2. [x] <span style="color:pink;">Bu çerez,kullanıcının oturum açma durumunu kontrol etmek için kullanılır.
3. [x] if not access_token <span style="color:pink;">Eğer access_token çerezi yoksa kullanıcıyı giriş yapma sayfasına yönlendirir.
</span>

4. [x] token_payload = jwt.decode(access_token, settings.SECRET_KEY, algorithms=['HS256']):<span style="color:lightblue;"> JWT kütüphanesini kullanarak 'access_token' çerezini çözer. Bu adımda, çerezin içindeki bilgileri almak için kullanılan bir işlem gerçekleşir.
</span>

5. [x]  user_id=token_payload["user_id] ve email=token_payload["email] <span style="color:yellowgreen;"> Token içindeki user_id,email bilgilerini çıkarır.

6. [x] request.user=CustomUser.objects.filter(email=email,id=user_id).first()
<span style="color:green;"> Gelen requesti tanımlamak için kullanılır.

7. [x] except jwt.ExpiredSignatureError: ve except jwt.InvalidTokenError: <span style="color:purple;"> Token'ın süresi dolmuşsa veya geçerli bir JWT değilse, uygun hata mesajlarıyla birlikte HttpResponseForbidden (403 Forbidden) döner.


### IS USER ADMIN VIEW

* Bu fonksiyon admin ise True,user ise False döndürür.

### HOME VIEW

* Frontend'e yetki verisi döner.

### GET USER VIEW

* True gelirse admin demektir.Tüm userları listeler ve yetkilendirebilir.

### USER REGISTER VIEW

* is_user admin fonksiyonu giriş yapmıs kullanıcının adminmi yoksa user mı olduğunu kontrol eder.
* POST methodu ile veriler alınır.
* Yeni bir CustomUser objesi oluşturulur,veritabanına kaydedilir.
* Kullanıcı oluşturulduktan sonra users tablosunda görüntülenir.

### UPDATE USER VIEW
* Update edilmek istenen user'ın bilgilerini getirir.Update edildiği zaman modeli kaydeder.


### GET FACTORIES

* Fabrikada çalışan işçileri ve kullanılan makineleri de getirerek ekrana veri döner.


### GET USER FACTORIES

* is_staff parametresi True olan kullanıcıların çalıştığı fabrikayı getirir.


### FACTORY UPDATE VIEW

* Update edilmek istenen fabrikanın verilerini fabrikada çalışan staffları ve kullanılan makineleri getirir.
* Update edildiği zaman da değişen verileri database'e kaydeder.


### FACTORY CREATE VIEW 

*Fabrika kaydı gerçekleştirir.Fabrikada çalışanları ve kullanılan makineleri many to many fieldla bağlı olduğu için set eder.

### GET MACHINES

* Tüm makinelerin listesini verir.


### MACHINE CREATE VIEW

* Giriş yapmış kullanıcının admin olup olmadığı kontrol edilir.
* Yeni bir makine objesi oluşturulur ve veritabanına kaydedilir.
* Makine oluşturulduktan sonra machines sayfasına yönlendirilir.
* Eğer istek method'u POST değilse, muhtemelen bir GET isteği, bu durumda makine oluşturma formunu görüntülemek için gerekli bağlamı (context) hazırla
return render(request, 'machine_create.html', context={'is_admin': is_admin})


### MACHINE UPDATE VIEW

* Machine_id bulunamaz ise boş bir form açılır 

### LOGOUT VIEW

1.[x] request.COOKIES sözlüğünden 'access_token' adlı çerezi siler.Kullanıcının oturumunu sonlandırmak için mevcut oturum çerezini temizler ve login.html sayfasına yönlendirir.



### UYGULAMADAN RESİMLER

#### GİRİŞ EKRANI


![Login Screen](static/assets/img/loginscreen.png?raw=true "Optional Title")

#### FABRİKA GÜNCELLEME EKRANI

![Update Factory](static/assets/img/updatefactory.png?raw=true "Optional Title")










