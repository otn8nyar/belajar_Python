# mengubah suatu data dengan nama kunci yang sama namun beda huruf pertama kapital
def main():
    d = {'satu': 10, 'dua': 20, 'tiga': 30}

    # elemen dictionary sebelum diubah
    print("Elemen dictionary sebelum diubah: ")
    print(d)

    # mengubah nilai elemen
    d['satu'] = 60

    # menambah elemen d['Satu']
    d['Satu'] = 130

    # elemen dictionary setelah diubah
    print("\nElemen dictionary setelah diubah: ")
    print(d)


if __name__ == "__main__":
    main()
