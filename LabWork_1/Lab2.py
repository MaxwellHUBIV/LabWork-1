# TODO Найдите количество книг, которое можно разместить на дискете

book_size = 25 * 50 * 100 * 4
byte_disk_size = 1.44 * 1024**2
count_books = byte_disk_size / book_size

print("Количество книг, помещающихся на дискету:", int(count_books))
