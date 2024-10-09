**_Disusun oleh Ignasius Bramantya Widiprasetya - 2306245604 - PBP F_**

## Tugas 2

### 1) Pembuatan Django

##### Check 1 : Membuat sebuah proyek Django baru


1. Buatlah sebuah direktory baru bernama `forza-shop` di komputer
2. Kemudian, buat juga _repository_ baru di Github bernama sama yaitu `forza-shop` dengan visibility _public_.
3. Dalam direktory baru tersebut, buka _command prompt_
4. Buatlah _virtual enviroment_ menggunakan python dengan command :
   ```bash
   python -m venv env
   ```
5. Lalu, aktifkan _virtual environement_ dengan command :
   ```bash
   env\Scripts\activate
   ```
6. _Virtual environment_ akan aktif yang ditandai (env) di awal baris input terminal
7. Buatlah file dengan nama `requirements.txt` di dalam direktori yang sama dan tambahkan beberapa _dependencies_ berikut di file tersebut :
   ```text
   django
   gunicorn
   whitenoise
   psycopg2-binary
   requests
   urllib3
   ```
8. Melakukan instalansi _dependencies_ pada `requirements.txt` dengan command :
   ```python
   pip install -r requirements.txt
   ```
9. Buatlah proyek Django baru dengan nama `forza-shop` dengan command :
   ```bash
   django-admin startproject forza_shop .
   ```

- Note : Pastikan `.` tertulis dalam baris command

10. Ubahlah isi variabel `ALLOWED_HOSTS` di file `settings.py` dengan menambahkan kode berikut :
    ```python
    ...
    ALLOWED_HOSTS = ["localhost", "127.0.0.1"]
    ...
    ```
11. Sebelumnya, pastikan terdapat file `manage.py` pada direktori yang aktif pada terminal kamu saat ini. Lalu, jalankan _server_ Django dengan command berikut :
    ```bash
    python manage.py runserver
    ```
12. Buka link [http://localhost:8000](http://localhost:8000/) pada browser dan pastikan muncul gambar roket yang menandakan bahwa Django berhasil diinstal. (seperti gambar berikut)
    ![Django Rocket](https://global.discourse-cdn.com/business7/uploads/djangoproject/original/3X/6/b/6b2c3c21ef8b9458b7eb6bdc843333e154b477d2.png)
13. Hentikan server dengan cara menekan `Ctrl+C` pada cmd.
14. Non aktifkan virtual environment (env) dengan command :
    ```bash
    deactivate
    ```

##### Check 2 : Membuat aplikasi dengan nama `main` pada proyek tersebut.

15. Buatlah aplikasi baru dengan nama **main** dengan menjalankan perintah berikut :
    ```bash
    python manage.py startapp main
    ```
16. Bukalan berkas `settings.py` di dalam direktori proyek `forza-shop`.
17. Tambahkanlah `'main'` ke dalam variabel `INSTALLED_APPS` seperti contoh berikut :
    ```python
    INSTALLED_APPS = [
        ...,
        'main'
    ]
    ```

##### Check 3 : Melakukan _routing_ pada proyek agar dapat menjalankan aplikasi `main`

18. Bukalah berkas `urls.py` di dalam direktori proyek `forza-shop`, **bukan yang ada di direktori `main`.**
19. Lakukan perubahan pada isi berkas tersebut seperti contoh kode berikut:

    ```python
    from django.contrib import admin
    from django.urls import path, include

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include('main.urls')),
    ]
    ```

##### Check 4 : Membuat model pada aplikasi `main` dengan nama Product dan memiliki atibut wajib.

20. Di direktori `main`, bukalah berkas `models.py`
21. Isilah berkas `models.py` dengan kode berikut :

    ```python
    from django.db import models

    class Product(models.Model):
        name = models.CharField(max_length=255)
        description = models.TextField()
        price = models.IntegerField()
        quantity = models.IntegerField()

        @property
        def is_available(self):
            return self.quantity > 0
    ```

22. Lakunlah migrasi model dengan menjalankan perintah berikut.
    ```bash
    python manage.py makemigrations
    ```
23. Terapkanlah migrasi ke dalam basis data lokal dengan menjalankan perintah berikut.
    ```bash
    python manage.py migrate
    ```

- Note: Setiap ada perubahan pada `models.py`, silahkan lakukan langkah 22 dan 23 kembali.

##### Check 5 : Membuat sebuah fungsi pada `views.py` untuk dikembalikan ke dalam sebuah _template_ html yang menampilkan nama aplikasi serta nama dan kelas kamu.

24. Bukalah berkas `views.py` yang terletak pada direktori `main`.
25. Gantilah isi berkas tersebut dengan kode berikut :

    ```python
    from django.shortcuts import render

    def show_main(request):
        context = {
            'app' : 'Forza-shop',
            'name': 'Ignasius Bramantya Widiprasetya',
            'class': 'PBP F'
        }

        return render(request, "main.html", context)
    ```

26. Buatlah direktori baru bernama `templates` dalam direktori `main`.
27. Di dalam direktori `templates`, buatlah berkas baru dengan nama `main.html`. Isi berkas `main.html` dengan kode berikut :

    ```html
    <h1>{{ app }}</h1>

    <h5>Name:</h5>
    <p>{{ name }}</p>
    <p></p>
    <h5>Class:</h5>
    <p>{{ class }}</p>
    <p></p>
    ```

##### Check 6 : Membuat sebuah _routing_ pada `urls.py` aplikasi `main` untuk memetakan fungsi yang telah dibuat pada `views.py`.

28. Buatlah berkas baru bernama `urls.py` di dalam direktori main.
29. Isi berkas tersebut dengan kode berikut :

    ```python
    from django.urls import path
    from main.views import show_main

    app_name = 'main'

    urlpatterns = [
        path('', show_main, name='show_main'),
    ]
    ```

###### RUNNING DAN TESTING PROYEK

30. Jalankan proyek Django dengan perintah berikut.
    ```bash
    python manage.py runserver
    ```
31. Bukalah laman http://localhost:8000/ dan lihat perubahannya.
32. Di direktori `main`, bukalah berkas `tests.py`.
33. Isi berkas tersebut dengan kode berikut :

    ```python
    from django.test import TestCase, Client
    from .models import Product

    class mainTest(TestCase):
        def test_main_url_is_exist(self):
            response = Client().get('')
            self.assertEqual(response.status_code, 200)

        def test_main_using_main_template(self):
            response = Client().get('')
            self.assertTemplateUsed(response, 'main.html')

        def test_nonexistent_page(self):
            response = Client().get('/skibidi/')
            self.assertEqual(response.status_code, 404)

        def test_available(self):
            product = Product.objects.create(
              name="Baju",
              description="Warna putih",
              price = 100000,
              quantity = 10,
            )
            self.assertTrue(product.is_available)
    ```

34. Jalankanlah berkas tes menggunakan perintah berikut :
    ```bash
    python manage.py test
    ```
35. Jika tes berhasil dan aman, maka akan muncul informasi berikut :

    ```bash
    Found 4 test(s).
    Creating test database for alias 'default'...
    System check identified no issues (0 silenced).
    ..
    ----------------------------------------------------------------------
    Ran 4 tests in 0.016s

    OK
    Destroying test database for alias 'default'...
    ```

##### Check 7: Membuat _deployment_ ke PWS terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-teman.

###### ADD, COMMIT, PUSH GITHUB :

36. Lakukan inisiasi direktori lokal `forza-shop` sebagai repositori git dengan menjalankan perintah berikut pada terminal :
    ```bash
    git init
    ```
37. Kemudian, tandai semua _file_ yang berada pada direktori tersebut sebagai _file_ yang akan di-_commit (tracked)_ dengan perintah berikut :
    ```bash
    git add .
    ```
38. Lanjutkan membuat pesan _commit_ yang sesuai dengan perubahan atau pembaharuan dengan perintah berikut :
    ```bash
    git commit -m "<PESAN KAMU>"
    ```
39. Pastikan saat ini kamu berada pada branch _main_ dengan menjalankan perntah berikut :
    ```bash
    git branch -M main
    ```
40. Hubungkan repositori lokal (direktori saat ini) dengan repositori di Github kamu dengan perintah berikut :
    ```bash
    git remote add origin <URL_REPO>
    ```

- Note : ubah `<URL_REPO>` dengan url github yang baru kamu buat.

41. Kemudian, push seluruh berkas ke repositori github dengan perintah berikut :
    ```bash
    git push -u origin main
    ```

###### PUSH PWS :

42. Buka halaman PWS pada https://pbp.cs.ui.ac.id/ , kemudian buatlah akun atau _Register_ menggunakan akun SSO kamu.
43. Lakukan _login_ menggunakan akun yang baru saja kamu buat.
44. Buatlah proyek baru dengan menekan tombol `Create New Project`. Kamu akan berpindah ke halaman untuk membuat proyek baru. Silahkan isi `Project Name` dengan forzashop. Setelah itu, tekan tombol `Create New Project` yang berwarna biru.
45. Simpan informasi _Project Credentials_ di tempat yang dan pastikan tidak hilang karena akan digunakan di langkah selanjutnya. **Jangan jalankan dulu instruksi _Project Command_.**
46. Lakukanlah update pada berkas `settings.py` di proyek Django kamu, tambahkan URL _deployment PWS_ pada variabel `ALLOWED_HOSTS` seperti kode berikut :
    ```python
    ...
    ALLOWED_HOSTS = ["localhost", "127.0.0.1", <NAMA DEPAN>-<NAMA TENGAH>-forzashop.pbp.cs.ui.ac.id]
    ...
    ```

- Note : ganti `<NAMA DEPAN>` dan `<NAMA TENGAH>` sesuai akun SSO kamu. Misal : jeremia-rangga-forzashop.pbp.cs.ui.ac.id .

47. Jalankan perintah berikut untuk melakukan push repositori lokal ke PWS kamu (jalankan satu per satu tiap baris) :

    ```bash
    git remote add pws http://pbp.cs.ui.ac.id/<USERNAME PWS>/forzashop

    git branch -M master

    git push pws master
    ```

48. Setelah menjalankan perintah tersebut, kamu akan diminta `username` dan `password`. Gunakan _Project Credentials_ yang telah kamu simpan (ingat kembali langkah 45).
49. Setelah menjalankan perintah tersebut, silahkan kembalikan branch ke main dengan perintah berikut :
    ```bash
    git branch -M main
    ```
50. Cari proyek kamu di laman PWS, kemudian cek statusnya. Jika status `Building` maka tunggu beberapa saat hingga status berubah menjadi `Running`.
51. Jika sudah `Running`, silahkan tekan tombol `View Project` lalu copy linknya dan buka di aplikasi Google Chrome. Pastikan https:// diganti dengan http:// pada link tersebut.

### 2) Bagan request client ke web aplikasi

![Bagan request & response Django](https://media.discordapp.net/attachments/1282983858366709760/1282983954428727297/image.png?ex=66e1576b&is=66e005eb&hm=517619d624477fa55cb868d4a1212506b33e854c7b3291eb4ed0586939663fe0&=&format=webp&quality=lossless&width=1428&height=994)


1.  **Client Request**: _Request_ dimulai dari klien (browser atau aplikasi lain dari pengguna) yang mengirimkan permintaan ke server.
2.  **urls.py**: Berkas ini berfungsi pengarah lalu lintas dalam aplikasi Django atau _routing_. Berkas ini yang menentukan URL mana yang perlu dipanggil dan view mana yang menanganinya. Ketika ada permintaan yang diterima, Django akan mencocokan URL dari permintaan dengan URL yang didefinisikan di `urls.py`.
3.  **views.py**: Setelah `urls.py` menentukan view mana yang harus merespons, kontrol dialihkan ke fungsi atau kelas di berkas `views.py`.
    View bertugas untuk memproses data yang diterima dan memberikan repsons yang sesuai kepada klien. Ini mungkin melibatkan pemanggilan data dari database melalui berkas model.
4.  **models.py**: View dapat berinteraksi dengan `models.py` untuk meminta data dari database.
    Berkas model pada Django mendefinisikan struktur data, menyediakan alat untuk manajemen database seperti mengambil, menambah atau mengubah data (query data).
5.  **Database**: berfungsi untuk menyimpan data yang nantinya akan diambil maupun ditambah.
6.  **models.py**: Data yang diambil dari database dikembalikan ke `models.py`, yang kemudian mengirimkannya kembali ke `views.py`.
7.  **views.py**: Setelah data diterima dari model, view memproses data tersebut dan mempersiapkan konten (biasanya berupa berkas HTML) untuk dikirim kembali ke klien.
8.  **HTML Template**: HTML templat diisi dengan data atau konteks yang disediakan oleh view. Templat ini kemudian di-render menjadi HTML lengkap yang siap dikirim ke klien melalui browser.
9.  **Client Response**: HTML yang sudah di-render dikirim kembali ke klien sebagai respons atas permintaan awal mereka.


### 3) Penjelasan fungsi git

GIT adalah alat yang digunakan oleh developer dan programmer sebagai sistem kontrol dalam pengembangan perangkat lunak. Tujuan utama dari GIT adalah untuk mengatur versi dari kode sumber, memungkinkan penentuan baris dan kode yang perlu ditambahkan atau diubah. Git dikembangkan oleh Linus Torvalds pada tahun 2005.

Berikut adalah fungsi git dalam pengembagan perangkat lunak :

1.  **Kontrol Versi**: Git memungkinkan _developer_ untuk menyimpan versi berbeda dari sebuah proyek (versi lama atau versi terkini). Hal ini memudahkan _developer_ untuk kembali ke versi sebelumnya, jika _software_ atau aplikasi mengalami masalah pada versi terbaru.
2.  **Kolaborasi**: Git sangat memudahkan kerja tim antar _developer_. Beberapa _developer_ dapat bekerja secara bersamaan pada proyek yang sama tanpa mengganggu pekerjaan orang lain. Git dapat mengelola perubahan dari semua _developer_ dan membantu menggabungkan atau _merging_ pekerjaan mereka secara efisien.
3.  **Pelacakan Perubahan**: Git mencatat setiap perubahan yang dibuat pada kode sumber atau kode utama. Ini mencakup informasi tentang siapa yang membuat perubahan, kapan perubahan itu dibuat, dan detail tentang apa yang diubah.
4.  **Pengembangan Paralel**: Git mendukung pembuatan cabang (_branches_) yang memungkinkan pengembang untuk bekerja pada fitur atau perbaikan secara terpisah dari kode utama (_main branch_). Cabang-cabang ini kemudian dapat digabungkan (_merge_) kembali ke cabang utama setelah pekerjaan selesai. Hal ini memudahkan _developer_ jika ingin mengembangkan fitur baru tanpa mengubah kode sumber atau kode utama.
5.  **Pemulihan**: Tersimpannya semua versi kode, memudahkan _developer_ untuk mengakses dan mengembalikan kode ke keadaan semula jika terjadi kesalahan atau data hilang.
6.  **Kemudahan Penggunaan**: Meskipun menyediakan fungsi kontrol versi yang canggih, Git dirancang untuk mudah digunakan. Ini memungkinkan _developer_ untuk fokus pada pengembangan perangkat lunak daripada mengelola perubahan kode.
7.  **Integrasi dengan Alat Lain**: Git dapat berintegrasi dengan baik dengan berbagai alat pengembangan perangkat lunak lainnya, termasuk _platform_ hosting seperti GitHub, GitLab, dan Bitbucket, serta alat pelacakan isu.
8.  **Kinerja Tinggi**: Git dirancang untuk memberikan kinerja yang cepat dan efisien bahkan dalam proyek dengan riwayat yang sangat besar atau bahkan banyak cabang (_branch_).

Pada intinya, git sangat berguna untuk pengembangan perangkat lunak. _Developer_ memungkinkan melakukan banyak hal seperti kolaborasi hingga penyimpanan perubahan kode dengan sangat mudah.

### 4) Alasan Django dijadikan permulaan pembelajaran pengembangan perangkat lunak

Menurut saya, Django menjadi pilihan pertama karena kita sebagai mahasiswa FASILKOM UI sudah mempelajari dasar bahasa yang digunakan Django yaitu python di semester 1. Hal ini tentu mempermudah dan mempercepat pembelajaran framework Django tanpa perlu mempelajari lagi python. Selain itu, Django juga memiliki struktur yang terorganisir berdasarkan pola desain "Model-View-Template" (MVT), yang memudahkan pemula memahami bagaimana aplikasi web dapat berinteraksi dengan database, mengelola logika, dan menampilkan data. Django juga menawarkan library yang sangat lengkap, mencakup banyak fitur bawaan seperti sistem autentikasi dan formulir, yang mengurangi kebutuhan untuk menulis kode dari nol.

Tentu masih banyak lagi keunggulan dari Django. Namun, hal yang sudah saya sebutkan diatas mencakup keseluruhan keunggulan utama dari Django.

### 5) Alasan mengapa model pada Django disebut sebagi ORM

Model dalam Django disebut sebagai ORM, yang merupakan singkatan dari "Object-Relational Mapping". ORM memungkinkan _developer_ untuk berinteraksi dengan database menggunakan kode yang berorientasi objek, bukan dengan menggunakan SQL langsung.

Berikut adalah beberapa alasan mengapa model Django disebut sebagai ORM:

1.  **Abstraksi**: ORM di Django menyediakan lapisan abstraksi yang memungkinkan _developer_ untuk berinteraksi dengan database melalui objek Python. Ini mengabstraksi kompleksitas SQL, sehingga _developer_ dapat bekerja lebih banyak dengan konsep Python daripada dengan detail database.
2.  **Manajemen Data**: Dengan ORM, objek dalam kode Python dapat dengan mudah dibuat, dibaca, diperbarui, dan dihapus melalui database tanpa perlu menulis kueri SQL secara eksplisit.
3.  **Portabilitas**: Kode yang menggunakan ORM lebih portabel. Artinya, aplikasi Django dapat beralih antar jenis database dengan perubahan konfigurasi minimal.
4.  **Keamanan**: ORM juga membantu dalam meningkatkan keamanan aplikasi. Penggunaan ORM mengurangi risiko serangan injeksi SQL, karena kueri yang dibangun melalui ORM lebih terstruktur dan dikontrol ketat oleh sistem.
5.  **Efisiensi Pengembangan**: Menggunakan ORM mempercepat proses pengembangan karena mengurangi jumlah kode yang perlu ditulis dan diuji. Ini juga membantu dalam memelihara kode yang lebih bersih dan lebih mudah untuk dimengerti dengan menggunakan hanya satu bahasa.


## Tugas 3

### 1) Mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?

Data delivery dibutuhkan dalam pengimplementasian platform untuk mengirimkan dan menerima data antara server dan klien, baik untuk pertukaran informasi antar sistem atau menampilkan data di frontend. Dengan data delivery, platform dapat berfungsi dinamis dan interaktif, memungkinkan pengguna untuk mengakses, mengirim, dan menyimpan informasi secara efisien.

### 2) Mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?

Mana yang lebih baik tergantung pada kebutuhan spesifik. XML lebih baik dalam menangani struktur yang kompleks dengan skema yang jelas, sedangkan JSON lebih sederhana dan lebih ringan. JSON lebih populer dibandingkan XML karena lebih mudah dibaca dan ditulis oleh manusia, memiliki ukuran yang lebih kecil, dan lebih cepat diakses dalam banyak aplikasi web modern. Selain itu, JSON juga lebih mudah diintegrasikan dengan JavaScript, yang banyak digunakan dalam pengembangan aplikasi berbasis web.

### 3) Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?

Method is_valid() pada form Django digunakan untuk memvalidasi data yang diinputkan pengguna berdasarkan aturan yang ditentukan dalam model atau form. Kita membutuhkan method ini untuk memastikan bahwa data yang diinput memenuhi kriteria yang diharapkan (seperti panjang karakter, tipe data, dll.) sebelum disimpan ke database. Jika validasi gagal, form akan mengembalikan pesan error yang dapat ditampilkan kepada pengguna.

### 4) Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?

CSRF (Cross-Site Request Forgery) token dibutuhkan untuk mencegah serangan CSRF, di mana penyerang dapat memalsukan permintaan dari pengguna yang sudah diautentikasi. Jika kita tidak menambahkan csrf_token pada form Django, aplikasi kita rentan terhadap serangan ini, di mana penyerang dapat mengirimkan permintaan yang tidak sah atas nama pengguna tanpa sepengetahuan mereka. Serangan ini dapat dimanfaatkan untuk mengambil alih akun pengguna, memodifikasi data, atau melakukan aksi berbahaya lainnya.

### 5) Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

Berikut langkah-langkah implementasi checklist:

1. Membuat form input: Saya membuat file forms.py di dalam direktori main dan mendefinisikan BuyEntryForm untuk menerima input dari model BuyEntry. Kemudian, di dalam views.py, saya membuat fungsi create_Buy_entry yang menangani form ini dan menambahkan data ke database saat validasi berhasil.

2. Menambahkan views baru untuk XML dan JSON: Saya menambahkan dua fungsi di views.py, yaitu show_xml dan show_json, yang masing-masing mengembalikan data dalam format XML dan JSON. Saya juga menambahkan versi by ID untuk setiap format dengan membuat show_xml_by_id dan show_json_by_id.

3. Routing URL: Di urls.py, saya membuat routing untuk setiap view baru (XML, JSON, XML by ID, dan JSON by ID) dengan menambahkan path ke masing-masing fungsi view.

4. Postman untuk tes data: Setelah mengimplementasikan semua views, saya menggunakan Postman untuk memastikan data dikirim dan diterima dengan benar dalam format XML dan JSON melalui permintaan GET ke endpoint yang sudah dibuat. 


### 5) Mengakses keempat URL di poin 2 menggunakan Postman, membuat screenshot dari hasil akses URL pada Postman

![XML](https://media.discordapp.net/attachments/1282983858366709760/1285263799842242611/Screenshot_2024-09-16_223805.png?ex=66e9a2b0&is=66e85130&hm=14e43e94efefac8ac9e72350554a63803de163c3b92b857a07c1b1af2c178180&=&format=webp&quality=lossless&width=1386&height=994)

![JSON](https://media.discordapp.net/attachments/1282983858366709760/1285263799489663069/Screenshot_2024-09-16_223819.png?ex=66eb9cf0&is=66ea4b70&hm=4ebfcdc712c72d8e59f4b54120e53efc0f9dd5c5892c414980b495be3154df5e&=&format=webp&quality=lossless&width=1376&height=994)

![XMLByID](https://media.discordapp.net/attachments/1282983858366709760/1285263799095656448/Screenshot_2024-09-16_223838.png?ex=66e9a2b0&is=66e85130&hm=3beee59d01b259cc278f9df787f6df388c17247371b22c51a8bce6286202321e&=&format=webp&quality=lossless&width=1368&height=994)

![JSONByID](https://media.discordapp.net/attachments/1282983858366709760/1285263798650933320/Screenshot_2024-09-16_223857.png?ex=66eb9cf0&is=66ea4b70&hm=6eb2793c719e317d8dd8efce525948cd891998def6500b11d2f704d893f766d8&=&format=webp&quality=lossless&width=1370&height=994)

## Tugas 4

### 1)

HttpResponseRedirect() adalah objek yang digunakan untuk melakukan pengalihan secara manual dengan menentukan URL, di mana objek ini merupakan turunan dari HttpResponse. Sebaliknya, redirect() adalah fungsi bawaan Django yang secara internal menggunakan HttpResponseRedirect, namun lebih dinamis karena bisa menerima berbagai jenis input, seperti nama view atau objek model, dan secara otomatis memetakan input tersebut menjadi URL yang sesuai menggunakan fungsi reverse(). Ini membuat redirect() lebih fleksibel dibandingkan HttpResponseRedirect(), terutama ketika URL mungkin berubah di masa mendatang. Selain itu, redirect() juga mendukung penggunaan objek model sebagai argumen langsung, yang akan secara otomatis mengarahkan ke URL detail dari objek tersebut. Sedangkan, dengan HttpResponseRedirect(), kita perlu secara manual menangani URL dengan memanfaatkan fungsi reverse().

### 2)

Untuk menghubungkan model Product dengan User di Django, relasi dilakukan dengan menambahkan ForeignKey pada model Product yang mengacu pada model User. Ini memungkinkan produk untuk dikaitkan dengan pengguna yang membuat atau memiliki produk tersebut. Dalam view create_product, ketika pengguna menambahkan produk baru, produk tersebut otomatis dikaitkan dengan pengguna yang sedang login melalui request.user. Pengguna ini kemudian disimpan sebagai bagian dari entri produk sebelum data produk disimpan ke basis data. Selain itu, di view show_main, produk yang ditampilkan difilter berdasarkan pengguna yang sedang login, menggunakan Product.objects.filter(user=request.user), sehingga hanya produk yang dimiliki oleh pengguna tersebut yang akan ditampilkan di halaman. Hal ini memastikan bahwa produk yang dibuat dan ditampilkan relevan dengan pengguna yang sedang mengakses aplikasi.

Dalam kode yang saya terapkan pada tugas ini, ada beberapa penghubungan yang saya lakukan. Berikut penjelasannya :

**1. Relasi antara `product` dan `user` di Model :**

Untuk menghubungkan model `Product` dengan pengguna (`User`), kita perlu menambahkan sebuah **ForeignKey** yang menghubungkan model `Product` dengan model `User`. Model `User` Django diimpor dari `django.contrib.auth.models`. Contoh definisi model untuk menghubungkan `Product` dan `User` bisa dilihat dari kode berikut :

```python
from django.db import models
import uuid
from django.contrib.auth.models import User

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.IntegerField()
    quantity = models.IntegerField()

    @property
    def is_available(self):
        return self.quantity > 0
```

**2. Penguhubungan di `create_product` View :**

Pada view `create_product`, ketika pengguna menambahkan produk baru, produk tersebut dihubungkan dengan pengguna yang sedang login melalui penggunaan `request.user`. Ini dilakukan dengan menambahkan pengguna ke `product_entry` sebelum disimpan ke basis data:

```python
def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST" :
        product_entry = form.save(commit=False)
        product_entry.user = request.user
        product_entry.save()
        return redirect('main:show_main')

    context = {'form': form}

    return render(request, "create_product.html", context)
```

**3. Filter produk berdasarkan pengguna**

Di view `show_main`, kita perlu memfilter produk berdasarkan pengguna yang sedang login menggunakan `Product.objects.filter(user=request.user)`. Ini memastikan bahwa hanya produk yang dibuat oleh pengguna tersebut yang ditampilkan:

```python
@login_required(login_url='/login')
def show_main(request):
    products = Product.objects.filter(user=request.user)  # Hanya ambil produk milik pengguna yang sedang login
    context = {
        'app' : 'Toko Ungu',
        'name': 'Jeremia Rangga',
        'class': 'PBP B',
        'products': products,  # Kirim produk ke template
        'last_login': request.COOKIES['last_login'],
        'username': request.user,
    }

    return render(request, "main.html", context)
```

### 3)

Authentication (autentikasi) dan authorization (otorisasi) adalah dua konsep penting dalam keamanan aplikasi web yang sering digunakan bersama. Autentikasi adalah proses untuk memverifikasi identitas pengguna, seperti ketika pengguna memasukkan nama pengguna dan kata sandi saat login, dan sistem memastikan bahwa kredensial tersebut sesuai dengan data yang ada di database. Di Django, autentikasi dikelola menggunakan modul django.contrib.auth, yang menyimpan informasi pengguna setelah berhasil diverifikasi. Jika kredensial valid, Django akan membuat sesi untuk menyimpan informasi login pengguna.

Di sisi lain, otorisasi adalah proses untuk memeriksa apakah pengguna memiliki izin atau hak akses untuk fitur tertentu di aplikasi, seperti mengedit atau melihat data. Django mengelola otorisasi melalui sistem izin (permissions) dan grup (groups), memungkinkan penentuan akses berdasarkan peran pengguna. Dekorator seperti @login_required dan @permission_required digunakan untuk membatasi akses ke halaman tertentu berdasarkan autentikasi dan izin.

Ketika pengguna login, Django pertama kali memverifikasi kredensial pengguna (autentikasi). Setelah autentikasi berhasil, sesi dibuat untuk menyimpan informasi pengguna. Berdasarkan otorisasi, Django kemudian mengecek apakah pengguna memiliki izin yang cukup untuk mengakses halaman atau fitur tertentu. Jika tidak, akses akan ditolak.

### 4)

Django memanfaatkan sesi dan cookie untuk mengelola pengguna yang telah login, sehingga pengguna tidak perlu login ulang setiap kali melakukan interaksi baru dengan server. Setelah pengguna berhasil login, Django secara otomatis membuat sesi khusus yang menyimpan informasi identitas pengguna, seperti ID pengguna, di sisi server. Informasi penting ini kemudian dihubungkan dengan ID sesi yang disimpan dalam sebuah cookie di browser pengguna. Ketika pengguna membuat permintaan (request) baru ke server, cookie tersebut dikirim kembali bersama permintaan, memungkinkan Django mengenali dan mengautentikasi pengguna tanpa memerlukan login ulang. Proses ini dikelola oleh Session Middleware yang memastikan bahwa setiap sesi dan cookie berfungsi dengan baik sesuai kebutuhan aplikasi. Selain itu, cookies memiliki kegunaan lain dalam pengembangan aplikasi web. Mereka sering digunakan untuk menyimpan preferensi pengguna, seperti pengaturan bahasa, tema, atau tata letak, yang membantu menjaga konsistensi pengalaman pengguna di berbagai sesi. Di sektor e-commerce, cookie digunakan untuk menyimpan item yang dimasukkan pengguna ke dalam keranjang belanja sehingga barang-barang tersebut tetap tersedia meskipun pengguna belum melakukan pembelian.

Cookies juga digunakan untuk melacak aktivitas pengguna di situs web melalui alat analitik, seperti Google Analytics, yang membantu pemilik situs memahami bagaimana pengguna berinteraksi dengan situs tersebut, termasuk halaman mana yang paling sering dilihat atau berapa lama waktu yang dihabiskan pada setiap halaman. Di sisi lain, dalam aplikasi yang menggunakan autentikasi berbasis token, seperti JSON Web Token (JWT), cookies sering digunakan untuk menyimpan token autentikasi yang memungkinkan pengguna tetap terhubung selama sesi berjalan. Cookies juga memainkan peran penting dalam pengiklanan, di mana data yang dikumpulkan dari kebiasaan pengguna di internet dapat digunakan untuk menampilkan iklan yang lebih relevan berdasarkan perilaku online mereka.

Namun, tidak semua cookie aman digunakan. Meski memiliki manfaat besar, cookies dapat menjadi sasaran serangan seperti Cross-Site Scripting (XSS), di mana penyerang dapat mengakses data sensitif yang disimpan di dalam cookie. Selain itu, cookies yang dikirim melalui koneksi tidak aman, seperti HTTP biasa, sangat rentan terhadap serangan man-in-the-middle, di mana data pengguna bisa dicegat oleh pihak ketiga. Ini berarti informasi yang dikirimkan melalui cookie dapat dicuri atau bahkan dimanipulasi oleh penyerang. Selain itu, menyimpan informasi sensitif dalam cookie, seperti kata sandi atau informasi pribadi, dapat berbahaya jika perangkat yang digunakan tidak aman atau diakses oleh orang lain. Oleh karena itu, meskipun cookie sangat membantu dalam meningkatkan pengalaman pengguna dan pengelolaan aplikasi, penting untuk memastikan bahwa cookie tersebut dikelola dengan hati-hati dan dilindungi dengan mekanisme keamanan yang tepat, seperti menggunakan koneksi HTTPS untuk mengenkripsi data yang dikirimkan antara pengguna dan server.

### 5)

##### Check 1 : Mengimplementasikan fungsi registrasi, login, dan logout untuk memungkinkan pengguna untuk mengakses aplikasi sebelumnya dengan lancar.

1. Sebelum memulai, saya harus mengaktifkan _virtual environment_ terlebih dahulu pada terminal menggunakan command sebagai berikut :
   ```bash
   python -m venv env
   env\Scripts\activate
   ```
2. Untuk membuat register form, saya perlu menambahkan fungsi register pada file `views.py` di subdirektori `main` seperti kode berikut :

   ```python
   from django.contrib.auth.forms import UserCreationForm
   from django.contrib import messages

   ...
   def register(request):
       form = UserCreationForm()

       if request.method == "POST":
           form = UserCreationForm(request.POST)
           if form.is_valid():
               form.save()
               messages.success(request, 'Your account has been successfully created!')
               return redirect('main:login')
       context = {'form':form}
       return render(request, 'register.html', context)
   ...
   ```

3. Saya juga perlu membuat berkas HTML baru dengan nama `register.html` pada direktori `main/templates`. Saya mengisi berkas tersebut dengan kode berikut :

   ```html
   {% extends 'base.html' %} {% block meta %}
   <title>Register</title>
   {% endblock meta %} {% block content %}

   <div class="login">
     <h1>Register</h1>

     <form method="POST">
       {% csrf_token %}
       <table>
         {{ form.as_table }}
         <tr>
           <td></td>
           <td>
             <input
               type="submit"
               name="submit"
               value="Daftar"
             />
           </td>
         </tr>
       </table>
     </form>

     {% if messages %}
     <ul>
       {% for message in messages %}
       <li>{{ message }}</li>
       {% endfor %}
     </ul>
     {% endif %}
   </div>

   {% endblock content %}
   ```

4. Selain register, saya juga perlu menambahkan fungsi login pada file `main/views.py`. Berikut penambahannya :

   ```python
   from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
   from django.contrib.auth import authenticate, login
   ...
   def login_user(request):
      if request.method == 'POST':
         form = AuthenticationForm(data=request.POST)

         if form.is_valid():
               user = form.get_user()
               login(request, user)
               response = HttpResponseRedirect(reverse("main:show_main"))
               response.set_cookie('last_login', str(datetime.datetime.now()))
               return response

      else:
         form = AuthenticationForm(request)
      context = {'form': form}
      return render(request, 'login.html', context)
   ...
   ```

5. Kemudian, saya juga perlu membuat berkas html baru untuk login pengguna. Saya membuat berkas tersebut pada direktori `main/templates/login.html` dengan kode sebagai berikut :

   ```html
   {% extends 'base.html' %} {% block meta %}
   <title>Login</title>
   {% endblock meta %} {% block content %}

   <div class="card m-4">
     <h5 class="card-header text-center">Login</h5>
     <div class="card-body d-flex justify-content-center">
       <div class="login">
         <form
           method="POST"
           action=""
         >
           {% csrf_token %}
           <table>
             {{ form.as_table }}
             <tr>
               <td></td>
               <td>
                 <input
                   class="btn login_btn btn-primary mt-3"
                   type="submit"
                   value="Login"
                 />
               </td>
             </tr>
           </table>
         </form>
         {% if messages %}
         <ul>
           {% for message in messages %}
           <li>{{ message }}</li>
           {% endfor %}
         </ul>
         {% endif %}
         <div class="d-flex m-1">
           <p>Don't have an account yet?</p>
           <a
             class="link-primary link-offset-2 link-underline-opacity-25 link-underline-opacity-100-hover"
             href="{% url 'main:register' %}"
             >Register Now</a
           >
         </div>
       </div>
     </div>
   </div>

   {% endblock content %}
   ```

6. Terakhir, saya juga perlu menambahkan fungsi logout agar pengguna dapat keluar dari akunnya. Berikut adalah penambahan kodenya pada `main/views.py`:
   ```python
   from django.contrib.auth import logout
   ...
   def logout_user(request):
       logout(request)
       response = HttpResponseRedirect(reverse('main:login'))
       response.delete_cookie('last_login')
       return response
   ...
   ```
7. Saya juga perlu menambahkan tombol logout pada berkas HTML `templates/main.html` agar pengguna dapat menekan dan keluar dari akunnya. Saya menambahkan kode berikut di bagian bawah berkas :
   ```html
   ...
   <a
     class="btn btn-primary"
     href="{% url 'main:logout' %} "
   >
     <button>Logout</button>
   </a>
   ...
   ```
8. Selanjutnya, saya perlu untuk melakukan routing ke ketiga fungsi tersebut dengan cara menambahkan _path url_ ke dalam `urlpatterns` untuk dapat mengakses ketiga fungsi tadi. Saya melakukan ini di file `main/urls.py`, berikut kode saya :

   ```python
   from django.urls import path
   from main.views import show_main, create_product, show_xml, show_json, show_xml_by_id, show_json_by_id
   from main.views import register, login_user, logout_user

   app_name = 'main'

   urlpatterns = [
       path('', show_main, name='show_main'),
       path('create-product', create_product, name='create_product'),
       path('xml/', show_xml, name='show_xml'),
       path('json/', show_json, name='show_json'),
       path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
       path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
       path('register/', register, name='register'), # Tambahkan ini
       path('login/', login_user, name='login'), # Tambahkan ini
       path('logout/', logout_user, name='logout'), # Tambahkan ini
   ]
   ```

9. Saya perlu merestriksi akses halaman agar hanya pengguna yang sudah log in saja yang dapat mengakses. Caranya adalah dengan menambahkan dekorator tepat diatas fungsi show_main. Berikut contoh kodenya :
   ```python
   ...
   @login_required(login_url='/login')
   def show_main(request):
   ...
   ```

##### Check 3 :Menghubungkan model `Product` dengan `User`.

10. Untuk menghubungkan model `Product` dengan `User`, saya perlu melakukan penambahan kode di file `main/models.py`. Berikut penambahannya :

    ```python
    from django.db import models
    import uuid
    from django.contrib.auth.models import User # Tambahkan baris ini

    class Product(models.Model):
        user = models.ForeignKey(User, on_delete=models.CASCADE) # Tambahkan baris ini
        id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
        name = models.CharField(max_length=255)
        description = models.TextField()
        price = models.IntegerField()
        quantity = models.IntegerField()

        @property
        def is_available(self):
            return self.quantity > 0
    ```

11. Kemudian, jangan lupa untuk melakukan migrate setelah perubahan pada `models.py`. Berikut commandnya :

    ```bash
    python manage.py  makemigrations
    python manage.py migrate
    ```

12. Saya perlu melakukan perubahan pada file `main/views.py` khususnya dibagian fungsi `create_product`. Berikut perubahannya :

    ```python
    def create_product(request):
        form = ProductForm(request.POST or None)

        if form.is_valid() and request.method == "POST" :
            product_entry = form.save(commit=False) # Perubahan
            product_entry.user = request.user # Perubahan
            product_entry.save()
            return redirect('main:show_main')

        context = {'form': form}

        return render(request, "create_product.html", context)
    ```

13. Kemudian, saya juga perlu melakukan sedikit perubahan pada fungsi `show_main` menjadi sebagai berikut :

    ```python
    @login_required(login_url='/login')
    def show_main(request):
        products = Product.objects.filter(user=request.user) # Perubahan
        context = {
            'app' : 'Toko Ungu',
            'name': request.user.username, # Perubahan
            'class': 'PBP B',
            'products': products,
            'last_login': request.COOKIES['last_login'],
        }

        return render(request, "main.html", context)
    ```

##### Check 4 : Menampilkan detail informasi pengguna yang sedang _logged in_ seperti _username_ dan menerapkan `cookies` seperti `last login` pada halaman utama aplikasi.

14. Untuk menerapkan cookies pada last login, saya perlu melakukan perubahan pada `main/views.py` sebagai berikut :
    ```python
    ...
    if form.is_valid():
                user = form.get_user()
                login(request, user)
                response = HttpResponseRedirect(reverse("main:show_main"))
                response.set_cookie('last_login', str(datetime.datetime.now()))
                return response
    ...
    ```
15. Saya juga perlu menambahkan baris kode baru pada fungsi `show_main`. Berikut penambahannya :
    ```python
    ...
    context = {
            'app' : 'Toko Ungu',
            'name': request.user.username,
            'class': 'PBP B',
            'products': products,
            'last_login': request.COOKIES['last_login'], # Penambahan
        }
     ...
    ```
16. Agar last_login ditampilkan maka saya perlu untuk melakukan penambahan kode di berkas `main.html`. Berikut penambahannya :
    ```html
    <!-- UserName Card -->
    <div class="px-3 py-1">
      <div class="card">
        <div class="card-header"><b>User Data :</b></div>
        <div class="card-body">
          <p>Username : <i>{{ name }}</i></p>
          <div
            class="alert alert-warning mt-3"
            role="alert"
          >
            <b>Sesi terakhir login : <i>{{ last_login }}</i></b>
          </div>
        </div>
      </div>
    </div>
    <!-- END UserName Card -->
    ```
17. Langkah terakhir, saya perlu mempersiapkan aplikasi ini untuk _environment production_. Untuk itu, saya perlu menambahkan kode pada direktori `toko_ungu/settings.py` dengan kode berikut :

```python
PRODUCTION = os.getenv("PRODUCTION", False)
DEBUG = not PRODUCTION
```

### 6) Bukti Checklist 2

1. Akun Pertama
![AKUN1](https://media.discordapp.net/attachments/1282983858366709760/1288352836249452575/Screenshot_2024-09-25_111119.png?ex=66f4df94&is=66f38e14&hm=8402b5e4ba151f29f09c056d146a05d1e651cc308234722bff1e53d8d58448ea&=&format=webp&quality=lossless&width=1590&height=994)

![AKUN1ISI](https://media.discordapp.net/attachments/1282983858366709760/1288352835649409065/Screenshot_2024-09-25_111128.png?ex=66f4df94&is=66f38e14&hm=16eb8138bf9b4d03614cd75a250d376637dca5c79b43ac24218a69124ad7c4ce&=&format=webp&quality=lossless&width=1590&height=994)

![AKUN2](https://media.discordapp.net/attachments/1282983858366709760/1288352834927984662/Screenshot_2024-09-25_111223.png?ex=66f4df94&is=66f38e14&hm=c863ddad380cf050c838db4fe2dee2dfa3adbe0d3851514a540158985dc83a3e&=&format=webp&quality=lossless&width=1590&height=994)

![AKUN2ISI](https://media.discordapp.net/attachments/1282983858366709760/1288352834286518343/Screenshot_2024-09-25_111335.png?ex=66f4df94&is=66f38e14&hm=8b14e7a5672df3402099ac3bca27125c364f099092d2ca0da9cee8679abfef8f&=&format=webp&quality=lossless&width=1590&height=994)

## Tugas 5

### 1) 
Jika terdapat beberapa CSS selector yang diterapkan pada elemen HTML yang sama, browser akan menentukan gaya yang diterapkan berdasarkan urutan prioritas atau spesifisitas (specificity) dari selector tersebut. Specificity ditentukan oleh beberapa faktor, termasuk inline styles yang memiliki prioritas tertinggi, diikuti oleh ID selectors, class selectors, attribute selectors, pseudo-class selectors, dan terakhir element selectors dan pseudo-element selectors. Sebagai contoh, selector berbasis ID seperti #header akan lebih kuat daripada selector berbasis class seperti .main, dan inline styles akan mengalahkan keduanya. Jika dua selector memiliki spesifisitas yang sama, aturan cascading (urutan di mana aturan muncul dalam file CSS) akan menentukan gaya mana yang diterapkan, dengan gaya yang terakhir memiliki prioritas lebih tinggi. Penggunaan !important juga dapat mengubah aturan prioritas ini dengan mengesampingkan spesifisitas selector lain, meskipun ini harus digunakan dengan hati-hati karena dapat membuat kode sulit dipelihara.

### 2)
Responsive design adalah konsep penting dalam pengembangan aplikasi web karena memastikan bahwa website atau aplikasi dapat diakses dengan nyaman dari berbagai perangkat, baik desktop, tablet, maupun ponsel. Dengan semakin banyaknya pengguna yang mengakses internet melalui perangkat seluler, website yang tidak responsif berisiko kehilangan audiens karena tampilan yang tidak optimal. Sebagai contoh, aplikasi seperti Google dan Facebook sudah menerapkan responsive design dengan baik, di mana layout mereka otomatis menyesuaikan dengan ukuran layar pengguna. Sebaliknya, beberapa situs web yang lebih tua atau bisnis lokal kecil mungkin belum responsif, sehingga tampilannya tidak sesuai di perangkat mobile dan mengakibatkan pengalaman pengguna yang buruk. Dalam konteks SEO, responsive design juga penting karena mesin pencari seperti Google mempertimbangkan responsivitas dalam algoritme peringkat mereka, yang dapat mempengaruhi visibilitas situs.

### 3)
Margin, border, dan padding adalah bagian dari model kotak CSS (CSS box model) yang digunakan untuk mengatur jarak dan ruang di sekitar elemen HTML. Margin adalah jarak di luar elemen yang memisahkannya dari elemen lain di sekitar, sedangkan border adalah garis yang mengelilingi elemen di luar padding, memberikan batas visual pada elemen. Padding, di sisi lain, adalah ruang antara konten elemen dan border-nya, yang berguna untuk memberikan jarak antara konten dan tepi elemen itu sendiri. Ketiga komponen ini bekerja bersama untuk mengontrol bagaimana elemen ditempatkan dalam layout, dan masing-masing dapat diatur secara independen menggunakan properti margin, border, dan padding dalam CSS. Dengan memahami perbedaan ini, pengembang web dapat mengatur layout dengan lebih tepat, memastikan elemen-elemen di halaman tampil secara proporsional dan seimbang.

### 4)
Flexbox dan Grid Layout adalah dua model tata letak dalam CSS yang sangat berguna untuk mengatur posisi dan aliran elemen di halaman web. Flexbox adalah model tata letak satu dimensi yang memungkinkan pengaturan elemen secara fleksibel di dalam kontainer, baik dalam arah horizontal maupun vertikal. Flexbox sangat cocok untuk pengaturan tata letak yang sederhana dan responsif, seperti mengatur elemen dalam satu baris atau kolom, dan memberikan kontrol yang mudah atas penyelarasan dan distribusi ruang. Di sisi lain, Grid Layout adalah model tata letak dua dimensi yang lebih kompleks, di mana elemen dapat ditempatkan dalam baris dan kolom. Grid sangat berguna untuk tata letak yang lebih kompleks seperti halaman beranda atau galeri, karena memungkinkan kontrol lebih besar atas ukuran dan posisi elemen. Secara umum, Flexbox lebih baik untuk tata letak linier (satu dimensi), sementara Grid lebih cocok untuk tata letak kompleks (dua dimensi) yang memerlukan penempatan elemen di sepanjang sumbu baris dan kolom.

### 5)
Saya telah berhasil mengimplementasikan seluruh item yang tercantum dalam checklist ini dengan baik. Pertama-tama, saya mengembangkan fungsi untuk menghapus dan mengedit product pada aplikasi, memastikan bahwa pengguna dapat dengan mudah melakukan perubahan atau menghapus produk yang telah disimpan. Setelah itu, saya melakukan kustomisasi desain pada template HTML dengan menggunakan CSS dan CSS framework seperti Bootstrap, Tailwind, atau Bulma, sesuai dengan ketentuan yang telah ditetapkan. Saya fokus untuk membuat halaman login, register, dan halaman tambah product menjadi lebih menarik dan intuitif, sehingga pengguna merasa nyaman saat melakukan interaksi. Kustomisasi ini juga melibatkan pembuatan halaman daftar product yang lebih menarik secara visual dan responsif terhadap berbagai ukuran perangkat.

Pada bagian daftar product, saya mengatasi dua kondisi: ketika belum ada product yang terdaftar, halaman akan menampilkan pesan informatif serta gambar, dan ketika ada product yang terdaftar, saya menampilkan detail setiap product menggunakan desain card yang telah saya buat sendiri (berbeda dari desain tutorial sebelumnya). Saya juga menambahkan dua tombol pada setiap card, yang memungkinkan pengguna untuk mengedit atau menghapus product secara langsung dari card tersebut. Selain itu, saya juga merancang navigation bar (navbar) untuk fitur-fitur utama aplikasi, memastikan bahwa navbar ini responsif dan bisa beradaptasi dengan berbagai ukuran perangkat, baik pada layar mobile maupun desktop, sehingga memberikan pengalaman pengguna yang lebih baik secara keseluruhannya.

## Tugas 6

### 1. 

JavaScript memiliki banyak manfaat dalam pengembangan aplikasi web, di antaranya:

1. **Interaktivitas Dinamis**: JavaScript memungkinkan elemen interaktif seperti tombol, formulir, dan animasi yang merespons tindakan pengguna, menjadikan aplikasi web lebih menarik dan intuitif.
2. **Pengolahan Data di Sisi Klien**: Dengan JavaScript, data dapat dimanipulasi di sisi klien tanpa perlu berulang kali mengirim permintaan ke server, sehingga meningkatkan efisiensi.
3. **Pengembangan Asynchronous (AJAX)**: JavaScript mendukung komunikasi asinkron dengan server menggunakan AJAX, sehingga data dapat diperbarui tanpa harus memuat ulang halaman.
4. **Kompatibilitas Multi-Platform**: JavaScript berjalan di hampir semua browser modern tanpa instalasi tambahan, menjadikannya ideal untuk pengembangan aplikasi web multi-platform.
5. **Mendukung Pengembangan Full-Stack**: JavaScript dapat digunakan di sisi klien dan server dengan framework seperti Node.js, memungkinkan pengembangan full-stack dengan satu bahasa pemrograman.

### 2.

Ketika menggunakan `fetch()`, fungsi ini mengembalikan *promise* yang memerlukan waktu untuk menyelesaikan permintaan ke server. `await` digunakan untuk menunggu *promise* tersebut selesai sebelum melanjutkan eksekusi kode. Dengan `await`, penulisan kode menjadi lebih sinkron dan mudah dibaca.

Contoh:
```javascript
async function getData() {
  const response = await fetch('https://api.example.com/data');
  const data = await response.json();
  console.log(data);
}
```

Jika `await` tidak digunakan, `fetch()` akan langsung mengembalikan *promise*, dan kode berikutnya akan dieksekusi sebelum respons selesai, yang bisa menyebabkan kesalahan dalam pemrosesan data.

### 3.

Decorator `csrf_exempt` digunakan untuk menonaktifkan mekanisme perlindungan **Cross-Site Request Forgery (CSRF)** pada Django. Berikut alasannya:

1. **Token CSRF Diperlukan**: Secara default, Django memerlukan token CSRF untuk semua permintaan POST. AJAX POST juga harus menyertakan token ini.
2. **Mempermudah Permintaan AJAX**: Jika AJAX POST tidak memerlukan token CSRF (misalnya untuk API publik), `csrf_exempt` dapat digunakan untuk mem-bypass pengecekan token CSRF.
3. **Framework Eksternal**: Beberapa framework front-end seperti React atau Vue.js tidak menangani token CSRF secara otomatis. `csrf_exempt` membantu menghindari kesalahan terkait token CSRF pada permintaan POST dari framework tersebut.

Jika `csrf_exempt` tidak digunakan dan AJAX POST tidak mengirimkan token CSRF, Django akan mengembalikan error 403 (Forbidden).

### 4.

Pembersihan data input di **backend** diperlukan karena:

1. **Keamanan yang Lebih Komprehensif**: Pengguna yang berniat jahat bisa memanipulasi permintaan HTTP dan melewati validasi di frontend. Oleh karena itu, backend harus memvalidasi semua input untuk mencegah serangan XSS atau SQL Injection.
2. **Integritas Data**: Pembersihan di backend memastikan bahwa data yang tersimpan di database aman, meskipun frontend telah memvalidasi input.
3. **Tidak Mengandalkan Klien**: Validasi di frontend dapat diabaikan oleh pengguna yang memodifikasi klien mereka. Backend harus memverifikasi keamanan data secara mandiri.

### 5.

#### Checklist 1: Menampilkan Card Product dengan AJAX GET
- Ubah fungsi `show_main` untuk tidak langsung mengirimkan produk dari view, dan modifikasi fungsi `show_json` untuk mengirim data produk milik pengguna yang sedang login.
- Hapus blok conditional dan ganti dengan elemen div `#product_entry_cards` yang kosong.
- Tambahkan script untuk melakukan `fetch()` ke URL `show_json` dan memuat produk dengan AJAX.

#### Checklist 2: Pengambilan Data dengan AJAX GET
- Tambahkan kode untuk memuat data produk milik pengguna yang sedang login menggunakan AJAX GET dan tampilkan produk dalam bentuk cards yang dinamis.

#### Checklist 3: Tombol untuk Membuka Modal dengan Form Penambahan Produk
- Tambahkan tombol yang membuka modal form penambahan produk, yang memanfaatkan AJAX POST untuk menyimpan produk baru.

#### Checklist 4: Fungsi View untuk Menambahkan Produk
- Buat fungsi view `create_product_ajax` di backend yang memproses form data produk baru dan menyimpan data ke database.

#### Checklist 5: Path `/create-ajax/`
- Tambahkan path `/create-ajax/` di `urls.py` yang mengarah ke fungsi `create_product_ajax`.

#### Checklist 6: Hubungkan Form Modal ke Path `/create-ajax/`
- Buat modal dengan form penambahan produk dan hubungkan form tersebut ke path `/create-ajax/` untuk mengirim data dengan AJAX POST.

#### Checklist 7: Refresh Asinkron
- Lakukan refresh asinkron pada halaman utama setelah produk ditambahkan tanpa memuat ulang halaman.

#### Addition: Pencegahan XSS
- Gunakan `DOMPurify` untuk membersihkan data yang akan ditampilkan di halaman dan lakukan validasi input di backend untuk menghindari serangan XSS.