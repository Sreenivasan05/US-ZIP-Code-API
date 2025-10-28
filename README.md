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

| Endpoint | Method | Description |
|-----------|---------|-------------|
| `/zipcode/{zip_code}` | GET | Retrieve ZIP code information |
| `/states` | GET | List all US states |
| `/counties/{state}` | GET | List counties for a state |
| `/validate/{zip_code}` | GET | Validate a ZIP code |
| `/distance` | GET | Calculate distance between ZIPs or coordinates |
| `/nearby` | GET | Find nearby ZIP codes |

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
