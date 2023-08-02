import numpy as np
import pandas as pd
import numpy as np
import pandas as pd
def data_parser():
  df = pd.read_csv("pbp-2021.csv")
  #Remove irrelevant columns
  df1 = df.drop(["GameId","Quarter","Minute","Second","Down","ToGo", "YardLine","SeriesFirstDown","NextScore","TeamWin","Yards","SeasonYear","IsIncomplete","IsTouchdown","IsSack"] , axis = 1)
  df1 = df1.drop(["IsChallenge","IsMeasurement","IsInterception","IsFumble","IsPenalty","IsTwoPointConversion","YardLineFixed","YardLineDirection","IsPenaltyAccepted","IsChallengeReversed","IsNoPlay","PenaltyYards","IsTwoPointConversionSuccessful"], axis = 1)
  df1 = df1.drop(["Unnamed: 10", "Unnamed: 12","Unnamed: 16","Unnamed: 17", "Description","Formation","IsRush","IsPass","PassType","Challenger","RushDirection","PenaltyTeam","PenaltyType"] , axis = 1)
  #Remove rows with indoor teams
  df2 = df1[(df1['OffenseTeam'] != "MIN") & (df1['OffenseTeam'] != "LAC") & (df1['OffenseTeam'] != "ARI") & (df1['OffenseTeam'] != "ATL") & (df1['OffenseTeam'] != "DAL") & (df1['OffenseTeam'] != "DET") & (df1['OffenseTeam'] != "HOU") & (df1['OffenseTeam'] != "IND") & (df1['OffenseTeam'] != "NO") & (df1['OffenseTeam'] != "LV") & (df1['OffenseTeam'] != "LAR") & (df1['OffenseTeam'] != "LA")]
  df2 = df2[(df2['DefenseTeam'] != "MIN") & (df2['DefenseTeam'] != "LAC") & (df2['DefenseTeam'] != "ARI") & (df2['DefenseTeam'] != "ATL") & (df2['DefenseTeam'] != "DAL") & (df2['DefenseTeam'] != "DET") & (df2['DefenseTeam'] != "HOU") & (df2['DefenseTeam'] != "IND") & (df2['DefenseTeam'] != "NO") & (df2['DefenseTeam'] != "LV") & (df2['DefenseTeam'] != "LAR") & (df2['DefenseTeam'] != "LA") ]
  #Remove rows with inaccurate play type
  df3 = df2.dropna(inplace = False, axis = 0) 
  df3 = df3[(df3['PlayType'] == "PASS") | (df3['PlayType'] == "RUSH") | (df3['PlayType'] == "FIELD GOAL")]
  #Name Change
  #df["relative_price"] = np.where(df["relative_price"] == 0, "Not Interested", (df.loc[:,"price"] - avg_price).astype(int))
  #df3['OffenseTeam'] = np.where(df3['OffenseTeam'] == "BUF" , "Buffalo Bills", 0)
  #Adding column to track play type
  #print(df3)
  pd.set_option('display.max_columns', None)  # or 1000
  pd.set_option('display.max_rows', None)  # or 1000
  pd.set_option('display.max_colwidth', -1)  # or 199
  return df3.groupby(["GameDate","OffenseTeam","DefenseTeam", "PlayType"]).aggregate({"PlayType" : "count"})
  
############ Function Call ############
data_parser()