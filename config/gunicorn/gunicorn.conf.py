import multiprocessing


bind = "0.0.0.0:8000"
log_level = 'info'
error_log ='-'
access_log = '-'
workers = multiprocessing.cpu_count() * 2 + 1