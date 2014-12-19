class LibOperation():
    def __init__(self, subject, func):
        self.subject = subject
        if func:
            self.func = func

    def execute(self, library):
        self.func(library, self.subject)

    def func(self, library):
        return NotImplemented

def add_song(library, subject):
    library.add_song(subject)

def remove_song(library, subject):
    library.library_db.del_song(subject)
