from reverse_words import reverse_words


# Basic Tests
def test_reverse_words_with_one_word():
    test_string = "Engineer"

    assert reverse_words(test_string) == "reenignE"


def test_reverse_words_with_two_word_sentence():
    test_string = "hello, world"

    assert reverse_words(test_string) == ",olleh dlrow"


def test_reverse_words_returns_unmodified_with_single_character_words():
    test_string = "a b c d e f g h ? 1 2 4"

    assert reverse_words(test_string) == test_string


def test_reverse_words_with_sentence_of_varying_length_words():
    test_string = "I strive to engineer the most efficient solutions."

    expected = "I evirts ot reenigne eht tsom tneiciffe .snoitulos"
    assert reverse_words(test_string) == expected


# Edge Cases
def test_reverse_words_returns_unmodified_with_empty_sentence():
    test_string = ""

    assert reverse_words(test_string) == ""


def test_reverse_words_returns_unmodified_with_None_input():
    test_string = None

    assert reverse_words(test_string) is None


def test_reverse_words_maintains_leading_and_trailing_whitespace():
    test_string = "   evol  "

    assert reverse_words(test_string) == "   love  "
