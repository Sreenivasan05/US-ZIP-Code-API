# US ZIP Code Data Service API

**US ZIP Code Data Service API** provides accurate and comprehensive information about ZIP codes, states, and geographic data for the United States.  
It supports ZIP code validation, distance calculations, and geospatial lookups based on latitude and longitude.

Built with **FastAPI** and **SQLite**, it’s lightweight, fast, and perfect for learning or integrating into data-driven applications.

---

## Live Demo
**Production URL:** [https://us-zip-code-api.vercel.app](https://us-zip-code-api.vercel.app)  
**Interactive Docs:** [https://us-zip-code-api.vercel.app/docs](https://us-zip-code-api.vercel.app/docs)

---

## Features

- Retrieve detailed information about any US ZIP code  
- List all US states (including the District of Columbia)  
-  List all counties for a given state  
- Validate ZIP code existence  
- Calculate distance between ZIP codes or coordinates  
- Find nearby ZIP codes by distance  

---


## 📘 API Summary

### 📍 API Endpoints Overview

| Endpoint | Method | Description |
|-----------|---------|-------------|
| `/zipcode/{zip_code}` | GET | Retrieve detailed information for a specific ZIP code. |
| `/states` | GET | Retrieve a list of all U.S. states including the District of Columbia. |
| `/counties?state={state_name}&page={page_number}` | GET | Retrieve all counties within a given U.S. state. |
| `/zipcode/{zip_code}/validate` | GET | Validate whether a ZIP code exists in the database. |
| `/calculate_distance?latitude1={lat1}&longitude1={lon1}&latitude2={lat2}&longitude2={lon2}` | GET | Calculate distance between two geographic coordinates. |
| `/zipcode_distance?zipcode1={zip1}&zipcode2={zip2}` | GET | Calculate distance between two ZIP codes. |
| `/nearby_location?latitude={lat}&longitude={lon}` | GET | Retrieve nearby ZIP codes based on a given latitude and longitude. |
| `/nearby_zipcodes/{zip_code}` | GET | Retrieve ZIP codes located near the specified ZIP code. |

---

## ⚙️ Tech Stack

| Component | Technology |
|------------|-------------|
| Language | Python 3.11 |
| Framework | FastAPI |
| Database | SQLite (`US_zipcodes.db`) |
| Hosting | Vercel (Serverless) |

---

👨‍💻 Author
[Sreenivasan](https://github.com/Sreenivasan05/US-ZIP-Code-API)

---

📝 License

This project is licensed under the MIT License — feel free to use and modify for educational or personal projects.
