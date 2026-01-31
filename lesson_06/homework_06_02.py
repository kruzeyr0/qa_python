while True:
  print("Enter a word with character 'h' or 'H':")
  set = input()

  if 'h' in set or 'H' in set:
    print("Word accepted. Cycle terminated.")
    break
