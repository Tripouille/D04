from FileLoader import FileLoader as fl


def proportionBySport(df, year, sport, gender):
    data = df.query('Year == @year & Sex == @gender').drop_duplicates(['Name'])
    totalSize = data.shape[0]
    size = data.query('Sport == @sport').shape[0]
    return size / totalSize


if __name__ == '__main__':
    df = fl.load("athlete_events.csv")
    print(proportionBySport(df, 2004, "Tennis", 'F'))
