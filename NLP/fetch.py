
import os

# Define the path to the "tekstit" folder in your working directory
folder_path = "NLP/corpora"

# Get a list of all subfolders (corpora) in the "tekstit" folder
corpora = [f for f in os.listdir(folder_path) if os.path.isdir(os.path.join(folder_path, f))]

# Iterate through each corpus folder and read its content
for corpus_name in corpora:
    # Define the path to the current corpus folder
    corpus_folder_path = os.path.join(folder_path, corpus_name)
    
    # Initialize a list to store the content of the corpus
    corpus_content = []
    
    # Iterate through the files in the corpus folder
    for filename in os.listdir(corpus_folder_path):
        file_path = os.path.join(corpus_folder_path, filename)
        
        # Read the content of each file and append it to the corpus_content list
        with open(file_path, 'r', encoding='utf-8') as file:
            file_content = file.read()
            corpus_content.append(file_content)

return corpus_content
return corpus_name # TARTTEEKS TÄTÄ EMMÄÄ TIIÄ JA JOS TARVII NII MITEN TÄÄ LAITETAA