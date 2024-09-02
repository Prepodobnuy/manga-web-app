import datetime
import os

class Logger(object):
    def __init__(
            self, 
            log_file_path: str = '',
            log_to_file: bool = True,
            log_to_term: bool = True,
            displayed_log_level: int = 1 
        ) -> None:

        self.path = f"{log_file_path} {self.__get_date()}.log"
        self.file_log = log_to_file
        self.term_log = log_to_term
        self.log_level = displayed_log_level
        self.log_generator = self.__log_generator()


        self.file = ""
        if self.file_log:
            with open(self.path, 'w', encoding='utf-8'): pass
            self.file = open(self.path, 'a', encoding='utf-8')

    def __del__(self) -> None:
        if self.file_log:
            self.file.close()

    def __get_date(self) -> str:
        dd = datetime.datetime.now().day
        mm = datetime.datetime.now().month
        yyyy = datetime.datetime.now().year
        s = datetime.datetime.now().second
        m = datetime.datetime.now().minute
        h = datetime.datetime.now().hour

        dd = f"0{dd}" if dd < 10 else dd
        mm = f"0{mm}" if mm < 10 else mm
        s = f"0{s}" if s < 10 else s
        m = f"0{s}" if m < 10 else m
        h = f"0{s}" if h < 10 else h

        return f"{dd}.{mm}.{yyyy} {h}:{m}:{s}"

    def __log_generator(self):
        while True:
            if self.term_log: print(self.message)
            if self.file_log: self.file.write(self.message + os.linesep)
            yield None
    
    def log(self, *args, log_level: int = 0):
        if not log_level >= self.log_level: return

        log_message = ""
        match log_level:
            case 2: log_message = "[warning] "
            case 3: log_message = "[error] "
            case 4: log_message = "[fatal] "

        self.message = f"{log_message}[{self.__get_date()}] "
        for arg in args:
            self.message += f"{arg} "
        next(self.log_generator)
