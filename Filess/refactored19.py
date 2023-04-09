class LoggableList(Loggable, list):
    def append(self, x):
        super().append(x)
        self.log(x)