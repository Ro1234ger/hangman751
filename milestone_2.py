import random

create_fruit_name_list = {"apple","peach","melon","lemon","grape"}
change_to_word_list = list(create_fruit_name_list)
generate_word = random.choice(change_to_word_list)
print(generate_word)