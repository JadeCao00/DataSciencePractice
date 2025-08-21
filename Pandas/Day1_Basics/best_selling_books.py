# 1 import pandas module
import pandas as pd

# 2 Load the spreadsheet
df = pd.read_csv('bestsellers_amazon.csv')

# 3 Explore the data
print(df.head()) # Get the first five rows of the spreadsheet
print(df.shape) # Get the shape of the spreadsheet
print(df.columns) # Get the column names of the spreadsheet
print(df.describe()) # Get summary statistics for each column
print(df.info()) # Get the data types and missing values

# 4 Clean the data
# Drop the duplicate rows
df.drop_duplicates(inplace=True)
## By setting the inplace parameter True, the changes are made directly to the original DataFrame

# Rename the columns, make them more descriptive
df.rename(columns={'Name':'Title','User Rating': 'Rating' ,'Year': 'Publication Year'}, inplace=True)
print(df.columns)

# Covert the data type
## Covert the 'price' column to a float data type, we can use the astype() function
df['Price'] = df['Price'].astype(float)

# 5 Run an analysis
# Analyse author popularity
author_counts = df['Author'].value_counts()
print(author_counts)

# Average rating by genre
avg_rating_by_genre = df.groupby('Genre')['Rating'].mean()
print(avg_rating_by_genre)

# 6 Export the result
# Export the top 10 selling authors to a CSV file
author_counts.head(10).to_csv('top_authors.csv')

# Export average rating by genre to a CSV file
avg_rating_by_genre.to_csv('avg_rating_by_genre.csv')

