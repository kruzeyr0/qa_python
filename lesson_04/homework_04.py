adwentures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""

##  ПЕРЕЗАПИСУЙТЕ зміст змінної adwentures_of_tom_sawer у завданнях 1-3
# task 01 ==
""" Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""

adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("\n", " ")    # replace newlines with space
print(adwentures_of_tom_sawer, end="\n\n")


# task 02 ==
""" Замініть .... на пробіл
"""

adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("....", " ")  # replace '....' with space
print(adwentures_of_tom_sawer, end="\n\n")

# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""

adwentures_of_tom_sawer = ' '.join(adwentures_of_tom_sawer.split()) # normalize multiple spaces to single space
print(adwentures_of_tom_sawer, end="\n\n")


# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""

count_h = adwentures_of_tom_sawer.count("h")    # count of 'h'
print(count_h, end="\n\n")


# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""

split_words_for_capitilize = adwentures_of_tom_sawer.split()  # split text into words
count_capitalized = sum(1 for word in split_words_for_capitilize if word.istitle())  # count words starting with a capital letter
print(count_capitalized, end="\n\n")


# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""

fitst_word_index = adwentures_of_tom_sawer.find("Tom")  # find first occurrence of 'Tom'
second_word_index = adwentures_of_tom_sawer.find("Tom", fitst_word_index + 1)  # find second occurrence of 'Tom'
print(second_word_index, end="\n\n")


# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""

adwentures_of_tom_sawer_sentences = None
adwentures_of_tom_sawer_sentences = adwentures_of_tom_sawer.split('. ')  # split text into sentences
print(adwentures_of_tom_sawer_sentences, end="\n\n")


# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""

fourth_sentence = adwentures_of_tom_sawer_sentences[3]  # get the fourth sentence

fourth_sentence_lower = fourth_sentence.lower() # convert to lowercase
print(fourth_sentence_lower, end="\n\n")


# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""

starts_with_by_the_time = any(sentence.startswith("By the time") for sentence in adwentures_of_tom_sawer_sentences) # check if any sentence starts with 'By the time'
print(starts_with_by_the_time, end="\n\n")


# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""

сount_words_last_sentence = len(adwentures_of_tom_sawer_sentences[-1].split())  # count words in the last sentence
print(сount_words_last_sentence, end="\n\n")

