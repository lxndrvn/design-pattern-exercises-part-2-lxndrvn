import random

class State(object):
    def mix(self):
        print("Mixing next song! DJ used {0} on {1}".format(self.technique, self.name))


class ControllerState(State):
    """
    DJ tool used for playing tracks from laptop.
    """
    def __init__(self, dj):
        self.dj = dj
        self.technique = "looping"
        self.name = "Controller"

    def change_dj_tool(self):
        print "Switching to turntable"
        self.dj.state = self.dj.turntable


class TurntableState(State):
    """
    DJ tool used for playing vinyl records.
    """
    def __init__(self, dj):
        self.dj = dj
        self.technique = "scratching"
        self.name = "Turntable"

    def change_dj_tool(self):
        print "Switching to controller"
        self.dj.state = self.dj.controller


class DJ(object):
    def __init__(self):
        self.turntable = TurntableState(self)
        self.controller = ControllerState(self)
        self.state = self.controller

    def change_dj_tool(self):
        self.state.change_dj_tool()

    def mix(self):
        self.state.mix()


def main():
    dj = DJ()
    for i in range(20):
        action = random.choice([dj.mix, dj.change_dj_tool])
        action()

if __name__ == '__main__':
    main()