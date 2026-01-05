# Importing the functions of the task in an external module
import text_analyzer

test_text = "Python is amazing! Python makes programming fun. Programming with Python is powerful."
print(text_analyzer.count_word_frequency(test_text))
print(text_analyzer.find_longest_words(test_text, 5))
print(text_analyzer.text_statistics(test_text, show_frequency=True, show_longest=True, top_n=3))
