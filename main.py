from collections import Counter
import math

pseudoCount = 1


def main():
    n = int(input())
    MSA = []
    for i in range(n):
        MSA.append(input())
    long_string = input()

    profile = find_profile(MSA)
    most_similar_substring = find_most_similar_substring(long_string, profile, len(MSA[0]))
    print(most_similar_substring)


def find_profile(MSA):
    MSA_count = len(MSA)
    letters_set, position_letters = get_all_letters(MSA)

    PSSM_matrix = {}
    for letter in letters_set:
        PSSM_matrix[letter] = {}

    # converting MSA to a raw frequency table with regards to pseudoCount
    for letter_row in PSSM_matrix.keys():
        for position_column in position_letters.keys():
            PSSM_matrix.get(letter_row)[position_column] = (position_letters.get(position_column)[letter_row] + pseudoCount) / (MSA_count + 21)

    # calculating overall frequency for each letter
    for letter_row in PSSM_matrix.keys():
        overall_freq = 0
        for frequency in PSSM_matrix.get(letter_row).values():
            overall_freq += frequency
        PSSM_matrix.get(letter_row)['overall_freq'] = overall_freq / len(MSA[0])

    # converting values of PSSM matrix into log2 of the values divided by overall_freq for each letter
    for letter_row in PSSM_matrix.keys():
        for position_column in PSSM_matrix.get(letter_row).keys():
            if PSSM_matrix.get(letter_row)[position_column] != 0:
                PSSM_matrix.get(letter_row)[position_column] = math.log2(PSSM_matrix.get(letter_row).get(position_column) / PSSM_matrix.get(letter_row).get('overall_freq'))

    return PSSM_matrix


def get_all_letters(MSA):
    letters_set = set()
    position_letters = {}
    for i in range(len(MSA[0])):
        position_letters[i] = []

    for sequence in MSA:
        for index in range(len(sequence)):
            letters_set.add(sequence[index])
            position_letters[index].append(sequence[index])

    for key in position_letters.keys():
        position_letters[key] = Counter(position_letters[key])

    return letters_set, position_letters


def find_most_similar_substring(long_string, profile, substring_len):
    best_substring = ''
    best_substring_score = -math.inf
    for i in range(len(long_string) - substring_len):
        substring = long_string[i:i+substring_len]
        substring_score = 0
        for index in range(len(substring)):
            if profile.__contains__(substring[index]):
                substring_score += profile.get(substring[index]).get(index)
        if substring_score > best_substring_score:
            best_substring_score = substring_score
            best_substring = substring

    return best_substring


if __name__ == '__main__':
    main()
