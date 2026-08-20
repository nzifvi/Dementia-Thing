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
        "Prefer not to say" : 6
    },
    "Q2" : { # what is your gender
        "Male"                    : 0,
        "Female"                  : 1,
        "Non-binary/third gender" : 2,
        "Prefer not to say"       : 3
    },
    "Q3" : {
        "Brighton and Hove" : 0,
        "East Sussex"       : 1,
        "West Sussex"       : 2,
        "Other"             : 3
    },
    "Q4" : { # what is relationship to person you care for
        "Spouse"              : 0,
        "Parent"              : 1,
        "Other family member" : 2,
        "Friend"              : 3,
        "Other"               : 4
    },
    "Q5" : { # are you currently providing unpaid care for person living w/ dementia
        "Yes" : 1,
        "No"  : 0
    },
    "Q6" : { # if Q5 = "No" then when did your caring role end
        "Less than 3 months ago" : 0,
        "3-6 months"             : 1,
        "6-12 months"            : 2,
        "12-24 months"           : 3
    }
}
df   = pandas.read_csv("data/dementiaData.csv")
df   = df.drop(index = [0, 1]).reset_index(drop = True) 
keys = questionEncodings.keys()
for key in keys:
    encodeColumn(df, key, questionEncodings[key])