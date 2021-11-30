def LongestWord(sen):

  # code goes here
  words = sen.split(' ')
  print(type(words))
  long_word = ''
  for each in words:
    if len(each) > len(long_word):
      long_word = each
  return long_word
