from books.models import Books


def format_books(data:Books):
    return {
        'pk':data.id,
        'Kitob_nomi':data.title,
        'Kitob_haqida_qisqacha':data.description,
        'rasm':data.image_book.url if data.image_book else None,
        'isbn':data.isbn,
        'narxi':data.price,
        'created_at':data.create_at
    }