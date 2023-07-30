
ALFA Script - Deskripsi Alat
============================

**ALFA Script** adalah alat berbasis Python dengan antarmuka baris perintah (command-line) yang membantu Anda mencari endpoint tertentu pada situs web. Alat ini akan memeriksa keberadaan endpoint seperti 'alfa\_data/alfacgiapi/' dan 'wp-admin/alfa\_data/alfacgiapi/' untuk mendeteksi potensi kerentanannya atau masalah keamanan pada situs web target.

Cara Penggunaan
---------------

Untuk menggunakan ALFA Script, ikuti langkah-langkah berikut:

1.  Klon repositori atau unduh skrip ke mesin lokal Anda.
2.  Pastikan Anda telah menginstal Python di sistem Anda.
3.  Instal pustaka yang diperlukan dengan perintah berikut:

    pip install requests

**Catatan:** Skrip ini menggunakan pustaka 'requests' untuk mengirim permintaan HTTP. Jika Anda belum menginstalnya, Anda perlu menginstalnya sebelum menjalankan skrip.

Menggunakan Alat
----------------

Untuk menjalankan skrip, buka terminal Anda (atau command prompt), navigasikan ke direktori yang berisi skrip 'alfa.py', dan jalankan perintah berikut:

    python3 alfa.py

Anda akan diminta untuk memilih apakah ingin menggunakan alat ini atau tidak. Jika Anda memilih 'Iya', Anda akan diminta untuk memasukkan nama domain yang ingin Anda periksa. Selain itu, Anda dapat menyediakan daftar domain dalam file teks (misalnya 'list.txt'), dan skrip akan memeriksa setiap domain dalam daftar tersebut.

**Peringatan:** Alat ini dimaksudkan untuk tujuan pendidikan dan pengujian etis saja. Penggunaan yang tidak sah dari alat ini pada situs web yang tidak Anda miliki atau tidak memiliki izin untuk diuji adalah ilegal dan tidak etis. Gunakan dengan bijaksana dan atas risiko Anda sendiri.

Lisensi
-------

Proyek ini dilisensikan di bawah Lisensi MIT. Lihat berkas 'LICENSE' untuk informasi lebih lanjut.
