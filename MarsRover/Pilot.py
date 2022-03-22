class Pilot:

    # Pilot constructor
    def __init__(self, pilot_name=None):
        self.pilot_name = pilot_name

    # Pilot getter
    @property
    def pilot_name(self):
        return self._pilot_name

    # Pilot setter
    @pilot_name.setter
    def pilot_name(self, value):
        if not value:
            self._pilot_name = "Unknown Pilot"
        else:
            self._pilot_name = value
