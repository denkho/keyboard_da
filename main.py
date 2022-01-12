from get_sentence import get_sentence, open_file, select_language
from sentence_output import sentence_output_input
from calculation_of_metrics import Metrics


if __name__ == '__main__':
    file_content = open_file(select_language())
    flag = 1
    while True:
        while True:
            user_input = input('Нажмите "Enter" для для старта клавиатурного тренажера, введите "z" для выхода: ')
            if not user_input:
                break
            elif user_input == 'z':
                exit()
        sentence = get_sentence(file_content)
        session_time, user_input = sentence_output_input(sentence)
        session_metrics = Metrics(session_time, user_input, sentence)
        if flag == 1:
            total_metrics = session_metrics
            flag = 0
        else:
            total_metrics += session_metrics
        print('Раунд:\t', session_metrics)
        print('Итого:\t', total_metrics)

