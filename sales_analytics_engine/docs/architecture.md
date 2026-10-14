sales-analytics-engine/

├── data/
│   └── orders.csv
│
├── analytics/
│   ├── __init__.py
│   ├── reader.py
│   ├── models.py
│   ├── transforms.py
│   ├── filters.py
│   └── reports.py
│
├── main.py
├── requirements.txt
└── README.md



Future Responsibility of Each Module

| File | Responsibility |
|------|----------------|
| `reader.py` | Stream rows from CSV using generators |
| `models.py` | Define the `Order` data model |
| `transforms.py` | Convert raw CSV rows into `Order` objects |
| `filters.py` | Reusable filtering functions |
| `reports.py` | Business calculations and reporting |
| `main.py` | Wire everything together |

Each module has one responsibility, following the Single Responsibility Principle.