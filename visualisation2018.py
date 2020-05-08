import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("./assets/data2018.csv")


def gradesToNumber(string):
    reference = {"A": 20, "B":17.5, "C": 15, "D": 12.5}
    out = 0
    for i in range(4):
        if i !=3:
            out += reference[string[i]]
        else:
            out += reference[string[i]]/2 
    return out + 15


def schoolToColor(school):
    if school == "Nanyang Technological University":
        return "blue"
    elif school == "Singapore Management University":
        return "green"
    else:
        return "red"



df["num_IGP"]= df["IGP"].apply(gradesToNumber)
df["color"] = df["university"].apply(schoolToColor)
# print(df.describe())
# print(df["gross_monthly_median"])
df.plot(kind = "scatter", x = "num_IGP", y = "gross_monthly_median", s= df["Course Places"] /1.5, color = df["color"], alpha = 0.5)
plt.yticks([2000, 3000, 4000, 5000, 6000])
plt.ylabel("Median Monthly Income")
plt.xlabel("IGP Score (10 percentile)")
plt.title("Future Income vs Entry Requirements")
plt.show()