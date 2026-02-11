import time

# Text-adventure tentang seorang kesatria yang menebus masa lalu


def clamp(val, minimum=0, maximum=100):
    return max(minimum, min(maximum, val))


def status(state):
    print("\n--- STATUS PEMAIN ---")
    print(f"HP        : {state['hp']}")
    print(f"Energi    : {state['energy']}")
    print(f"Air       : {state['water']}")
    print(f"Makanan   : {state['food_stock']}")
    print(f"Minuman   : {state['drink_stock']}")
    print(f"Penebusan : {state['penebusan']}")
    print("---------------------\n")


def makan_minum(state):
    while True:
        print("\nMenu Makan/Minum:")
        print("1) Makan (pakai 1 makanan, +20 energi)")
        print("2) Minum (pakai 1 minuman, +25 air)")
        print("3) Kembali")
        pilih = input("Pilih opsi: ")
        if pilih == '1':
            if state['food_stock'] <= 0:
                print("Kamu tidak punya makanan.")
            else:
                state['food_stock'] -= 1
                state['energy'] = clamp(state['energy'] + 20)
                print("Kamu makan dan merasa lebih berenergi.")
        elif pilih == '2':
            if state['drink_stock'] <= 0:
                print("Kamu tidak punya minuman.")
            else:
                state['drink_stock'] -= 1
                state['water'] = clamp(state['water'] + 25)
                print("Kamu minum dan merasa segar kembali.")
        elif pilih == '3':
            break
        else:
            print("Pilihan tidak dikenal.")
        status(state)


def travel(state):
    state['energy'] -= 15
    state['water'] -= 20
    state['hp'] -= 5
    state['energy'] = clamp(state['energy'], 0, 100)
    state['water'] = clamp(state['water'], 0, 100)
    state['hp'] = clamp(state['hp'], 0, 100)


def check_game_over(state):
    if state['hp'] <= 0 or state['energy'] <= 0 or state['water'] <= 0:
        print("\nKamu terlalu lelah dan perlu beristirahat. Perjalanan dihentikan untuk keselamatanmu.")
        ending(state, forced=True)
        return True
    if state['food_stock'] <= 0 and state['drink_stock'] <= 0 and state['energy'] < 30:
        print("\nPersediaan hampir habis dan kamu lelah. Perjalanan tidak bisa dilanjutkan.")
        ending(state, forced=True)
        return True
    return False


def pilih_negara():
    print("Pilih tujuan:")
    print("1) Embershard (pegunungan)")
    print("2) Lumoria (hutan bercahaya)")
    print("3) Aetherwind (negara langit)")
    print("4) Ferrundale (teknologi kuno)")
    print("5) Meridia (oasis gurun)")
    print("6) Cek status / makan-minum")
    print("7) Akhiri perjalanan")
    print("8) Peperangan (uji pilihan moral — non-graphic)")
    print("9) Istirahat (pulihkan kondisi jika memungkinkan)")
    return input("Masukkan pilihan: ")


def embershard(state):
    print("\nKau tiba di Embershard, pegunungan yang sunyi namun indah.")
    print("1) Bantulah penduduk memperbaiki jembatan kecil (tindakan baik)")
    print("2) Lewati lama dan lanjut perjalanan (netral)")
    c = input("Pilihanmu: ")
    if c == '1':
        state['penebusan'] += 1
        print("Penduduk berterima kasih. Hatimu terasa ringan.")
    else:
        print("Kau memilih melanjutkan perjalanan tanpa campur tangan.")


def lumoria(state):
    print("\nDi Lumoria, hutan bercahaya, kau bertemu alam yang tenang.")
    print("1) Bantu hewan yang tersesat menemukan jalan pulang (tindakan baik)")
    print("2) Hanya mengamati dari jauh dan pergi (netral)")
    c = input("Pilihanmu: ")
    if c == '1':
        state['penebusan'] += 1
        print("Kau membantu hewan itu kembali ke keluarganya.")
    else:
        print("Kau memilih untuk menjaga jarak dan melanjutkan.")


def aetherwind(state):
    print("\nAetherwind terhampar di atas awan; kota-kota di udara mengajarkan banyak hal.")
    print("1) Bantu memperbaiki alat komunikasi komunitas (tindakan baik)")
    print("2) Menolak dan fokus pada tujuanmu (netral)")
    c = input("Pilihanmu: ")
    if c == '1':
        state['penebusan'] += 1
        print("Perbaikanmu membantu banyak orang tetap terhubung.")
    else:
        print("Kau memilih untuk melanjutkan perjalanan sendiri.")


def ferrundale(state):
    print("\nFerrundale penuh mesin dan penemuan. Orang-orang di sini menghargai kerja keras.")
    print("1) Bantu memperbaiki alat rusak di bengkel komunitas (tindakan baik)")
    print("2) Menawarkan saran singkat lalu pergi (netral)")
    c = input("Pilihanmu: ")
    if c == '1':
        state['penebusan'] += 1
        print("Usahamu membuat komunitas jadi lebih efisien.")
    else:
        print("Kau memberi sedikit bantuan lalu berpisah.")


def meridia(state):
    print("\nMeridia adalah oasis di gurun — tempat banyak pelancong beristirahat.")
    print("1) Bagikan persediaan kecilmu kepada yang membutuhkan (tindakan baik)")
    print("2) Hemat persediaan untuk perjalananmu sendiri (netral)")
    c = input("Pilihanmu: ")
    if c == '1':
        if state['food_stock'] > 0 or state['drink_stock'] > 0:
            # berbagi sedikit
            if state['food_stock'] > 0:
                state['food_stock'] -= 1
            if state['drink_stock'] > 0:
                state['drink_stock'] -= 1
            state['penebusan'] += 1
            print("Kebaikanmu membuat suasana menjadi hangat.")
        else:
            print("Kau ingin membantu, tapi persediaanmu sudah habis.")
    else:
        print("Kau memutuskan untuk menabung persediaan.")


def peperangan(state):
    print("\nSebuah ketegangan terjadi di dekatmu terkait persediaan lokal.")
    print("Pilih pendekatan (semua opsi digambarkan tanpa kekerasan):")
    print("1) Menjadi mediator dan membantu kedua pihak mencapai solusi (tindakan baik)")
    print("2) Mengatur perlindungan non-konfrontatif untuk warga (netral)")
    print("3) Mengabaikan dan melanjutkan perjalanan (netral)")
    c = input("Pilihanmu: ")
    if c == '1':
        state['penebusan'] += 1
        state['energy'] = clamp(state['energy'] - 10)
        state['water'] = clamp(state['water'] - 5)
        state['hp'] = clamp(state['hp'] - 2)
        print("Kau berhasil menenangkan situasi melalui kata-kata dan empati. Penebusan bertambah.")
    elif c == '2':
        state['energy'] = clamp(state['energy'] - 20)
        state['water'] = clamp(state['water'] - 10)
        state['hp'] = clamp(state['hp'] - 5)
        print("Kau membantu mengorganisir perlindungan dan tempat aman. Warga berterima kasih.")
    else:
        print("Kau memilih tidak ikut campur dan melanjutkan perjalanan.")


def istirahat(state):
    print("\nPilihan istirahat:")
    print("1) Istirahat nyaman di penginapan (akan menggunakan 1 makanan dan 1 minuman jika tersedia)")
    print("2) Istirahat sederhana tanpa persediaan")
    print("3) Batal")
    c = input("Pilihanmu: ")
    if c == '1':
        used_food = 0
        used_drink = 0
        if state['food_stock'] > 0:
            state['food_stock'] -= 1
            used_food = 1
        if state['drink_stock'] > 0:
            state['drink_stock'] -= 1
            used_drink = 1
        if used_food or used_drink:
            state['hp'] = clamp(state['hp'] + 40)
            state['energy'] = clamp(state['energy'] + 50)
            state['water'] = clamp(state['water'] + 30)
            print("Istirahat nyaman membuatmu pulih lebih baik.")
        else:
            print("Persediaan tidak cukup untuk istirahat nyaman. Pilih istirahat sederhana atau kumpulkan persediaan.")
    elif c == '2':
        state['hp'] = clamp(state['hp'] + 20)
        state['energy'] = clamp(state['energy'] + 25)
        state['water'] = clamp(state['water'] + 10)
        print("Istirahat sederhana membantu menyegarkan tubuh.")
    else:
        print("Batal istirahat.")


def ending(state, forced=False):
    print("\n--- AKHIR PERJALANAN ---")
    if forced:
        print("Perjalanan berakhir karena keselamatan atau persediaan habis.")
    print(f"Penebusan akhir: {state['penebusan']}")
    alive = state['hp'] > 0 and state['energy'] > 0 and state['water'] > 0
    if state['penebusan'] >= 4 and alive:
        print("Hasil: Penebusan penuh — kau telah tumbuh dan menebus banyak kesalahanmu.")
        print("Masyarakat menghargai tanggung jawabmu dan kau pulang dengan damai.")
    elif state['penebusan'] >= 2 and alive:
        print("Hasil: Penebusan sebagian — perjalanan mengajarkanmu banyak, masih ada jalan.")
        print("Kau pulang lebih bijak dan bersedia terus belajar.")
    else:
        print("Hasil: Penebusan belum tercapai — persediaan atau pilihan menghambat perjalananmu.")
        print("Namun kisah ini belum berakhir; ada kesempatan untuk mencoba lagi di masa depan.")
    print("Terima kasih telah memainkan cerita ini.")
    exit(0)


def game_utama():
    print("--- PETUALANGAN: KESATRIA PENEBUSAN ---")
    nama = input("Namamu, kesatria: ")
    print(f"Selamat datang, {nama}. Tujuanmu adalah menebus kesalahan masa lalu melalui tindakan.")

    state = {
        'hp': 100,
        'energy': 100,
        'water': 100,
        'food_stock': 3,
        'drink_stock': 3,
        'penebusan': 0
    }

    while True:
        if check_game_over(state):
            break
        choice = pilih_negara()
        if choice == '1':
            travel(state)
            embershard(state)
        elif choice == '2':
            travel(state)
            lumoria(state)
        elif choice == '3':
            travel(state)
            aetherwind(state)
        elif choice == '4':
            travel(state)
            ferrundale(state)
        elif choice == '5':
            travel(state)
            meridia(state)
        elif choice == '6':
            status(state)
            makan_minum(state)
        elif choice == '7':
            ending(state)
        elif choice == '8':
            peperangan(state)
        elif choice == '9':
            istirahat(state)
        else:
            print("Pilihan tidak dikenal.")

        # Setelah setiap lokasi, tunjukkan status singkat
        status(state)


if __name__ == '__main__':
    game_utama()