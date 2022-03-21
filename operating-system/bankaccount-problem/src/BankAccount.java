class BankAccount {
	int balance;

	void deposit(int amount) {
		balance = balance + amount;
	}

	void withdraw(int amount) {
		balance = balance - amount;
	}

	int getBalance() {
		return balance;
	}
}
