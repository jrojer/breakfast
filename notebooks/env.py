import dotenv
import os

dotenv.load_dotenv()


def _getOrThrow(key):
    value = os.getenv(key)
    if value is None:
        raise RuntimeError(f"Missing environment variable: {key}")
    return value


OPENAI_API_KEY = _getOrThrow("OPENAI_API_KEY")
