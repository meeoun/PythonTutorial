from Backup import Backup
source = "C:\\Users\\kpark\\Documents\\PythonTutorial\\Tutorials\\PythonTutorial\\Code\\CustomBackupSolution\\source"
destination = "C:\\Users\\kpark\\Documents\\PythonTutorial\\Tutorials\\PythonTutorial\\Code\\CustomBackupSolution\\destination"

backup = Backup(source, destination)
backup.sync()
