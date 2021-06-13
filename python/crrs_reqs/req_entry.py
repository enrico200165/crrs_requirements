

class ReqEntry:
    """
    a crrs requirement entry
    only the main fields likely to be necessary (4-5 omitted)
    """
    def __init__(self, rp_spec_id, req_id, name, description, status, source, rationale, target_subtarget):
        self._rp_spec_ID = rp_spec_id
        self._req_ID = req_id
        self._name = name
        self._description = description
        self._status = status
        self._source = source
        self._rationale = rationale
        self._target_subtarget = target_subtarget

    def values_list(self):
        return [self._rp_spec_ID, self._req_ID, self._name, self._description, self._status,
                self._source, self._rationale, self._target_subtarget]

    @property
    def rp_spec_id(self): return self._rp_spec_ID

    @property
    def req_id(self): return self._req_ID

    @property
    def name(self): return self._name

    @property
    def description(self): return self._description

    @property
    def status(self): return self._status

    @property
    def source(self): return self._source

    @property
    def rationale(self): return self._rationale

    @property
    def target_subtarget(self): return self._target_subtarget
