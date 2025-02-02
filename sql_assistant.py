from transformers import pipeline
import sqlite3
from flask import Flask, request, render_template

# Initialize Flask app
app = Flask(__name__)

# Load a pre-trained transformer model for Question-Answering (distilled BERT model)
qa_pipeline = pipeline("question-answering", model="distilbert-base-uncased")

# Function to connect to the SQLite database
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row  # This allows accessing columns by name
    return conn

# Function to process the query and map it to SQL
def process_query(query):
    # Simplified rule-based query processing based on keywords and intent matching
    
    if "employees" in query and "department" in query:
        department = query.split("in the")[-1].strip().split("department")[0].strip()
        return f"SELECT * FROM Employees WHERE Department = '{department}'"

    if "manager" in query and "department" in query:
        department = query.split("department")[-1].strip()
        return f"SELECT Manager FROM Departments WHERE Name = '{department}'"

    if "hired after" in query:
        hire_date = query.split("after")[-1].strip()
        return f"SELECT * FROM Employees WHERE Hire_Date > '{hire_date}'"

    if "total salary" in query and "department" in query:
        department = query.split("department")[-1].strip()
        return f"SELECT SUM(Salary) FROM Employees WHERE Department = '{department}'"
    
    return None  # Return None when query cannot be understood

# Function to execute the SQL query and return the result
def execute_query(sql_query):
    if sql_query is None:  # Handle invalid or unrecognized query
        return "Sorry, I couldn't understand the query."
    
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(sql_query)
        result = cursor.fetchall()
        conn.close()
        
        # Convert the result to a list of dictionaries for better display
        if result:
            result_dict = [dict(row) for row in result]
        else:
            result_dict = []
        
        return result_dict
    
    except sqlite3.OperationalError as e:
        # Handle SQL errors (e.g., invalid query or connection issues)
        return f"An error occurred while executing the query: {str(e)}"

# Route to display the home page with the form
@app.route('/', methods=['GET', 'POST'])
def home():
    result = None
    error = None
    
    if request.method == 'POST':
        user_input = request.form.get('query', '').strip()
        
        if not user_input:
            error = 'Query is missing.'
        else:
            # Process the query and map to SQL
            sql_query = process_query(user_input)
            
            # Execute SQL and return the result
            result = execute_query(sql_query)
            if not result:
                result = 'No results found or query could not be processed.'
    
    return render_template('index.html', result=result, error=error)

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
