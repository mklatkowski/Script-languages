import json
import sys


def to_json(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    num_chars = len(content)
    num_lines = content.count('\n') + 1

    words = content.split()
    num_words = len(words)

    freq_chars = {}
    freq_words = {}

    for char in content:
        if char in freq_chars:
            freq_chars[char] += 1
        else:
            freq_chars[char] = 1

    for word in words:
        if word in freq_words:
            freq_words[word] += 1
        else:
            freq_words[word] = 1

    most_common_char = max(freq_chars, key=freq_chars.get)
    most_common_word = max(freq_words, key=freq_words.get)

    data = {
        "filepath": filepath,
        "num_chars": num_chars,
        "num_words": num_words,
        "num_lines": num_lines,
        "most_common_char": most_common_char,
        "most_common_word": most_common_word
    }
    sys.stdout.write(json.dumps(data))


if __name__ == "__main__":
    to_json(sys.argv[1])