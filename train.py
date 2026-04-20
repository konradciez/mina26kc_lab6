def load_data():
    print('Loading training data...')

def preprocess_features(df):
   """Normalize numeric features."""
   return (df - df.mean()) / df.std()
