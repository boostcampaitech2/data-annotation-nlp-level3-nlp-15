import os
import kss
from glob import glob
import numpy as np
from tqdm import tqdm  # make individual files as sentences

# designate root path for the data
DATA_ROOT_PATH = "./data"

# read txt file from line by line
def read_txt(path):
    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()
    return lines


# make preprocessing function
def preprocess(list_lines: list) -> list:
    # remove \n
    list_lines = [line.strip() for line in list_lines]

    # remove empty lines
    list_lines = [line for line in list_lines if line]

    # remove duplicate elements from the list_lines
    list_lines = list(set(list_lines))
    return list_lines


def break_sentence(list_sentences: list) -> list:
    """
    break the string items of the list_poetic_sentences by ".", "!", "?"
    into two different string and and back to the list
    """

    # drop empty items
    list_sentences = [sentence for sentence in list_sentences if sentence]

    # strip whitespace
    list_sentences = [sentence.strip() for sentence in list_sentences]

    # split string item into sublist
    list_sentences = [kss.split_sentences(sentence) for sentence in list_sentences]

    # pull out items from the nested list
    list_sentences = [item for sublist in list_sentences for item in sublist]

    # drop empty items
    list_sentences = [sentence for sentence in list_sentences if sentence]

    return list_sentences


def preprocess_individual_sentences(input_list):
    # drop items length less than 15 characters
    input_list_dropped = [item for item in input_list if len(item) > 15]

    # drop items where the string is only constituted with alphabets
    # input_list_dropped = [item for item in input_list_dropped if not item.isalpha()]
    return input_list_dropped


# make sampling function from the list
def sampling(list_lines: list, n: int) -> list:
    # sampling
    list_lines = np.random.choice(list_lines, n)
    list_lines = list(list_lines)
    return list_lines


if __name__ == "__main__":
    list_files = glob(os.path.join(DATA_ROOT_PATH, "*.txt"))
    for file_item in list_files:
        lines = read_txt(file_item)
        lines = preprocess(lines)
        lines = break_sentence(lines)
        list_concat = list_concat + lines
    print(sampling(list_concat, n=20))

    list_concat_dropped = preprocess_individual_sentences(list_concat)

    with open(os.path.join("./", "result.txt"), "w", encoding="utf-8") as f:
        for sentence in list_concat_dropped:
            if "\n" in sentence:
                f.write(sentence)
            else:
                f.write(sentence + "\n")

    with open("./result.txt", "r", encoding="utf-8") as f:
        list_concat_loaded = f.readlines()
    print(len(list_concat_loaded))

    for index_no, item in enumerate(tqdm(list_concat_loaded)):
        # name the file as result_0001.txt, result_0002.txt, etc.
        with open(
            os.path.join("./", "result_" + str(index_no).zfill(4) + ".txt"),
            "w",
            encoding="utf-8",
        ) as f:
            f.write(item)
