import csv

# Your exact data (copied from your message)
data = """text,actual_sentiment
"Just tried the new iPhone, it is absolutely fire! 🔥",POSITIVE
"The Netflix was delayed for 3 hours. Never using them again.",NEGATIVE
"Does anyone know if the Uber is open on Sundays?",NEUTRAL
"I am so impressed with the Amazon Delivery today. Highly recommend!",POSITIVE
"The update is okay, nothing special but it gets the job done.",NEUTRAL
"Avoid this Coffee Machine at all costs. It broke after two days.",NEGATIVE
"Finally, a Skincare Kit that actually works as advertised. Super happy. 😊",POSITIVE
"Comparing the specs between this Laptop and the older version.",NEUTRAL
"I've been on hold for an hour. This Airlines is a joke.",NEGATIVE
"Loving the new update! Everything feels so much smoother now. ✨",POSITIVE
"The customer support for Local Gym is the best I have ever experienced.",POSITIVE
"I'm so frustrated with this Electric Scooter. Total waste of money. 😡",NEGATIVE
"Just saw the news about the new Netflix release.",NEUTRAL
"The Uber is okay, nothing special but it gets the job done.",NEUTRAL
"Terrible experience with the latest update. It keeps crashing. 📉",NEGATIVE
"Just tried the new Coffee Machine, it is absolutely fire! 🔥",POSITIVE
"I am so impressed with the Amazon Delivery today. Highly recommend!",POSITIVE
"Avoid this iPhone at all costs. It broke after two days.",NEGATIVE
"Comparing the specs between this Electric Scooter and the older version.",NEUTRAL
"The Airlines was delayed for 3 hours. Never using them again.",NEGATIVE
"Finally, a Laptop that actually works as advertised. Super happy. 😊",POSITIVE
"Does anyone know if the Local Gym is open on Sundays?",NEUTRAL
"I've been on hold for an hour. This Netflix is a joke.",NEGATIVE
"Just saw the news about the new Skincare Kit release.",NEUTRAL
"The update is okay, nothing special but it gets the job done.",NEUTRAL
"Just tried the new Coffee Machine, it is absolutely fire! 🔥",POSITIVE
"The customer support for Amazon Delivery is the best I have ever experienced.",POSITIVE
"Avoid this Electric Scooter at all costs. It broke after two days.",NEGATIVE
"Reading the manual for my new Laptop right now.",NEUTRAL
"I am so impressed with the Airlines today. Highly recommend!",POSITIVE
"I'm so frustrated with this iPhone. Total waste of money. 😡",NEGATIVE
"The Uber was delayed for 3 hours. Never using them again.",NEGATIVE
"Finally, a Coffee Machine that actually works as advertised. Super happy. 😊",POSITIVE
"Comparing the specs between this Skincare Kit and the older version.",NEUTRAL
"The customer support for Netflix is the best I have ever experienced.",POSITIVE
"Just saw the news about the new Laptop release.",NEUTRAL
"The update is okay, nothing special but it gets the job done.",NEUTRAL
"Avoid this Electric Scooter at all costs. It broke after two days.",NEGATIVE
"Loving the new update! Everything feels so much smoother now. ✨",POSITIVE
"I am so impressed with the Amazon Delivery today. Highly recommend!",POSITIVE
"I've been on hold for an hour. This Airlines is a joke.",NEGATIVE
"Reading the manual for my new iPhone right now.",NEUTRAL
"Does anyone know if the Local Gym is open on Sundays?",NEUTRAL
"The Netflix is okay, nothing special but it gets the job done.",NEUTRAL
"Just tried the new Laptop, it is absolutely fire! 🔥",POSITIVE
"Terrible experience with the latest update. It keeps crashing. 📉",NEGATIVE
"Avoid this Coffee Machine at all costs. It broke after two days.",NEGATIVE
"Finally, a Skincare Kit that actually works as advertised. Super happy. 😊",POSITIVE
"Comparing the specs between this Electric Scooter and the older version.",NEUTRAL
"The customer support for Uber is the best I have ever experienced.",POSITIVE
"I'm so frustrated with this iPhone. Total waste of money. 😡",NEGATIVE
"Just saw the news about the new Netflix release.",NEUTRAL
"The update is okay, nothing special but it gets the job done.",NEUTRAL
"I am so impressed with the Amazon Delivery today. Highly recommend!",POSITIVE
"Loving the new update! Everything feels so much smoother now. ✨",POSITIVE
"The Airlines was delayed for 3 hours. Never using them again.",NEGATIVE
"I've been on hold for an hour. This Local Gym is a joke.",NEGATIVE
"Reading the manual for my new Laptop right now.",NEUTRAL
"Comparing the specs between this Coffee Machine and the older version.",NEUTRAL
"Just tried the new Skincare Kit, it is absolutely fire! 🔥",POSITIVE
"Avoid this Electric Scooter at all costs. It broke after two days.",NEGATIVE
"Finally, a iPhone that actually works as advertised. Super happy. 😊",POSITIVE
"The customer support for Uber is the best I have ever experienced.",POSITIVE
"Just saw the news about the new Netflix release.",NEUTRAL
"The update is okay, nothing special but it gets the job done.",NEUTRAL
"I am so impressed with the Amazon Delivery today. Highly recommend!",POSITIVE
"I'm so frustrated with this Coffee Machine. Total waste of money. 😡",NEGATIVE
"The Airlines was delayed for 3 hours. Never using them again.",NEGATIVE
"Terrible experience with the latest update. It keeps crashing. 📉",NEGATIVE
"Loving the new update! Everything feels so much smoother now. ✨",POSITIVE
"Reading the manual for my new Laptop right now.",NEUTRAL
"Does anyone know if the Local Gym is open on Sundays?",NEUTRAL
"Just tried the new Electric Scooter, it is absolutely fire! 🔥",POSITIVE
"I've been on hold for an hour. This Netflix is a joke.",NEGATIVE
"Avoid this iPhone at all costs. It broke after two days.",NEGATIVE
"Finally, a Skincare Kit that actually works as advertised. Super happy. 😊",POSITIVE
"The customer support for Uber is the best I have ever experienced.",POSITIVE
"Comparing the specs between this Coffee Machine and the older version.",NEUTRAL
"Just saw the news about the new Amazon Delivery release.",NEUTRAL
"The update is okay, nothing special but it gets the job done.",NEUTRAL
"I am so impressed with the Airlines today. Highly recommend!",POSITIVE
"I'm so frustrated with this Laptop. Total waste of money. 😡",NEGATIVE
"The Netflix was delayed for 3 hours. Never using them again.",NEGATIVE
"Avoid this Skincare Kit at all costs. It broke after two days.",NEGATIVE
"Loving the new update! Everything feels so much smoother now. ✨",POSITIVE
"Just tried the new iPhone, it is absolutely fire! 🔥",POSITIVE
"Reading the manual for my new Electric Scooter right now.",NEUTRAL
"Does anyone know if the Local Gym is open on Sundays?",NEUTRAL
"The Uber is okay, nothing special but it gets the job done.",NEUTRAL
"Terrible experience with the latest update. It keeps crashing. 📉",NEGATIVE
"Finally, a Coffee Machine that actually works as advertised. Super happy. 😊",POSITIVE
"I am so impressed with the Amazon Delivery today. Highly recommend!",POSITIVE
"I've been on hold for an hour. This Airlines is a joke.",NEGATIVE
"Comparing the specs between this Laptop and the older version.",NEUTRAL
"Just saw the news about the new Skincare Kit release.",NEUTRAL
"The update is okay, nothing special but it gets the job done.",NEUTRAL
"Avoid this Electric Scooter at all costs. It broke after two days.",NEGATIVE
"The customer support for Netflix is the best I have ever experienced.",POSITIVE
"Loving the new update! Everything feels so much smoother now. ✨",POSITIVE
"Just tried the new iPhone, it is absolutely fire! 🔥",POSITIVE"""

# Split into lines and parse
lines = data.strip().split('\n')
rows = []

for line in lines[1:]:  # Skip header
    if ',' in line:
        text_part, sentiment = line.split(',', 1)
        # Handle quotes properly
        text = text_part.strip().strip('"')
        sentiment = sentiment.strip().strip('"')
        rows.append([text, sentiment])

# Write to CSV
with open('sentiment_dataset.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['text', 'actual_sentiment'])
    writer.writerows(rows)

print(f"✅ Created 'sentiment_dataset.csv' with {len(rows)} rows!")
print("File ready for your ML projects!")
