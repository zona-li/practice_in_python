class Solution:
  def lengthLongestPath(self, input):
    ret, tmp = 0, {-1: 0}
    for line in input.split('\n'):
      depth = line.count('\t')
      tmp[depth] = tmp[depth - 1] + len(line) - depth
      if line.count('.'):
        ret = max(ret, tmp[depth] + depth)
    return ret
    