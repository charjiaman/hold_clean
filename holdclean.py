from tkinter import Label
import pandas as pd


def main():

    filepath = r".\all_wip_positions.csv"
    df=pd.read_csv(filepath)
    df_new1 = df.loc[
        (df['Owner'] != 'INV-NS') & 
        (df['Owner'] != 'INV-S') & 
        (df['Owner'] != 'DEMO') & 
        (df['Work Station'].isin(['91-FLIP','88-NOV DEP', '92-FE CMP', '95-SCRUB','89-SACVD', '81-MET DEP', '99-GOLD ROOM', '87-BE HDP', '90-EDGE TRIM', '97-BOND', '82-WCVD', '83-AST', '91-FE GRIND', '86-FE HDP']))
    ]
    df_new = df_new1[['Lot', 'Product',	'Owner', 'Priority Level',	'Operation', 'Area', 'Work Station', 'Qty', 'Days At', 'Hold Code', 'Hold Message']]
    df_new.sort_values(by=['Days At'], inplace=True,  ascending=False)
    print(df_new)
    df_new.to_csv('.\CleanWip.csv')

if __name__ == "__main__":
    main()  
