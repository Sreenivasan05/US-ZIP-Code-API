import sqlite3
import os, json



class DatabaseManagement:
    def __init__(self, db_filename):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        self.db_path = os.path.join(base_dir, db_filename)
        self.connection = None
    
    def connect_to_db(self):
        try:
            self.connection = sqlite3.connect(self.db_path, check_same_thread = False)
            self.connection.row_factory = sqlite3.Row

            self.connection.create_function("initcap", 1, lambda s: s.title() if s else s)

            print("connected to SQLite db")
        except Exception as e:
            print(f"Error connecting to SQLite: {e}")

    def get_connection(self):

        if self.connection is None:
            self.connect_to_db()
        cursor = self.connection.cursor()
        try:
            yield cursor
        except Exception as e:
            self.connection.rollback()
            raise e
        finally:
            cursor.close()

    def close_pool(self):
        if self.connection:
            self.connection.close()
            print("closed SQLite connection")

def get_zipcode_data(zipcode,curr):
    curr.execute("""
    SELECT 
	postal_code, 
	initcap(place_name) as place_name,
	initcap(state_name) as state_name,
	state_code,
	initcap(county_name) as county_name,
	county_code,
	latitude, longitude 
	FROM zipcodes
	where postal_code = ?;
""",(zipcode,))
    data_zipcode = curr.fetchone()

    return data_zipcode

def get_states_name():
    # directly returning the data without calling the data from database
    states_list = [
    "Alabama",
    "Alaska",
    "Arizona",
    "Arkansas",
    "California",
    "Colorado",
    "Connecticut",
    "Delaware",
    "District Of Columbia",
    "Florida",
    "Georgia",
    "Hawaii",
    "Idaho",
    "Illinois",
    "Indiana",
    "Iowa",
    "Kansas",
    "Kentucky",
    "Louisiana",
    "Maine",
    "Maryland",
    "Massachusetts",
    "Michigan",
    "Minnesota",
    "Mississippi",
    "Missouri",
    "Montana",
    "Nebraska",
    "Nevada",
    "New Hampshire",
    "New Jersey",
    "New Mexico",
    "New York",
    "North Carolina",
    "North Dakota",
    "Ohio",
    "Oklahoma",
    "Oregon",
    "Pennsylvania",
    "Rhode Island",
    "South Carolina",
    "South Dakota",
    "Tennessee",
    "Texas",
    "Utah",
    "Vermont",
    "Virginia",
    "Washington",
    "West Virginia",
    "Wisconsin",
    "Wyoming"
]

    return states_list

def get_counties_name(state_name:str,offset:int,curr):

    offset = max((offset - 1) * 50, 0)

    curr.execute("""
        SELECT json_group_array(initcap(county_name)) AS county_name
        FROM (
            SELECT DISTINCT county_name
            FROM zipcodes
            WHERE state_name = ?
            ORDER BY county_name ASC
            LIMIT 50 OFFSET ?
        );
    """, (state_name, offset))
    row = curr.fetchone()
    if row and row["county_name"]:
        counties = json.loads(row["county_name"])
    return {state_name.capitalize(): counties}

def get_zipcode_location(zip:int,curr):
    curr.execute("""SELECT latitude,longitude from zipcodes where postal_code = ?""",(zip,))
    loc = curr.fetchone()
    return loc

def get_nearby_location(lat_start, lat_end,long_start,long_end,curr):
    curr.execute("""
    SELECT
    postal_code, 
	initcap(place_name) as place_name,
	initcap(state_name) as state_name,
	state_code,
	initcap(county_name) as county_name,
	county_code,
	latitude, longitude 

    FROM zipcodes
    WHERE latitude BETWEEN ? AND ?
    AND
    longitude BETWEEN ? AND ?;
    """,(lat_start,lat_end,long_start,long_end))
    data = curr.fetchall()
    return data

db_conn = DatabaseManagement("US_zipcodes.db")