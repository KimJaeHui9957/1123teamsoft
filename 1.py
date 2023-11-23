import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# 엑셀 파일에서 데이터 읽기
csv_file = 'C:/Users/218/Downloads/cox-violent-parsed_filt_usable.csv'  # 파일경로를 실제 엑셀 파일의 경로로 변경해주세요
data = pd.read_csv(csv_file)

# 데이터 확인 (옵션)
print(data.head())

# 데이터 시각화 (Matplotlib 사용)
plt.figure(figsize=(10, 6))
plt.bar(data['sex'], data['age'], color='skyblue')  # 실제 열의 이름으로 수정해주세요
plt.xlabel('sex')
plt.ylabel('age')
plt.title('CSV Data Visualization')
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()

# 그래프를 HTML 파일로 저장
output_html = 'output_graph.html'
plt.savefig('output_graph.png')  # 그래프를 이미지로 저장 (선택사항)
plt.savefig('output_graph.svg')  # 그래프를 SVG로 저장 (선택사항)
plt.savefig('output_graph.pdf')  # 그래프를 PDF로 저장 (선택사항)
plt.savefig(output_html)  # 그래프를 HTML 파일로 저장

# HTML 파일로 출력
html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <title>Excel Data Visualization</title>
</head>
<body>
    <h1>Excel Data Visualization</h1>
    <img src="output_graph.png" alt="Graph">
</body>
</html>
"""

with open(output_html, 'w') as file:
    file.write(html_content)

print(f"그래프를 {output_html} 파일로 저장하였습니다.")
