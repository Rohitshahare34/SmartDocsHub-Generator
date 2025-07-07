# SmartDocsHubApp 🚀

![Django](https://img.shields.io/badge/Django-5.1.7-green?logo=django)
![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Status](https://img.shields.io/badge/status-active-brightgreen)

Welcome to **SmartDocsHubApp** – a simple solution for generating, previewing, and downloading digital certificates, invitations, letters, and reports as PDFs. Users just fill out a form for each document type and instantly get a professional PDF download—no CSV or Excel upload required.

---

## 🎬 Demo Video

[![Watch the demo]()

_

---

## ✨ Key Features

| Feature                        | Description                                                      |
|--------------------------------|------------------------------------------------------------------|
| 📝 Easy Form Input             | Fill out a simple form for each document type                     |
| 🖼️ Custom Templates           | Choose from multiple beautiful templates for each document        |
| 📄 PDF Generation              | Instantly download high-quality PDF documents                     |
| 👀 Live Preview                | See a real-time preview before downloading                        |
| 🔒 Secure & Private            | Your data stays local and is not stored                           |

---



## 🚀 Quick Start

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/SmartDocsHubApp.git
   cd SmartDocsHubApp
   ```
2. **Create a virtual environment**
   ```bash
   python -m venv venv
   venv\Scripts\activate  # On Windows
   ```
3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
4. **Configure environment variables**
   - Copy `.env.example` to `.env` and fill in your secrets (if needed)
5. **Run migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
6. **Create a superuser**
   ```bash
   python manage.py createsuperuser
   ```
7. **Start the development server**
   ```bash
   python manage.py runserver
   ```
8. **Open in your browser**
   - http://127.0.0.1:8000/

---

## 📂 Project Structure

```
SmartDocsHubApp/
├── manage.py
├── requirements.txt
├── .env
├── SmartDocsHub/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── SmartDocsHubApp/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── migrations/
│   └── templates/
├── media/
├── static/
├── templates/
│   └── SmartDocsHubApp/
│       ├── base.html
│       ├── home.html
│       ├── certificate_page.html
│       ├── invitation.html
│       ├── letter.html
│       └── report.html
└── venv/
```

---

## 💡 Usage

- Go to the section for Certificate, Invitation, Letter, or Report.
- Fill out the form with the required details.
- Preview your document live.
- Click the download button to get your PDF instantly.

---

## 🤝 Contributing

We welcome contributions! To get started:
1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 🌐 GitHub Repository

[SmartDocsHubApp on GitHub](https://github.com/your-username/SmartDocsHubApp) <!-- Replace with your actual repo link --> 