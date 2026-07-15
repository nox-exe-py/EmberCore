
"""
EmberCore Configuration
Only global bot settings belong here.

Everything related to a Discord server
(channels, roles, tickets, logs, economy settings,
Minecraft server, etc.) is stored in the database
and configured using slash commands.
"""

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# =====================================================
# BOT
# =====================================================

BOT_NAME = "EmberCore"
BOT_VERSION = "1.0.0"

# =====================================================
# DISCORD
# =====================================================

TOKEN = os.getenv("TOKEN")
OWNER_ID = int(os.getenv("OWNER_ID", "0"))

# =====================================================
# DATABASE
# =====================================================

DATABASE_FILE = "database/embercore.db"

# =====================================================
# EMBEDS
# =====================================================

DEFAULT_COLOR = 0xF97316
SUCCESS_COLOR = 0x22C55E
ERROR_COLOR = 0xEF4444
WARNING_COLOR = 0xFACC15

# =====================================================
# LOGGING
# =====================================================

LOG_LEVEL = "INFO"

# =====================================================
# BOT STATUS
# =====================================================

STATUS_TEXT = "/help | EmberCore"
STATUS_TYPE = "watching"

# =====================================================
# DEFAULT PREFIX
# (Reserved for future use. EmberCore uses slash commands.)
# =====================================================

DEFAULT_PREFIX = "/"

# =====================================================
# VERSION INFO
# =====================================================

AUTHOR = "EmberCore Development Team"
GITHUB = ""
WEBSITE = ""
SUPPORT_SERVER = ""
