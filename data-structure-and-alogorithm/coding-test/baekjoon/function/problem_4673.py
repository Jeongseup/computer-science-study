
def solve() -> None:

	def self(n: int) -> int:
		d = n
		for word in str(n):
			d += int(word)

		return d

	natural_set = set(range(1, 10001))
	self_set = set()

	for i in range(1, 10001):
		self_set.add(self(i))

	for num in sorted(natural_set - self_set):
		print(num)

solve()
