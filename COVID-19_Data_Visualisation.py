import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def fetch_covid_data():
    url = "https://api.covid19api.com/summary"
    try:
        response = requests.get(url)
        response.raise_for_status()  
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

def process_data(data):
    if data is None:
        return None, None
    
    # Convert global data to DataFrame
    global_data = pd.DataFrame([data['Global']])
    
    # Convert countries data to DataFrame
    countries_data = pd.DataFrame(data['Countries'])
    
    return global_data, countries_data

def create_visualizations(global_data, countries_data):
    if global_data is None or countries_data is None:
        print("No data available to create visualizations.")
        return

    sns.set(style="whitegrid")
    
    plt.figure(figsize=(10, 6))
    global_data_plot = global_data[['TotalConfirmed', 'TotalDeaths', 'TotalRecovered']].melt()
    sns.barplot(x='variable', y='value', data=global_data_plot, palette='viridis')
    plt.title('Global COVID-19 Cases, Deaths, and Recoveries')
    plt.xlabel('Category')
    plt.ylabel('Count')
    plt.show()
    
    top_10_confirmed = countries_data.nlargest(10, 'TotalConfirmed')
    plt.figure(figsize=(14, 7))
    sns.barplot(x='TotalConfirmed', y='Country', data=top_10_confirmed, palette='rocket')
    plt.title('Top 10 Countries by Total Confirmed COVID-19 Cases')
    plt.xlabel('Total Confirmed Cases')
    plt.ylabel('Country')
    plt.show()
    
    top_10_deaths = countries_data.nlargest(10, 'TotalDeaths')
    plt.figure(figsize=(14, 7))
    sns.barplot(x='TotalDeaths', y='Country', data=top_10_deaths, palette='mako')
    plt.title('Top 10 Countries by Total COVID-19 Deaths')
    plt.xlabel('Total Deaths')
    plt.ylabel('Country')
    plt.show()

def main():
    # Fetch the data
    data = fetch_covid_data()
    
    # Process the data
    global_data, countries_data = process_data(data)
    
    # Create visualizations
    create_visualizations(global_data, countries_data)

if __name__ == "__main__":
    main()
