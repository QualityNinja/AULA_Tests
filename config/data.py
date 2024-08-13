import os
from dotenv import load_dotenv

load_dotenv()

# Логин и пароль


class Data:
    LOGIN = os.getenv("LOGIN")
    PASSWORD = os.getenv("PASSWORD")
