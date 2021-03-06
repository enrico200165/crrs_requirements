import os.path

import crrs_reqs_global_defs as g
import build_req_df_bare as bld


"""
    code for readability, keep for when implementing
    # readability
    results = readability.getmeasures(re.description, lang='en')
    readability_fleisch = results['readability grades']['FleschReadingEase']
    textstat_fleisch = textstat.flesch_reading_ease(re.description)
    if textstat_fleisch - readability_fleisch > 20:
        print(
            "[{}]\n{}\n{}\n{}\n\n".format(re.rp_spec_id, textstat_fleisch, readability_fleisch, re.description))
        pass
"""


filepath = os.path.join(g.path, g.filename_a6)
df = bld.reqs_from_word_file(filepath)
print(df.columns)
#print(df[g.status_key][0:5])
#print(df[g.status_key].value_counts())
print("\n", df[g.target_subtarget_key].value_counts())
