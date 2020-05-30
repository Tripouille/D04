from FileLoader import FileLoader as fl

class SpatioTemporalData:
    def __init__(self, data):
        self.data = data

    def when(self, location):
        return list(self.data.query("City == @location")
                    .drop_duplicates(["Year"])["Year"])

    def where(self, year):
        return list(self.data.query("Year == @year")
            .drop_duplicates(["City"])["City"])


if __name__ == '__main__':
    sp = SpatioTemporalData(fl.load("athlete_events.csv"))
    print(sp.where(1896))
    print(sp.where(2016))
    print(sp.when('Athina'))
    print(sp.when('Paris'))
