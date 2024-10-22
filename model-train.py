import cv2
import os
import pickle

dataset_path = 'dataset'
features_file = 'features.pkl'
names_file = 'names.pkl'

# Initialize ORB detector
orb = cv2.ORB_create()

def extract_features():
    all_features = []
    all_names = []

    # Iterate over all images in the dataset folder
    for file in os.listdir(dataset_path):
        if file.endswith(".jpg"):
            img_path = os.path.join(dataset_path, file)
            img = cv2.imread(img_path, 0)  # Load in grayscale
            keypoints, descriptors = orb.detectAndCompute(img, None)

            if descriptors is not None:
                all_features.append(descriptors)
                all_names.append(file.split('_')[0])  # Extract user name from the file

    # Save features and names using pickle
    with open(features_file, 'wb') as f:
        pickle.dump(all_features, f)
    with open(names_file, 'wb') as f:
        pickle.dump(all_names, f)

    print("Features and names saved successfully.")

# Call the function to extract features
extract_features()



