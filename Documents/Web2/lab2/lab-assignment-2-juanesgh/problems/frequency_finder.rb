def find_frequency(sentence, word)
  a = sentence.downcase.split()
  b = word.downcase()
  return a.count(b)
end