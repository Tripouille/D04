import pandas as pd


class FileLoader:
    @staticmethod
    def load(path):
        file = pd.read_csv(path)
        print("Loading dataset of dimensions {} x {}"
              .format(file.shape[0], file.shape[1]))
        return file

    @staticmethod
    def display(df, n):
        print(df.head(n)) if n > 0 else print(df.tail(-n))

if __name__ == '__main__':
    df = FileLoader.load("athlete_events.csv")
    print("n > 0")
    FileLoader.display(df, 1)
    print("n < 0")
    FileLoader.display(df, -1)
    print("n == 0")
    FileLoader.display(df, 0)
