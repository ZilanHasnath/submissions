class Solution:

  def checkInclusion(self, s1: str, s2: str) -> bool:
    len1, len2 = len(s1), len(s2)

    if len1 > len2:
      return False

    count1 = [0] * 26
    count2 = [0] * 26

    for i in range(len1):
      count1[ord(s1[i]) - ord("a")] += 1
      count2[ord(s2[i]) - ord("a")] += 1

    matches = sum(1 for i in range(26) if count1[i] == count2[i])

    for i in range(len1, len2):
      if matches == 26:
        return True

      r_idx = ord(s2[i]) - ord("a")
      count2[r_idx] += 1
      if count2[r_idx] == count1[r_idx]:
        matches += 1
      elif count2[r_idx] == count1[r_idx] + 1:
        matches -= 1

      l_idx = ord(s2[i - len1]) - ord("a")
      count2[l_idx] -= 1
      if count2[l_idx] == count1[l_idx]:
        matches += 1
      elif count2[l_idx] == count1[l_idx] - 1:
        matches -= 1

    return matches == 26