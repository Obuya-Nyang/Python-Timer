import time


class TimeError(Exception):
    pass


class Timer:
    # class instantiation
    def __init__(self):
        self._start_time = None

    # start a new timer
    def start(self):
        if self._start_time is not None:
            raise TimeError(f"Timer is running. Use .stop() to stop it.")

        self._start_time = time.perf_counter()

    # stop a timer and report elapsed time
    def stop(self):
        if self._start_time is None:
            raise TimeError(f"Timer is not running. Use .start() to start it.")

        elapsed_time = time.perf_counter() - self._start_time
        self._start_time = None
        print(f"Elapsed time: {elapsed_time:0.4f} seconds")
