import pandas as pd

# adding M/F
block1_mf = ['M', 'F', 'M', 'M', 'M', 'F', 'M', 'F', 'F', 'F', 'F', 'F', 'F', 'M', 'F', 'F', 'F', 'F', 'F', 'M', 'F',
             'F', 'M', 'F', 'F', 'F', 'F', 'F', 'M', 'M', 'F', 'F', 'M', 'M', 'F', 'F', 'F', 'F', 'F', 'M', 'M']
block1_io = ['I', 'O', 'I', 'I', 'I', 'O', 'I', 'I', 'I', 'O', 'O', 'O', 'O', 'O', 'O', 'I', 'I', 'O', 'I', 'O', 'O',
             'O', 'O', 'I', 'O', 'I', 'O', 'O', 'O', 'I', 'I', 'I', 'I', 'I', 'I', 'O', 'I', 'O', 'I', 'O', 'I']
block2_mf = ['M', 'F', 'F', 'M', 'M', 'F', 'F', 'F', 'F', 'F', 'M', 'F', 'F', 'M', 'F', 'M', 'M', 'F', 'F', 'F', 'F',
             'M', 'M', 'F', 'F', 'M', 'F', 'F', 'F', 'M', 'F', 'F', 'M', 'M', 'M', 'F', 'F', 'M', 'M', 'F', 'F']
block2_io = ['O', 'O', 'I', 'O', 'I', 'I', 'O', 'O', 'O', 'I', 'I', 'O', 'I', 'I', 'O', 'I', 'O', 'O', 'I', 'I', 'I',
             'I', 'O', 'I', 'I', 'O', 'I', 'O', 'O', 'O', 'O', 'I', 'O', 'I', 'I', 'O', 'I', 'I', 'O', 'I', 'O']
block3 = []
block4 = []
block5 = []
block6 = []
block7 = []
block8 = []

df1 = pd.DataFrame(columns=['ID', 'M/F', 'I/O', 'Trigger Response'])
df1.index.name = 'Index'
print(df1)

df1['M/F'] = block1_mf
df1['I/O'] = block1_io
print(df1)

df2 = pd.DataFrame(columns=['ID', 'M/F', 'I/O', 'Trigger Response'])
df2.index.name = 'Index'
df2['M/F'] = block2_mf
df2['I/O'] = block2_io
print(df2)

df2 = df2.to_csv('test.csv')