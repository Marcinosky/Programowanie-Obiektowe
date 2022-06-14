import pupil_exception

class Pupil:

    grades = {1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6}

    def __init__(self, given_name: str, given_surname: str):
        self.name = given_name
        self.surname = given_surname
        self._marks = {}

    @property
    def name(self):
        return self._name

    @property
    def marks(self):
        return self._marks

    @name.setter
    def name(self, name: str):
        if name.isalpha() and len(name) > 2:
            self._name = name
        elif not name.isalpha():
            raise pupil_exception.NameNotAlphaException
        else:
            raise pupil_exception.NameTooShortException

    @property
    def surname(self):
        return self._surname

    @surname.setter
    def surname(self, surname: str):
        if surname.isalpha() and len(surname) > 2:
            self._surname = surname
        elif not surname.isalpha():
            raise pupil_exception.NameNotAlphaException
        else:
            raise pupil_exception.NameTooShortException

    def complete_marks(self, subject: str, mark):
        if mark in Pupil.grades:
            self._marks[subject] = mark
        else:
            raise pupil_exception.IncorrectMark

    def print_marks(self):
        for subject, mark in self._marks:
            print(f"{subject}: {mark}")

    def mean(self):
        all_marks = sum(self._marks.values())
        return all_marks / len(self._marks)

    def __str__(self):
        return f"{self._name} {self._surname}: {self.mean()}"
