## User Profile Analyzer via AI API
## Overview

The User Profile Analyzer is a Python-based API that:

1. Authenticates users against a local SQLite database.

2. Collects user traits such as area of interest, strengths, and weaknesses.

3. Uses Ollama (local LLM) to generate AI-based feedback and career suggestions.

4. Returns structured JSON responses.

## Features

1. User Authentication with username & password (hashed using bcrypt).

2. Profile Submission (area of interest, strengths, weaknesses).

3. AI Integration with Ollama for local LLM responses.

