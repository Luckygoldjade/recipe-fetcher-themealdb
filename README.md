## Recipe Fetcher Microservice (Server) — `recipe-fetcher-themealdb`

**Ingredient List Provider for Meal Search Client**  
This Python-based microservice fetches ingredient data from TheMealDB API and returns it as a JSON response through ZeroMQ messaging. It was built to serve as the data provider for a partner’s recipe lookup client microservice.

This repository contains my independent copy of a collaborative academic project completed as part of the
Computer Science program.

---

## Overview

This microservice acts as a backend API proxy that:

- Retrieves a list of ingredients from TheMealDB API.
- Sends the fetched data over ZeroMQ in JSON format.
- Supports a partner's microservice client that allows users to input an ingredient and receive a list of related recipes.

This was developed as part of a collaborative microservice system demonstrating asynchronous messaging and distributed microservice design using Python and ZeroMQ.

---

## Technologies Used

- **Python 3**
- **Requests** (`requests`)
- **ZeroMQ** (`pyzmq`)

---

## Features

- Connects to public **TheMealDB** API to fetch ingredients
- Handles network errors and timeouts gracefully
- Sends data via **ZeroMQ REP socket**
- Modular and testable Python structure

---

## How to Run the Server

### 1. Install Requirements

```bash
pip install -r requirements.txt
```

### 2. Start the Server

```bash
python recipe_data_server.py
```

Make sure this server is running before the client connects via ZeroMQ.

---

## File Structure

- recipe-fetcher-themealdb/
  - recipe_data_server.py     # Main server application (calls MealDB API, returns data over ZeroMQ)
  - requirements.txt          # Dependency list
  - README.md                 # Project overview and instructions
  - docs/
    - *.png and *.pdf: Diagrams, demo screenshots, and design notes
    - demo_video.mp4: Terminal screen capture of server in action

---

## Communication Protocol

- **Messaging System**: ZeroMQ
- **Socket Type**: REQ/REP
- **Data Format**: JSON
- **API Source**: [https://www.themealdb.com/api/json/v1/1/list.php?i=list](https://www.themealdb.com/api/json/v1/1/list.php?i=list)

### Example JSON Response

```json
{
  "meals": [
    {
      "idIngredient": "1",
      "strIngredient": "Chicken",
      "strDescription": "Chicken is a versatile protein...",
      "strType": null
    },
    ...
  ]
}
```

---

## Screenshots and Demo

- **Screenshots**:  
  Terminal output, API response preview, and data received by the client are available under `/docs/screenshots/`.

- **Demo Video**:  
  Watch a brief demo of the microservice in action:  
  📹 `docs/demo_video.mp4` or hosted version (optional: YouTube, GitHub Video Preview)

---

## Notes

- This microservice is designed to be queried by a partner's client that helps users search for recipes.
- Can be easily extended to support other endpoints from TheMealDB API.

---

## License

This project is for demonstration and educational purposes. No affiliation with TheMealDB.
