from SampleSubject import SampleSubject
from SampleObserver1 import SampleObserver1
from SampleObserver2 import SampleObserver2

with SampleSubject() as sub:
    with SampleObserver1(sub) as ob1:
        sub.set_kpis(1, 2, 3)
        sub.set_kpis(4, 2, 3)
        with SampleObserver2(sub) as ob2:
            sub.set_kpis(10, 20, 30)
            sub.set_kpis(40, 20, 30)
        sub.set_kpis(4, 2, 3)
print("All context should be clear...")
sub.set_kpis(4, 2, 20)
