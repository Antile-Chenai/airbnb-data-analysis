import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print("Starting Airbnb Market Analysis Project...")

# Load dataset
data = pd.DataFrame({
    "Neighborhood": ["A", "B", "C", "A", "B", "C"],
    "Price": [120, 150, 200, 130, 160, 210],
    "Bedrooms": [1,2,3,2,3,4]
})

# Compute neighborhood stats
neighborhood_stats = data.groupby("Neighborhood")["Price"].mean().reset_index()

# Plot average price by neighborhood
sns.set_style('whitegrid')
plt.figure(figsize=(8,5))
sns.barplot(x='Neighborhood', y='Price', data=neighborhood_stats)
plt.title('Average Price by Neighborhood')
plt.savefig('avg_price_by_neighborhood.png')
plt.close()

# Plot price distribution
plt.figure(figsize=(8,5))
sns.histplot(data['Price'], bins=10)
plt.title('Price Distribution')
plt.savefig('price_distribution.png')
plt.close()

# Scatterplot price vs bedrooms
plt.figure(figsize=(8,5))
sns.scatterplot(x='Bedrooms', y='Price', hue='Neighborhood', data=data)
plt.title('Price vs Bedrooms')
plt.savefig('price_vs_bedrooms.png')
plt.close()

# Summary stats
print("Neighborhood price summary:")
print(neighborhood_stats)
print("\nAirbnb Market Analysis Project Completed!")
