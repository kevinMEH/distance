import matplotlib.pyplot as plot

def scatter_plot(filtered_coords, centroids, score):
    plot.style.use("_mpl-gallery")
    figure, axes = plot.subplots(figsize=(8, 6))

    x, y, colors, sizes = [], [], [], []
    for i, coords in enumerate(filtered_coords):
        centroid = centroids[i]
        color = 20 + i / len(filtered_coords) * 60
        for ex, wy in coords:
            x.append(wy)
            y.append(ex)
            sizes.append(3)
            colors.append(color)
        x.append(centroid[1])
        y.append(centroid[0])
        sizes.append(20)
        colors.append(100)

    axes.text(0.05, 0.03, "Score: " + str(score),
        verticalalignment = "bottom",
        horizontalalignment = "left",
        transform = axes.transAxes,
        fontsize = 14
    )
    
    plot.subplots_adjust(bottom = 0.075, left = 0.075)
    plot.gca().set_aspect("equal")
    axes.scatter(x, y, s=sizes, c=colors, vmin=0, vmax=100)
    plot.show()

def line_plot(x, y):
    plot.plot(x, y)
    plot.xticks(range(0, x[-1] + 1, x[-1] // 10))
    plot.grid(True, axis = "x")
    plot.show()
    # plot.sh
