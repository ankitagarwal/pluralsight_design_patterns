from AbsObserver import AbsObserver


class SampleObserver1(AbsObserver):

    def update(self, values):
        print("Printing in SampleObserver1 -------------------")
        print(values)

