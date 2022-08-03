import pandas as pd
df = pd.read_csv('finalData.csv')
print(df.head())
print(df.columns)
df.drop(['Unnamed: 0'], axis = 1, inplace = True)
print(df.head())
print(df.dtypes)
df['Radius'] = df['Radius'].apply(lambda x: x.replace('$', '').replace(',', '')).astype('float')
radius = df['Radius'].to_list()
mass = df['Mass'].to_list()
gravity = []
def convertToSi(radius, mass):
    for i in range(0, len(radius) - 1):
        radius[i] = radius[i] * 6.957e+8
        mass[i] = mass[i] * 1.989e+30
convertToSi(radius, mass)
def gravityCalculation(radius, mass):
    G = 6.674e-11
    for index in range(0, len(mass)):
        g = (mass[index] * G) / ((radius[index]) ** 2)
        gravity.append(g)
gravityCalculation(radius, mass)
df['Gravity'] = gravity
print(df)
df.to_csv('starWithGravity.csv')
print(df.dtypes)