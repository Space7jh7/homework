def repeat(text: str, count: int) -> tuple[str, int]:
    return text * count, int(text * count)

message: tuple[str, int] = repeat("API", 2)
print(message)
assert message == "APIAPI"