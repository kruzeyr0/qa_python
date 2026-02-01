while True:
  print("Enter a word with character 'h' or 'H':")
  target_line = input()

  if 'h' in target_line or 'H' in target_line:
    print("Word accepted. Cycle terminated.")
    break
