data_siswa = {
    "Kim Mingyu": {'NamaSiswa': 'Kim Mingyu', 'NIM': '3175001', 'MataPelajaran': 'Biologi', 'NilaiTugas': 88, 'NilaiUTS': 79, 'NilaiUAS': 85, 'Grade': 'A', 'Keterangan': 'Lulus'},
    "Jeon Wonwoo": {'NamaSiswa': 'Jeon Wonwoo', 'NIM': '3175002', 'MataPelajaran': 'Biologi', 'NilaiTugas': 90, 'NilaiUTS': 79, 'NilaiUAS': 80, 'Grade': 'A', 'Keterangan': 'Lulus'},
    "Yoon Jeonghan": {'NamaSiswa': 'Yoon Jeonghan', 'NIM': '3175003', 'MataPelajaran': 'Biologi', 'NilaiTugas': 60, 'NilaiUTS': 50, 'NilaiUAS': 50, 'Grade': 'E','Keterangan': 'Tidak Lulus'}
}

def main_menu ():
    global pilih
    pilih = int(input('''
++++SELAMAT DATANG DI SMA NEGERI 3 BEKASI++++

Pilihan Menu:
    1. Menampilkan Data Siswa
    2. Menambah Data Siswa
    3. Memperbaharui/Mengubah Data Siswa
    4. Menghapus Data Siswa
    5. Keluar
        
Silahkan masukkan angka Menu yang ingin anda jalankan: '''))
    return pilih

## FITUR READ ##
# Fungsi untuk menampilkan semua data siswa
def tampilkan(data):
    print('\nDaftar Data Siswa:')
    print('-' * 140)
    print('No\t Nama Siswa\t NIM\t\t Mata Pelajaran\t\t Nilai Tugas\t Nilai UTS\t Nilai UAS\t Grade\t Keterangan')
    print('-' * 140)

    for i, siswa in enumerate(data, start=1):
        print('{}\t {}\t {}\t {}\t\t {}\t\t {}\t\t {}\t\t {}\t {}'.format(
            i, siswa['NamaSiswa'], siswa['NIM'], siswa['MataPelajaran'], siswa['NilaiTugas'],
            siswa['NilaiUTS'], siswa['NilaiUAS'], siswa['Grade'], siswa['Keterangan']))
    
    print('-' * 140)

# Fungsi untuk mencari siswa berdasarkan nama
def cari_siswa(data_siswa):
    cari_nama_siswa = input('\nMasukkan Nama Siswa yang ingin dicari: ').strip() 
    format_nama_siswa = cari_nama_siswa.title() 
    
    if format_nama_siswa in data_siswa:
        tampilkan([data_siswa[format_nama_siswa]])
    else:
        print(f'\n===Siswa dengan nama "{format_nama_siswa}" tidak ditemukan di dalam database===')

# Fungsi untuk menampilkan siswa yang lulus
def tampilkan_siswa_lulus(data_siswa):
    siswa_lulus = [siswa for siswa in data_siswa.values() if siswa['Keterangan'] == 'Lulus'] 
    
    if siswa_lulus:
        tampilkan(siswa_lulus)
    else:
        print('\n===Tidak ada siswa yang lulus===')

# Fungsi menjalankan fitur Read
def menu_read_siswa(opsi):
    while True:
        opsi = int(input('''
------------------------------------------------------------------------------------------------
Pilihan menampilkan data:
    1. Tampilkan semua data siswa
    2. Cari Nama Siswa
    3. Lihat siswa yang Lulus
    4. Kembali ke Menu Utama

Masukkan angka Pilihan yang ingin dijalankan: '''))
        if opsi == 1:
            if len(data_siswa) > 0:
                tampilkan(data_siswa.values())
            else:
                print('\n===Tidak ada data siswa yang tersimpan===')
        elif opsi == 2:
            if len(data_siswa) > 0:
                cari_siswa(data_siswa)
            else:
                print('\n===Tidak ada data siswa yang tersimpan===')
        elif opsi == 3:
            if len(data_siswa) > 0:
                tampilkan_siswa_lulus(data_siswa)
            else:
                print('\n===Tidak ada siswa yang tersimpan===')
        elif opsi == 4:
            break
        else:
            print('\n===Pilihan tidak valid. Silahkan pilih opsi yang tersedia===')

### FITUR CREATE ###
#Menentukan Grade Siswa
def grade_siswa(nilai_akhir):
    if nilai_akhir >= 90:
        return 'A'
    elif nilai_akhir >= 80:
        return 'B'
    elif nilai_akhir >= 70:
        return 'C'
    elif nilai_akhir >= 50:
        return 'D'
    else:
        return 'E'

#Menentukan Keterangan Siswa
def keterangan(nilai_akhir):
    if nilai_akhir >= 60:
        return 'Lulus'
    else:
        return 'Tidak Lulus'

#Menjalankan Fitur Create
def menu_create_siswa(opsi):
    while True:
        opsi = input('''
-----------------------------------------------------------------------------------------------------------------------------
Apakah Anda ingin menambahkan data siswa? (y/n): ''').strip().lower()
        
        if opsi == 'y':
            nama_siswa = input('Masukkan Nama Siswa: ').strip().title()
            if nama_siswa in data_siswa:
                print(f'\n ===Data siswa dengan nama {nama_siswa} sudah tersimpan di database===')
            else:
                nim = input('Masukkan NIM: ').strip()
                mata_pelajaran = input('Masukkan Mata Pelajaran: ').strip()
                nilai_tugas = input('Masukkan Nilai Tugas: ').strip()
                if nilai_tugas.replace('.', '', 1).isdigit():
                    nilai_tugas = float(nilai_tugas)
                else:
                    print('===Nilai Tugas harus berupa angka===')
                    continue
                nilai_uts = input('Masukkan Nilai UTS: ').strip()
                if nilai_uts.replace('.', '', 1).isdigit():
                    nilai_uts = float(nilai_uts)
                else:
                    print('===Nilai UTS harus berupa angka===')
                    continue
                nilai_uas = input('Masukkan Nilai UAS: ').strip()
                if nilai_uas.replace('.', '', 1).isdigit():
                    nilai_uas = float(nilai_uas)
                else:
                    print('===Nilai UAS harus berupa angka===')
                    continue
                nilai_akhir = (nilai_tugas * 0.4) + (nilai_uts * 0.3) + (nilai_uas * 0.3)
                grade = grade_siswa(nilai_akhir)
                keterangan_siswa = keterangan(nilai_akhir)
                simpan = input('\nApakah Anda ingin menyimpan data? (y/n): ').strip().lower()
                if simpan == 'y':
                    data_siswa[nama_siswa] = {'NamaSiswa': nama_siswa, 'NIM': nim, 'MataPelajaran': mata_pelajaran, 'NilaiTugas': nilai_tugas,'NilaiUTS': nilai_uts,'NilaiUAS': nilai_uas,'Grade': grade,'Keterangan': keterangan_siswa}
                    print('===Data Berhasil Disimpan===')
                else:
                    print('===Data Belum Tersimpan===') 
        elif opsi == 'n':
            break
        else:
            print('===Pilihan tidak valid. Harap masukkan "y" atau "n"===')


## FITUR UPDATE ##
#Menjalankan Fitur Update
def menu_update_siswa(opsi):
    while True:
        opsi = input('''
-----------------------------------------------------------------------------------------------------------------------------
Apakah Anda ingin mengupdate data siswa? (y/n): ''').strip().lower()

        if opsi == 'y':
            nama_siswa = input('Masukkan Nama Siswa yang ingin diupdate: ').strip()
            nama_siswa_format = nama_siswa.title()

            if nama_siswa_format in data_siswa:
                print(f'\n===Data siswa ditemukan, silakan masukkan data baru untuk {nama_siswa_format}===')
                mata_pelajaran = input(f'Masukkan Mata Pelajaran baru (Mata pelajaran lama: {data_siswa[nama_siswa_format]["MataPelajaran"]}): ').strip()
                
                nilai_tugas_str = input(f'Masukkan Nilai Tugas baru (nilai lama: {data_siswa[nama_siswa_format]["NilaiTugas"]}): ').strip()
                nilai_tugas = float(nilai_tugas_str) if nilai_tugas_str else data_siswa[nama_siswa_format]["NilaiTugas"]

                nilai_uts_str = input(f'Masukkan Nilai UTS baru (nilai lama: {data_siswa[nama_siswa_format]["NilaiUTS"]}): ').strip()
                nilai_uts = float(nilai_uts_str) if nilai_uts_str else data_siswa[nama_siswa_format]["NilaiUTS"]

                nilai_uas_str = input(f'Masukkan Nilai UAS baru (nilai lama: {data_siswa[nama_siswa_format]["NilaiUAS"]}): ').strip()
                nilai_uas = float(nilai_uas_str) if nilai_uas_str else data_siswa[nama_siswa_format]["NilaiUAS"]

                nilai_akhir = (nilai_tugas * 0.4) + (nilai_uts * 0.3) + (nilai_uas * 0.3)
                grade = grade_siswa(nilai_akhir)
                keterangan_siswa = keterangan(nilai_akhir)

                simpan = input('\nApakah Anda ingin menyimpan perubahan? (y/n): ').strip().lower()
                if simpan == 'y':
                    data_siswa[nama_siswa_format].update({
                        'MataPelajaran': mata_pelajaran if mata_pelajaran else data_siswa[nama_siswa_format]['MataPelajaran'],
                        'NilaiTugas': nilai_tugas,
                        'NilaiUTS': nilai_uts,
                        'NilaiUAS': nilai_uas,
                        'Grade': grade,
                        'Keterangan': keterangan_siswa
                    }) # Penggunaan.update memperbarui dictionary dengan data baru tanpa menghapus data lain.
                    print('\n===Data Berhasil Diupdate===')
                else:
                    print('\n===Data Tidak Diupdate===')
            else:
                print(f'\n===Data siswa dengan nama {nama_siswa_format} tidak ditemukan===')
        elif opsi == 'n':
            break
        else:
            print('===Pilihan tidak valid. Harap masukkan "y" atau "n"===')


## FITUR DELETE ###
def menu_delete_siswa(opsi):
    while True:
        opsi = input('''
------------------------------------------------------------------------------------------------
Apakah anda ingin menghapus data siswa? (y/n): ''').strip().lower()
        
        if opsi == 'y':
            cari_nama_siswa = input('\nMasukkan Nama Siswa yang ingin dicari: ').strip().title()
            if cari_nama_siswa in data_siswa:
                print(f'\nData ditemukan untuk siswa {cari_nama_siswa}:')
                tampilkan([data_siswa[cari_nama_siswa]])

                hapus = input('Apakah anda ingin menghapus data siswa ini? (y/n): ').strip().lower()
                
                if hapus == 'y':
                    del data_siswa[cari_nama_siswa]
                    print('\n=== Data siswa berhasil dihapus===')
                else:
                    print('\n===Data siswa tidak dihapus===')
            else:
                print(f'\n===Tidak ada data siswa dengan nama {cari_nama_siswa}===')
        elif opsi == 'n':
            print('\n===Anda memilih untuk tidak menghapus data.===')
            break
        else:
            print('\n===Pilihan tidak valid, silakan masukkan "y" atau "n"===')

def menu_keluar():
    print('\n===Anda Telah keluar dari Aplikasi SMAN 3 Bekasi===')
    print('\n')
    exit()


while True:
    pilih = main_menu()
    if(pilih == 1):
        menu_read_siswa (data_siswa)
    elif(pilih == 2):
        menu_create_siswa (data_siswa)
    elif(pilih == 3):
        menu_update_siswa (data_siswa)
    elif (pilih == 4):
        menu_delete_siswa (data_siswa)
    elif (pilih == 5) :
        menu_keluar ()
    else:
        print('\n===Silahkan masukkan indeks menu yang tersedia===')