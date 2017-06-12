

def _get_subjects(df):
    df_gr = df.groupby('Subject')
    subjects = []
    for subject in df_gr.groups:
        subjects.append(Subject(df_gr.get_group(subject)))
    return subjects


class Subject(object):

    def __init__(self, df):
        self.df = df

    def get_labels(self):
        return None

    def get_data(self):
        return None

    def plot(self):
        return None


class SubjectCollection(object):

    def __init__(self, df):
        self.df = df
        self.subjects = _get_subjects(df)





