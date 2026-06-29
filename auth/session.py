import os
from core.user_client import EtherUserClient
from config.config import Config


def session_exists() -> bool:
    return os.path.exists(f"{Config.SESSION_NAME}.session")


async def is_session_authorized() -> bool:
    client_wrapper = EtherUserClient()

    await client_wrapper.connect()

    try:
        return await client_wrapper.is_authorized() is True

    except Exception:
        return False