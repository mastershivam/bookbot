from stats import split_book_text
from stats import character_count
from stats import character_sorting
import sys



def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents



def main(path):

    path = sys.argv[1]

    book_data=get_book_text(path)

    print('============ BOOKBOT ============')
    print(f'Analyzing book found at {path}')

    print('----------- Word Count ----------')
    length_book =split_book_text(book_data)

    print(f'Found {length_book} total words')

    ch_count=character_count(book_data)


    sorted_chs=character_sorting(ch_count)

    print('--------- Character Count -------')

    for i in sorted_chs:
        if i[0].isalpha():
            print(f"{i[0]}: {i[1]} ")
        else:
            pass



if len(sys.argv) !=2:
    print("Usage: python3 main.py <path_to_book>")

main(sys.argv[1])