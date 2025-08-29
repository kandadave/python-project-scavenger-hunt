# Urban Quest Creator CLI

A Python-based command-line interface for creating and managing urban scavenger hunt quests, with user-input clues and a SQLite database.

By David Chumo

## Description

This is a robust, interactive CLI application designed to allow users to create, manage, and explore urban scavenger hunt quests. It leverages SQLAlchemy for database operations, Click for the command-line interface, and Alembic for database migrations. The application supports creating users and quests, viewing quest creators, and listing all quests created by a specific user with detailed information including location, type, and clue. It uses a SQLite database (quests.db) for persistence and features a simplified location validation that accepts any non-empty string.



## Features

- **User Management**: Create, delete, list, and find users by ID, with optional email and preferences.
- **Quest Management**: Create, delete, list, and find quests by ID, with details including name, location, type, clue, and creation date.
- **View Quest Creator**: Display the user who created a specific quest.
- **View User's Quests**: List all quests created by a specific user, showing ID, name, location, type, clue, and creation date.
- **ASCII Map Display**: Generate an ASCII art representation of any location using the `art` library.
- **Persistence**: All user and quest data is stored in a SQLite database (`quests.db`) with a schema managed by Alembic migrations.

## How to Use

### Requirements

- A computer with Python 3.8+ installed.
- Pipenv for managing virtual environments and dependencies.
- A terminal/command line.
- A code editor (VS Code recommended).
- SQLite for database operations.

### Installation Process

**1. Clone the repository:**

```bash
git clone [https://github.com/kandadave/urban-quest-creator](https://github.com/kandadave/urban-quest-creator)
cd urban-quest-creator
````

**2. Install Dependencies:**

Navigate to the project root directory and install dependencies using Pipenv:

```bash
pipenv install
```

**3. Activate Virtual Environment:**

```bash
pipenv shell
```

**4. Apply Database Migrations:**

Set up the SQLite database (`quests.db`) with the required schema:

```bash
pipenv run alembic upgrade head
```

**5. (Optional) Seed the Database:**

Populate the database with sample data:

```bash
python lib/db/seed.py
```

### Running the Application

Start the CLI application:

```bash
python -m lib.main
```

Interact with the main menu to:

  - Manage users (create, delete, list, find, view quests).
  - Manage quests (create, delete, list, find, view creator).
  - Display an ASCII map for a location.

**Example usage:**

  - **Create a user**: Select 1 -\> 1, enter name (e.g., Dave), email (e.g., dave@gmail.com), preferences (e.g., Adventure).
  - **Create a quest**: Select 2 -\> 1, enter name (e.g., Archives Mystery), creator ID (e.g., 1), location (e.g., Nairobi), type (e.g., Adventure), clue (e.g., Find the hidden artifact).
  - **View user’s quests**: Select 1 -\> 5, enter user ID (e.g., 1) to see all quests with details.

## Technologies Used

  - **Python 3.8+**: Core programming language for the application.
  - **SQLAlchemy**: ORM for managing SQLite database operations.
  - **Click**: Library for building the command-line interface.
  - **Alembic**: Tool for handling database migrations.
  - **Art**: Library for generating ASCII art maps.
  - **SQLite**: Lightweight database for storing user and quest data.
  - **Pytest**: Framework for running unit tests.

## Support and Contact Details

If you have any questions, suggestions, or need assistance, please contact:
**Email**: kandachumo@gmail.com

## License

```
MIT License

Copyright (c) 2025 David Chumo

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
```

