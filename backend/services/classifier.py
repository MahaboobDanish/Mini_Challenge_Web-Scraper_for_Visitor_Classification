from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from collections import Counter
import joblib
import random
import nltk
# Initialize NLTK resources
nltk.download('punkt')
nltk.download('stopwords')
stop_words = set(stopwords.words("english"))

# Dummy training data (replace with real dataset for production)
dummy_data = [
    "This article is about technology, covering advancements in tech, gadgets, software, and digital trends.",
    "Content on health and wellness, including life-related news, fitness, nutrition, and mental well-being.",
    "Insights into the stock market, finance tips, personal investment, and global economic news.",
    "Learning resources on education, including academic research, career advice, and online learning materials.",
    "Lifestyle content focusing on fitness, fashion, shopping trends, and well-being routines for daily life.",
    "Exploration and travel-related content, guiding readers on destinations, travel tips, and cultural experiences.",
    "This is related to sports and leisure activities, including both indoor and outdoor hobbies and athletic news.",
    "Entertainment news about movies, anime, TV series, shopping, and recreational outings and events.",
    "Content about food culture, recipes, cuisines from around the world, and unique beverages and dining experiences.",
    "Updates on national and international politics, government activities, elections, and public policies.",
    "Coverage of global business news, economic insights, entrepreneurship, and company developments.",
    "Environmental news on nature, climate issues, pollution, and conservation of Earths natural resources.",
    "Exploring arts and culture, including literature, visual arts, history of paintings, and cultural expressions worldwide.",
    "Gaming content covering online, mobile, and outdoor games, including player communities and related hobbies.",
    "Topics in science and engineering, including developments in mathematics, physics, chemistry, and tech innovation.",
    "Discussions on social issues globally, including societal challenges, cultural perspectives, and humanitarian efforts.",
    "Latest news updates on current events, breaking headlines, official meetings, and major global events."
]

dummy_labels = ['Technology', 'Health', 'Finance', 'Education', 'Lifestyle', 'Travel', 
          'Sports', 'Entertainment', 'Food & Drink', 'Politics', 'Business', 
          'Environment', 'Arts & Culture', 'Gaming', 'Science', 'Social Issues', 'News']

# Initialize the vectorizer and classifier
vectorizer = TfidfVectorizer(stop_words="english")
classifier = MultinomialNB()

# Fit the vectorizer and classifier on the dummy data
X_train = vectorizer.fit_transform(dummy_data)
classifier.fit(X_train, dummy_labels)

# Function to extract meaningful words from the content
def extract_keywords(content):
    words = word_tokenize(content.lower())
    filtered_words = [word for word in words if word not in stop_words and word.isalpha()]
    word_counts = Counter(filtered_words)
    return word_counts.most_common(5)  # Return top 5 most frequent words

# Function to generate dynamic questions and options based on the scraped content
def generate_dynamic_questions(content, predicted_category):
    """Generate questions and options based on the scraped content."""
    
    # Extract keywords and topics from the scraped content
    keywords = extract_keywords(content)
    topics = [keyword[0] for keyword in keywords]
    
    # Define question templates (multiple variants for variety)
    question_templates = [
        "What is your primary reason for visiting {topic} content?",
        "Are you interested in {topic} news/fields?",
        "Are you looking for {topic} tips/planning?",
        "What type of {topic} content are you interested in?",
        "Are you interested in {topic} related?",
        "Would you like to explore {topic} services or resources?",
        "Are you more focused on {topic} or {topic} related?",
        "Which of the following {topic} topics interest you the most?",
        "How would you like to engage with {topic} content?"
    ]
    
    # Randomly select a question template from the list
    selected_question_template = random.choice(question_templates)
    
    # Use the first keyword/topic or fallback to a generic one
    topic = topics[0] if topics else "content"
    
    # Format the selected question with the topic
    question = selected_question_template.format(topic=topic)
    
    # Define options based on predicted category
    options = {
        "Technology": ["Latest tech trends", "Product reviews and unboxings", "Tech tutorials and guides", "Tech news and updates", "Software and app recommendations"],
        "Health": ["Fitness routines and exercises", "Nutrition advice and meal plans", "Mental health tips and resources", "Medical news and breakthroughs", "Healthy living guides"],
        "Finance": ["Stock market trends and insights", "Personal finance management", "Cryptocurrency and blockchain news", "Investment strategies and tips", "Financial planning and budgeting"],
        "Education": ["Online courses and certifications", "Career advice and development", "Research papers and studies", "Learning resources for students", "Study guides and resources"],
        "Lifestyle": ["Fashion trends and styles", "Home decor inspiration", "Personal development resources", "Wellness and fitness trends", "Lifehacks for a better living", "Relationship guides"],
        "Travel": ["Explore new travel destinations", "Travel tips and planning guides", "Booking discounts and promotions", "Adventure travel stories", "Travel blogs and reviews"],
        "Sports": ["Football news and updates", "Basketball game highlights", "Fitness routines for athletes",  "Sports psychology and performance", "Game analysis and predictions",  "Major tournament insights",  "Sports betting tips"],
    "Entertainment": ["Movie reviews and recommendations", "TV shows and series", "Celebrity interviews and news", "Music news and album releases","Streaming platform highlights","Video game reviews", "Upcoming film releases"],
    "Food & Drink": ["Healthy recipes and meal ideas", "Restaurant reviews", "Gourmet cooking tips", "Food trends and innovations", "Wine and cocktail recipes", "Food travel destinations", "Dieting and nutrition advice"],
    "Politics": [
        "Global political analysis", 
        "Election news and forecasts", 
        "Government policies and laws", 
        "International relations", 
        "Political opinions and debates", 
        "Policy proposals and reforms"
    ],
    "Business": [
        "Entrepreneurship tips and resources", 
        "Business news and trends", 
        "Startup advice", 
        "Leadership development", 
        "Marketing and branding", 
        "Sales strategies and tips", 
        "Investment and funding opportunities"
    ],
    "Environment": [
        "Climate change news and updates", 
        "Sustainable living tips", 
        "Environmental conservation", 
        "Wildlife protection efforts", 
        "Green technologies", 
        "Pollution control and clean energy"
    ],
    "Arts & Culture": [
        "Museum exhibitions and art reviews", 
        "Cultural events and festivals", 
        "Art techniques and styles", 
        "Artist interviews and profiles", 
        "Cultural history and heritage", 
        "Literature recommendations"
    ],
    "Gaming": [
        "Video game releases and reviews", 
        "Gaming hardware and technology", 
        "Esports updates and events", 
        "Gaming tutorials and walkthroughs", 
        "Game reviews", 
        "Streaming platforms for gamers"
    ],
    "Science": [
        "Space exploration news", 
        "Scientific research and discoveries", 
        "Biotechnology updates", 
        "Physics theories and advancements", 
        "Environmental science", 
        "Medical research breakthroughs"
    ],
    "Social Issues": [
        "Human rights and activism", 
        "Social justice movements", 
        "Gender equality discussions", 
        "Poverty and homelessness", 
        "Racial justice and diversity", 
        "LGBTQIA+ rights"
    ],
    "News": [
        "Breaking news updates", 
        "Global news and reports", 
        "Local news stories", 
        "Political news", 
        "Economic and financial news", 
        "Health and wellness news"
    ]
    }
    
    # Get options for the predicted category
    category_options = options.get(predicted_category, ["Other"])
    
    return {
        "question": question,
        "options": category_options
    }

# Function to classify content and generate dynamic questions and options
def classify_content(content):
    """Classifies text content and generates dynamic questions and options."""
    
    # Transform the input content into the vectorized form
    X_test = vectorizer.transform([content])
    
    # Predict category based on the transformed content
    predicted_category = classifier.predict(X_test)[0]
    
    # Generate dynamic questions and options based on content
    result = generate_dynamic_questions(content, predicted_category)
    
    # print("****RESULT****", result)
    return result


# Intial Ways

# # from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.model_selection import train_test_split
# from sklearn.datasets import fetch_20newsgroups
# from sklearn.naive_bayes import MultinomialNB
# from sklearn.pipeline import make_pipeline
# import seaborn as sns
# import matplotlib.pyplot as plt
# import pandas as pd
# import re

# # Improved training data (realistic placeholders for production)
# dummy_data = [
#     "Latest advancements in artificial intelligence.",
#     "News on global health and wellness.",
#     "Investing in stocks and personal finance.",
#     "Tech tutorials and coding guides.",
#     "Fitness tips and mental health advice."
# ]

# dummy_labels = [
#     "Technology",
#     "Health",
#     "Finance",
#     "Education",
#     "Lifestyle"
# ]

# # Function to clean text data (removes non-alphanumeric characters and stop words)
# def clean_text(text):
#     text = re.sub(r'\s+', ' ', text)  # Remove extra spaces
#     text = re.sub(r'[^\w\s]', '', text)  # Remove punctuation
#     return text.lower()  # Lowercase the text

# # Prepare the vectorizer and classifier pipeline
# vectorizer = TfidfVectorizer(stop_words="english")
# classifier = MultinomialNB()

# # Preprocessing the training data (cleaning)
# cleaned_data = [clean_text(content) for content in dummy_data]

# # Fit the vectorizer and classifier on the cleaned data
# X_train = vectorizer.fit_transform(cleaned_data)
# classifier.fit(X_train, dummy_labels)

# # Optionally, save the trained model and vectorizer for later use
# # joblib.dump(vectorizer, 'vectorizer.pkl')
# # joblib.dump(classifier, 'classifier.pkl')

# def classify_content(content):
#     """Classifies text content and generates questions and options.

#     Args:
#         content (str): The text content to classify.

#     Returns:
#         dict: Contains questions and multiple-choice options for user categorization.
#     """
#     # Clean the content
#     cleaned_content = clean_text(content)
    
#     # Transform the input content into the vectorized form
#     X_test = vectorizer.transform([cleaned_content])
    
#     # Predict category based on the transformed content
#     predicted_category = classifier.predict(X_test)[0]

#     # Generate dynamic questions and options based on category
#     questions = {
#         "Technology": "What is your primary reason for visiting tech-related content?",
#         "Health": "What aspect of health are you most interested in?",
#         "Finance": "What financial topics would you like to explore?",
#         "Education": "What kind of educational content are you looking for?",
#         "Lifestyle": "Which lifestyle areas are you most interested in?"
#     }

#     options = {
#         "Technology": ["Latest trends in AI", "Tech product reviews", "Programming tutorials", "Tech news and analysis"],
#         "Health": ["Fitness and exercise", "Nutrition and diets", "Mental health", "Medical research news"],
#         "Finance": ["Stock market investments", "Personal finance management", "Cryptocurrency trends", "Investment strategies"],
#         "Education": ["Online courses", "Career development", "University research", "Learning resources and tools"],
#         "Lifestyle": ["Fashion and style", "Health and wellness", "Travel and adventures", "Personal development and growth"]
#     }

#     # Return the generated questions and options based on the classified category
#     return {
#         "questions": questions.get(predicted_category, "What brings you here today?"),
#         "options": options.get(predicted_category, ["Other"])
#     }


# ===============================

# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.naive_bayes import MultinomialNB
# import joblib
# import random

# # Dummy training data (replace with real dataset for production)
# dummy_data = [
#     "This is about tech.",
#     "Health related news.",
#     "Stock market and finance.",
#     "Learning and education.",
#     "Fitness and lifestyle."
# ]

# dummy_labels = [
#     "Technology",
#     "Health",
#     "Finance",
#     "Education",
#     "Lifestyle"
# ]

# # Initialize the vectorizer and classifier
# vectorizer = TfidfVectorizer(stop_words="english")
# classifier = MultinomialNB()

# # Fit the vectorizer and classifier on the dummy data
# X_train = vectorizer.fit_transform(dummy_data)
# classifier.fit(X_train, dummy_labels)

# # Optionally, save the trained model and vectorizer for later use
# # joblib.dump(vectorizer, 'vectorizer.pkl')
# # joblib.dump(classifier, 'classifier.pkl')

# def generate_dynamic_questions_and_options(category):
#     """Generate more dynamic questions and options based on the category."""
#     question_templates = {
#         "Technology": [
#             "What is your primary reason for visiting tech-related content?",
#             "Are you interested in the latest technology trends or product reviews?",
#             "What tech-related topics would you like to explore?"
#         ],
#         "Health": [
#             "Are you interested in health tips or medical news?",
#             "What aspect of health are you looking to explore today?",
#             "Would you like to read about fitness, nutrition, or mental health?"
#         ],
#         "Finance": [
#             "Are you looking for investment tips or financial planning?",
#             "Do you want to learn about stock market trends or personal finance?",
#             "Are you interested in cryptocurrency news or financial advice?"
#         ],
#         "Education": [
#             "What type of educational content are you interested in?",
#             "Are you seeking career advice or research material?",
#             "Would you prefer learning resources or online courses?"
#         ],
#         "Lifestyle": [
#             "Are you interested in lifestyle tips, trends, or wellness?",
#             "Do you want to read about travel, fashion, or home decor?",
#             "Would you like to explore personal development or wellness content?"
#         ]
#     }

#     options_templates = {
#         "Technology": [
#             ["Latest trends", "Product reviews", "Guides", "News"],
#             ["Tech gadgets", "AI innovations", "Programming tutorials", "Startups"],
#             ["Software reviews", "Hardware guides", "Tech news", "Developer tools"]
#         ],
#         "Health": [
#             ["Fitness", "Nutrition", "Mental Health", "Medical News"],
#             ["Yoga", "Exercise routines", "Healthy eating", "Medical breakthroughs"],
#             ["Mental wellness", "Physical health", "Health tips", "Medical news"]
#         ],
#         "Finance": [
#             ["Stock market", "Personal finance", "Cryptocurrency", "Investment tips"],
#             ["Retirement planning", "Savings", "Budgeting", "Investing"],
#             ["Real estate", "Financial independence", "Personal finance", "Crypto investing"]
#         ],
#         "Education": [
#             ["Online courses", "Career advice", "Research", "Learning resources"],
#             ["Higher education", "Job interviews", "Skill development", "Academic research"],
#             ["Workshops", "Certifications", "Internships", "Learning resources"]
#         ],
#         "Lifestyle": [
#             ["Fashion", "Home decor", "Travel", "Personal development"],
#             ["Self-improvement", "Health and wellness", "Leisure", "Creative hobbies"],
#             ["Mindfulness", "Fitness goals", "Work-life balance", "Family and relationships"]
#         ]
#     }

#     # Randomly pick one question and one set of options from the category
#     selected_question = random.choice(question_templates.get(category, ["What brings you here?"]))
#     selected_options = random.choice(options_templates.get(category, [["Other"]]))

#     return {
#         "questions": selected_question,
#         "options": selected_options
#     }

# def classify_content(content):
#     """Classifies text content and generates dynamic questions and options.

#     Args:
#         content (str): The text content to classify.

#     Returns:
#         dict: Contains questions and multiple-choice options for user categorization.
#     """
#     # Transform the input content into the vectorized form
#     X_test = vectorizer.transform([content])
    
#     # Predict category based on the transformed content
#     predicted_category = classifier.predict(X_test)[0]
#     print(f"Predicted Category: {predicted_category}")  # Debug log

#     # Generate dynamic questions and options based on the category
#     questions_and_options = generate_dynamic_questions_and_options(predicted_category)

#     return questions_and_options


# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.naive_bayes import MultinomialNB
# import joblib

# # Dummy training data (replace with real dataset for production)
# dummy_data = [
#     "This is about tech.",
#     "Health related news.",
#     "Stock market and finance.",
#     "Learning and education.",
#     "Fitness and lifestyle."
# ]

# dummy_labels = [
#     "Technology",
#     "Health",
#     "Finance",
#     "Education",
#     "Lifestyle"
# ]

# # Initialize the vectorizer and classifier
# vectorizer = TfidfVectorizer(stop_words="english")
# classifier = MultinomialNB()

# # Fit the vectorizer and classifier on the dummy data
# X_train = vectorizer.fit_transform(dummy_data)
# classifier.fit(X_train, dummy_labels)

# # Optionally, save the trained model and vectorizer for later use
# # joblib.dump(vectorizer, 'vectorizer.pkl')
# # joblib.dump(classifier, 'classifier.pkl')

# def classify_content(content):
#     """Classifies text content and generates questions.

#     Args:
#         content (str): The text content to classify.

#     Returns:
#         dict: Contains questions and multiple-choice options for user categorization.
#     """
#     # Transform the input content into the vectorized form
#     X_test = vectorizer.transform([content])
    
#     # Predict category based on the transformed content
#     predicted_category = classifier.predict(X_test)[0]

#     # Generate dynamic questions and options based on category
#     questions = {
#         "Technology": "What is your primary reason for visiting tech-related content?",
#         "Health": "Are you interested in health tips or medical news?",
#         "Finance": "Are you looking for investment tips or financial planning?",
#         "Education": "What type of educational content are you interested in?",
#         "Lifestyle": "Are you interested in lifestyle tips, trends, or wellness?"
#     }

#     options = {
#         "Technology": ["Latest trends", "Product reviews", "Guides", "News"],
#         "Health": ["Fitness", "Nutrition", "Mental Health", "Medical News"],
#         "Finance": ["Stock market", "Personal finance", "Cryptocurrency", "Investment tips"],
#         "Education": ["Online courses", "Career advice", "Research", "Learning resources"],
#         "Lifestyle": ["Fashion", "Home decor", "Travel", "Personal development"]
#     }

#     return {
#         "questions": questions.get(predicted_category, "What brings you here?"),
#         "options": options.get(predicted_category, ["Other"])
#     }



# To load a pre-trained model and vectorizer (uncomment when needed):
# vectorizer = joblib.load('vectorizer.pkl')
# classifier = joblib.load('classifier.pkl')


# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.naive_bayes import MultinomialNB

# def classify_content(content):
#     """Classifies text content and generates questions.

#     Args:
#         content (str): The text content to classify.

#     Returns:
#         dict: Contains questions and multiple-choice options for user categorization.
#     """

#     # Simulate classification for simplicity

#     categories = ['Technology', 'Health', 'Finance', 'Education', 'Lifestyle']
#     vectorizer = TfidfVectorizer(stop_words="english")
#     classifier = MultinomialNB()

#     # For demonstration purposes only, replace with your actual training dataset
#     dummy_data = ["This is about tech.", "Health related news.", "Stock market and finance.",
#                   "Learning and education.", "Fitness and lifestyle."]
#     dummy_labels = ["Technology", "Health", "Finance", "Education", "Lifestyle"]

#     # Train the classifier
#     X_train = vectorizer.transform(dummy_data)
#     classifier.fit(X_train, dummy_labels)

#     # Predict the category
#     X_test = vectorizer.transform([content])
#     predict_category = classifier.predict(X_test)[0]

#     # Generate dynamic questions and options based on category
#     questions = {
#         "Technology": "What is your primary reason for visiting tech-related content?",
#         "Health": "Are you interested in health tips or medical news?",
#         "Finance": "Are you looking for investment tips or financial planning?",
#         "Education": "What type of educational content are you interested in?",
#         "Lifestyle": "Are you interested in lifestyle tips, trends, or wellness?"
#     }

#     options = {
#         "Technology": ["Latest trends", "Product reviews", "Guides", "News"],
#         "Health": ["Fitness", "Nutrition", "Mental Health", "Medical News"],
#         "Finance": ["Stock market", "Personal finance", "Cryptocurrency", "Investment tips"],
#         "Education": ["Online courses", "Career advice", "Research", "Learning resources"],
#         "Lifestyle": ["Fashion", "Home decor", "Travel", "Personal development"]
#     }

#     return {
#         "questions": questions.get(predict_category, "What brings you here?"),
#         "options": options.get(predict_category, ["Other"])
#     }