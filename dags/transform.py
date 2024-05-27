import pandas as pd

#Function definition
#Convert a duration string to total minutes.
def convert_durationcolumn_to_minutes(duration_str):
    duration_str = duration_str.strip()
    if 'hr' in duration_str and 'min' in duration_str:
        hours, minutes = duration_str.split(' ')[0], duration_str.split(' ')[2]
        total_minutes = int(hours) * 60 + int(minutes)
    elif 'min' in duration_str:
        total_minutes = int(duration_str.split(' ')[0])
    else:
        total_minutes = 0
    return total_minutes

#Modify the genres string by taking the first half of each genre name.
def modified_genrescolumn(genres_str):
    genres_str = genres_str.strip()
    list_genres_modified = [item[:len(item)//2] for item in genres_str.split(', ')]
    return ', '.join(list_genres_modified)

#Read and transform data column
#Read data
df = pd.read_csv(r"/opt/airflow/input/Top_Anime_data.csv")

#Transform English column
df = df.rename(columns={'English': 'Name'})

#Transform Aired column
df[['Aired_from', 'Aired_to']] = df['Aired'].str.split(' to ', expand=True)
df.drop(columns=['Aired'], inplace=True)

#Transform Duration column
df['Duration'] = df['Duration'].apply(convert_durationcolumn_to_minutes)
df.rename(columns={'Duration': 'Duration (min per ep)'}, inplace=True)

#Transform Genres column
df['Genres'] = df['Genres'].apply(lambda x: x if isinstance(x, str) else '')
df['Genres'] = df['Genres'].apply(modified_genrescolumn)

#Select columns in new Dataframe
selected_columns = ["Rank","Score","Popularity", "Members", "Name", "Genres", "Type", "Episodes", "Duration (min per ep)", "Status", "Aired_from", "Aired_to", "Studios", "Source","Rating"]
selected_df = df[selected_columns]

#Save new Dataframe to csv file
selected_df.to_csv(r'/opt/airflow/output/Top_Anime_data_output.csv', index=False)


