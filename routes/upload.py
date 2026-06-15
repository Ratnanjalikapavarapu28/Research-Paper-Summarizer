import os
import uuid

def save_uploaded_files(uploaded_files):

    os.makedirs("uploads", exist_ok=True)

    saved_paths = []

    for file in uploaded_files:

        unique_name = f"{uuid.uuid4()}_{file.name}"
        path = os.path.join("uploads", unique_name)

        with open(path, "wb") as f:
            f.write(file.getbuffer())

        saved_paths.append(path)

    return saved_paths