import sqlite3 as sl

class Dictionary:
    def __init__(self, base="russian.txt"):
        self.local_dictionary = set()
        self.dictionary_options = dict()
        self._generate_local_dictionary(base)

    # def generate_base():
    #     con = sl.connect('dictionary.db')
    #     cursor = con.cursor()
    #
    #     cursor.execute("""
    #             create table if not exists Words (
    #                 id integer primary key autoincrement,
    #                 word varchar(32) not null
    #             );
    #         """)
    #
    #     cursor.execute("""
    #                 create table if not exists VariantsWordForms (
    #                     variant_id integer primary key autoincrement,
    #                     word_id integer,
    #                     variants varchar(32) not null,
    #                     foreign key (word_id) references Words (id)
    #                 );
    #             """)

    def _generate_local_dictionary(self, base):
        with open(base) as f:
            for row in f:
                self.local_dictionary.add(row.rstrip('\n'))

    def add_variants(self, incorrect_word, *variants):
        if incorrect_word not in self.dictionary_options:
            self.dictionary_options[incorrect_word] = set(variants)
        else:
            self.dictionary_options[incorrect_word].add(variants)