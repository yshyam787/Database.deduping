
# Deduping the database using the dededupe library
import pandas as pd
import pandas_dedupe

data = pd.read_excel('Book1.ods')  # reading the excel file
df = pd.DataFrame(data)  # importing the dataframecolumns = [{e: e.strip()} for e in df.columns]
columns = {}
for i in df.columns:
    columns = columns | {i: i.strip()}
df.rename(columns=columns, inplace=True) #renaming the columns and removing the spaces.

df2 = pandas_dedupe.dedupe_dataframe(df, ["Shipper", "Shipper Address"]) #Deduping the databas

df2_groupby = df2.copy()

for index, row in df2.iterrows(): #for interating over the rows of Shipper and Shipper Address.
    print(row["Shipper"], ["Shipper Address"]) #print out the unique databse

with pd.ExcelWriter('DedupedDatabase.ods') as writer:
    df.to_excel(writer, sheet_name='Original')
    df2.to_excel(writer, sheet_name='Deduped')

    


