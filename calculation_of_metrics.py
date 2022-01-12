from count_mistakes import count_mistakes


class Metrics:
    """Класс для определения, расчета и вывода метрик"""

    def __init__(self, session_time, user_input, sentence):
        self.number_of_characters = len(sentence)
        self.input_time = session_time
        self.user_input = len(user_input)
        self.sentence = sentence
        self.number_of_errors = count_mistakes(sentence, user_input)

    @property
    def cpm(self):
        """Расчет количества символов в минуту"""
        return round((self.user_input / self.input_time) * 60)

    @property
    def percent_err(self):
        """Расчет процента ошибок"""
        return round((self.number_of_errors / self.number_of_characters) * 100)

    @percent_err.setter
    def percent_err(self, value):
        self._percent_err = value

    @cpm.setter
    def cpm(self, value):
        self._cpm = value

    def __add__(self, cls):
        """Переопределение метода сложения метрик"""
        answer = Metrics(self.input_time + cls.input_time, f"{self.user_input} {cls.user_input}",
            f"{self.sentence} {cls.sentence}")
        answer.number_of_characters = self.number_of_characters + cls.number_of_characters
        answer.user_input = self.user_input + cls.user_input
        answer.input_time = self.input_time + cls.input_time
        answer.cpm = (self.cpm + cls.cpm) // 2
        answer.number_of_errors = self.number_of_errors + cls.number_of_errors  
        return answer

    def __str__(self):
        """Переопределение метода вывода метрики"""
        return f"Символов: {self.number_of_characters}, симв./мин.: {self.cpm}, \
ошибок: {self.number_of_errors}, процент ошибок: {self.percent_err}%"
