# Docker-Naruto_remainder
<img alt="logo" src="https://raw.githubusercontent.com/riecho14/Docker-Dendam-Si-Tikus/image_assets/logo.svg" width="400">

> Containerize Pygame with Docker.

## Nama dan NIM Anggota Kelompok
| Nama | NIM | Github |
| :---: | :---: | :---: |
|Murliana                       | 120140076 | [Murli235](https://github.com/Murli235)           |
|Muhammad Qomarudin             | 120140116 | [masQ-21dev](https://github.com/masQ-21dev)       |
|Alya Dian Risda                | 120140143 | [Alyaadr](https://github.com/alyaadr)             |
|Ryco Afta Gian Aidil           | 120140159 | [Rycoafta](https://github.com/Rycoafta)           |
|Jhon Penator Sianturi          | 120140138 | [JhonPudan35](https://github.com/JhonPudan35)     |

## Naroto Remainder
#### Deskripsi Projek
Aplikasi ini merupakan permainan yang dibuat menggunakan library pygame. dalam permainan ini
player diminta untuk mencari dua buah kartu yang sama. tujuan dari ini adalah mencari score. Daan tantangan 
dari game ini adalah player harus mencari pasangan setiap katru yang tersedia dalam batas waktu yang ditentukan.
permainan ini terdapat 5 level, yang setiap level nya memiliki jumlah kartu dan waktu yang berbeda.
## Cara Menjalankan Kontainer
Clone repositori ini atau [unduh disini](https://github.com/masQ-21dev/Docker-naruto-remainder/archive/refs/heads/main.zip), dan pastikan folder dari repositori tersebut berada di drictory `~/Documents`.
jika tida, pindahkan folder dari repo tersebut ke folder `~/Documents` seperti pada gambar berikut:
<img alt="Dockument" src="https://github.com/masQ-21dev/Docker-naruto-remainder/blob/main/assets/images/save_Documents.png">

Selanjutnya buka terminal pada direktori folder tersebut lalu jalankan perintah build seperti berikut:

    make build-naruto-remainder

lalu pastikan ada repositori "dendamsitikus" pada docker, dengan cara jalankan command images untuk melihat daftar images pada local storage seperti berikut:

    docker images

Jika proses build telah selesai, jalankan perintah run seperti berikut:
##### untuk Linux

    make run-linux

##### untuk Mac

    make run-mac

Langkah terakhir yaitu menjalankan pygame melalui container yang telah kita buat dengan perintah seperti berikut:

    python3 -m main.py

## container ini hanya bisa di jalanakan di terminal linux dan mac, tidak dapat dijalakan di windows karena di windows tidak terdapat X11
## Video Demo Kontainer

[![LIHAT VIDEO DISINI](http://img.youtube.com/vi/SO_tl0iAmhU/0.jpg)](http://www.youtube.com/watch?v=SO_tl0iAmhU)

KLIK GAMBAR UNTUK MELIHAT VIDEO
