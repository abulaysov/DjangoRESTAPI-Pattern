
class UserCreateService:
    """Simple example of service"""

    def __init__(self, email: str, username: str, password: str):
        self.email = email
        self.username = username
        self.password = password

    def execute(self):
        self._create()
        self._send_email()

    def _create(self):
        print(f"Creating user: {self.username}")

    def _send_email(self):
        print(f"Sending email: {self.email}")
