from FileLoader import FileLoader as fl


def howManyMedals(df, name):
    data = df.query('Name == @name')
    data = data.groupby(['Year'])['Medal']
    res = {}
    for yearData in data:
        res[yearData[0]] = {}
        res[yearData[0]]['G'] = sum(yearData[1] == 'Gold')
        res[yearData[0]]['S'] = sum(yearData[1] == 'Silver')
        res[yearData[0]]['B'] = sum(yearData[1] == 'Bronze')
    return res


if __name__ == '__main__':
    df = fl.load("athlete_events.csv")
    print(howManyMedals(df, 'Kjetil Andr Aamodt'))
