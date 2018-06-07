'''Checks the internet

This program will check the status of some websites'''

import subprocess

subprocess.check_output(["ping", "-c", "1", "google.com"])

