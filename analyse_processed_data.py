"""A script to analyse book data."""

import pandas as pd
import altair as alt
import altair_viewer



if __name__ == "__main__":
    # Make DataFrame
    books_df = pd.read_csv('PROCESSED_DATA.csv')


    # Books per decade
    grouped_decade = books_df.groupby((books_df['year']//10) *10)['title'].count().reset_index()
    grouped_decade.columns = ['Decade', 'Book Count']
    source = pd.DataFrame(
        {"Decade": grouped_decade['Decade'], "Books released": grouped_decade['Book Count']}
    )
    base = alt.Chart(source).encode(
        alt.Theta("Books released:Q").stack(True),
        alt.Color("Decade:N")
    )
    pie = base.mark_arc(outerRadius=120)
    text = base.mark_text(radius=140, size=20).encode(text="Decade:N")
    pie_chart = pie + text
    pie_chart.save('decade_releases.png')


    # Top authors
    grouped_author = books_df.groupby(books_df['author_name'])['ratings'].sum().reset_index()
    grouped_author = grouped_author.sort_values(by="ratings", ascending=False)
    grouped_author = grouped_author.head(10)
    source = pd.DataFrame({
    'author': grouped_author["author_name"],
    'total ratings': grouped_author["ratings"]
    })
    bar_chart = alt.Chart(source).mark_bar().encode(
        x='author',
        y='total ratings'
    )
    bar_chart.save('top_authors.png')
