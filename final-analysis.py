import pandas as pd ,matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.ticker as mticker
import os
import time 

start_time = time.time()
print(f'the starting time is {start_time}')


# loaded at the end
df = pd.read_csv('final_data.csv')

print(f'we are working with {df.shape[0]} rows')


# Step 1: Clean and split airline names
df['segmentsAirlineName'] = df['segmentsAirlineName'].str.replace(r'\s*\|\|\s*', '||', regex=True)


# drop the null values
df.dropna(subset=['segmentsEquipmentDescription', 'segmentsDistance'], inplace=True)


# function to calculate the total distance

def calculate_total_traveled_distance(segment_distance_list):
  vals = segment_distance_list.split('||')
  # i.isdigit() is a str method in python
  valid_values = [ i for i in vals if i and i.isdigit()]
  return sum(map(int,valid_values))


# ----------------------------------------totalDistance------------------------------------------------------
#.apply() runs in C-optimized pandas code. inshort python is slow, C is very fast
df['total_distance'] = df['segmentsDistance'].apply(calculate_total_traveled_distance) 

df = df.drop(['totalTravelDistance'], axis=1)
# df.rename(columns={'old_column_name': 'new_column_name'})
df = df.rename(columns={'total_distance': 'totalTravelDistance'})

# ----------------------------------------totalDistance------------------------------------------------------

# ----------------------------------------Airports count ------------------------------------------------------

arrival_airports = df['segmentsArrivalAirportCode'].str.split(r'\|\|').explode()
arrival_airport_count = arrival_airports.value_counts()

departure_airports = df['segmentsDepartureAirportCode'].str.split(r'\|\|').explode()
departure_airport_count = departure_airports.value_counts()

airport_count = pd.concat([arrival_airport_count,departure_airport_count], axis=1)
airport_count.columns = ['arrival_airport_count','departure_airport_count']


airport_count['total'] = airport_count['arrival_airport_count'] +  airport_count['departure_airport_count']

sns.set_theme()
ax = airport_count['total'].head().plot(kind='barh')
ax.xaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f'{int(x):,}'))  # Format x-axis numbers with commas

plt.xlabel('count')
plt.ylabel('Airport Code')
plt.title('Most used airports in the US')

# Define the directory and file path
folder = "Graphs"
file_path = os.path.join(folder, "most-used-airports.png")

# Create the directory if it does not exist
os.makedirs(folder, exist_ok=True)

plt.savefig(file_path, dpi=300, bbox_inches="tight")
plt.close() 

# ----------------------------------------Airports count ------------------------------------------------------


# ---------------------------------------- Common Connections in Multi-Leg Flights ------------------------------------------------------

# Extract the first departure and arrival airport codes
# taking the first column from the list as explained above
df['departure'] = df['segmentsDepartureAirportCode'].str.split(r'\|\|', expand=True)[0] 
df['arrival'] = df['segmentsArrivalAirportCode'].str.split(r'\|\|', expand=True)[0] # the 1st item in the 'list' <- easier to think of it as a list

# Create a "route" column
df['route'] = df['departure'] + "->" + df['arrival']

sns.set_theme()

plt.title("Top conncections used ")
df['route'].value_counts().head(5).plot(kind='barh')
plt.xlabel('Count')
plt.ylabel('Connection')


# Define the directory and file path
folder = "Graphs"
file_path = os.path.join(folder, "Top-connections-used-firstStop.png")

# Create the directory if it does not exist
os.makedirs(folder, exist_ok=True)

plt.savefig(file_path, dpi=300, bbox_inches="tight")
plt.close() 

# ---------------------------------------- Common Connections in Multi-Leg Flights ------------------------------------------------------



# ---------------------------------------- WHERE PEOPLE IN THE US TRAVEL TO IN THE US ?  ------------------------------------------------------

start_location =  df['segmentsDepartureAirportCode'].str.split(r'\|\|', expand=True)[0] 

def get_final_destination(x):
  final = ''
  for i in x: 
    if i != None: 
      final = i
      
  return final


end_location = df['segmentsArrivalAirportCode'].str.split(r'\|\|').apply(get_final_destination)

df['start_END_Destination'] = start_location + '->' + end_location

route_counts = df['start_END_Destination'].value_counts()
route_counts.head(10).plot(kind='barh')

sns.set_theme()


plt.xlabel("Count")
plt.ylabel("Start to End Destinations ")
plt.title('where most people in the US travel inside the US')

# Define the directory and file path
folder = "Graphs"
file_path = os.path.join(folder, "most-travelled-to-in-US.png")

# Create the directory if it does not exist
os.makedirs(folder, exist_ok=True)

plt.savefig(file_path, dpi=300, bbox_inches="tight")
plt.close() 

# ---------------------------------------- WHERE PEOPLE IN THE US TRAVEL TO IN THE US ?  ------------------------------------------------------



# ---------------------------------------- Departures and total fare { can i prove a connection ?} ------------------------------------------------------



# i want to catch the flights where the departure segment contains something like 
# Filter rows where column 0 contains at least two "->" separators
# three_or_more_departures_df = df[df['full_route'].str.contains(r'[^ ]+ -> [^ ]+ -> ', regex=True)]
three_or_more_departures_df = df[df['segmentsDepartureAirportCode'].str.contains(r"^[A-Z]{3}\|\|[A-Z]{3}\|\|", regex=True)]


arrival_airports = 'segmentsArrivalAirportCode'	
departure_airports = 'segmentsDepartureAirportCode'

# i want tickets which exactly have 2 departures
two_departure_df = df[
    df[departure_airports].str.contains(r"^[A-Z]{3}\|\|[A-Z]{3}$", regex=True)
]


# i want tickets which exactly have 1 departure
nonStop_tickets = df[
    df[departure_airports].str.contains(r"^[A-Z]{3}$", regex=True)
]


sns.set_theme()


# the KDP - GRAPH
plt.figure(figsize=(10, 6))
sns.kdeplot(three_or_more_departures_df.totalFare, label='3+ Departures', fill=True, alpha=0.5)
sns.kdeplot(two_departure_df.totalFare, label='2 Departures', fill=True, alpha=0.5)
sns.kdeplot(nonStop_tickets.totalFare, label='1 Departure', fill=True, alpha=0.5)

plt.xlabel('Total Fare')
plt.ylabel('Density')
plt.title('Comparison of Total Fare Distributions')
plt.legend()


# Define the directory and file path
folder = "Graphs"
file_path = os.path.join(folder, "kdp-totalfare.png")

# Create the directory if it does not exist
os.makedirs(folder, exist_ok=True)

plt.savefig(file_path, dpi=300, bbox_inches="tight")
plt.close() 


# HISTOGRRRRRAMMMM
sns.set_theme()

# Plot histograms together
plt.figure(figsize=(10, 6))
three_or_more_departures_df.totalFare.hist(alpha=0.8, label='3+ Departures', bins=70)
two_departure_df.totalFare.hist(alpha=0.5, label='2 Departures', bins=70)
nonStop_tickets.totalFare.hist(alpha=0.5, label=' 1 Departure', bins=70)


# Add labels and title
plt.xlabel('Total Fare')
plt.ylabel('Frequency')
plt.title('Comparison of Total Fare Distributions')
plt.xlim((0,1000))
plt.legend()


# Define the directory and file path
folder = "Graphs"
file_path = os.path.join(folder, "hist-totalfare.png")

# Create the directory if it does not exist
os.makedirs(folder, exist_ok=True)

plt.savefig(file_path, dpi=300, bbox_inches="tight")
plt.close() 





# ---------------------------------------- Departures and total fare { can i prove a connection ?} ------------------------------------------------------







# ---------------------------------------- MOST USED AIRLINES ------------------------------------------------------



sns.set_theme()


plt.figure(figsize=(12,7))
plt.xticks(rotation=45)
ax = df['segmentsAirlineName'].str.split(r"\|\|").explode().value_counts().head().plot(kind='barh')
ax.xaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f'{int(x):,}'))  # Format x-axis numbers with commas
plt.ylabel("Airline Names")
plt.xlabel("Count")
plt.title('Most Used Airlines')

# Define the directory and file path
folder = "Graphs"
file_path = os.path.join(folder, "most-used-airlines.png")

# Create the directory if it does not exist
os.makedirs(folder, exist_ok=True)

plt.savefig(file_path, dpi=300, bbox_inches="tight")
plt.close() 
# ---------------------------------------- MOST USED AIRLINES ------------------------------------------------------



# ---------------------------------------- EXPENSIVE DESTINATIONS  ------------------------------------------------------
sns.set_theme()


airline_fare_stats = (
    df.groupby('start_END_Destination', observed=True)['totalFare']
    .agg(['mean', 'median','min', 'max', 'count'])
    .sort_values(by='median', ascending=False)
)
airline_fare_stats['median'].head().plot(kind='barh')
plt.ylabel('DESTINATION')
plt.xlabel('Top Median Fares $')
plt.title("EXPENSIVE DESTINATIONS")
plt.tight_layout()


# Define the directory and file path
folder = "Graphs"
file_path = os.path.join(folder, "topMedian-Start-to-End.png")

# Create the directory if it does not exist
os.makedirs(folder, exist_ok=True)

plt.savefig(file_path, dpi=300, bbox_inches="tight")
plt.close() 

# ---------------------------------------- EXPENSIVE DESTINATIONS  ------------------------------------------------------



# ---------------------------------------- CHEAPEST DESTINATIONS  ------------------------------------------------------

sns.set_theme()


airline_fare_stats = (
    df.groupby('start_END_Destination', observed=True)['totalFare']
    .agg(['mean', 'median','min', 'max', 'count'])
    .sort_values(by='median', ascending=True)
)
airline_fare_stats['median'].head().plot(kind='barh')
plt.ylabel('DESTINATION')
plt.xlabel('Cheapest Median Fares $')
plt.title(" CHEAPEST DESTINATIONS  ")
plt.tight_layout()


# Define the directory and file path
folder = "Graphs"
file_path = os.path.join(folder, "cheapMedianFare-Start-to-End.png")

# Create the directory if it does not exist
os.makedirs(folder, exist_ok=True)

plt.savefig(file_path, dpi=300, bbox_inches="tight")
plt.close() 



# ---------------------------------------- CHEAPEST DESTINATIONS  ------------------------------------------------------


print("Null values in the dataset")
print(df.isna().sum())

end_time = time.time()

print(f'the end time is {end_time}')

time_taken = end_time - start_time


print(f'the total time taken is {time_taken:.2f} seconds')









