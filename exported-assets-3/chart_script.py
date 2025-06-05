import plotly.graph_objects as go

# Define phases with correct colors based on activity type
phases_data = [
    {"name": "Project Setup", "color": "#1FB8CD", "type": "setup"},  # Blue for setup
    {"name": "Core Arch", "color": "#ECEBD5", "type": "development"},  # Green for development
    {"name": "UI/Visual", "color": "#ECEBD5", "type": "development"},  # Green for development
    {"name": "Stage Features", "color": "#ECEBD5", "type": "development"},  # Green for development
    {"name": "Integration", "color": "#FFC185", "type": "integration"},  # Orange for integration
    {"name": "Testing", "color": "#B4413C", "type": "testing"}  # Red for testing
]

# Sub-steps for each phase (shortened to fit character limits)
substeps = [
    ["C++/Win32", "VS Setup", "Config"],
    ["Win Mgr", "Events", "Tracking"],
    ["Thumbnails", "Sidebar", "Animation"],
    ["Grouping", "Position", "Focus"],
    ["Hooks", "Desktop", "Optimize"],
    ["Unit Tests", "Integration", "Performance"]
]

# Create figure
fig = go.Figure()

# Box dimensions and positions
box_width = 2.0
box_height = 0.8
x_center = 0
y_positions = [5, 4, 3, 2, 1, 0]  # Top to bottom

# Add boxes for each phase
for i, (phase, y_pos) in enumerate(zip(phases_data, y_positions)):
    # Main phase box
    fig.add_shape(
        type="rect",
        x0=x_center - box_width/2,
        y0=y_pos - box_height/2,
        x1=x_center + box_width/2,
        y1=y_pos + box_height/2,
        fillcolor=phase["color"],
        line=dict(color="black", width=1),
        opacity=0.9
    )
    
    # Phase title
    fig.add_annotation(
        x=x_center,
        y=y_pos + 0.15,
        text=f"<b>{phase['name']}</b>",
        showarrow=False,
        font=dict(size=11, color="black")
    )
    
    # Sub-steps (shortened)
    substep_text = " • ".join(substeps[i])
    fig.add_annotation(
        x=x_center,
        y=y_pos - 0.15,
        text=substep_text,
        showarrow=False,
        font=dict(size=9, color="black")
    )

# Add connecting arrows between phases
for i in range(len(y_positions) - 1):
    # Add arrow line
    fig.add_shape(
        type="line",
        x0=x_center,
        y0=y_positions[i] - box_height/2,
        x1=x_center,
        y1=y_positions[i+1] + box_height/2,
        line=dict(color="black", width=3)
    )
    
    # Add arrowhead
    fig.add_annotation(
        x=x_center,
        y=y_positions[i+1] + box_height/2,
        ax=x_center,
        ay=y_positions[i+1] + box_height/2 + 0.15,
        arrowhead=2,
        arrowsize=1.5,
        arrowwidth=3,
        arrowcolor="black",
        showarrow=True
    )

# Update layout
fig.update_layout(
    title="Win Stage Mgr Dev Process",
    xaxis=dict(range=[-2.5, 2.5], showgrid=False, showticklabels=False, zeroline=False),
    yaxis=dict(range=[-0.8, 5.8], showgrid=False, showticklabels=False, zeroline=False),
    plot_bgcolor="white",
    showlegend=False
)

# Save the chart
fig.write_image("windows_stage_manager_dev_flowchart.png")