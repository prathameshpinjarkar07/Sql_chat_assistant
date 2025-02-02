# Chat Assistant for SQLite Database

## Overview
This is a Python-based Flask application that provides a chat assistant for querying an SQLite database. The assistant can process natural language queries and convert them into SQL commands to fetch data from an SQLite database. It supports queries like retrieving employees in a department, listing managers, fetching employees hired after a specific date, and calculating salary expenses.

## Features
- Accepts natural language queries.
- Converts queries into SQL commands.
- Fetches and displays data from an SQLite database.
- Handles edge cases and invalid queries gracefully.

## Requirements
- Python 3.x
- Flask
- SQLite3
- Transformers 

## Setup Instructions

### Prerequisites
- Python 3.x installed
- `pip` for installing dependencies

### Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/chat-assistant-sqlite.git
   cd chat-assistant-sqlite
