class Indenter:
    def __init__(self):
        self.level = 0

    def __enter__(self):
        self.level += 1

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.level -= 1

    def write(self, text):
        print('\t' * self.level + text)


indent = Indenter()  # had to add this to make this work despite what book said.
with indent:
    indent.write('hi!')
    with indent:
        indent.write('hello!')
        with indent:
            indent.write('bonjour')
    indent.write('hey')
