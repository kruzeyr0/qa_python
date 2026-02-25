"""
Ваша команда та ви розробляєте систему входу для веб-додатка,
і вам потрібно реалізувати тести на функцію для логування подій в системі входу.
Дано функцію, напишіть набір тестів для неї.
"""

import logging

_STATUS_TO_LEVEL = {
    "success": logging.INFO,
    "expired": logging.WARNING,
    "failed": logging.ERROR,
}


def _get_logger() -> logging.Logger:
    logger = logging.getLogger("log_event")
    if logger.handlers:
        return logger

    logger.setLevel(logging.INFO)
    handler = logging.FileHandler("login_system.log")
    handler.setFormatter(logging.Formatter("%(asctime)s - %(message)s"))
    logger.addHandler(handler)
    logger.propagate = False
    return logger


def log_event(username: str, status: str):
    """
    Логує подію входу в систему.

    username: Ім'я користувача, яке входить в систему.

    status: Статус події входу:

    * success - успішний, логується на рівні info
    * expired - пароль застаріває і його слід замінити, логується на рівні warning
    * failed  - пароль невірний, логується на рівні error
    """
    log_message = f"Login event - Username: {username}, Status: {status}"
    level = _STATUS_TO_LEVEL.get(status, logging.ERROR)
    _get_logger().log(level, log_message)
