# dictionary yang nilainya tidak berasal dari tipe data sejenis

def main():
    # nilai dictionary berbeda tipe data
    d = {'nama': "Arimbi", 'uts': 95.25, 'uas': 92.75, 'nilai': "A"}

    # menampilkan nilai dictionary
    print("Nama\t\t: ", d['nama'])
    print("Nilai UTS\t: ", d['uts'])
    print("Nilai UAS\t: ", d['uas'])
    print("Nilai Indeks\t: ", d['nilai'])


if __name__ == "__main__":
    main()
