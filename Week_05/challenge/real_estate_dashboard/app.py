from flask import Flask, render_template
import pandas as pd
import matplotlib.pyplot as plt
import os

app = Flask(__name__)

# Load the data
data_file = '/workspaces/scientific_programming/Week_05/challenge/apartments_data_enriched_cleaned.csv'
df = pd.read_csv(data_file)

# Calculate KPIs
average_price = df['price'].mean()
average_area = df['area'].mean()

# Create a price distribution plot
plt.figure(figsize=(10, 6))
plt.hist(df['price'], bins=30, edgecolor='k', color='skyblue')
plt.title('Price Distribution')
plt.xlabel('Price')
plt.ylabel('Frequency')
plot_path = os.path.join('static', 'price_distribution.png')
plt.savefig(plot_path)
plt.close()

@app.route('/')
def index():
    return render_template('index.html', 
                           avg_price=round(average_price, 2), 
                           avg_area=round(average_area, 2), 
                           table_data=df.to_html(classes='table table-striped', index=False))

if __name__ == '__main__':
    app.run(debug=True)