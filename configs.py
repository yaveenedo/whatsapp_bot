import os

path_project_folder = os.path.dirname(os.path.realpath(__file__))
path_log_file = os.path.join(path_project_folder, 'logs', 'log.txt')
windows_username = os.environ.get('username')