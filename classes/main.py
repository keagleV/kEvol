import matplotlib.pyplot as plt

import matplotlib
import matplotlib.pyplot as plt


a=str(2.4)

fig = plt.figure()
ax = fig.add_subplot()
fig.subplots_adjust(top=0.85)

# Set titles for the figure and the subplot respectively
fig.suptitle('bold figure suptitle', fontsize=14, fontweight='bold')


ax.set_title('trap')
ax.set_xlabel('xlabel')
ax.set_ylabel('ylabel')



# ax.text(3, 8, 'boxed italics text in data coords', style='italic',
#         bbox={'facecolor': 'red', 'alpha': 0.5, 'pad': 10})

ax.plot([2,1,1], [1,5,4])

plt.show()

# ax.annotate('annotate', xy=(2, 1), xytext=(3, 4))

# plt.xlabel("s")
# plt.ylabel("rr")
# # print textstr
# plt.text(1000,2000, "textstr", fontsize=14)
# plt.grid(True)
# plt.subplots_adjust(left=0.25)
# plt.title("ffName")

# plt.plot([1,2],[4,2])

# plt.show()