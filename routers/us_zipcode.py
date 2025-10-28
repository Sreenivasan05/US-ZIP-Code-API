from fastapi import APIRouter, Depends, status, HTTPException
from database_operation import db_conn
import database_operation, schemas
from calculations import calculate_dis, haversine, calculate_coordinate_ranges


router  = APIRouter()

@router.get("/ping")
async def ping():
    return "OK"

@router.get("/zipcode/{zipcode}")
async def get_zipcode_data(zipcode:int,cursor = Depends(db_conn.get_connection)):
    zipcode_data = database_operation.get_zipcode_data(zipcode,cursor)

    if not zipcode_data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"No data for this zipcode {zipcode}")
    return zipcode_data

@router.get("/states")
async def get_states_list():
    states_list = database_operation.get_states_name()
    return states_list

@router.get("/counties")
async def read_item(item:schemas.Counties = Depends(),cursor = Depends(db_conn.get_connection)):
    counties_list = database_operation.get_counties_name(item.state,item.page,cursor)
    if not counties_list:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"No counties found for the state {item.state}, check the state name in the states method")
    return counties_list

@router.get("/zipcode/{zipcode}/validate")
async def validate_zipcode(zipcode:int,cursor = Depends(db_conn.get_connection)):
    valid_zipcode = database_operation.get_zipcode_data(zipcode,cursor)
    return {"valid": True} if valid_zipcode else {"valid": False} 

@router.get("/calculate_distance")
async def distance_btw_two_latlong(location:schemas.TwoLocation = Depends()):
    distance_result = calculate_dis([location.latitude1,location.longitude1],[location.latitude2,location.longitude2])
    return distance_result


@router.get("/zipcode_distance")
async def distance_btw_zipcode(zipdata:schemas.TwoZipcode = Depends(),cursor = Depends(db_conn.get_connection)):
    loc1 = database_operation.get_zipcode_location(zipdata.zipcode1,cursor)
    if not loc1:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No data for this zipcode {zipdata.zipcode1}")
    loc2 = database_operation.get_zipcode_location(zipdata.zipcode2,cursor)
    if not loc2:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No data for this zipcode {zipdata.zipcode2}")
    distance = calculate_dis([loc1["latitude"],loc1["longitude"]],[loc2["latitude"],loc2["longitude"]])
    return distance

@router.get("/nearby_location")
async def nearby_loc_of_loc(loca:schemas.Location = Depends(),cursor = Depends(db_conn.get_connection)):
    lat_range, lon_range = calculate_coordinate_ranges(lat=loca.latitude,lon=loca.longitude,distance_km=10)
    nearby_loc = database_operation.get_nearby_location(lat_range[0],lat_range[1],lon_range[0],lon_range[1],cursor)
    sorted_nearby_loc = sorted(nearby_loc,key=lambda loc:haversine(loca.latitude,loca.longitude,loc["latitude"],loc['longitude']))
    return sorted_nearby_loc[0:11] 

@router.get("/nearby_zipcodes/{zipcode}")
async def nearby_zipcodes(zipcode:int,cursor = Depends(db_conn.get_connection)):
    zipcode_loc = database_operation.get_zipcode_location(zipcode,cursor)
    if not zipcode_loc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No data for this zipcode {zipcode}")
    lat_range, lon_range = calculate_coordinate_ranges(lat=zipcode_loc["latitude"],lon=zipcode_loc["longitude"],distance_km=5)
    nearby_loc = database_operation.get_nearby_location(lat_range[0],lat_range[1],lon_range[0],lon_range[1],cursor)
    sorted_nearby_loc = sorted(nearby_loc,key=lambda loc:haversine(zipcode_loc["latitude"],zipcode_loc["longitude"],loc["latitude"],loc['longitude']))
    return sorted_nearby_loc[1:11]

