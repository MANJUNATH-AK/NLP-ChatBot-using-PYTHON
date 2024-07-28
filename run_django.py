
# run_django.py
import os
import sys
import webbrowser
from django.core.management import execute_from_command_line

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chatbot_project.settings')
    webbrowser.open('http://127.0.0.1:8000')
    execute_from_command_line([sys.argv[0], 'runserver', "--noreload"])
    # execute_from_command_line(["manage.py", "runserver", "--noreload"])
