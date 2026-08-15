from app.database import get_connection
import pandas as pd 

def seed_pincodes(pincode,area):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """INSERT OR IGNORE INTO regional_pincodes(pincode,area,city,state)
        VALUES(?,?,"South 24 Parganas","WestBengal")
        """,(pincode,area))
    
    conn.commit()
    conn.close()

df = pd.read_csv('south_24_parganas_areas.csv')

for index,data in df.iterrows():
    pincode = data['Pincode']
    area = data['Area Name']
    seed_pincodes(pincode,area)
