# ShareBin

ShareBin is a simple file-sharing web application that allows users to upload files and receive a unique code to download them later. Files automatically expire after **24 hours** to ensure security and prevent storage clutter.

## Features

- 📂 **Upload Files**: Drag and drop or select files manually.
- 🔑 **Unique Code**: Each upload generates a unique code for downloading.
- 📥 **Download Files**: Enter the unique code to retrieve your file.
- ⏳ **Auto-Delete**: Files are deleted after 24 hours.

---

## Screenshots

_Upload files easily with the drag-and-drop feature._

_Enter the unique code to download your file._

---

## Installation

### **1. Clone the Repository**

```bash
git clone https://github.com/calvincandiec137/ShareBinV2.git
cd ShareBinV2
```

### **2. Set Up a Virtual Environment (Optional but Recommended)**

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

### **3. Install Dependencies**

```bash
pip install -r requirements.txt
```

### **4. Configure the Database**

Create a MySQL database and update your `db.env` file with the correct credentials:

```
DB_HOST=localhost
DB_USER=fileUser
DB_PASSWORD=share_user
DB_NAME=sharebin
```

Then, create the required table:

```sql
CREATE TABLE files (
    code VARCHAR(8) PRIMARY KEY,
    file_path TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

---

## Running the Application

```bash
streamlit run app.py
```

This will start the web app, and you can access it in your browser at `http://localhost:8501`.

---

## Auto-Delete Old Files

To remove files after 24 hours, a cleanup script is included.

### **Run Cleanup Manually**

```bash
python cleanup.py
```

## Contributing

Pull requests are welcome! If you find issues or have suggestions, feel free to open an issue.

---

## License

![MIT License](https://img.shields.io/badge/License-MIT-blue.svg)
