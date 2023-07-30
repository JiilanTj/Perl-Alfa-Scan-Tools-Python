import requests

# Definisi kode warna ANSI Escape Sequence
kuning = "\033[93m"
putih = "\033[97m"
blue = "\033[94m"
merah = "\033[91m"
reset = "\033[0m"

def alfaa(domainn):
    # Definisikan fungsi alfaa() seperti pada skrip yang diberikan
    try:
        domainn = domainn.replace('https://', '').replace('http://', '')
        domainn = 'http://'+domainn
        op = requests.get(domainn + '/ALFA_DATA/alfacgiapi/', timeout=10)
        op1 = requests.get(domainn + '/wp-admin/ALFA_DATA/alfacgiapi/', timeout=10)
        op2 = requests.get(domainn + '/wp-content/ALFA_DATA/alfacgiapi/', timeout=10)
        op3 = requests.get(domainn + '/wp-plugins/ALFA_DATA/alfacgiapi/', timeout=10)
        op4 = requests.get(domainn + '/wp-includes/ALFA_DATA/alfacgiapi/', timeout=10)
        op5 = requests.get(domainn + '/wp-content/plugins/wp-file-manager/lib/php/connector.minimal.php', timeout=10)
        op6 = requests.get(domainn + '/wp-content/plugins/dzs-zoomsounds/savepng.php', timeout=10)
        op7 = requests.get(domainn + '/uploads/pengumuman/ALFA_DATA/alfacgiapi/', timeout=10)
        op8 = requests.get(domainn + '/uploads/ALFA_DATA/alfacgiapi/', timeout=10)
        op9 = requests.get(domainn + '/images/ALFA_DATA/alfacgiapi/', timeout=10)
        op10 = requests.get(domainn + '/img/ALFA_DATA/alfacgiapi/', timeout=10)
        op11 = requests.get(domainn + '/alfacgiapi/', timeout=10)
        op12 = requests.get(domainn + '/wp-admin/alfacgiapi/', timeout=10)
        op13 = requests.get(domainn + '/wp-content/alfacgiapi/', timeout=10)
        op14 = requests.get(domainn + '/wp-plugins/alfacgiapi/', timeout=10)
        op15 = requests.get(domainn + '/wp-includes/alfacgiapi/', timeout=10)
        op16 = requests.get(domainn + '/wp-content/plugins/alfacgiapi/', timeout=10)
        op17 = requests.get(domainn + '/wp-content/plugins/dzs-zoomsounds/alfacgiapi/', timeout=10)
        op18 = requests.get(domainn + '/wp-content/plugins/wp-file-manager/alfacgiapi/', timeout=10)
        op19 = requests.get(domainn + '/uploads/pengumuman/alfacgiapi/', timeout=10)
        op20 = requests.get(domainn + '/uploads/alfacgiapi/', timeout=10)
        op21 = requests.get(domainn + '/uploads/site/alfacgiapi/', timeout=10)
        op22 = requests.get(domainn + '/images/alfacgiapi/', timeout=10)
        op23 = requests.get(domainn + '/img/alfacgiapi/', timeout=10)
        op24 = requests.get(domainn + '/assets/alfacgiapi/', timeout=10)
        op25 = requests.get(domainn + '/assets/files/alfacgiapi/', timeout=10)
        op26 = requests.get(domainn + '/assets/admin/alfacgiapi/', timeout=10)
        op27 = requests.get(domainn + '/assets/images/alfacgiapi/', timeout=10)
        op28 = requests.get(domainn + '/upload/alfacgiapi/', timeout=10)
        op29 = requests.get(domainn + '/wp-content/plugins/ALFA_DATA/alfacgiapi/', timeout=10)
        op30 = requests.get(domainn + '/uploads/pengumuman/ALFA_DATA/alfacgiapi/', timeout=10)
        op31 = requests.get(domainn + '/uploads/ALFA_DATA/alfacgiapi/', timeout=10)
        op32 = requests.get(domainn + '/uploads/site/ALFA_DATA/alfacgiapi/', timeout=10)
        op33 = requests.get(domainn + '/images/ALFA_DATA/alfacgiapi/', timeout=10)
        op34 = requests.get(domainn + '/img/ALFA_DATA/alfacgiapi/', timeout=10)
        op35 = requests.get(domainn + '/assets/ALFA_DATA/alfacgiapi/', timeout=10)
        op36 = requests.get(domainn + '/assets/files/ALFA_DATA/alfacgiapi/', timeout=10)
        op37 = requests.get(domainn + '/assets/admin/ALFA_DATA/alfacgiapi/', timeout=10)
        op38 = requests.get(domainn + '/assets/images/ALFA_DATA/alfacgiapi/', timeout=10)
        op39 = requests.get(domainn + '/upload/ALFA_DATA/alfacgiapi/', timeout=10)
        if 'perl.alfa' in op.text:
            print(kuning + "-|" + putih + domainn + blue + ' ==> ' + hijau + ' Found Alfa ' + reset)
            open("Result/Alfa-perl.txt", "a").write(domainn + '/ALFA_DATA/alfacgiapi/\n')
        elif "perl.alfa" in op1.text:
            print(kuning + "-|" + putih + domainn + blue + ' ==> ' + hijau + ' Found Alfa ' + reset)
            open("Result/Alfa-perl.txt", "a").write(domainn + '/wp-admin/ALFA_DATA/alfacgiapi/\n')
        elif "perl.alfa" in op2.text:
            print(kuning + "-|" + putih + domainn + blue + ' ==> ' + hijau + ' Found Alfa ' + reset)
            open("Result/Alfa-perl.txt", "a").write(domainn + '/wp-content/ALFA_DATA/alfacgiapi/\n')
        elif "perl.alfa" in op3.text:
            print(kuning + "-|" + putih + domainn + blue + ' ==> ' + hijau + ' Found Alfa ' + reset)
            open("Result/Alfa-perl.txt", "a").write(domainn + '/wp-plugins/ALFA_DATA/alfacgiapi/\n')
        elif "perl.alfa" in op4.text:
            print(kuning + "-|" + putih + domainn + blue + ' ==> ' + hijau + ' Found Alfa ' + reset)
            open("Result/Alfa-perl.txt", "a").write(domainn + '/wp-includes/ALFA_DATA/alfacgiapi/\n')
        elif '{"error":["errUnknownCmd"]}' in op5.text:
            print(kuning + "-|" + putih + domainn + blue + ' ==> ' + hijau + ' Found Wpfm ' + reset)
        elif 'error:http raw post data does not exist' in op6.text:
            print(kuning + "-|" + putih + domainn + blue + ' ==> ' + hijau + ' Found Savepng ' + reset)
            open("Result/Savepng.txt", "a").write(domainn + '/wp-content/plugins/dzs-zoomsounds/savepng.php\n')
        elif "perl.alfa" in op7.text:
            print(kuning + "-|" + putih + domainn + blue + ' ==> ' + hijau + ' Found Alfa ' + reset)
            open("Result/Alfa-perl.txt", "a").write(domainn + '/uploads/pengumuman/ALFA_DATA/alfacgiapi/\n')
        elif "perl.alfa" in op8.text:
            print(kuning + "-|" + putih + domainn + blue + ' ==> ' + hijau + ' Found Alfa ' + reset)
            open("Result/Alfa-perl.txt", "a").write(domainn + '/uploads/ALFA_DATA/alfacgiapi/\n')
        elif "perl.alfa" in op9.text:
            print(kuning + "-|" + putih + domainn + blue + ' ==> ' + hijau + ' Found Alfa ' + reset)
            open("Result/Alfa-perl.txt", "a").write(domainn + '/images/ALFA_DATA/alfacgiapi/\n')
        elif "perl.alfa" in op10.text:
            print(kuning + "-|" + putih + domainn + blue + ' ==> ' + hijau + ' Found Alfa ' + reset)
            open("Result/Alfa-perl.txt", "a").write(domainn + '/img/ALFA_DATA/alfacgiapi/\n')
        elif "perl.alfa" in op11.text:
            print(kuning + "-|" + putih + domainn + blue + ' ==> ' + hijau + ' Found Alfa ' + reset)
            open("Result/Alfa-perl.txt", "a").write(domainn + '/alfacgiapi/\n')
        elif "perl.alfa" in op12.text:
            print(kuning + "-|" + putih + domainn + blue + ' ==> ' + hijau + ' Found Alfa ' + reset)
            open("Result/Alfa-perl.txt", "a").write(domainn + '/wp-admin/alfacgiapi/\n')    
        elif "perl.alfa" in op13.text:
            print(kuning + "-|" + putih + domainn + blue + ' ==> ' + hijau + ' Found Alfa ' + reset)
            open("Result/Alfa-perl.txt", "a").write(domainn + '/wp-content/ALFA_DATA/alfacgiapi/\n')
        elif "perl.alfa" in op14.text:
            print(kuning + "-|" + putih + domainn + blue + ' ==> ' + hijau + ' Found Alfa ' + reset)
            open("Result/Alfa-perl.txt", "a").write(domainn + '/wp-plugins/alfacgiapi/\n')   
        elif "perl.alfa" in op15.text:
            print(kuning + "-|" + putih + domainn + blue + ' ==> ' + hijau + ' Found Alfa ' + reset)
            open("Result/Alfa-perl.txt", "a").write(domainn + '/wp-includes/alfacgiapi/\n')
        elif "perl.alfa" in op16.text:
            print(kuning + "-|" + putih + domainn + blue + ' ==> ' + hijau + ' Found Alfa ' + reset)
            open("Result/Alfa-perl.txt", "a").write(domainn + '/wp-content/plugins/dzs-zoomsounds/alfacgiapi/\n')
        elif "perl.alfa" in op17.text:
            print(kuning + "-|" + putih + domainn + blue + ' ==> ' + hijau + ' Found Alfa ' + reset)
            open("Result/Alfa-perl.txt", "a").write(domainn + '/wp-content/plugins/wp-file-manager/alfacgiapi/\n')
        elif "perl.alfa" in op18.text:
            print(kuning + "-|" + putih + domainn + blue + ' ==> ' + hijau + ' Found Alfa ' + reset)
            open("Result/Alfa-perl.txt", "a").write(domainn + '/uploads/alfacgiapi/\n')
        elif "perl.alfa" in op19.text:
            print(kuning + "-|" + putih + domainn + blue + ' ==> ' + hijau + ' Found Alfa ' + reset)
            open("Result/Alfa-perl.txt", "a").write(domainn + '/uploads/site/alfacgiapi/\n')
        elif "perl.alfa" in op20.text:
            print(kuning + "-|" + putih + domainn + blue + ' ==> ' + hijau + ' Found Alfa ' + reset)
            open("Result/Alfa-perl.txt", "a").write(domainn + '/img/ALFA_DATA/alfacgiapi/\n')
        elif "perl.alfa" in op21.text:
            print(kuning + "-|" + putih + domainn + blue + ' ==> ' + hijau + ' Found Alfa ' + reset)
            open("Result/Alfa-perl.txt", "a").write(domainn + '/uploads/pengumuman/alfacgiapi/\n')
        elif "perl.alfa" in op22.text:
            print(kuning + "-|" + putih + domainn + blue + ' ==> ' + hijau + ' Found Alfa ' + reset)
            open("Result/Alfa-perl.txt", "a").write(domainn + '/images/alfacgiapi/\n')
        elif "perl.alfa" in op23.text:
            print(kuning + "-|" + putih + domainn + blue + ' ==> ' + hijau + ' Found Alfa ' + reset)
            open("Result/Alfa-perl.txt", "a").write(domainn + '/img/alfacgiapi/\n')
        elif "perl.alfa" in op24.text:
            print(kuning + "-|" + putih + domainn + blue + ' ==> ' + hijau + ' Found Alfa ' + reset)
            open("Result/Alfa-perl.txt", "a").write(domainn + '/assets/alfacgiapi/\n')
        elif "perl.alfa" in op25.text:
            print(kuning + "-|" + putih + domainn + blue + ' ==> ' + hijau + ' Found Alfa ' + reset)
            open("Result/Alfa-perl.txt", "a").write(domainn + '/assets/files/alfacgiapi/\n')
        elif "perl.alfa" in op26.text:
            print(kuning + "-|" + putih + domainn + blue + ' ==> ' + hijau + ' Found Alfa ' + reset)
            open("Result/Alfa-perl.txt", "a").write(domainn + '/assets/admin/alfacgiapi/\n')
        elif "perl.alfa" in op27.text:
            print(kuning + "-|" + putih + domainn + blue + ' ==> ' + hijau + ' Found Alfa ' + reset)
            open("Result/Alfa-perl.txt", "a").write(domainn + '/assets/images/alfacgiapi/\n')
        elif "perl.alfa" in op28.text:
            print(kuning + "-|" + putih + domainn + blue + ' ==> ' + hijau + ' Found Alfa ' + reset)
            open("Result/Alfa-perl.txt", "a").write(domainn + '/upload/alfacgiapi/\n')
        elif "perl.alfa" in op29.text:
            print(kuning + "-|" + putih + domainn + blue + ' ==> ' + hijau + ' Found Alfa ' + reset)
            open("Result/Alfa-perl.txt", "a").write(domainn + '/wp-content/plugins/ALFA_DATA/alfacgiapi/\n') 
        elif "perl.alfa" in op30.text:
            print(kuning + "-|" + putih + domainn + blue + ' ==> ' + hijau + ' Found Alfa ' + reset)
            open("Result/Alfa-perl.txt", "a").write(domainn + '/uploads/pengumuman/ALFA_DATA/alfacgiapi/\n')         
        elif "perl.alfa" in op31.text:
            print(kuning + "-|" + putih + domainn + blue + ' ==> ' + hijau + ' Found Alfa ' + reset)
            open("Result/Alfa-perl.txt", "a").write(domainn + '/uploads/ALFA_DATA/alfacgiapi/\n')
        elif "perl.alfa" in op32.text:
            print(kuning + "-|" + putih + domainn + blue + ' ==> ' + hijau + ' Found Alfa ' + reset)
            open("Result/Alfa-perl.txt", "a").write(domainn + '/uploads/site/ALFA_DATA/alfacgiapi/\n')
        elif "perl.alfa" in op33.text:
            print(kuning + "-|" + putih + domainn + blue + ' ==> ' + hijau + ' Found Alfa ' + reset)
            open("Result/Alfa-perl.txt", "a").write(domainn + '/images/ALFA_DATA/alfacgiapi/\n') 
        elif "perl.alfa" in op34.text:
            print(kuning + "-|" + putih + domainn + blue + ' ==> ' + hijau + ' Found Alfa ' + reset)
            open("Result/Alfa-perl.txt", "a").write(domainn + '/img/ALFA_DATA/alfacgiapi/\n') 
        elif "perl.alfa" in op35.text:
            print(kuning + "-|" + putih + domainn + blue + ' ==> ' + hijau + ' Found Alfa ' + reset)
            open("Result/Alfa-perl.txt", "a").write(domainn + '/ALFA_DATA/alfacgiapi/\n') 
        elif "perl.alfa" in op36.text:
            print(kuning + "-|" + putih + domainn + blue + ' ==> ' + hijau + ' Found Alfa ' + reset)
            open("Result/Alfa-perl.txt", "a").write(domainn + '/files/ALFA_DATA/alfacgiapi/\n')
        elif "perl.alfa" in op37.text:
            print(kuning + "-|" + putih + domainn + blue + ' ==> ' + hijau + ' Found Alfa ' + reset)
            open("Result/Alfa-perl.txt", "a").write(domainn + '/assets/admin/ALFA_DATA/alfacgiapi/\n')
        elif "perl.alfa" in op38.text:
            print(kuning + "-|" + putih + domainn + blue + ' ==> ' + hijau + ' Found Alfa ' + reset)
            open("Result/Alfa-perl.txt", "a").write(domainn + '/assets/images/ALFA_DATA/alfacgiapi/\n')
        elif "perl.alfa" in op39.text:
            print(kuning + "-|" + putih + domainn + blue + ' ==> ' + hijau + ' Found Alfa ' + reset)
            open("Result/Alfa-perl.txt", "a").write(domainn + '/upload/ALFA_DATA/alfacgiapi/\n')             
        else:
            print(kuning + '-|' + putih + domainn + blue + ' ==> ' + merah + '  Unknown   '+ reset)

    except:
        print(kuning + '-|' + putih + domainn + blue + ' ==> ' + merah + '  Bad Host   '+ reset)

def main():
    while True:
        print("Apakah Anda ingin menggunakan tools?")
        print("1. Iya")
        print("2. Tidak")
        pilihan = input("Masukkan pilihan (1/2): ")

        if pilihan == "1":
            list_filename = input("Masukkan nama file teks yang berisi daftar domain (contoh: list.txt): ")
            try:
                with open(list_filename, 'r') as file:
                    domains = file.readlines()
                for domain in domains:
                    domain = domain.strip()
                    if domain:
                        alfaa(domain)
            except FileNotFoundError:
                print("File tidak ditemukan. Harap periksa nama file dan pastikan file berada di direktori yang sama dengan script.")
            except Exception as e:
                print("Terjadi kesalahan saat membaca file: ", str(e))
        elif pilihan == "2":
            print("Terima kasih telah menggunakan tools.")
            break
        else:
            print("Pilihan tidak valid. Harap masukkan 1 atau 2.")


if __name__ == "__main__":
    main()

