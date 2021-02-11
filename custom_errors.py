class NameTooShortError(ValueError):
    pass


raise NameTooShortError("foo")
