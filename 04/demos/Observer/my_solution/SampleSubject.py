from AbsSubject import AbsSubject


class SampleSubject(AbsSubject):
    _open_tickets = -1
    _closed_tickets = -1
    _new_tickets = -1

    def set_kpis(self, opn, closed, new):
        self._open_tickets = opn
        self._closed_tickets = closed
        self._new_tickets = new
        self.notify(self.get_kpi())

    def get_kpi(self):
        return self._open_tickets, self._closed_tickets, self._new_tickets
