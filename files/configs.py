import json

class GraphUnitConfig:
    def __init__(self):
        self.unitname = "unit template"
        self.grid_label = True
        self.grid_ticks_minor = 5
        self.grid_ticks_major = 10
        self.startmin = 0
        self.startmax = 100

        return

    # TODO serializing *should* be moved to its own module under /files/
    def serializeConfig(self, filepath):
        with open(filepath, 'w') as fp:
            json.dump(self.__dict__, fp, sort_keys=True, indent=4, separators=(',', ':'))

    def deserializeConfig(self, filepath):
        with open(filepath, 'r') as fp:
            self.__dict__ = json.load(fp)
        return self