from cx_Freeze import setup, Executable
  
setup(name = "App" ,
      version = "0.1" ,
      description = "" ,
      executables = [Executable("app_main.py")])