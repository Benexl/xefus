# SPDX-FileCopyrightText: 2026 Benexl <benextempest@gmail.com>
# SPDX-FileContributor: benexl
#
# SPDX-License-Identifier: AGPL-3.0-or-later

import os
from pathlib import Path

from platformdirs import (
    user_cache_path,
    user_config_path,
    user_data_path,
    user_log_path,
)

APP_NAME = os.environ.get("XEFUS_APP_NAME") or "xefus"

CONFIG_DIR = user_config_path(APP_NAME)

_env_config_path = os.environ.get("XEFUS_CONFIG_PATH")
CONFIG_FILE = Path(_env_config_path) if _env_config_path else CONFIG_DIR / "config.toml"

CACHE_DIR = user_cache_path(APP_NAME)

DATA_DIR = user_data_path(APP_NAME)

LOG_DIR = user_log_path(APP_NAME)
