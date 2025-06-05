import pandas as pd
import plotly.express as px

# Load data
data = [
  {"API 유형": "Win32 API", "개수": 5},
  {"API 유형": "COM Interface", "개수": 4},
  {"API 유형": ".NET/WPF", "개수": 3},
  {"API 유형": "자동화 라이브러리", "개수": 3},
  {"API 유형": "DirectComposition", "개수": 3},
  {"API 유형": "서드파티 도구", "개수": 3}
]

df = pd.DataFrame(data)

# Create the bar chart with a single color
fig = px.bar(
    df, 
    x='API 유형', 
    y='개수',
    color_discrete_sequence=['#1FB8CD']  # Using a single color for all bars
)

# Update layout
fig.update_layout(
    title='API 유형별 창 관리 도구 개수',
    showlegend=False
)

# Update x-axis - rotate labels for better readability
fig.update_xaxes(
    title='API 유형',
    tickangle=15  # Slight rotation for better readability
)

# Update y-axis - start at 0 and make grid more visible
fig.update_yaxes(
    title='개수',
    range=[0, 6],  # Explicit range from 0
    gridwidth=1.5  # Increase grid width for better visibility
)

# Save the figure as PNG
fig.write_image("api_tools_count.png")

# Display the figure
fig.show()