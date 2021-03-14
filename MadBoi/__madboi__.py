import html
import re, os
import importlib
import json
import re
import os, sys
import time
import traceback
from sys import argv
from typing import Optional
import os
from telegram import (
    Chat,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
    ParseMode,
    Update,
    User,
)
from telegram.error import (
    BadRequest,
    ChatMigrated,
    NetworkError,
    TelegramError,
    TimedOut,
    Unauthorized,
)
from telegram.ext import (
    CallbackContext,
    CallbackQueryHandler,
    CommandHandler,
    Filters,
    MessageHandler,
)
from telegram.ext.dispatcher import DispatcherHandlerStop, run_async
from telegram.utils.helpers import escape_markdown



+-+ +-+ +-+ +-+      +-+ +-+ +-+                                                                                                             +-+ +-+ +-+ +-+      +-+ +-+ +-+
|D| |E| |A| |D|      |E| |N| |D|                                                                                                             |D| |E| |A| |D|      |E| |N| |D|
+-+ +-+ +-+ +-+      +-+ +-+ +-+                                                                                                             +-+ +-+ +-+ +-+      +-+ +-+ +-+

