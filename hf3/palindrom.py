def is_palindrom(n: str) -> bool:
    result = n == n[::-1]
    if result:
        return True
    else:
        return False
