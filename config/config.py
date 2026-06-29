from dotenv import load_dotenv
import os

load_dotenv()


class Config:

    API_ID: int = int(os.getenv("30422005", 0))
    API_HASH: str = os.getenv("5170ded206641d73215baf40175a6924", "")
    OWNER_ID: int = int(os.getenv("8693729060", 0))
    
    BOT_TOKEN: str = os.getenv("BOT_TOKEN", "")
    BOT_USERNAME: str = os.getenv("BOT_USERNAME", "")  # Without @, e.g. "Etheruserbot"
    
    SESSION_NAME: str = os.getenv("SESSION_NAME", "etheruserbot")
    SESSION_DIR: str = os.getenv("SESSION_DIR", "sessions")

    MONGO_URI: str = os.getenv("MONGO_URI", "")
    DB_NAME: str = os.getenv("DB_NAME", "Ether")
    
    DEBUG: bool = os.getenv("DEBUG", "False").lower() == "true"
    
    # Dm Protection Settings
    DM_MAX_WARNS: int = int(os.getenv("DM_MAX_WARNS", "3"))
    
    @classmethod
    def validate(cls) -> None:
        missing = []
        
        if not cls.API_ID:
            missing.append("API_ID")
        if not cls.API_HASH:
            missing.append("API_HASH")
        if not cls.OWNER_ID:
            missing.append("OWNER_ID")
        
        if missing:
            raise ValueError(
                f"Missing required environment variables: {', '.join(missing)}"
            )


# Validate on import
Config.validate()
