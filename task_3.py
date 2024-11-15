def read_file(filename: str):
    with open(filename) as f:
        file = f.read().rstrip().split('\n')
        return [filename, str(len(file))] + file


def sorted_files(filenames: list[str]) -> list[list[str]]:
    return sorted(map(read_file, filenames), key=len)


def write_file(filename: str, files: list[list[str]]) -> None:
    with open(filename, 'a') as f:
        for file in files:
            # file.append('\n')
            f.write('\n'.join(file) + '\n')


if __name__ == '__main__':
    files = sorted_files(['1.txt', '2.txt', '3.txt'])
    write_file('result.txt', files)
