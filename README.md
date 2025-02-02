# SQLite Chat Assistant
---

## Overview

This project implements a Python-based chat assistant that interacts with an SQLite database to answer user queries. The assistant accepts natural language queries, converts them into SQL queries, and fetches data from the database to provide clear and formatted responses.

The database contains two tables: **Employees** and **Departments**, which store employee details and department information, respectively.


---

## Features

- Accepts natural language queries.
- Converts queries into SQL for database interaction.
- Provides formatted and meaningful responses.
- Handles invalid queries gracefully.
- Supports multiple types of queries (e.g., filtering by department, date, or salary).

---

## Supported Queries

The chat assistant supports the following types of queries:

1. **Show employees in a department:**
   - Example: "Show me all employees in the Sales department."
   
2. **Find the manager of a department:**
   - Example: "Who is the manager of the Engineering department?"

3. **List employees hired after a specific date:**
   - Example: "List all employees hired after 2021-01-01."

4. **Calculate total salary expense for a department:**
   - Example: "What is the total salary expense for the Marketing department?"

5. **& More...**

---

## How It Works

1. **User Input:** The user submits a natural language query via the web interface or API.
2. **Query Parsing:** The chat assistant parses the input and identifies the intent (e.g., "show employees," "find manager").
3. **SQL Conversion:** Based on the parsed intent, the assistant generates an appropriate SQL query.
4. **Database Interaction:** The SQL query is executed against the SQLite database.
5. **Response Formatting:** The results are formatted into a human-readable response and returned to the user.

---

## Installation and Setup

### Prerequisites
- Python 3.8 or higher
- `sqlite3` library (built-in with Python)
- Flask

### Steps to Run Locally

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/sqlite-chat-assistant.git
   cd sqlite-chat-assistant
   ```

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Initialize the Database:**
   Run the script to create and populate the SQLite database:
   ```bash
   python database.py
   ```

4. **Start the Application:**
   ```bash
   python sql_assistant.py
   ```

5. **Access the Application:**
   Open your browser and navigate to `http://localhost:5000`.

---

## Usage

1. Enter a query in the text box provided on the web interface.
2. Click the "Submit" button to get the response.
3. The assistant will display the results below the query box.

Example Queries:
- "Show me all employees in the Sales department."
- "Who is the manager of the Marketing department?"
- "List all employees hired after 2021-01-01."
- "What is the total salary expense for the Engineering department?"

---

## Error Handling

The chat assistant includes robust error handling mechanisms:

- **Invalid Queries:** If the query cannot be parsed, the assistant returns a message like "Invalid query. Please try again."
- **No Results Found:** If no data matches the query, the assistant responds with "No results found."
- **Incorrect Department Names:** If the department name is invalid, the assistant informs the user with a message like "Department not found."
- **Invalid Date Formats:** If the date format is incorrect, the assistant prompts the user to enter a valid date.

---

## Known Limitations

1. The assistant currently supports only predefined query patterns. Complex or ambiguous queries may not be handled correctly.
2. The application does not support advanced SQL operations such as joins or aggregations beyond summing salaries.
3. The database schema is fixed, and additional columns or tables require manual updates to the code.

---

## Suggestions for Improvement

1. **Natural Language Processing (NLP):** Integrate an NLP library to improve query parsing and handle more complex user inputs.
2. **Advanced SQL Support:** Extend the assistant to support JOIN operations and more complex queries.
3. **User Interface Enhancements:** Add features like autocomplete, query history, and better formatting for results.
4. **Performance Optimization:** Optimize the database queries for large datasets.

---


