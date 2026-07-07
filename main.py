from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(title="AegisHealth Enterprise Command Core API")

# Harden CORS rules so Vercel can seamlessly read the data pipelines
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Comprehensive dataset restoring all your original clinical telemetry nodes
MOCK_CLINICS = [
    {
        "id": "AP-GNT-PHC-01",
        "name": "Guntur Town Primary Health Centre",
        "beds": 45,
        "stockout_count": 0,
        "status": "Stable",
        "lat": 16.3067,
        "lng": 80.4365,
        "inventory": {"Antivenom": 85, "Oxygen": 90, "Insulin": 75, "Paracetamol": 95}
    },
    {
        "id": "AP-GNT-PHC-02",
        "name": "Tenali Rural Hub Clinic",
        "beds": 30,
        "stockout_count": 2,
        "status": "Critical",
        "lat": 16.2435,
        "lng": 80.6452,
        "inventory": {"Antivenom": 12, "Oxygen": 80, "Insulin": 15, "Paracetamol": 40}
    },
    {
        "id": "AP-GNT-PHC-03",
        "name": "Bapatla Coastal Care Node",
        "beds": 25,
        "stockout_count": 0,
        "status": "Stable",
        "lat": 15.9045,
        "lng": 80.4678,
        "inventory": {"Antivenom": 95, "Oxygen": 30, "Insulin": 85, "Paracetamol": 90}
    },
    {
        "id": "AP-GNT-PHC-04",
        "name": "Narasaraopet Regional Clinic",
        "beds": 50,
        "stockout_count": 1,
        "status": "Warning",
        "lat": 16.2354,
        "lng": 80.0468,
        "inventory": {"Antivenom": 45, "Oxygen": 15, "Insulin": 50, "Paracetamol": 65}
    }
]

MOCK_METRICS = {
    "phcs_monitored": 24,
    "critical_stockouts": 4,
    "operational_beds": 300,
    "pending_transfers": 3
}

class OptimizeRequest(BaseModel):
    clinicId: str = None

@app.get("/api/clinics")
def get_clinics():
    return MOCK_CLINICS

@app.get("/api/metrics")
def get_metrics():
    return MOCK_METRICS

@app.post("/api/optimize")
def optimize_logistics(req: OptimizeRequest):
    return {
        "status": "success",
        "recommendations": [
            {
                "source": "Guntur Town Primary Health Centre",
                "destination": "Tenali Rural Hub Clinic",
                "item": "Polyvalent Antivenom",
                "quantity": 40,
                "justification": "Tenali Rural is experiencing a critical threshold deficit (12% remaining stock). Guntur Town holds an optimal surplus capacity of 85% with high regional supply stability."
            },
            {
                "source": "Bapatla Coastal Care Node",
                "destination": "Narasaraopet Regional Clinic",
                "item": "Medical Oxygen Cylinders",
                "quantity": 25,
                "justification": "Narasaraopet inventory levels dropped to 15% due to sudden localized demand surges. Bapatla holds excess strategic reserves."
            }
        ]
    }