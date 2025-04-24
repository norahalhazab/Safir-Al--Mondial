# Safir Al-Mondial 🏟️✈️

**Safir Al-Mondial** is a Saudi Arabia sports tourism assistant that helps users with personalized recommendations and event information. It offers features like match schedules, fan event recommendations, local market suggestions, museum listings, and restaurant recommendations. Powered by **Google's Gemini API**, the app allows users to interact via a chatbot that processes their queries and provides relevant results.

## Features:
- **Match schedule lookup**: Get up-to-date information on sports matches.
- **Fan meetup recommendations**: Discover fan events tailored to your preferences.
- **Local market suggestions**: Explore gender-specific markets and places to shop.
- **Museum listings**: Find museums based on province and type.
- **Restaurant recommendations**: Discover restaurants based on your city.
- **AI-powered theme suggestions**: Chat with the assistant for additional personalized recommendations.

## Data Sources:
The app uses CSV data files to provide recommendations:
- **Fan Preferences**: Data on fan events and their style.
- **Markets**: Information on local markets, gender filtering, and place names.
- **List_of_public_and_private_museums**: List of museums with typology and province-based filtering.
- **Restaurants**: Data on restaurants available in various cities in Saudi Arabia.
- **Matches**: Sports event schedules.
- **Stadiums**:list of Stadiums in the 5 host city for the world cup.

## Technology Stack:
- **Flask**: For the web framework.
- **pandas**: For handling and filtering the data.
- **Google Gemini API**: For generating AI-powered responses through the chatbot.
- **HTML**: For front-end design (UI).

## Figma Prototype:
You can view the app's **Figma prototype** by downloading the PDF here:
[Click here to download and view the Figma prototype PDF](https://www.figma.com/proto/LoDv61xafTExHhTknEO4Na/Let-s-Travel--Travel-app-home-screens--Community-?node-id=469-693&t=Yv7VehLNE6oAeMEN-1&scaling=scale-down&content-scaling=fixed&page-id=1%3A2&starting-point-node-id=469%3A693&show-proto-sidebar=1)

Once downloaded, click on the prototype to explore the interactive design and user interface.

## Installation & Setup:
### Prerequisites:
- **Python 3.x**
- **pip** (Python's package installer)
- **Google Gemini API access**

### Steps:
1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/your-username/Safir-Al-Mondial.git
   cd Safir-Al-Mondial
Install the required dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Set up the Gemini API:

Replace the API key in the chatbot.py file with your own valid Gemini API key.

You can get the key from Google Cloud.

Ensure that the required CSV files are placed in the appropriate directory on your machine (data_path). The files should be named as follows:

fan_preferences.csv

List_of_public_and_private_museums.csv

matches.csv

Sample_Restaurant_Dataset.csv

saudi_markets.csv

Stadiums.csv

Run the Flask application:

bash
Copy
Edit
python chatbot.py
Open a browser and go to http://127.0.0.1:5000/ to interact with the chatbot.

Usage:
Once the app is running, open your browser and visit http://127.0.0.1:5000/.

You'll be greeted with a chatbot interface where you can ask about:

Fan events: Example query: "Show me fan event in Riyadh for modern style".

Markets: Example query: "What are the markets in Riyadh for unisex?"



Restaurants: Example query: "Find me restaurant in jeddah".

Fallback: If the message doesn't match any of the above, the chatbot will use Google Gemini to generate a response.
