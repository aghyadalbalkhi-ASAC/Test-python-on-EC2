import matplotlib.pyplot as plt
url = r"./onion.png"
pic = plt.imread(url)
print(pic)

print(pic.shape)


fig = plt.figure()
ax = fig.subplots()


ax.imshow(pic)
plt.show()

f = ax.imshow(pic[:, :, 1], alpha=0.5, cmap='gray',  vmin=0, vmax=500, aspect='auto')

f = ax.imshow(pic[:, :, 1], alpha=0.5, cmap='gray',  vmin=0, vmax=500, aspect='auto')


ax.set_xlim(0, 2500)
ax.set_ylim(2500, 0)
ax.axis('off')

plt.savefig(r"sds.jpg", bbox_inches='tight', pad_inches=0)