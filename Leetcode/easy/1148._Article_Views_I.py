""" 1148. Article Views I
Easy

Table: Views

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| article_id    | int     |
| author_id     | int     |
| viewer_id     | int     |
| view_date     | date    |
+---------------+---------+
There is no primary key (column with unique values) for this table, the table may have duplicate rows.
Each row of this table indicates that some viewer viewed an article (written by some author) on some date. 
Note that equal author_id and viewer_id indicate the same person.
 

Write a solution to find all the authors that viewed at least one of their own articles.

Return the result table sorted by id in ascending order.

The result format is in the following example.


Example 1:

Input: 
Views table:
+------------+-----------+-----------+------------+
| article_id | author_id | viewer_id | view_date  |
+------------+-----------+-----------+------------+
| 1          | 3         | 5         | 2019-08-01 |
| 1          | 3         | 6         | 2019-08-02 |
| 2          | 7         | 7         | 2019-08-01 |
| 2          | 7         | 6         | 2019-08-02 |
| 4          | 7         | 1         | 2019-07-22 |
| 3          | 4         | 4         | 2019-07-21 |
| 3          | 4         | 4         | 2019-07-21 |
+------------+-----------+-----------+------------+
Output: 
+------+
| id   |
+------+
| 4    |
| 7    |
+------+
"""

# 🍏 Hope this solution might be useful for someone!
# Find observations where author_id are equal views. It's mean that author visited his own work.
# Drop observations by author_id columns to make sure that count each author only once.
# Sort observations by author_id columns
# Take only values from author_id Series
# Create DataFrame for submission with columns=['id']

import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    authors = views[views['author_id'] == views['viewer_id']] \
        .drop_duplicates(subset='author_id') \
        .sort_values(by='author_id').author_id.values

    return pd.DataFrame(data=authors, columns=['id'])
