/****** ¼ÒºñÀÚ ******/
class Consumer extends Thread {
	Buffer b;
	int N;

	Consumer(Buffer b, int N) {
		this.b = b;
		this.N = N;
	}

	public void run() {
		int item;
		for (int i = 0; i < N; i++)
			item = b.remove();
	}
}