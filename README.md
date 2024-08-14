# Multi-Purpose Image , PDF & Other Tools
## Table of Contents
- [Overview](#-overview)
- [Features](#%EF%B8%8F-features)
- [Libraries-Used](#-libraries-used)
- [Project-Structure](#%EF%B8%8F-project-structure)
- [Getting-Start](#-getting-started)
- [Authentication](#-authentication)
- [Image-Processing](#%EF%B8%8F-image-processing)
- [Message-System](#-messaging-system)
- [Contribution](#-contributing)
- [License](#-license)
- [Author](#-author)
- [Contact](#-contact)
  
## 🚀 Overview

This repository contains a Python-based web application built with Streamlit. It offers various functionalities related to image processing and PDF manipulation, with additional features for authenticated users.

## 🛠️ Features

- 🔐 User Authentication
- 🖼️ Background Removal from Images
- 📄 Image to PDF Conversion
- 💬 Messaging System (for authenticated users)

## 📚 Libraries Used

- [Streamlit](https://streamlit.io/): For creating the web application interface
- [Pillow (PIL)](https://python-pillow.org/): For image processing
- [rembg](https://github.com/danielgatis/rembg): For background removal
- [PyPDF2](https://pypdf2.readthedocs.io/): For PDF manipulation
- [pandas](https://pandas.pydata.org/): For data handling

## 🏗️ Project Structure
```
├── an.py
├── requirements.txt
|── userdata.txt
|── newuserdata.txt
├── ant/
│   ├── CJ_image/
│   ├── DNC_image/
│   ├── ML_image/
│   ├── PL_image/
│   ├── RDBMS_image/
│   ├── SE_image/
│   ├── SMM_image/
│   ├── csv/
│   ├── excel/
│   ├── mp3f/
│   ├── mp4f/
│   ├── pdf/
│   ├── text/
│   ├── zip_folder/
│   ├── answer.txt
│   ├── code.txt
│   ├── message.txt
│   └── question.txt
└── README.md
```
## 🚀 Getting Started

1. Clone this repository:
```sh
git clone https://github.com/deepanshu414/benefittool.git
```
2. Navigate to the project directory:
```sh
cd benefittool
```
3. Install the required dependencies:
```sh
pip install -r requirements.txt
```
4. Run the Streamlit app:
```sh
streamlit run an.py
```

## 🔑 Authentication

The app features a login system:
- Specific users have access to all features
- Non-authenticated users can only access background removal and image-to-PDF conversion

## 🖼️ Image Processing

### Background Removal
Upload an image, and the app will remove its background using the `rembg` library.

### Image to PDF Conversion
Convert uploaded images to PDF format.

## 💬 Messaging System

Authenticated users can access a messaging section to send and receive messages.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check [issues page](https://github.com/deepanshu414/benefittool/issues).

## 📝 License

This project is licensed under the GPL License - see the [LICENSE](LICENSE) file for details.


## 👨‍💻 Author

Your Name
- GitHub: [@deepanshu414](https://github.com/deepanshu414)
- LinkedIn: [deepanshu](https://www.linkedin.com/in/deepanshu-antil-865508263/)

## 📞 Contact
If you have any questions or suggestions, please open an issue or contact the repository owner.

Happy Tools! 🎉



