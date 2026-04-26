from text_utils import normalize_text, word_count, contains_word

text = "  Today is the holiday of bright Easter!  "

print(normalize_text(text))
print(word_count(text))
print(contains_word(text, "of"))
print(len(text))