# Django_Rest_API
- This is a Django REST API project that allows you to perform CRUD (Create, Read, Update, Delete) operations on card data. You can use the API to manage card information including title, description, and creation date.

## Getting Started

To set up and run the project locally, follow these steps:

- Clone the repository to your local machine:
  ```bash
  git clone https://github.com/mham7/Django_Rest_API.git

**Create a virtual environment and activate it:**
python -m venv myenv
myenv\Scripts\activate  # On Windows
source myenv/bin/activate  # On macOS and Linux

**Run the development server:**
python manage.py runserver

**API Endpoints**
1) GET /api/cards/: Retrieve a list of all cards.
2) POST /api/cards/: Create a new card.
3) GET /api/cards/<id>/: Retrieve details of a specific card.
4) PUT /api/cards/<id>/: Update a specific card.
5) DELETE /api/cards/<id>/: Delete a specific card.

**Technologies Used**
1) Django
2) Django REST framework



