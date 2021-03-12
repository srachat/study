import os
import re
from typing import Any, Dict, Optional


def render_template(template_name: str, data: Optional[Dict[str, Any]] = None) -> str:
    if not os.path.exists("templates"):
        raise FileNotFoundError("Templates folder was not found")

    template_file_path = f"templates/{template_name}"
    if not os.path.exists(template_file_path):
        raise FileNotFoundError("Template does not exist")

    return _populate_template(template_file_path, data)


def _populate_template(template_file_path: str, data: Optional[Dict[str, Any]]) -> str:
    with open(template_file_path) as template:
        template_string = template.read()

    if not data:
        return template_string

    left_part = r"{\s*%\s*"
    right_part = r"\s*%\s*}"

    for key, value in data.items():
        key_pattern = left_part + str(key) + right_part
        template_string = re.sub(key_pattern, str(value), template_string)

    return template_string

