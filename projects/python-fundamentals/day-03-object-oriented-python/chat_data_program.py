class User:
    total_users = 0

    def __init__(self, username: str, email: str):
        self.username = username
        self.email = email

        User.total_users += 1

    def display_profile(self) -> None:
        print(f"Username: {self.username}")
        print(f"Email: {self.email}")

    def display_role(self) -> None:
        print("Role: User")

    @classmethod
    def display_total_users(cls) -> None:
        print(f"Total users: {cls.total_users}")


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


class AIModel:
    total_models = 0

    def __init__(
        self,
        name: str,
        provider: str,
        context_window: int
    ):
        self.name = name
        self.provider = provider
        self.context_window = context_window

        AIModel.total_models += 1

    def display_info(self) -> None:
        print(f"Model: {self.name}")
        print(f"Provider: {self.provider}")
        print(f"Context window: {self.context_window} tokens")

    def supports_request(
        self,
        input_tokens: int,
        output_tokens: int
    ) -> bool:
        total_tokens = input_tokens + output_tokens

        return total_tokens <= self.context_window

    @classmethod
    def display_total_models(cls) -> None:
        print(f"Total models: {cls.total_models}")

    @staticmethod
    def is_valid_provider(provider: str) -> bool:
        valid_providers = [
            "openai",
            "anthropic",
            "google",
            "meta"
        ]

        return provider.lower() in valid_providers


class ChatMessage:
    total_messages = 0

    def __init__(
        self,
        sender: User,
        content: str,
        role: str
    ):
        self.sender = sender
        self.content = content
        self.role = role
        self.is_edited = False

        ChatMessage.total_messages += 1

    def display_message(self) -> None:
        edited_text = ""

        if self.is_edited:
            edited_text = " (edited)"

        print(
            f"[{self.role.upper()}] "
            f"{self.sender.username}: "
            f"{self.content}{edited_text}"
        )

    def edit_content(self, new_content: str) -> None:
        self.content = new_content
        self.is_edited = True

    def word_count(self) -> int:
        return len(self.content.split())

    @classmethod
    def display_total_messages(cls) -> None:
        print(f"Total messages: {cls.total_messages}")

    @staticmethod
    def is_valid_role(role: str) -> bool:
        valid_roles = [
            "user",
            "assistant",
            "system"
        ]

        return role.lower() in valid_roles


class ChatSession:
    def __init__(
        self,
        owner: User,
        model: AIModel
    ):
        self.owner = owner
        self.model = model
        self.messages: list[ChatMessage] = []

    def add_message(self, message: ChatMessage) -> None:
        self.messages.append(message)

    def display_chat(self) -> None:
        print(f"Chat owner: {self.owner.username}")
        print(f"AI model: {self.model.name}")
        print()
        print("Messages:")

        for message in self.messages:
            message.display_message()

    def message_count(self) -> int:
        return len(self.messages)


# --------------------------------------------------
# CREATE USERS
# --------------------------------------------------

user_1 = User(
    "abubakr",
    "abubakr@example.com"
)

admin_1 = AdminUser(
    "sara",
    "sara@example.com",
    [
        "manage users",
        "delete messages"
    ]
)


# --------------------------------------------------
# CREATE AI MODEL
# --------------------------------------------------

model_1 = AIModel(
    "Nova Pro",
    "OpenAI",
    1_000_000
)


# --------------------------------------------------
# DISPLAY USERS
# --------------------------------------------------

print("=== USERS ===")

print()

user_1.display_profile()
user_1.display_role()

print()

admin_1.display_profile()
admin_1.display_role()
admin_1.display_permissions()

print()

User.display_total_users()


# --------------------------------------------------
# DISPLAY AI MODEL
# --------------------------------------------------

print()
print("=== AI MODEL ===")
print()

model_1.display_info()

print()

print(
    f"Request supported: "
    f"{model_1.supports_request(800_000, 200_000)}"
)

print(
    f"Provider valid: "
    f"{AIModel.is_valid_provider(model_1.provider)}"
)

AIModel.display_total_models()


# --------------------------------------------------
# CREATE CHAT MESSAGES
# --------------------------------------------------

message_1 = ChatMessage(
    user_1,
    "What is inheritance in Python?",
    "user"
)

message_2 = ChatMessage(
    admin_1,
    "Inheritance allows one class to reuse another class.",
    "assistant"
)

message_3 = ChatMessage(
    user_1,
    "What about composition?",
    "user"
)

message_4 = ChatMessage(
    admin_1,
    "Composition means one object contains or uses other objects.",
    "assistant"
)


# --------------------------------------------------
# CREATE CHAT SESSION
# --------------------------------------------------

chat_session = ChatSession(
    user_1,
    model_1
)


# --------------------------------------------------
# ADD MESSAGES TO CHAT SESSION
# --------------------------------------------------

chat_session.add_message(message_1)
chat_session.add_message(message_2)
chat_session.add_message(message_3)
chat_session.add_message(message_4)


# --------------------------------------------------
# DISPLAY CHAT
# --------------------------------------------------

print()
print("=== CHAT SESSION ===")
print()

chat_session.display_chat()

print()

print(
    f"Messages in this session: "
    f"{chat_session.message_count()}"
)

ChatMessage.display_total_messages()


# --------------------------------------------------
# EDIT A MESSAGE
# --------------------------------------------------

print()
print("=== EDITED MESSAGE ===")
print()

message_1.edit_content(
    "Can you explain inheritance in Python?"
)

message_1.display_message()

print()

ChatMessage.display_total_messages()


# --------------------------------------------------
# VALIDATE ROLES
# --------------------------------------------------

print()
print("=== ROLE VALIDATION ===")
print()

print(
    f"user: "
    f"{ChatMessage.is_valid_role('user')}"
)

print(
    f"ASSISTANT: "
    f"{ChatMessage.is_valid_role('ASSISTANT')}"
)

print(
    f"admin: "
    f"{ChatMessage.is_valid_role('admin')}"
)