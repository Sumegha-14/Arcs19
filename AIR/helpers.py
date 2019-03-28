import pandas as pd
def get_index(place,month):
    df=pd.read_csv("./andhra.csv",parse_dates=["Sampling Date"])
    df.rename(columns={'City/Town/Village/Area': 'Place'}, inplace=True)
    places=sorted(df["Place"].unique())
    place_index=places.index(place)
    months=['April', 'August', 'December', 'February', 'January', 'July', 'June', 'March', 'May', 'November', 'October', 'September']
    month_index=months.index(month)
    return place_index,month_index

