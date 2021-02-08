import os
import shutil


class Backup:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination
        self.source_files = os.listdir(self.source)
        self.destination_files = os.listdir(self.destination)

    def sync(self):
        # Remove files in destination that do not exist in source
        for file in self.destination_files:
            if file not in self.source_files:
                os.remove(f"{self.destination}\\{file}")

        # Copy source files to destination if they are not already there
        for file in self.source_files:
            if file not in self.destination_files:
                shutil.copy(f"{self.source}\\{file}", f"{self.destination}\\{file}")
