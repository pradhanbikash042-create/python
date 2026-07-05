class Account:
    def __init__(self, account_holder):
        self.account_holder = account_holder
        self._balance = 0

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"{amount} deposited successfully.")
        else:
            print("Invalid amount")

    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
            print(f"{amount} withdrawn successfully.")
        else:
            print("Insufficient balance")

    def get_balance(self):
        return self._balance

    def set_balance(self, amount):
        if amount >= 0:
            self._balance = amount
        else:
            print("Balance cannot be negative.")


class SavingsAccount(Account):
    def __init__(self, account_holder, interest_rate):
        super().__init__(account_holder)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        return self.get_balance() * self.interest_rate / 100


class CheckingAccount(Account):
    def __init__(self, account_holder, overdraft_limit):
        super().__init__(account_holder)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount <= self.get_balance() + self.overdraft_limit:
            new_balance = self.get_balance() - amount
            self.set_balance(new_balance)
            print(f"{amount} withdrawn successfully.")
        else:
            print("Overdraft limit exceeded.")


class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.posts = []

    def post(self, content):
        self.posts.append(content)
        print("Post created successfully.")

    def comment(self, content):
        print(f"{self.username} commented: {content}")

    def display_posts(self):
        print(f"\nPosts by {self.username}")
        for post in self.posts:
            print("-", post)


class Admin(User):
    def __init__(self, username, email):
        super().__init__(username, email)

    def delete_post(self, user, post):
        if post in user.posts:
            user.posts.remove(post)
            print("Post deleted successfully.")
        else:
            print("Post not found.")

    def display_posts(self):
        print(f"\nAdmin view - posts by {self.username}")
        super().display_posts()


if __name__ == "__main__":
    account = Account("Alice")
    account.deposit(100)
    account.withdraw(30)
    print("Balance:", account.get_balance())

    savings = SavingsAccount("Bob", 5)
    savings.deposit(200)
    print("Savings interest:", savings.calculate_interest())

    checking = CheckingAccount("Charlie", 50)
    checking.deposit(80)
    checking.withdraw(100)
    print("Checking balance:", checking.get_balance())

    user1 = User("bikash", "pra@example.com")
    user1.post("Hello everyone")
    user1.comment("This is my first post")
    user1.display_posts()

    admin1 = Admin("admin", "admin@example.com")
    admin1.delete_post(user1, "Hello everyone")
    admin1.display_posts()


