# Project Overview

This is a Flask-based web application for "Redline.service", a company that provides repair services for computers, appliances, and cars. The application serves as a public-facing website with information about the company's services, an about us page, a video gallery, and a contact form.

## Main Technologies

*   **Backend:** Python with Flask
*   **Frontend:** HTML, Tailwind CSS, JavaScript
*   **Data:** Service information is stored in a `services.json` file.

## Architecture

The project follows a standard Flask application structure:

*   `app.py`: The main application file containing the Flask routes and logic.
*   `templates/`: Contains the HTML templates for the different pages. It uses a `base.html` template for the common layout.
*   `static/`: Contains the static assets like CSS, JavaScript, and images.
*   `data/`: Contains the `services.json` file, which acts as a simple database for the services offered.

# Building and Running

To run the project, you need to have Python and Flask installed.

1.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

2.  **Run the application:**

    ```bash
    python app.py
    ```

The application will be available at `http://localhost:8080`.

# Development Conventions

*   **Styling:** The project uses Tailwind CSS for styling. Custom styles are defined in `static/css/styles.css`.
*   **JavaScript:** The main JavaScript file is `static/js/main.js`. It handles the theme switcher, mobile menu, and other interactive elements.
*   **Data:** The services are loaded from `data/services.json`. To add or modify services, you need to edit this file. The file now includes "Бесплатная диагностика" and "Ремонт от 500р".
*   **Contact Form:** The contact form currently prints the submitted data to the console. The email sending or database saving logic needs to be implemented.
