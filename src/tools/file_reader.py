import os

class CvFileReader:
    @staticmethod
    def read(path):
        try:
            with open(path, "r") as f:
                return f.read()
        except FileNotFoundError:
            return None
