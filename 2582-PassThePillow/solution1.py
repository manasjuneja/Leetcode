class Solution:
	def passThePillow(self, n: int, time: int) -> int:

		current = 1
		cycle = 1

		while time > 0:

			if cycle % 2 != 0:
				current = current + 1
			else:
				current = current - 1 

			if current == n or current == 1:
				cycle = cycle + 1

			time = time - 1

		return current
