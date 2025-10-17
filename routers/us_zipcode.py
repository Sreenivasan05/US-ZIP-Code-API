from fastapi import APIRouter, Depends, status, HTTPException
from database_operation import db_conn
import database_operation, schemas


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

