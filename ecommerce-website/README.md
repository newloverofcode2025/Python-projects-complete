# Ecommerce Website

This is a simple e-commerce website built using **Flask** (a Python web framework) and **Jinja2** templates. The website allows users to view product details, add items to a cart, and view their cart contents.

## Table of Contents

1. [Features](#features)
2. [Prerequisites](#prerequisites)
3. [Project Structure](#project-structure)
4. [Installation](#installation)
5. [Running the Application](#running-the-application)
6. [Usage](#usage)
7. [Troubleshooting](#troubleshooting)
8. [Contributing](#contributing)
9. [License](#license)

---

## Features

- **Product Detail Page**: Displays product information, including name, description, price, images, and rating.
- **Add to Cart**: Users can add products to their cart.
- **Cart Page**: Displays all items in the cart and calculates the total price.
- **Session-Based Cart**: Cart items are stored temporarily in the session (cleared when the browser is closed).

---

## Prerequisites

Before running this project, ensure you have the following installed:

1. **Python 3.x**: You can download it from [python.org](https://www.python.org/downloads/).
2. **pip**: Python's package installer (usually comes with Python).
3. **A Modern Web Browser**: To view the application.

---

## Project Structure

The project has the following structure:

```
ecommerce-website/
│
├── app.py                  # Main Flask application
├── requirements.txt        # Dependencies
├── static/                 # Static files (CSS, JS, images)
│   └── style.css           # Custom CSS
└── templates/              # Jinja2 templates
    ├── base.html           # Base template
    ├── product_detail.html # Product detail page
    └── cart.html           # Cart page
```

---

## Installation

### Step 1: Clone the Repository

If you have access to the repository, clone it using:

```bash
git clone https://github.com/your-repo/ecommerce-website.git
cd ecommerce-website
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

Open your browser and navigate to:

- **Product Detail Page**: [http://127.0.0.1:5000/](http://127.0.0.1:5000/)
- **Cart Page**: [http://127.0.0.1:5000/cart](http://127.0.0.1:5000/cart)

---

## Usage

### Product Detail Page

1. Visit the homepage (`/`) to view the product details.
2. The page displays:
   - Product name, description, price, and images.
   - Star rating based on the product's rating.
3. Click the "Add to Cart" button to add the product to your cart.

### Cart Page

1. Navigate to `/cart` to view your cart.
2. The cart displays:
   - A list of all items added to the cart.
   - The total price of all items.
3. If the cart is empty, a message will indicate that.

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
- **Placeholder Images**: Placeholder images are sourced from [via.placeholder.com](https://via.placeholder.com/).

---

## Contact

For questions or feedback, feel free to reach out:

- Email: abhishekninja@yahoo.com
- GitHub: [Your GitHub Profile](https://github.com/newloverofcode2025)

---

Save this content as `README.md` in the root of your `ecommerce-website` folder. It provides a comprehensive guide for anyone who wants to use, contribute to, or extend your project. Let me know if you need further assistance!