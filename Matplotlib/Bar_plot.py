import matplotlib.pyplot as plt
language = ["python","C", "C++","Java"]
popular = [85,70,65,82]
z = [20,30,40,50]

c = ["gold","royalblue","navy","teal"]

plt.xlabel("Languages",fontsize=15)
plt.ylabel("Popular Score",fontsize=10)
plt.title("Matplotlib bar",fontsize=15)

# plt.bar(language,popular, color=c,width=0.4,align="edge",edgecolor="aqua",linewidth=4,linestyle=":",alpha=0.6)

plt.bar(language,popular, color="r",width=0.4,label="popularity")
plt.bar(language,z, color="gold",width=0.4,label="popularity1")

plt.legend()
plt.show()
