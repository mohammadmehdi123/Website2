from flask import Flask, render_template, request
from transformers import pipeline

app = Flask(__name__)

# ایجاد یک پردازشگر برای تولید متن با مدل فارسی
generator = pipeline('text-generation', model='HooshvareLab/gpt2-fa')  # استفاده از مدل GPT-2 فارسی

def get_answer_from_gpt(question):
    # تولید پاسخ از مدل
    response = generator(question, max_length=100, num_return_sequences=1)
    return response[0]['generated_text'].strip()

@app.route('/', methods=['GET', 'POST'])
def home():
    answer = None
    if request.method == 'POST':
        question = request.form['question']
        if question.strip():  # بررسی می‌کنیم که سوال خالی نباشد
            answer = get_answer_from_gpt(question)  # گرفتن پاسخ از GPT
        else:
            answer = "لطفاً سوال خود را وارد کنید."  # اگر سوال خالی بود
    return render_template('index.html', answer=answer)

if __name__ == '__main__':
    app.run(debug=True)
