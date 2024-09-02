def main():
  file_path = "books/frankenstein.txt"
  book_text = get_book_text(file_path)
  word_count = get_word_count(book_text)
  character_map = get_char_map(book_text)
  alphabet_list = get_alpha_list(character_map)
  alphabet_list.sort(reverse=True, key=sort_on)
  print(f"--- Begin report of {file_path} ---")
  print(f"The document consists of {word_count} words")
  print("\n")
  for dict in alphabet_list:
    print(f'The character \'{dict["alphabet"]}\' was found {dict["num"]} times')
  print("--- End report ---")

def get_book_text(file_path):
  with open(file_path) as f:
    return f.read()

def get_word_count(book_text):
  words = book_text.split()
  return len(words)

def get_char_map(book_text):
  char_map = {}
  for char in book_text:
    char = char.lower()
    if char not in char_map:
      char_map[char] = 1
    else:
      char_map[char] += 1
  return char_map

def get_alpha_list(char_map):
  alpha_list = []
  for key in char_map.keys():
    if key.isalpha():
      temp_dict = {}
      temp_dict["alphabet"] = key
      temp_dict["num"] = char_map[key]
      alpha_list.append(temp_dict)
  return alpha_list

def sort_on(dict):
  return dict["num"]

main()