sales-analytics-engine/

data/
    orders.csv

analytics/

    reader.py
        Read CSV lazily.

    models.py
        Define the Order model.

    transforms.py
        Convert raw CSV rows into Order objects.

    filters.py
        Reusable filtering functions.

    reports.py
        Analytics and report generation.

main.py
        Application entry point.

README.md
requirements.txt