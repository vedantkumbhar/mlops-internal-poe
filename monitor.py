import pandas as pd
from evidently import Report
from evidently.presets import DataDriftPreset

reference_data = pd.DataFrame({
    "input_value": [10, 12, 11, 13, 12, 14, 10, 11]
})

current_data = pd.DataFrame({
    "input_value": [20, 22, 21, 23, 25, 24, 22, 21]
})

report = Report([
    DataDriftPreset()
])

result = report.run(
    reference_data,
    current_data
)

result.save_html("evidently_report.html")

print("Evidently monitoring completed.")
print("Report saved as evidently_report.html")