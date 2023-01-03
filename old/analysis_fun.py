


def clean(df,col):
    df['children']=df['children'].fillna(0)

def fun(df,colname):
        colname1 = colname + '_1'
        colname1=df.reindex(df.index.repeat(df[colname]))
        colname1[colname]=colname1[colname].replace(colname1[colname].unique(),colname)
        colname1.rename(columns={colname: "people"}, inplace=True)
        return colname1
    



