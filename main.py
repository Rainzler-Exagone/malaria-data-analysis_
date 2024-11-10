import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.subplots as make_subplots
import datetime as datetime
import geopandas as gpd

malaria_death_df = pd.read_csv("C:\\Users\\yasse_q\\Downloads\\data.csv")
malaria_cases_df = pd.read_csv("C:\\Users\\yasse_q\\Downloads\\estimated-cases.csv")
print(malaria_death_df.head(20))

# for more details about the table
print(malaria_death_df.info())

# to get more staistics details
print(malaria_death_df.describe())



statewise = pd.pivot_table(malaria_death_df, index=["Location"], values=["FactValueNumeric"], aggfunc="sum")
statewise = statewise.sort_values(by="FactValueNumeric", ascending=False)

cases = pd.pivot_table(malaria_cases_df, index=["Location"], values=["FactValueNumeric"], aggfunc="sum")
cases = cases.sort_values(by="FactValueNumeric", ascending=False)


html = statewise.style.background_gradient(cmap="cubehelix").to_html()
with open("statewise_gradient.html", "w") as file:
    file.write(html)
print("Table saved as 'statewise_gradient.html'")


top10 = malaria_death_df.groupby(by='Period').max()[['FactValueNumeric']]
# fig = plt.figure(figsize=(16,9))
# plt.title("Malaria deaths")

# ax = sns.barplot(data=top10.iloc[:90], y='FactValueNumeric', x='Period')
# ax.set_xlabel("Location")
# ax.set_ylabel("Malaria Deaths")
# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.show() 

top10_cases = malaria_cases_df.groupby(by='Period').max()[['FactValueNumeric']]
# fig = plt.figure(figsize=(16,9))
# plt.title("Top 10 states with most malaria cases")

# ax = sns.barplot(data=top10_cases.iloc[:10], y='FactValueNumeric', x='Period')
# ax.set_xlabel("Location")
# ax.set_ylabel("Malaria cases")
# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.show() 
malaria_cases_2021_df = malaria_cases_df[malaria_cases_df['Period'] == 2021]
map_fig =px.scatter_geo(malaria_cases_2021_df,locations='SpatialDimValueCode',projection="orthographic",color='FactValueNumeric',opacity=.8,hover_name='Location',hover_data=['FactValueNumeric','Period'])
map_fig.show()


fig = plt.figure(figsize=(12, 6))
ax = sns.lineplot(data=malaria_cases_df[malaria_cases_df['Location'].isin(['Algeria','Angola','Ghana','Mali','Niger','Somalia','Mauritania'])], x='Period', y='FactValueNumeric', hue='Location')
ax.set_title("African affected countries",size=10)

# Create a figure with two subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 9))

# Plot malaria deaths
sns.barplot(data=top10, y='FactValueNumeric', x=top10.index, ax=ax1)
ax1.set_title("Malaria Deaths")
ax1.set_xlabel("Period")
ax1.set_ylabel("Malaria Deaths")
ax1.tick_params(axis='x', rotation=45)

# Plot malaria cases
sns.barplot(data=top10_cases, y='FactValueNumeric', x='Period', ax=ax2)
ax2.set_title("Malaria Cases")
ax2.set_xlabel("Period")
ax2.set_ylabel("Malaria Cases")
ax2.tick_params(axis='x', rotation=45)

# Adjust layout
plt.tight_layout()
plt.show()



