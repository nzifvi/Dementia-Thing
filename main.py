import pandas

def encodeColumn(df, columnName, columnEncodings):
    df[columnName] = df[columnName].map(columnEncodings)

questionEncodings = {
    "Q1" : { # what is your age
        "18-29"             : 0,
        "30-39"             : 1,
        "40-49"             : 2,
        "50-59"             : 3,
        "60-69"             : 4,
        "70 years or over"  : 5,
        "Prefer not to say" : -1
    },
    "Q2" : {
        
    }
}
df   = pandas.read_csv("data/dementiaData.csv")
df   = df.drop(index = [0, 1]).reset_index(drop = True) 
keys = questionEncodings.keys()
for key in keys:
    encodeColumn(df, key, questionEncodings[key])