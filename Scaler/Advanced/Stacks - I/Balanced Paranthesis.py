import collections

class Solution:
	# @param A : string
	# @return an integer
	def solve(self, A):
		pair = { '}' : '{', ')' : '(', ']' : '[' }
		st = collections.deque()
		for ch in A:
			if ch in pair.values():
				st.append(ch)
			else:
				if len(st) == 0 or st[-1] != pair[ch]:
					return 0
				else:
					st.pop()
		return 1 if len(st) == 0 else 0
