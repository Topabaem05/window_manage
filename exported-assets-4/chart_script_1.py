import pandas as pd
import plotly.graph_objects as go

# Create DataFrame from the provided data
data = [
  {"API 유형": "Win32 API", "구현 난이도": 8, "기능성": 7},
  {"API 유형": "COM Interface", "구현 난이도": 9, "기능성": 8},
  {"API 유형": ".NET/WPF", "구현 난이도": 6, "기능성": 7},
  {"API 유형": "자동화 라이브러리", "구현 난이도": 5, "기능성": 9},
  {"API 유형": "DirectComposition", "구현 난이도": 7, "기능성": 8},
  {"API 유형": "서드파티 도구", "구현 난이도": 2, "기능성": 6}
]

df = pd.DataFrame(data)

# Creating the grouped bar chart
fig = go.Figure()

# Add bars for implementation difficulty
fig.add_trace(go.Bar(
    x=df["API 유형"],
    y=df["구현 난이도"],
    name="구현 난이도",
    marker_color="#1FB8CD",
    cliponaxis=False
))

# Add bars for functionality
fig.add_trace(go.Bar(
    x=df["API 유형"],
    y=df["기능성"],
    name="기능성",
    marker_color="#FFC185",
    cliponaxis=False
))

# Update layout
fig.update_layout(
    title="API/라이브러리 난이도-기능성 비교",
    barmode='group',
    legend=dict(orientation='h', yanchor='bottom', y=1.05, xanchor='center', x=0.5)
)

# Update axes
fig.update_xaxes(title="API 유형")
fig.update_yaxes(title="점수 (1-10)", range=[0, 10])

# Save the chart
fig.write_image("api_comparison.png")

fig