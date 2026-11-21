#!/usr/bin/env python3
"""Run Phase 2 and tee output to log."""
import subprocess, sys

log_path = '/home/dannyryan1980/The-Silent-Strata/audit/phase2_progress.log'

with open(log_path, 'w') as log_f:
    proc = subprocess.Popen(
        ['/home/dannyryan1980/autonovel/.venv/bin/python3',
         '/home/dannyryan1980/autonovel/phase2_chapters.py'],
        stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
        text=True, bufsize=1
    )
    for line in proc.stdout:
        log_f.write(line)
        log_f.flush()
    proc.wait()
    log_f.write(f'\nExit code: {proc.returncode}\n')
