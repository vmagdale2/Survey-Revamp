# Sentiment Analysis for the Overall Conference Experience Survey Question
query = """
WITH SentimentMapping AS (
    SELECT
        sr.Overall_Conf_Exp AS ResponseValue, # UPDATE WITH NEW COLUMN
        CASE
            WHEN r.ConfExpID = 1 OR r.ConfExpID = 2  THEN 'Positive'
            WHEN r.ConfExpID = 4 or r.ConfExpID = 3 THEN 'Neutral'
            WHEN r.ConfExpID = 5 THEN 'Negative'
        END AS Sentiment
    FROM
        `sunlit-apricot-433319-h3.Mercedes_Survey.Survey_Response` sr
    JOIN
        `sunlit-apricot-433319-h3.Mercedes_Survey.OCE_Ratings` r
    ON
        sr.Overall_Conf_Exp = r.ConfExpID # UPDATE WITH NEW COLUMN
)
SELECT
    Sentiment,
    COUNT(*) AS Count
FROM
    SentimentMapping
GROUP BY
    Sentiment
ORDER BY
    Count DESC
"""

# Run the query
query_job = client.query(query)

# Fetch results
results = query_job.result()

# Extract data for visualization
sentiments = []
counts = []
for row in results:
    sentiments.append(row.Sentiment)
    counts.append(row.Count)

# Create the bar chart
plt.figure(figsize=(8, 5))
plt.bar(sentiments, counts)
plt.title("Overall Conference Experience", fontsize=16)
plt.xlabel("Sentiment", fontsize=14)
plt.ylabel("Count", fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

# Add data labels on bars
for i, count in enumerate(counts):
    plt.text(i, count + 1, str(count), ha='center', fontsize=12)

# Show the chart
plt.tight_layout()
plt.show()

# Sentiment Analysis for the Engaging and Informative Survey Question