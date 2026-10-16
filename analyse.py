import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
data=pd.read_csv("data.txt")
data=data[["post_number","likes","comments"]]
data["likes_comments_ratio"]=np.where(data["comments"]>0, data["likes"]/data["comments"],np.nan)
data["zero_comments"]=data["comments"]==0
print(data)
valid = data["likes_comments_ratio"].dropna()
median = valid.median()
mad = (valid-median).abs().median()
if mad > 0:
    data["anomaly"] = ((data["likes_comments_ratio"]-median).abs()> 3 * mad)
else:
    data["anomaly"] = data["likes_comments_ratio"]!=median
print(data[["post_number", "likes_comments_ratio", "anomaly"]])

sns.lineplot(data=data, x="post_number", y="likes_comments_ratio")
zero_data=data[data["zero_comments"]]
if not zero_data.empty:
    plt.scatter(zero_data["post_number"],[0] * len(zero_data),color="red",label="Zero comments",)
    plt.legend()
anomaly_data = data[data["anomaly"] == True]
plt.scatter(anomaly_data["post_number"],anomaly_data["likes_comments_ratio"],color="red",label="Anomaly",)
plt.legend()   
plt.title("ENGAGEMENT ANOMELY GRAPH")
plt.xlabel("post number")
plt.ylabel("likes/comments")
plt.show()
print(data)

