import json
import argparse
import sys
import re
import os
from collections import defaultdict


def possibilities_normalization(dict_with_model_of_my_text):
    """
    Функция, пересчитывающая вероятности в словаре
    dict_with_model_of_my_text: словарь, в котором пересчитываются вероятности
    """
    for word in list(dict_with_model_of_my_text.keys()):
        words_occurrence_sum = sum(list(
            dict_with_model_of_my_text[word].values()))
        for next_word in dict_with_model_of_my_text[word].keys():
            dict_with_model_of_my_text[word][next_word] /= words_occurrence_sum


def writinig_model_of_text_into_dict(dict_with_model_of_my_text,
                                     is_lower, input_file=None):
    """
    Функция, записывающая модель текста в словарь из словарей
    при этом приводя к нижнему регистру при необходимости
    is_lower: флажок, показывающий нужно ли приводить к lowercase
    dict_with_model_of_my_text: словарь, в который нужно записать модель
    input_file: файл с входными данными
    """
    input = sys.stdin if input_file is None else open(input_file, "r")
    last_word_of_last_line = ""
    for line in input:
        if is_lower is True:
            line = line.lower()
        words = [last_word_of_last_line]
        words += re.findall(r"\w+", line)
        for i in range(len(words) - 1):
            dict_with_model_of_my_text[words[i]][words[i+1]] += 1
        last_word_of_last_line = words[-1]

    input.close()


def train(input_dir, is_lower):
    """
    Функция, обрабатывающая переданную директорию и записывающая
    в файл модель текста
    is_lower: флажок, показывающий нужно ли приводить к lowercase
    input_dir: директория, где лежат файлы с входными данными
    """
    dict_with_model_of_my_text = defaultdict(
        lambda: defaultdict(int))
    if input_dir is None:
        writinig_model_of_text_into_dict(dict_with_model_of_my_text, is_lower)
    else:
        for file in os.listdir(input_dir):
            if file.endswith(".txt"):
                input_file_name = input_dir + "/" + str(file)
                writinig_model_of_text_into_dict(
                    dict_with_model_of_my_text, is_lower, input_file_name)

    possibilities_normalization(dict_with_model_of_my_text)

    json.dump(dict_with_model_of_my_text, output)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--model', type=str,
                        help="place where analise is written",
                        required=True)
    parser.add_argument('--lc', action='store_true',
                        default=False,
                        help='going to lowercase')
    parser.add_argument('--input-dir', type=str, default=None,
                        help='directory with input file')
    args = parser.parse_args()
    output = open(args.model, "w")
    train(args.input_dir, args.lc)
    output.close()
