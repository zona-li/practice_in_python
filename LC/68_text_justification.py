import math


class Solution:
  def make_sections(self, words, maxWidth):
    result = []
    composed_str = []
    curr_len = 0
    for word in words:
      space_left = maxWidth - curr_len
      added_len = len(word)
      if added_len <= space_left:
        curr_len += added_len + 1
        composed_str.append(word)
      else:
        result.append(composed_str)
        composed_str = [word]
        curr_len = len(word) + 1
    if len(composed_str):
      result.append(composed_str)
    return result

  def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
    sections = self.make_sections(words, maxWidth)
    result = []
    for idx, section in enumerate(sections):
      result_str = ""
      if len(section) == 1:
        result_str = section[0]
        while len(result_str) < maxWidth:
          result_str += ' '
      else:
        if idx == len(sections) - 1:
          for index, word in enumerate(section):
            if index < len(section) - 1:
              result_str += word + ' '
            else:
              result_str += word
          while len(result_str) < maxWidth:
            result_str += ' '
        else:
          total_len = sum([len(s) for s in section])
          num_spaces = maxWidth - total_len
          avg_space = math.floor(num_spaces / (len(section) - 1))
          append_count = num_spaces - avg_space * (len(section) - 1)
          for index, word in enumerate(section):
            if index < len(section) - 1:
              result_str += word + ' ' * avg_space
              if append_count > 0:
                append_count -= 1
                result_str += ' '
            else:
              result_str += word
      result.append(result_str)
    return result
