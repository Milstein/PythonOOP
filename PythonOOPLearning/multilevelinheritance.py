class MusicalInstrument:
    no_of_major_keys = 12


class StringInsturment(MusicalInstrument):
    type_of_wood = 'Tonewood'


class Guitar(StringInsturment):
    def __init__(self):
        self.no_of_strings = 6
        print(
            'This guitar consists of {} strings. It is made up of {} and it can play {} keys.'.format(self.no_of_strings, self.type_of_wood, self.no_of_major_keys))


guitar = Guitar()