high_score_filename = 'my_high_score.csv'

import pandas as pd

df = pd.read_csv(high_score_filename,
                 sep=';',
                 names=['datetime', 'score'],
                 index_col='datetime')

df.plot(ylim=(0, None),
        title='My FlapPyBird scores',
        use_index=False,
        xlabel='Attempt #')