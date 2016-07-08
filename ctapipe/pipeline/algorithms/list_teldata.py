from time import sleep
import threading


class ListTelda():

    def __init__(self, configuration=None):
        self.configuration = configuration

    def init(self):
        print("--- ListTelda init ---")

    def run(self, event):
        if event != None:
            res = list(event.dl0.tels_with_data)
            return res

    def finish(self):
        print("--- ListTelda finish ---")
