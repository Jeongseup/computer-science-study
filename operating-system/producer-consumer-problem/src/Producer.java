/****** »ý»êÀÚ ******/
class Producer extends Thread {
	Buffer b;
	int N;

	Producer(Buffer b, int N) {
		this.b = b;
		this.N = N;
	}

	public void run() {
		for (int i = 0; i < N; i++)
			b.insert(i);
	}
}