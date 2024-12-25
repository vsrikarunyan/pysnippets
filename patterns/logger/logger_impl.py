from .logger import Logger, LogLevel
import threading


class LoggerImpl(Logger):
    _instance = None
    _lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super(LoggerImpl, cls).__new__(cls)
        return cls._instance
    
    def __init__(self, log_file_path):
        if not hasattr(self, 'initialized'):
            self.log_file_path = log_file_path if log_file_path else 'application.log'
            self.file = None
            self.lock = threading.Lock()
            self.initialized = True

    def __enter__(self):
        self.file = open(self.log_file_path, 'a', encoding='utf-8')
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()

    @staticmethod
    def get_instance() -> Logger:
        return LoggerImpl('application.log')

    @staticmethod
    def reset_instance() -> None:
        with LoggerImpl._lock:
            LoggerImpl._instance = None

    def log(self, level: LogLevel, message: str) -> None:
        with self.lock:
            if self.file:
                self.file.write(f'{level.name}: {message}\n')

    def set_log_file(self, file_path: str) -> None:
        self.log_file_path = file_path

    def get_log_file(self) -> str:
        return self.log_file_path

    def flush(self) -> None:
        if self.file:
            self.file.flush()

    def close(self) -> None:
        if self.file:
            self.file.close()
            self.file = None
