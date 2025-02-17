# Meeting Assistant

A **modern, dark-themed, responsive web application** built using Flask to help users create and manage meeting agendas, details, participants, and summaries. The app is lightweight, easy to use, and designed with a sleek UI for both desktop and mobile devices.

---

## Table of Contents

1. [Features](#features)
2. [Prerequisites](#prerequisites)
3. [Project Structure](#project-structure)
4. [Installation](#installation)
5. [Running the Application](#running-the-application)
6. [Usage](#usage)
7. [Screenshots](#screenshots)
8. [Troubleshooting](#troubleshooting)
9. [Contributing](#contributing)
10. [License](#license)

---

## Features

- **Agenda Creation**:
  - Add agenda items.
  - Remove agenda items.
  - Reorder agenda items (via up/down buttons).

- **Meeting Details**:
  - Input meeting title, date, time, and location.

- **Participants Management**:
  - Add and remove participants.

- **Meeting Summary**:
  - View all meeting details, agenda items, and participants in one place.

- **Dark Theme**:
  - Modern, dark-themed UI with clean typography and subtle animations.

- **Responsive Design**:
  - Fully responsive layout for mobile, tablet, and desktop.

- **Session-Based Storage**:
  - Temporary storage of meeting data in session variables.

---

## Prerequisites

Before running this project, ensure you have the following installed:

1. **Python 3.x**: Download it from [python.org](https://www.python.org/downloads/).
2. **pip**: Python's package installer (usually comes with Python).
3. **A Modern Web Browser**: To view the application.

---

## Project Structure

The project has the following structure:

```
meeting-assistant/
│
├── app.py                  # Main Flask application
├── requirements.txt        # Dependencies
├── static/                 # Static files (CSS)
│   └── style.css           # Custom CSS
└── templates/              # Jinja2 templates
    ├── base.html           # Base template
    ├── agenda.html         # Agenda creation page
    ├── meeting_details.html # Meeting details page
    ├── participants.html   # Participants management page
    └── summary.html        # Meeting summary page
```

---

## Installation

### Step 1: Clone the Repository

If you have access to the repository, clone it using:

```bash
git clone https://github.com/your-repo/meeting-assistant.git
cd meeting-assistant
```

If you don't have access to a repository, manually create the folder structure and copy the files as described in the [Project Structure](#project-structure) section.

### Step 2: Install Dependencies

Install the required Python packages by running:

```bash
pip install -r requirements.txt
```

This will install Flask, which is the only dependency for this project.

---

## Running the Application

### Step 1: Start the Flask Server

Run the Flask application using the following command:

```bash
python app.py
```

By default, the app will run on `http://127.0.0.1:5000/`.

### Step 2: Access the Application

Open your browser and navigate to the following pages:

- **Agenda Creation**: [http://127.0.0.1:5000/](http://127.0.0.1:5000/)
- **Meeting Details**: [http://127.0.0.1:5000/meeting_details](http://127.0.0.1:5000/meeting_details)
- **Participants Management**: [http://127.0.0.1:5000/participants](http://127.0.0.1:5000/participants)
- **Meeting Summary**: [http://127.0.0.1:5000/summary](http://127.0.0.1:5000/summary)

---

## Usage

### Agenda Creation

1. Visit the homepage (`/`) to view the agenda creation page.
2. Add agenda items using the input field and "Add Item" button.
3. Remove or reorder agenda items as needed.

### Meeting Details

1. Navigate to `/meeting_details` to input meeting details.
2. Enter the meeting title, date, time, and location.
3. Save the details to store them temporarily.

### Participants Management

1. Navigate to `/participants` to manage participants.
2. Add participants using the input field and "Add Participant" button.
3. Remove participants as needed.

### Meeting Summary

1. Navigate to `/summary` to view a summary of the meeting.
2. The summary includes all meeting details, agenda items, and participants.

---

## Screenshots

### Agenda Creation Page
![Agenda Creation](https://via.placeholder.com/800x400?text=Agenda+Creation+Page)

### Meeting Details Page
![Meeting Details](https://via.placeholder.com/800x400?text=Meeting+Details+Page)

### Participants Management Page
![Participants Management](https://via.placeholder.com/800x400?text=Participants+Management+Page)

### Meeting Summary Page
![Meeting Summary](https://via.placeholder.com/800x400?text=Meeting+Summary+Page)

---

## Troubleshooting

### 1. Blank Page or Missing Content

- **Check Terminal Logs**: Look for any errors in the terminal where you ran `python app.py`.
- **Verify File Structure**: Ensure all `.html` files are in the `templates` folder and `style.css` is in the `static` folder.
- **Browser Console**: Open the browser's developer tools (`F12`) and check the **Console** and **Network** tabs for errors.

### 2. CSS Not Loading

- Ensure the `static` folder exists and contains `style.css`.
- Verify the `<link>` tag in `base.html` points to the correct CSS file:
  ```html
  <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
  ```

### 3. Python Errors

- Common issues include:
  - Indentation errors in `app.py`.
  - Missing dependencies (run `pip install -r requirements.txt` again).
- Fix any errors reported in the terminal.

---

## Contributing

We welcome contributions! Here’s how you can help:

1. **Fork the Repository**: Create a fork of this project on GitHub.
2. **Clone Your Fork**: Clone your forked repository to your local machine.
3. **Create a Branch**: Create a new branch for your changes:
   ```bash
   git checkout -b feature/your-feature-name
   ```
4. **Make Changes**: Add or modify files as needed.
5. **Test Locally**: Ensure your changes work by running the application locally.
6. **Submit a Pull Request**: Push your changes to GitHub and submit a pull request.

---

## License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

- **Flask**: The lightweight Python web framework used to build this application.
- **Jinja2**: The templating engine used for rendering HTML pages.
- **CSS Flexbox/Grid**: Used for creating a responsive and modern layout.

---

## Contact

For questions or feedback, feel free to reach out:

- Email: abhishekninja@yahoo.com
- GitHub: [Your GitHub Profile](https://github.com/newloverofcode2025)

---

Save this content as `README.md` in the root of your `meeting-assistant` folder. It provides a comprehensive guide for anyone who wants to use, contribute to, or extend your project. Let me know if you need further assistance!