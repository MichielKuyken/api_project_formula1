from passlib.context import CryptContext


pwd_context = CryptContext(schemes=["argon2", "bcrypt"], deprecated=False)


def get_password_hash(password):
    return pwd_context.hash(password)
