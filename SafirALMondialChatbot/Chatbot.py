import os
import pandas as pd
from flask import Flask, render_template, request, jsonify
import google.generativeai as genai

# ========== إعداد Gemini ==========
API_KEY = 'AIzaSyAXoaBbM2MA-2do0GoR1xZ75wgqgqlNweI'
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-1.5-pro-002')
chat = model.start_chat(history=[])

# ========== تحميل البيانات ==========
data_path = r'C:\Users\norah\PycharmProjects\SafirALMondialChatbot'

csv_files = {
    'fan_preferences': 'fan_preferences.csv',
    'museums_data': 'museums.csv',
    'matches': 'matches.csv',
    'restaurant_data': 'Sample_Restaurant_Dataset.csv',
    'market_data': 'saudi_markets.csv',
    'stadiums': 'Stadiums.csv'
}

dataframes = {}
for key, filename in csv_files.items():
    file_path = os.path.join(data_path, filename)
    try:
        dataframes[key] = pd.read_csv(file_path, encoding='ISO-8859-1')
    except Exception as e:
        print(f"Error loading {filename}: {e}")

# ========== دوال المساعدة ==========
def get_fan_events(city, style):
    # Load fan events data from CSV
    df = pd.read_csv('fan_preferences.csv', sep=',')


    # Normalize the input (city and style) to lowercase for case-insensitive comparison
    city = city.lower()
    style = style.lower()

    # Filter the dataframe based on city and style (case-insensitive matching)
    filtered_df = df[
        (df['City'].str.lower() == city) &
        (df['Style'].str.lower().str.contains(style))  # Check if style is part of the 'Style' column
        ]

    return filtered_df

def get_markets(city, gender):
    df = dataframes.get('market_data')
    if df is not None:
        markets = df[
            (df['City'].str.lower() == city.lower()) &
            (df['Gender'].str.lower().isin([gender.lower(), 'unisex']))
        ]
        return markets
    return pd.DataFrame()


def get_restaurants(city):
    df = dataframes.get('restaurant_data')
    if df is not None:
        restaurants = df[df['City'].str.lower() == city.lower()]
        return restaurants
    return pd.DataFrame()

def get_museums(city, typology):
    df = dataframes.get('museums_data')
    if df is not None:
        df.columns = df.columns.str.strip().str.lower()
        museums = df[
            (df['city'].str.lower() == city.lower()) &
            (df['typology'].str.lower() == typology.lower())
        ]
        return museums
    return pd.DataFrame()



# ========== تطبيق Flask ==========
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat_response():
    user_msg = request.form['message'].strip().lower()
    response = ""

    # -------- Fan Events --------
    if "fan event" in user_msg:
        city = extract_value(user_msg, 'in')
        style = extract_value(user_msg, 'style')
        df = get_fan_events(city, style)
        if not df.empty:
            response = "🎪 Matching Fan Events:\n" + '\n'.join(
                f"- {row['Fan festival']} ({row['Style']})" for _, row in df.iterrows()
            )
        else:
            response = "ℹ️ No matching fan events found."

    # -------- Markets --------
    elif "market" in user_msg:
        city = extract_value(user_msg, 'in')
        gender = extract_value(user_msg, 'for')
        df = get_markets(city, gender)
        if not df.empty:
            response = f"🛍 Markets in {city.title()}:\n" + '\n'.join(
                f"- {row['Place_Name']} ({row['Gender']})" for _, row in df.iterrows()
            )
        else:
            response = "ℹ️ No matching markets found."

        # -------- Restaurants --------
    elif "restaurant" in user_msg:
        city = extract_value(user_msg, 'in')
        df = get_restaurants(city)
        if not df.empty:
            response = f"🍴 Restaurants in {city.title()}:\n" + '\n'.join(
                f"- {row['name']} (Rating: {row['rating']}, Cuisines: {row['Cuisines'].strip('[]').replace('/', '')})"
                for _, row in df.iterrows()
            )
        else:
            response = "ℹ️ No matching restaurants found."
    # -------- Museums --------
    elif "museum" in user_msg:
        city = extract_value(user_msg, 'in')
        typology = extract_value(user_msg, 'type')
        df = get_museums(city, typology)
        if not df.empty:
            response = f"🏛 Museums in {city.title()}:\n" + '\n'.join(
                f"- {row['asset name']} " for _, row in df.iterrows()
            )
        else:
            response = "ℹ️ No matching museums found."



    # -------- Fallback to Gemini --------
    else:
        gemini_reply = chat.send_message(user_msg)
        response = gemini_reply.text

    return jsonify({'response': response})

# ========== دالة بسيطة لاستخلاص الكلمات ==========
def extract_value(text, keyword):
    try:
        parts = text.split(keyword)
        return parts[1].strip().split()[0]
    except:
        return ""

if __name__ == '__main__':
    app.run(debug=True)