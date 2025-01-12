# Vision Search Backend

## v1

Image search works as follows:

- User could query by image
- For image query:
    - User sends an image to the backend
    - Backend extracts features from the image
        - resize the image to a fixed size
        - extract features using a pre-trained model
        - normalize the features
    - Backend searches the database for images with similar features
        - vector similarity search
    - Backend returns the results to the user

## v2

- User could query by text or image
- For text query:
    - User sends a text query to the backend
    - Backend searches the database for the text query
        - Full text search for metadata fields
        - Full text search for tags
    - Backend returns the results to the user
- For image query:
    - User sends an image to the backend
    - Backend extracts features from the image
        - resize the image to a fixed size
        - extract features using a pre-trained model
        - normalize the features
    - Backend searches the database for images with similar features
        - vector similarity search
    - Backend returns the results to the user
