
from typing import List

import pkg_resources


def get_lines(pkg_name: str, resource_name: str) -> List[str]:
    resource_content = pkg_resources.resource_string(pkg_name, resource_name)
    return list(filter(None, resource_content.decode().splitlines()))
