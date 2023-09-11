with open("books/frankenstein.txt") as f:
  file_contents = f.read()
  # read the whole contents to the console
  # print(file_contents)

  # count the words = 77986
  words = file_contents.split()
  # print(len(words))

  # count letters in file
  letters_count = {}
  for char in file_contents.lower():
    if char not in letters_count:
      letters_count[char] = 1
    else:
      letters_count[char] += 1
  # print(letters_count)

  # generate report
  print("--- Begin report of books/frankenstein.txt ---")
  print(f"{len(words)} words found in the document\n")
  letters_list = list(letters_count.items())
  letters_list.sort(key=lambda x: x[1], reverse=True)
  for key, value in letters_list:
    if key.isalpha():
      print(f"The '{key}' character was found {value} times\n")
  print("--- End report ---")


