from AbsObserver import AbsObserver


class SampleObserver2(AbsObserver):

    def update(self, values):
        print("Printing in SampleObserver2 -------------------")
        print(values)

