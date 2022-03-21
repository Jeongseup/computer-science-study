class Buffer {
	int[] buf;
	int size;
	int count;
	int in;
	int out;

	Buffer(int size) {
		buf = new int[size];
		this.size = size;
		count = in = out = 0;
	}

	void insert(int item) {
		/* check if buf is full */
		while (count == size)
			;

		/* buf is not full */
		buf[in] = item;
		in = (in + 1) % size;
		count++;
	}

	int remove() {
		/* check if buf is empty */
		while (count == 0)
			;

		/* buf is not empty */
		int item = buf[out];
		out = (out + 1) % size;
		count--;
		return item;
	}

}
