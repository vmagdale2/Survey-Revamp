dataset_table = "UPDATE WITH TABLE"

query = f"""
SELECT
  Gen_Feed # UPDATE WITH COLUMN
FROM
  `{project_id}.{dataset_table}`
WHERE
  Gen_Feed IS NOT NULL # UPDATE WITH SAME COLUMN
"""

query_job = client.query(query)
results = query_job.result()

responses = [row.Gen_Feed for row in results] # UPDATE WITH SAME COLUMN
text_data = " ".join(responses)

wordcloud = WordCloud(
    width=800,
    height=400,
    background_color="white",
    stopwords=None
).generate(text_data)

# Plot the word cloud
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.title("Word Cloud for [Insert Topic Here]", fontsize=20) # UPDATE WITH TOPIC
plt.show()