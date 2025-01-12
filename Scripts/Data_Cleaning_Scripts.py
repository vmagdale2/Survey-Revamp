import pandas as pd

# Define file path

# Load file path

# Standardize column names

# Convert data types

# Create new tables & columns for 3NF normalization


import os
import pandas as pd

from google.cloud import bigquery

project_id = "UNDISCLOSED"
client = bigquery.Client(project=project_id)

dataset_id = "Mercedes_Survey"
table_names = [
    "EL_Ratings",
    "Event_Int_Ratings",
    "Event_Interests",
    "NS_Ratings",
    "OCE_Ratings",
    "PEI_Ratings",
    "Respondent",
    "Survey_Response"
]

dfs = {}

for table_name in table_names:
    table_full_name = f"{project_id}.{dataset_id}.{table_name}"
    print(f"Loading table {table_full_name}...")

    query = f"SELECT * FROM `{table_full_name}`"
    df = client.query(query).to_dataframe()

    # Store DataFrame in a dictionary
    dfs[table_name] = df

print("All tables loaded into dataframes successfully!")

survey_df = dfs["Survey_Response"]  # the Survey_Response DataFrame

rename_map = {
    "Name": "Name",
    "Company": "Company",
    "Job Title": "Job Title",
    "How would you rate the overall conference experience?": "Overall_Conf_Exp",
    "Were the presentations engaging and informative?": "Pres_Eng_Inf",
    "Which presentations / speakers did you find particularly insightful or engaging?": "Insigh_Speakers",
    "Any topics or areas which you wished had been covered during the summit but were not?": "Miss_Topics",
    "How satisfied are you with the networking opportunities provided?": "Netw_Satisf",
    "Any suggestions for us to improve your networking experience?": "Netw_Sugg",
    "How would you rate the conference venue and facilities?": "Eval_Logistics",
    "What areas could be improved for future conferences?": "Feed_Fut_Confs",
    "3rd European Green Steel Summit 2025 (Mar. 25-26 | Germany)": "Interest_Ev_1",
    "3rd China Green Steel Summit 2024 (Nov. 21-22 | Shanghai, China)": "Interest_Ev_2",
    "2nd European Green Aluminium Summit 2024 (Nov. 20-21 | Frankfurt, Germany)": "Interest_Ev_3",
    "Do you have any other suggested event theme(s) for the organizer?": "Cont_Ideation",
    "Any other comments or suggestions?": "Gen_Feed"
}

survey_df = survey_df.rename(columns=rename_map)

dfs["Survey_Response"] = survey_df

print("\nColumn names standardized for Survey_Response table.")
print("New column names:", list(survey_df.columns))

survey_df["Name"] = survey_df["Name"].astype(str)
survey_df["Company"] = survey_df["Company"].astype(str)
survey_df["Job Title"] = survey_df["Job Title"].astype(str)
survey_df["Insigh_Speakers"] = survey_df["Insigh_Speakers"].astype(str)
survey_df["Miss_Topics"] = survey_df["Miss_Topics"].astype(str)
survey_df["Netw_Sugg"] = survey_df["Netw_Sugg"].astype(str)
survey_df["Feed_Fut_Confs"] = survey_df["Feed_Fut_Confs"].astype(str)
survey_df["Cont_Ideation"] = survey_df["Cont_Ideation"].astype(str)
survey_df["Gen_Feed"] = survey_df["Gen_Feed"].astype(str)

for col in ["Overall_Conf_Exp", "Pres_Eng_Inf", "Netw_Satisf", "Eval_Logistics"]:
    if col in survey_df.columns:
        # Convert to float or int as appropriate
        survey_df[col] = pd.to_numeric(survey_df[col], errors="coerce")

for col in ["Interest_Ev_1", "Interest_Ev_2", "Interest_Ev_3"]:
    if col in survey_df.columns:
        # Here we assume "Yes"/"No" or "True"/"False" type entries
        # Adjust as needed for your actual data
        survey_df[col] = survey_df[col].astype(str).str.lower().map(
            {"true": True, "false": False, "yes": True, "no": False}
        )
dfs["Survey_Response"] = survey_df

print("\nData types converted for Survey_Response table:")
print(survey_df.dtypes)