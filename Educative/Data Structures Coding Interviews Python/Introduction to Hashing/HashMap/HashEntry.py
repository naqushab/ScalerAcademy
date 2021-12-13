class HashEntry:
    def __init__(self, key, value) -> None:
        self.key = key
        self.value = value
        self.next = None

    def __str__(self) -> str:
        return f'Key : {self.key}, Value : {self.value}'
