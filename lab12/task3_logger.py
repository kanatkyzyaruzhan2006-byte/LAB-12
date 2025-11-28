from abc import ABC, abstractmethod

class Logger(ABC):
    def header(self):
        print("=== LOG START ===")

    @abstractmethod
    def log(self, message):
        pass


class FileLogger(Logger):
    def log(self, message):
        with open("log.txt", "a", encoding="utf-8") as f:
            f.write(message + "\n")


class ConsoleLogger(Logger):
    def log(self, message):
        print(message)


f = FileLogger()
f.header()
f.log("Сообщение записано в файл")

c = ConsoleLogger()
c.header()
c.log("Сообщение в консоли")
