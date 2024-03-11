import re


def build_route_path(path: str) -> re.Pattern:
    if not path.strip():
        raise ValueError("Invalid path")

    route_regex_param = r":([a-zA-Z]+)"
    path_with_params = re.sub(route_regex_param, r"(?P<\1>[a-z0-9\-_]+)", path)
    path_regex = re.compile(rf"^{path_with_params}(?P<query>\?(.*))?$")

    return path_regex
