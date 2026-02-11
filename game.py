#!/usr/bin/env python3
import sys

def main():
    print("Selamat datang di Dunia Fantasy — Desa Kegelapan.")
    name = input("Nama pemain: ").strip()
    if not name:
        name = "Pahlawan"

    print(f"\n{name}, desa ini dikuasai oleh penjahat yang menekan rakyat.")
    print("Tuan desa memohon bantuanmu untuk memberantas kejahatan dan membebaskan masyarakat.")
    print("\nPilih jalur yang ingin kamu ambil:")
    print("1) jln Hos tcokro")
    print("2) Gunung")
    print("3) Kerajaan Iblis")
    print("4) Kerajaan Penjahat")

    choice = input("Masukkan 1-4 (atau ketik nama jalur): ").strip().lower()

    if choice in ('1', 'jln hos tcokro', 'jln', 'hos tcokro', 'hos', 'tcokro'):
        print("\nKamu memilih jalan 'jln Hos tcokro'. Jalan sempit, banyak gang.")
        print("Di jalan itu ada para penjahat yang menjaga pintu masuk.")
        action = input("Apakah kamu 'serang' langsung atau 'selip' menyelinap? (serang/selip): ").strip().lower()
        if action in ('serang', 's'):
            print("\nKamu bertarung gagah berani dan berhasil menundukkan penjahat tersebut.")
            print("Rakyat mulai melihat harapan. Kamu berhasil membersihkan jalan.")
            print("Misi berhasil! Desa selamat berkat keberanianmu.")
        else:
            print("\nKamu menyelinap melewati gelapnya gang dan berhasil menghindari pertempuran.")
            print("Tanpa diketahui, kamu memasang jebakan pada markas penjahat dan memanggil pasukan.")
            print("Dengan strategi, penjahat ditangkap tanpa banyak jatuh korban. Desa selamat.")

    elif choice in ('2', 'gunung'):
        print("\nKamu memilih jalur 'Gunung'. Medan terjal dan kabut tebal.")
        print("Di puncak, seorang pemimpin penjahat menjaga harta curian.")
        action = input("Kamu ingin 'tantang' pemimpin itu atau cari 'bantuan' penduduk? (tantang/bantuan): ").strip().lower()
        if action in ('tantang', 't'):
            print("\nPertarungan di puncak sangat sengit. Dengan keberanian dan sedikit keberuntungan, kamu menang.")
            print("Pemimpin penjahat ditangkap, harta dikembalikan kepada rakyat.")
            print("Desa kembali damai. Selamat, pahlawan!")
        else:
            print("\nKamu meminta bantuan penduduk desa untuk mengepung gunung.")
            print("Dengan kerja sama, penjahat tak berkutik. Rakyat bersyukur.")
            print("Desa terbebas berkat kebijaksanaanmu.")

    else:
        print("\nPilihan tidak dikenal. Jalur tersesat membuatmu kehilangan waktu.")
        print("Penjahat semakin kuat. Coba lagi nanti.")

    # Tambahan: jalur ke Kerajaan Iblis
    if choice in ('3', 'kerajaan iblis', 'ib'):
        print("\nKamu berani memilih menuju Kerajaan Iblis. Aura gelap menyelimuti.")
        print("Gerbang iblis dijaga oleh makhluk bayangan yang menakutkan.")
        action = input("Apakah kamu 'hadapi' mereka atau 'mundur' dan siasati? (hadapi/mundur): ").strip().lower()
        if action in ('hadapi', 'h'):
            print("\nPertarungan melawan makhluk bayangan menguji jiwa dan keberanianmu.")
            print("Dengan tekad, kamu mengalahkan beberapa penjaga namun harus mengorbankan tenaga.")
            print("Di dalam istana, kamu menemukan artefak yang mengusir kegelapan. Desa terbantu.")
        else:
            print("\nKamu mundur dan merencanakan serangan dengan mantra pelindung.")
            print("Dengan persiapan, kamu menyelinap ke dalam dan memecah kekuatan iblis dari dalam.")
            print("Kerajaan Iblis melemah, ancaman mereda.")

    # Tambahan: jalur ke Kerajaan Penjahat
    if choice in ('4', 'kerajaan penjahat', 'penjahat'):
        print("\nKamu menuju Kerajaan Penjahat — benteng penuh kriminal dan konspirasi.")
        print("Di sana, pasukan bayaran dan pembunuh profesional berjaga.")
        action = input("Kamu ingin 'infiltrate' menyusup atau 'ajak' dialog dengan pemimpin? (infiltrate/ajak): ").strip().lower()
        if action in ('infiltrate', 'i', 's'):
            print("\nKamu menyusup dengan licik, menggagalkan rencana para penjahat dari dalam.")
            print("Rakyat aman, dan jaringan kriminal hancur.")
        else:
            print("\nKamu mencoba berdialog dengan pemimpin untuk memecah kesetiaan.")
            print("Setelah negosiasi licik, beberapa panglima berbalik, membuat kerajaan penjahat runtuh.")

    print("\nTerima kasih telah bermain.")


if __name__ == '__main__':
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nKeluar dari permainan. Sampai jumpa.")
        sys.exit(0)
