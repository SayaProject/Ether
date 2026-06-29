import hashlib
import base64

# Official channels - DO NOT MODIFY
_CHANNELS = {
    "Saya Project": "https://github.com/SayaProject",
    "Saya Projectt": "https://t.me/SayaProject"
}

_INTEGRITY_SIGNATURE = base64.b64encode(
    str(sorted(_CHANNELS.items())).encode()
).decode()


def get_channels():
    return _CHANNELS.copy()


def validate_integrity():
    current_signature = base64.b64encode(
        str(sorted(_CHANNELS.items())).encode()
    ).decode()
    
    return current_signature == _INTEGRITY_SIGNATURE


def get_channel_list():
    return list(_CHANNELS.values())


def get_channel_names():
    """Get channel names."""
    return list(_CHANNELS.keys())


def generate_integrity_hash():
    channel_string = str(sorted(_CHANNELS.items()))
    return hashlib.sha256(channel_string.encode()).hexdigest()[:32]


if __name__ == "__main__":
    print("Current integrity hash:")
    print(generate_integrity_hash())
