# Python Classes and Object-Oriented Programming

## What Is a Class?

A class is a blueprint used to create objects.

It defines the data and behavior that objects of that type should have.

Example:

```python
class User:
    pass
```

This creates a class named `User`, but no object has been created yet.

---

## What Is an Object?

An object is an instance created from a class.

```python
class User:
    pass


user = User()
```

Here:

```text
User
```

is the class.

And:

```text
user
```

is an object created from that class.

Multiple objects can be created from the same class:

```python
user_one = User()
user_two = User()
```

They are separate objects even though they share the same class structure.

---

## The Constructor

The constructor initializes a new object.

In Python, the constructor method is:

```python
__init__()
```

Example:

```python
class User:
    def __init__(self, name: str, email: str) -> None:
        self.name = name
        self.email = email
```

Creating an object:

```python
user = User(
    name="Abubakr",
    email="abubakr@example.com",
)
```

When the object is created, Python automatically calls:

```python
__init__()
```

---

## Understanding `self`

`self` refers to the current object.

```python
class User:
    def __init__(self, name: str) -> None:
        self.name = name
```

In:

```python
self.name = name
```

the parameter:

```text
name
```

contains the value passed to the constructor.

The attribute:

```text
self.name
```

stores that value inside the object.

Example:

```python
user = User("Sara")

print(user.name)
```

Output:

```text
Sara
```

Each object stores its own data:

```python
user_one = User("Sara")
user_two = User("Ahmed")

print(user_one.name)
print(user_two.name)
```

Output:

```text
Sara
Ahmed
```

---

## Instance Attributes

Instance attributes belong to individual objects.

```python
class AIModel:
    def __init__(
        self,
        name: str,
        version: str,
    ) -> None:
        self.name = name
        self.version = version
```

Usage:

```python
model = AIModel(
    name="Text Generator",
    version="1.0",
)

print(model.name)
print(model.version)
```

Each `AIModel` object can have different values.

---

## Instance Methods

An instance method is a function defined inside a class that works with an object.

```python
class User:
    def __init__(self, name: str) -> None:
        self.name = name

    def introduce(self) -> str:
        return f"My name is {self.name}."
```

Usage:

```python
user = User("Abubakr")

message = user.introduce()

print(message)
```

Output:

```text
My name is Abubakr.
```

Instance methods receive `self` as their first parameter.

Through `self`, they can access and modify the object’s attributes.

---

## Modifying Object State

Methods can change the values stored inside an object.

```python
class User:
    def __init__(self, name: str, is_active: bool = True) -> None:
        self.name = name
        self.is_active = is_active

    def deactivate(self) -> None:
        self.is_active = False
```

Usage:

```python
user = User("Sara")

print(user.is_active)

user.deactivate()

print(user.is_active)
```

Output:

```text
True
False
```

The object’s current stored data is often called its state.

---

## Class Attributes

A class attribute belongs to the class and is shared by its objects.

```python
class User:
    platform_name = "AI Platform"

    def __init__(self, name: str) -> None:
        self.name = name
```

Usage:

```python
user_one = User("Sara")
user_two = User("Ahmed")

print(user_one.platform_name)
print(user_two.platform_name)
```

Both objects access the same class attribute.

Instance attributes usually represent data unique to each object.

Class attributes usually represent shared information.

---

## Class Methods

A class method works with the class instead of one specific object.

It uses:

```python
@classmethod
```

and receives:

```python
cls
```

as its first parameter.

Example:

```python
class AIModel:
    model_count = 0

    def __init__(self, name: str) -> None:
        self.name = name
        AIModel.model_count += 1

    @classmethod
    def get_model_count(cls) -> int:
        return cls.model_count
```

Usage:

```python
model_one = AIModel("Classifier")
model_two = AIModel("Text Generator")

print(AIModel.get_model_count())
```

Output:

```text
2
```

A class method can access or modify class-level information.

---

## Alternative Constructors

Class methods can also create objects in different ways.

```python
class User:
    def __init__(self, name: str, email: str) -> None:
        self.name = name
        self.email = email

    @classmethod
    def from_string(cls, user_data: str) -> "User":
        name, email = user_data.split(",")

        return cls(
            name=name,
            email=email,
        )
```

Usage:

```python
user = User.from_string(
    "Abubakr,abubakr@example.com"
)

print(user.name)
print(user.email)
```

This is called an alternative constructor.

---

## Static Methods

A static method belongs logically to a class but does not need access to:

```text
self
```

or:

```text
cls
```

It uses:

```python
@staticmethod
```

Example:

```python
class UserValidator:
    @staticmethod
    def is_valid_email(email: str) -> bool:
        return "@" in email and "." in email
```

Usage:

```python
result = UserValidator.is_valid_email(
    "user@example.com"
)

print(result)
```

Output:

```text
True
```

A static method is useful when a helper function is closely related to the class but does not require object or class data.

---

## Instance Method vs Class Method vs Static Method

### Instance method

```python
def method(self):
```

Works with a specific object.

Can access:

```text
self.attribute
```

### Class method

```python
@classmethod
def method(cls):
```

Works with the class.

Can access:

```text
cls.class_attribute
```

### Static method

```python
@staticmethod
def method():
```

Does not automatically receive an object or class.

Used for related utility logic.

---

## Inheritance

Inheritance allows one class to reuse and extend another class.

The original class is called the parent or base class.

The new class is called the child or derived class.

Example:

```python
class User:
    def __init__(self, name: str) -> None:
        self.name = name

    def get_role(self) -> str:
        return "User"


class AdminUser(User):
    def get_role(self) -> str:
        return "Admin"
```

Usage:

```python
admin = AdminUser("Abubakr")

print(admin.name)
print(admin.get_role())
```

`AdminUser` inherits:

```text
name
```

and other behavior from `User`.

Conceptually:

```text
AdminUser IS A User
```

---

## Using `super()`

`super()` allows a child class to call behavior from its parent class.

```python
class User:
    def __init__(self, name: str) -> None:
        self.name = name


class AdminUser(User):
    def __init__(
        self,
        name: str,
        permissions: list[str],
    ) -> None:
        super().__init__(name)
        self.permissions = permissions
```

This line:

```python
super().__init__(name)
```

calls the constructor from `User`.

Without it, the child class would need to duplicate the parent initialization logic.

---

## Method Overriding

A child class can replace a method inherited from its parent.

```python
class User:
    def describe_role(self) -> str:
        return "Standard user"


class AdminUser(User):
    def describe_role(self) -> str:
        return "Administrator"
```

Usage:

```python
user = User()
admin = AdminUser()

print(user.describe_role())
print(admin.describe_role())
```

Output:

```text
Standard user
Administrator
```

Both classes use the same method name but provide different behavior.

---

## Composition

Composition means one object contains or uses other objects.

Example:

```python
class AIModel:
    def __init__(self, name: str) -> None:
        self.name = name


class ChatSession:
    def __init__(self, model: AIModel) -> None:
        self.model = model
        self.messages: list[str] = []
```

Usage:

```python
model = AIModel("Assistant Model")
session = ChatSession(model)
```

Conceptually:

```text
ChatSession HAS an AIModel
```

Composition represents a “has-a” relationship.

Inheritance represents an “is-a” relationship.

```text
Inheritance:
AdminUser IS A User

Composition:
ChatSession HAS an AIModel
```

---

## Example: Chat Message Class

```python
class ChatMessage:
    def __init__(
        self,
        sender: str,
        content: str,
    ) -> None:
        self.sender = sender
        self.content = content

    def format_message(self) -> str:
        return f"{self.sender}: {self.content}"
```

Usage:

```python
message = ChatMessage(
    sender="User",
    content="Explain machine learning.",
)

print(message.format_message())
```

Output:

```text
User: Explain machine learning.
```

The class keeps message data and message-related behavior together.

---

## Example: AI Model Class

```python
class AIModel:
    def __init__(
        self,
        name: str,
        provider: str,
        max_tokens: int,
    ) -> None:
        self.name = name
        self.provider = provider
        self.max_tokens = max_tokens

    def describe(self) -> str:
        return (
            f"{self.name} by {self.provider} "
            f"supports {self.max_tokens} tokens."
        )
```

Usage:

```python
model = AIModel(
    name="Text Model",
    provider="Example Provider",
    max_tokens=4096,
)

print(model.describe())
```

---

## Separation of Responsibilities

Classes should have clear responsibilities.

Less maintainable:

```python
class Application:
    def create_user(self):
        pass

    def clean_dataset(self):
        pass

    def send_email(self):
        pass

    def run_ai_model(self):
        pass
```

This class is responsible for unrelated tasks.

A clearer design could use:

```python
class UserService:
    pass


class DatasetCleaner:
    pass


class EmailService:
    pass


class AIModelService:
    pass
```

Each class focuses on one area of the application.

---

## Classes as Data Models

A class can represent structured application data.

```python
class CleaningStats:
    def __init__(
        self,
        average_age: float,
        average_score: float,
        highest_score: int,
        lowest_score: int,
    ) -> None:
        self.average_age = average_age
        self.average_score = average_score
        self.highest_score = highest_score
        self.lowest_score = lowest_score
```

Instead of returning four unrelated variables:

```python
average_age
average_score
highest_score
lowest_score
```

the program can return one object:

```python
stats = CleaningStats(
    average_age=25.0,
    average_score=88.2,
    highest_score=95,
    lowest_score=81,
)
```

Then access:

```python
stats.average_age
stats.average_score
stats.highest_score
stats.lowest_score
```

---

## Why Classes Matter in AI Development

Classes are frequently used to represent:

- AI models
- Users
- Chat messages
- Chat sessions
- Documents
- Embeddings
- Predictions
- Training configurations
- Dataset information
- API clients
- Evaluation results
- Application services

Example architecture:

```text
models/
    ChatMessage
    PredictionResult
    ModelConfiguration

services/
    LLMService
    EmbeddingService
    EvaluationService
```

Classes help organize complex applications into understandable components.

---

## When to Use a Class

A class is useful when:

- Several pieces of data belong together.
- Functions repeatedly operate on the same data.
- Multiple similar objects need to be created.
- An object must maintain state.
- Inheritance or composition represents the problem clearly.
- A larger application needs organized responsibilities.

A simple function may be better when:

- The task is small.
- No persistent object state is required.
- The logic only transforms input into output.
- Creating a class would add unnecessary complexity.

Not every function needs to become a class.

---

## Summary

A class is a blueprint for creating objects.

Important concepts include:

- Classes define structure and behavior.
- Objects are instances of classes.
- `__init__()` initializes new objects.
- `self` refers to the current object.
- Instance attributes store object-specific data.
- Instance methods operate on objects.
- Class attributes store shared data.
- Class methods operate on the class.
- Static methods provide related utility behavior.
- Inheritance represents an “is-a” relationship.
- Composition represents a “has-a” relationship.
- Classes can represent both data and application behavior.

Well-designed classes make larger Python and AI applications easier to understand, extend, test, and maintain.