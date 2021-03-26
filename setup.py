import cx_Freeze

executables = [cx_Freeze.Executable("snakeGame01.py")]

cx_Freeze.setup(
    name="Snake game",
    options={"build_exe": {"packages":["pygame","random","os","time"],
                           "include_files":["collision.mp3", "Root.mp3", "beep.mp3", "background.mp3", "highScore.txt"]}},
    executables = executables

    )