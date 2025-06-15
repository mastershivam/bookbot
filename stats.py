def split_book_text(book_text):
    book_text_split = book_text.split()
    num_words = len(book_text_split)
    return num_words

from collections import Counter
def character_count(book_text):
    book_text_lower=book_text.lower()
    char_counter=Counter(book_text_lower)
    return char_counter

def character_sorting(counter_dict):
    counter_dict_sorted = counter_dict.most_common()
    return counter_dict_sorted

