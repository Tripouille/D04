from FileLoader import FileLoader as fl


def youngestFellah(df, year):
    res = df.query('Year == @year')
    res = res.groupby(['Sex'])['Age'].min()
    return {'f': res['F'], 'm': res['M']}


if __name__ == '__main__':
    df = fl.load("athlete_events.csv")
    print(youngestFellah(df, 2004))
