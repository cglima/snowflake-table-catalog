# Snowflake Table Catalog

This project is a web application to visualize table metadata from a Snowflake database.

## Architecture

The application is built with a modern full-stack architecture, separating the frontend and backend concerns.

- **Backend:** A Python application built with FastAPI, following Clean Architecture principles. It provides a REST API to access the Snowflake table data.
- **Frontend:** A React application built with TypeScript, also following Clean Architecture principles. It consumes the backend API and provides a user-friendly interface to visualize the data.

There is also a legacy Streamlit application in the `streamlit_app` directory.

## How to Run

### Backend

The backend can be run locally with Python or with Docker.

**Running locally:**

1. **Install dependencies:**
   ```bash
   pip install -r backend/requirements.txt
   ```

2. **Set up environment variables:**

   Create a `.env` file in the root of the project and add the following variables:

   - **For development (using CSV):**
     ```bash
     APP_ENV=development
     ```

   - **For production (using Snowflake):**
     ```bash
     APP_ENV=production
     SNOWFLAKE_USER=your_user
     SNOWFLAKE_PASSWORD=your_password
     SNOWFLAKE_ACCOUNT=your_account
     ```

3. **Start the server:**
   ```bash
   uvicorn backend.main.server:app --reload
   ```

The server will be available at `http://127.0.0.1:8000`.

**Running with Docker:**

1. **Build the Docker image:**

   From the `backend` directory, run:
   ```bash
   docker build -t snowflake-table-catalog-backend .
   ```

2. **Run the container:**
   ```bash
   docker run -p 8000:8000 snowflake-table-catalog-backend
   ```

The application will be available at `http://localhost:8000`.

### Frontend

The frontend can be run locally with Node.js or with Docker.

**Running locally:**

1. **Install dependencies:**
   ```bash
   cd frontend
   npm install
   ```

2. **Start the development server:**
   ```bash
   npm start
   ```

   This will start the application in development mode and open it at `http://localhost:3000`.

**Running with Docker:**

1. **Build the Docker image:**
   ```bash
   docker build -t snowflake-table-catalog-frontend .
   ```

2. **Run the container:**
   ```bash
   docker run -p 3000:3000 snowflake-table-catalog-frontend
   ```

The application will be available at `http://localhost:3000`.