
import docx

from ms_word_table_class import MSWordTable

import crrs_reqs_global_defs as g


class ReqEntryWordTable(MSWordTable):

    def __init__(self, table):
        if not isinstance(table, docx.table.Table):
            exit(2)
        super().__init__(table)
        self._target_subtarget = g.not_set

    def get_name_value(self, name):
        ret_text = self.get_tex_cell_row_id(name, 1, 0)
        return name, ret_text

    @property
    def rp_spec_id2(self):
        return self.get_name_value(g.rp_spec_id_val)

    @property
    def rp_spec_id(self):
        return self.rp_spec_id2[1]

    @property
    def req_id2(self):
        return self.get_name_value(g.req_id_val)

    @property
    def req_id(self):
        return self.req_id2[1]

    @property
    def name2(self):
        return self.get_name_value(g.name_val)

    @property
    def name(self):
        return self.name2[1]

    @property
    def description2(self):
        return self.get_name_value(g.description_val)

    @property
    def description(self):
        return self.description2[1]

    @property
    def status2(self):
        return self.get_name_value(g.status_val)

    @property
    def status(self):
        return self.status2[1]

    @property
    def source2(self):
        return self.get_name_value(g.source_val)

    @property
    def source(self):
        return self.source2[1]

    @property
    def rationale2(self):
        return self.get_name_value(g.rationale_val)

    @property
    def rationale(self):
        return self.rationale2[1]

    @property
    def target_subtarget2(self):
        ret = self.get_name_value(g.target_subtarget_val)
        return ret

    @property
    def target_subtarget(self):
        return self.target_subtarget2[1]
