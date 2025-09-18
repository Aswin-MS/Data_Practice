import numpy as np
import pandas as pd
lst=([[101,'aswin','ms',22,'python',20000,'kochi'],
      [102,'rajeev','k',21,'bigdata',21000,'calicut'],
      [103,'madhav','s',25,'testing',19000,'kochi'],
      [103, 'madhav', 's', 25, 'testing', 19000, 'kochi'],
      [104,'akshay','kk',22,'testing',19500,'tvm'],
      [105,'rahul','m',30,'webdev',30000,'thrissur'],
      [106,'amal','m',22,'bigdata',22000,'kannur'],
      [107,'alan','g',24,'python',26000,'calicut'],
      [107,'alan','pp',24,'python',26000,'calicut']])
df=pd.DataFrame(lst)
df.columns=['id','fname','lname','age','prof','salary','loc']
df1=df.drop_duplicates()
print(df1)