import pandas as pd
import matplotlib.pyplot as plt

# Example data (assuming it's similar to what you're using)
x_labels = ['2023-01', '2023-02', '2023-03', '2023-04']
columns_sequence = ['Category A', 'Category B', 'Category C']
data = {
    'Category A': [3, 5, 2, 4],
    'Category B': [2, 3, 4, 2],
    'Category C': [1, 2, 3, 1]
}
df = pd.DataFrame(data, index=x_labels)
columns_colors = ['lightblue', 'lightgreen', 'lightcoral']

# Plot stacked bar chart
ax = df[columns_sequence].plot(kind="bar", stacked=True, ax=plt.gca(), color=columns_colors)

plt.title(f"Unrelated Categorization - Candidate X")
plt.ylabel("Number of articles")
plt.xlabel("Log files (by date)")

# Add value labels on top of the bars
cumulative_heights = [0] * len(df)  # Initialize cumulative heights for each bar stack

for p in ax.patches:
    height = p.get_height()
    x_center = p.get_x() + p.get_width() / 2
    x_index = int(p.get_x() + p.get_width() / 2)  # Find the corresponding x index
    
    # Add the current height to the cumulative height for this stack
    cumulative_heights[x_index] += height
    
    # Only add annotation if height > 0
    if height > 0:
        ax.annotate(
            str(height),                                   # Value to display
            (x_center, cumulative_heights[x_index] - height / 2),  # X,Y-coordinate (slightly below top of stack)
            ha='center',                                  # Horizontal alignment
            va='center',                                  # Vertical alignment
            fontsize=12,                                  # Font size
            color='red',                                  # Font color
            fontweight='bold'                            # Bold font
           #bbox=dict(boxstyle="round,pad=0.3", 
           #           edgecolor="none", facecolor="white")  # Add background box to make text clearer
        )

# Adjust x-axis limits and labels
plt.xticks(ticks=list(range(len(x_labels))), labels=x_labels, rotation=0)

# Show the plot
plt.show()