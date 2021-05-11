pseudoCount = 1


def main():
    n = int(input())
    MSA = []
    for i in range(n):
        MSA.append(input())
    long_string = input()

    profile = find_profile(MSA)
    most_similar_substring = find_most_similar_substring(long_string, profile)
    print(most_similar_substring)


def find_profile(MSA):
    return ''


def find_most_similar_substring(long_string, profile):
    return ''


if __name__ == '__main__':
    main()
