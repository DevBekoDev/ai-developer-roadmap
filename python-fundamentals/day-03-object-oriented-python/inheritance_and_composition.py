class User:
    def __init__(self, username: str, email: str):
        self.username = username
        self.email = email

    def display_profile(self) -> None:
        print(f"Username: {self.username}")
        print(f"Email: {self.email}")

    def display_role(self) -> None:
        print("Role: User")


class AdminUser(User):
    def __init__(
        self,
        username: str,
        email: str,
        permissions: list[str]
    ):
        super().__init__(username, email)
        self.permissions = permissions

    def display_role(self) -> None:
        print("Role: Administrator")

    def display_permissions(self) -> None:
        print("Permissions:")

        for permission in self.permissions:
            print(f"- {permission}")


class ChatMessage:
    def __init__(self, sender: User, content: str):
        self.sender = sender
        self.content = content

    def display_message(self) -> None:
        print(f"{self.sender.username}: {self.content}")


class ChatSession:
    def __init__(self, owner: User):
        self.owner = owner
        self.messages: list[ChatMessage] = []

    def add_message(self, message: ChatMessage) -> None:
        self.messages.append(message)

    def display_chat(self) -> None:
        print(f"Chat owner: {self.owner.username}")
        print("Messages:")

        for message in self.messages:
            message.display_message()


user_1 = User(
    "abubakr",
    "abubakr@example.com"
)

admin_1 = AdminUser(
    "sara",
    "sara@example.com",
    ["delete messages", "manage users"]
)

print("Regular user")
user_1.display_profile()
user_1.display_role()

print()

print("Administrator")
admin_1.display_profile()
admin_1.display_role()
admin_1.display_permissions()

print()

message_1 = ChatMessage(
    user_1,
    "What is inheritance?"
)

message_2 = ChatMessage(
    admin_1,
    "Inheritance allows one class to reuse another class."
)

chat_session = ChatSession(user_1)

chat_session.add_message(message_1)
chat_session.add_message(message_2)

chat_session.display_chat()