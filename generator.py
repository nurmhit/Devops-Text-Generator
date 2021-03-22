import argparse
import json
import sys
import random
import numpy
import re
import scipy
import pandas
from collections import defaultdict


def loading_model_from_file():
    dict_with_model_of_my_text = json.load(input)
    return dict_with_model_of_my_text


def generating_text(dict_with_model_of_my_text, first_word, length,
                    max_amount_of_words_in_one_paragraph):
    """
    Функция, которая на вход получает первое слово, если оно есть,
    и длину последовательности, на основе этого генерирует
    последовательность следующим образом
    берет слово, смотрит на все возможные последующие
    и выбирает с помощью вероятности каждого из них
    first_word: Первое слово
    length: длина генерируемого текста
    max_amount_of_words_in_one_paragraph: максимальное количество слов
    в одном абзаце
    dict_with_model_of_my_text: словарь с моделью данного текста
    """
    words_list = []
    if first_word is None:
        first_word = random.choice(
            list(dict_with_model_of_my_text.keys()))
    current_word = first_word
    for index in range(length):
        words_list.append(current_word)
        current_word = numpy.random.choice(
            list(dict_with_model_of_my_text[current_word].keys()),
            p=list(dict_with_model_of_my_text[current_word].values()))
        if len(words_list) >= max_amount_of_words_in_one_paragraph:
            text = ' '.join(words_list) + ' '
            output.write(text + '\n')
            words_list = []
        """
        Переменная text содержит в себе абзац, который был сгенерирован
        на данный момент.
        В случае, если количество слов превысит максимально допустимое
        (max_amount_of_words_in_one_paragraph), мы выводим наш абзац
        и начинаем генерацию нового, в случае необходимости
        """
    output.write(' '.join(words_list) + ' ' + '\n')


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--model', type=str,
                        help="place where analise is written",
                        required=True)
    parser.add_argument('--seed', type=str, default=None, help='first_word')
    parser.add_argument('--length', type=int,
                        help='how many words should be generated',
                        required=True)
    parser.add_argument('--output', type=str, default=None,
                        help='output file')
    parser.add_argument("--max-words", type=int,
                        help="maximum number of words in one paragraph",
                        default=100
                        )
    args = parser.parse_args()

    input = open(args.model, "r")
    output = sys.stdout if args.output is None else open(args.output, "w")
    dict_with_model_of_my_text = loading_model_from_file()
    generating_text(dict_with_model_of_my_text, args.seed, args.length,
                    args.max_words)
    input.close()
    output.close()
