class User:
    def __init__(self, email, password):
        self.email = email
        self.password = password

    def toDict(self):
        return {
            "email": self.email,
            "password": self.password
        }

    @classmethod
    def fromDict(cls, data):
        return cls(
            email=data.get("email"),
            password=data.get("password")
        )