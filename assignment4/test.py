import pandas as pd
import numpy as np

import pandas as pd
data = {'City': ['New York', 'Chicago', 'Austin'], 'Population': [8.3, 2.7, 0.9]}
df = pd.DataFrame(data, index=['a', 'b', 'a'])
print(df.loc['a'])