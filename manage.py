#!/usr/bin/env python
#!/usr/bin/eval PYTHONPATH=/home/mgdb/modules python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mangalw.settings")
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
else:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mangalw.settings")
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
