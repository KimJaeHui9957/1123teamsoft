from flask import Flask, render_template, request
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
import base64

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            # 업로드한 파일을 데이터프레임으로 읽기
            df = pd.read_csv(file)
            
            # 예시 시각화 - 나이 분포
            plt.figure()
            df['age'].value_counts().plot(kind='bar', color='skyblue')
            plt.title('Age Distribution')
            plt.xlabel('Age')
            plt.ylabel('Count')

            # 그래프 이미지를 base64로 변환하여 HTML에 삽입
            img = BytesIO()
            plt.savefig(img, format='png')
            img.seek(0)
            graph_url = base64.b64encode(img.getvalue()).decode()
            graph = f'data:image/png;base64,{graph_url}'

            return render_template('result.html', graph=graph)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=1234)
