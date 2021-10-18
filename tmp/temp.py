import sqlite3
import pandas as pd

book_detail_csv = "C:/Users/Admin/Desktop/Data_Science_Goodreads/data/info_book_detail_per_30.csv"
user_rating_csv = "C:/Users/Admin/Desktop/Data_Science_Goodreads/data/user_rating_book_filter_per_30.csv"
conn = sqlite3.connect("db.sqlite3")

df_book_detail = pd.read_csv(book_detail_csv)

df_book_detail.rename(columns={"Rating": "Rating_Avg", "Rating_Counts": "Rating_Count", "Reviews_Counts": "Reviews_Count", "Book_ID":"Book_Id"}, inplace = True)


df_user_rating = pd.read_csv(user_rating_csv)

df_user_detail = df_user_rating[["user_id", "username", "user_url"]].copy()
df_user_detail.rename(columns={"user_id": "User_Id", "username": "Username", "user_url": "User_Url"}, inplace = True)
df_user_detail.sort_values("User_Id", inplace = True)
df_user_detail.drop_duplicates(subset = ["User_Id", "User_Url"], inplace = True)
df_user_detail.set_index("User_Id", inplace=True)


df_user_rating = df_user_rating[["user_id", "book_id", "user_rating"]]
df_user_rating.rename(columns={"user_id": "User_id", "book_id": "Book_id", "user_rating": "User_Rating"}, inplace = True)
df_user_rating.sort_values(by=["User_id", "Book_id"], inplace = True)



# df_user_rating.to_sql("User_Rating", conn, if_exists='append', index=False, chunksize=500, method="multi")
# print("Done write to SQL")


# df_user_detail.to_sql("User_Info", conn, if_exists='append', index=True)
# print("Done write to SQL")

# df_book_detail.to_sql("Book_Details", conn, if_exists='append', index=True, index_label="Book_Id")
# print("Done write to SQL")