def extract_query_params(query: str) -> dict:
    if not query.startswith("?"):
        raise ValueError("Invalid query string")

    query = query[1:]
    params = query.split("&")

    query_params = {}

    for param in params:
        parts = param.split("=")
        if len(parts) != 2 or not parts[0] or parts[1] == "":
            raise ValueError("Invalid query parameter: missing '=' or value")
        key, value = parts
        query_params[key] = value

    return query_params
