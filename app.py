from flask import Flask, render_template, request

app = Flask(__name__)

# ================= HOME =================
@app.route('/')
def home():
    return render_template('index.html')


# ================= HEALTH =================
@app.route('/health', methods=['GET', 'POST'])
def health():

    if request.method == 'POST':

        age = request.form.get('age')
        duration = request.form.get('duration')
        selected = request.form.getlist('symptoms')

        results = []
        suggestions = []
        risk = "Low 🟢"

        # ================= CONDITIONS ================= #

        if "fever" in selected:
            results.append("🤒 You may be experiencing an infection as fever is the body’s natural response to fight bacteria or viruses.")
            suggestions.append("💧 Stay hydrated and take proper rest.")

        if "cough" in selected:
            results.append("😷 Cough may indicate irritation or infection in your respiratory system.")
            suggestions.append("☕ Avoid cold drinks and take warm fluids.")

        if "headache" in selected:
            results.append("😖 Headache can be caused by stress, dehydration, or lack of sleep.")
            suggestions.append("🛌 Take proper rest and reduce screen time.")

        if "fatigue" in selected or "weakness" in selected:
            results.append("⚡ Persistent fatigue or weakness may indicate low energy levels or nutritional deficiency.")
            suggestions.append("🍗 Eat protein-rich and nutritious food.")

        if "vomiting" in selected or "nausea" in selected:
            results.append("🤢 These symptoms may be related to digestive issues or possible food poisoning.")
            suggestions.append("🚫 Avoid outside food and drink plenty of fluids.")

        if "chest pain" in selected:
            results.append("❤️ Chest pain could indicate a serious heart or lung condition and should not be ignored.")
            suggestions.append("🚨 Consult a doctor immediately.")
            risk = "High 🔴"

        if "anxiety" in selected:
            results.append("🧠 Anxiety may be linked to mental stress, overthinking, or emotional imbalance.")
            suggestions.append("🧘 Practice meditation and relaxation techniques.")

        if "sleep problems" in selected:
            results.append("😴 Sleep problems may indicate poor sleep habits or stress.")
            suggestions.append("🌙 Maintain a proper sleep schedule.")

        if "acidity" in selected:
            results.append("🔥 Acidity is often caused by unhealthy eating habits or spicy food.")
            suggestions.append("🥗 Avoid oily and spicy food.")

        if "hair fall" in selected:
            results.append("💇 Hair fall can be due to nutritional deficiency or stress.")
            suggestions.append("💊 Take vitamins and maintain a balanced diet.")

        if "frequent urination" in selected:
            results.append("🩸 Frequent urination may be a sign of high blood sugar or diabetes risk.")
            suggestions.append("🧪 Check your blood sugar levels.")

        if "body pain" in selected:
            results.append("💪 Body pain may be due to fatigue, infection, or lack of proper rest.")
            suggestions.append("🛌 Take rest and stay hydrated.")

        if "stomach pain" in selected:
            results.append("🍽️ Stomach pain may be related to digestive issues or unhealthy food intake.")
            suggestions.append("🥣 Eat light food and avoid junk food.")

        if "sore throat" in selected:
            results.append("🗣️ Sore throat may indicate throat infection or cold.")
            suggestions.append("🍵 Drink warm water and avoid cold items.")

        # ================= COMBINATION LOGIC ================= #

        if "fever" in selected and "cough" in selected:
            results.append("🔥 Combination of fever and cough strongly indicates a viral or respiratory infection.")
            suggestions.append("🛌 Take proper rest and consult a doctor if symptoms persist.")

        if "fatigue" in selected and "hair fall" in selected:
            results.append("⚠️ Fatigue along with hair fall may indicate nutritional deficiency.")
            suggestions.append("🥦 Improve diet with vitamins and minerals.")
            # ================= RISK LEVEL ================= #

        if len(selected) >= 4:
            risk = "Moderate 🟠"

        if len(selected) >= 8:
            risk = "High 🔴"

        # ================= DEFAULT ================= #

        if not results:
            results.append("🙂 No major symptoms detected, but maintain a healthy lifestyle.")
            suggestions.append("🥗 Eat healthy, exercise regularly, and stay hydrated.")

        return render_template(
            'result.html',
            results=results,
            suggestions=suggestions,
            risk=risk
        )

    return render_template('health.html')

# ================= DIET ================#
@app.route('/diet', methods=['GET', 'POST'])
def diet():
    if request.method == 'POST':
        file = request.files['food_image']
        food = request.form['food_type']   # 👈 IMPORTANT LINE

        # 🍎 FRUIT
        if food == "apple":
            result = {
                "food": "Healthy Food 🥗",
                "protein": "2g",
                "carbs": "20g",
                "fiber": "5g",
                "calories": "90 kcal",
                "suggestion": "Great choice! Keep eating clean 💚"
            }

        # 🍚 RICE
        elif food == "rice":
            result = {
                "food": "Rice 🍚",
                "protein": "4g",
                "carbs": "45g",
                "fiber": "1g",
                "calories": "200 kcal",
                "suggestion": "Eat with dal or veggies 👍"
            }

        # 🥛 MILK
        elif food == "milk":
            result = {
                "food": "Milk 🥛",
                "protein": "8g",
                "carbs": "12g",
                "fiber": "0g",
                "calories": "150 kcal",
                "suggestion": "Good for bones 💪"
            }

        # 🍔 JUNK
        elif food == "burger":
            result = {
                "food": "Junk Food 🍔",
                "protein": "10g",
                "carbs": "50g",
                "fiber": "2g",
                "calories": "400 kcal",
                "suggestion": "Avoid junk frequently ❌"
            }

        # 🍗 PROTEIN
        elif food == "chicken":
            result = {
                "food": "Protein Rich Food 🍗",
                "protein": "25g",
                "carbs": "5g",
                "fiber": "0g",
                "calories": "250 kcal",
                "suggestion": "Great for muscle growth 💪"
            }

        else:
            result = {
                "food": "Mixed Food 🍽",
                "protein": "6g",
                "carbs": "25g",
                "fiber": "3g",
                "calories": "180 kcal",
                "suggestion": "Maintain balance ⚖️"
            }

        return render_template('diet_result.html', data=result)

    return render_template('diet.html')

# ================= BMI =================
@app.route('/bmi', methods=['GET', 'POST'])
def bmi():
    if request.method == 'POST':
        height = float(request.form['height'])
        weight = float(request.form['weight'])

        bmi_value = weight / ((height / 100) ** 2)

        if bmi_value < 18.5:
            result = "Underweight 😟"
            color = "#00bcd4"
            suggestion = "Eat more nutritious food 🍎"
        elif bmi_value < 25:
            result = "Normal Weight ✅"
            color = "#00e676"
            suggestion = "Maintain your lifestyle 💪"
        elif bmi_value < 30:
            result = "Overweight ⚠️"
            color = "#ff9800"
            suggestion = "Exercise more 🏃‍♀️"
        else:
            result = "Obese ❌"
            color = "#ff5252"
            suggestion = "Consult doctor + strict diet 🥗"

        return render_template(
            'bmi.html',
            result=result,
            bmi_value=round(bmi_value, 2),
            suggestion=suggestion,
            color=color
        )

    return render_template('bmi.html')

# ================= ABOUT =================
@app.route('/about')
def about():
    return render_template('about.html')


# ================= GUIDE =================
@app.route('/guide')
def guide():
    return render_template('guide.html')


#================== STORE =================
@app.route('/store')
def store():
    return render_template('store.html')

# ================= RUN =================

    import os

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
