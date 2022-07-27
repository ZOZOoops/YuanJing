import os

class PathName():

    dir_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    common_path = os.path.join(dir_path,'common')
    config_path = os.path.join(dir_path,'config')
    drivers_path = os.path.join(dir_path,'drivers')
    practice_path = os.path.join(dir_path,'practice')
    testcases_path = os.path.join(dir_path,'testcases')
    testlog = os.path.join(dir_path,'testlog')







