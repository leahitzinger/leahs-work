import pandas as pd


def cleans_nans(df,columns,fill):
    for col in columns:
        df[col]=df[col].fillna(fill)

def duplecating_rows(df,colname): 
        df1 = colname + '_df'
        df1=df.reindex(df.index.repeat(df[colname]))
        df1[colname]=df1[colname].replace(df1[colname].unique(),colname)
        df1.rename(columns={colname: "people"}, inplace=True)
        return df1
    
def counts_values(df,col,dropna=False):
    a=df[col].value_counts(dropna,sort=True)
    if a[a.iloc[:,0]].isnull() and a[a.iloc[:,1]]>500:
        df=df.drop[col]
    return df


    
    





