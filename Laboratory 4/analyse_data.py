import os
import json
import shlex
import subprocess
import sys
import to_json


def analyse_data(path):

    results = []
    data = os.listdir(path)

    for file in data:
        filepath = os.path.join(path, file)
        ext = os.path.splitext(filepath)[-1].lower()

        if ext == '.txt':
            output = subprocess.run(['python',  'to_json.py', filepath], capture_output=True)
            data = json.loads(output.stdout)
            results.append(data)

    num_files = len(results)
    num_chars = sum(d['num_chars'] for d in results)
    num_words = sum(d['num_words'] for d in results)
    num_lines = sum(d['num_lines'] for d in results)

    # freq_chars = {}
    # freq_words = {}
    #
    # for d in results:
    #     for char, count in d['most_common_char'].items():
    #         if char in freq_chars:
    #             freq_chars[char] += count
    #         else:
    #             freq_chars[char] = count
    #
    #     for word, count in d['most_common_word'].items():
    #         if word in freq_words:
    #             freq_words[word] += count
    #         else:
    #             freq_words[word] = count
    #
    # most_common_char = max(freq_chars, key=freq_chars.get)
    # most_common_word = max(freq_words, key=freq_words.get)

    toReturn = {
        "read_files": num_files,
        "num_chars": num_chars,
        "num_words:": num_words,
        "num_lines": num_lines
    }

    return toReturn


if __name__ == '__main__':
    result = analyse_data(sys.argv[1])
    print(result)
