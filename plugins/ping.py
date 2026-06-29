import time
from telethon import events
from utils.logger import get_logger

logger = get_logger("EtherPing")


def setup(ether, db, owner_id):


# ============================================
# Ping Command
# ============================================
    
    @ether.on(events.NewMessage(pattern=r"^\.ping$", outgoing=True))
    async def ping_handler(event):
        start = time.time()

        if event.sender_id != owner_id:
            return
        msg = await event.reply("<blockquote>🏓 <i>Pinging...</i></blockquote>", parse_mode="html")
        
        latency = int((time.time() - start) * 1000)
        
        await msg.edit(
            f"<blockquote>"
            f"🏓 <b>Pong!</b>\n"
            f"⚡ <code>{latency}ms</code>"
            "</blockquote>",
            parse_mode="html"
        )
        
        try:
            await event.delete()
        except Exception:
            pass
    
    logger.info("Ping plugin loaded")
