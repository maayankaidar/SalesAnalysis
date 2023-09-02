import globals as glb


def send_apology_email(df):
    contact_list = []

    # Data Extracting
    df_not_arrived = df[(df['STATUS'] == 'On Hold') | (df['STATUS'] == 'In Process') | (df['STATUS'] == 'Disputed')]
    df_late_orders = df_not_arrived[glb.TODAYS_DATE - df['ORDERDATE'] > glb.ONE_WEEK]

    # Extract unique contact names
    unique_last_names = df_late_orders['CONTACTLASTNAME'].unique()
    unique_first_names = df_late_orders['CONTACTFIRSTNAME'].unique()

    # Create a list to store contact names
    for last_name, first_name in zip(unique_last_names, unique_first_names):
        contact_name = last_name + " " + first_name
        contact_list.append(contact_name)

    email_text = "Apology emails sent to:\n" + "\n".join(contact_list)
    email_text += "\n"
    print(email_text)


def clean_dates(df):
    data_frame = df['ORDERDATE'].apply(lambda x: glb.datetime.strptime(x, glb.DATE_FORMAT))
    print("Dates have been reformatted.")
    print("\n")
    return data_frame


def country_sales(df):
    shipped_df = df[df['STATUS'] == 'Shipped']
    country_counts = shipped_df['COUNTRY'].value_counts()
    country_counts.plot(kind='bar', color='red')
    glb.plt.xlabel('Country')
    glb.plt.ylabel('Sales')
    glb.plt.title('Count of Orders by Country (Shipped)')
    glb.plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
    glb.plt.tight_layout()  # Adjust layout to prevent labels from getting cut off
    glb.plt.show()
    print("Minimal sales: " + str(country_counts.min()) + " in " + country_counts.idxmin())
    print("Maximal sales: " + str(country_counts.max()) + " in " + country_counts.idxmax())
    print("Average sales: " + str(country_counts.mean().round(2)))
    print("\n")


def month_trending_sales(df, start_date, end_date):
    shipped_df = df[df['STATUS'] == 'Shipped']
    filtered_df = shipped_df[(shipped_df['ORDERDATE'] >= start_date) & (shipped_df['ORDERDATE'] <= end_date)]
    month_counts = filtered_df.groupby([filtered_df['ORDERDATE'].dt.year, filtered_df['ORDERDATE'].dt.month]).size()
    month_counts.plot(kind='bar', color='green')
    glb.plt.xlabel('Months')
    glb.plt.ylabel('Amount')
    glb.plt.title('Trending sales by months')
    glb.plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
    glb.plt.tight_layout()  # Adjust layout to prevent labels from getting cut off
    glb.plt.show()

    min_month = month_counts.idxmin()
    max_month = month_counts.idxmax()
    print("Minimal sales: " + str(month_counts.min()) + " in month " + f"{min_month[1]}/{min_month[0]}")
    print("Maximal sales: " + str(month_counts.max()) + " in month " + f"{max_month[1]}/{max_month[0]}")
    print("Average sales: " + str(month_counts.mean().round(2)))
    print("\n")
