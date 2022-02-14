import re


def function_separation(filename: str, content: str) -> list:
    if len(re.findall("}\n{3,}", content)) > 0:
        index: int = content.split("\n\n\n")[0].count('\n') + 2
        return [{"type": "minor", "file": filename, "line": index, "name": "G2: Separation of functions"}]
    return []
