import enum


class Highlighting(enum.Enum):
    Red = '\033[31m'
    Reset = '\033[0m'


def highlight_different_characters(word, option):
    i, j = 0, 0
    marked_option = ''
    while i < len(word) and j < len(option):
        if word[i] != option[j]:
            marked_option += Highlighting.Red.value + option[j] + Highlighting.Reset.value
        else:
            marked_option += option[j]
        i += 1
        j += 1
    if j != len(option):
        marked_option += Highlighting.Red.value + option[j:] + Highlighting.Reset.value
    return marked_option
