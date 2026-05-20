# 1. Install
#pip install ydata-profiling

# 2. Import
from altair import Config
import pandas as pd
from ydata_profiling import ProfileReport
from kafkamessageapp.configurations.conf import KafkaConfig
# 3. Load your data
df = pd.read_csv(KafkaConfig.pizza_path)

# 4. Generate the report
profile = ProfileReport(
    df,
    title="Pizz Data Profile",
    explorative=True
)

# 5. Save as HTML (opens in browser)
profile.to_file(KafkaConfig.report_path)