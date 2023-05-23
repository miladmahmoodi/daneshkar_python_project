# daneshkar_python_project
This repository was created with ❤️ for Daneshkar's Python Bootcamp project.
# Cinema Ticket

This project is a cinema ticket reservation system implemented in Python. It allows users to create accounts, manage their profiles, view available movie sessions, and reserve seats. The system also supports different subscription types and offers various discounts based on user's membership duration and birthday.

## Features

- User registration with mandatory birthdate
- Automatic registration date storage
- Users can have multiple bank accounts
- Bank accounts support deposit, withdrawal, and transfer operations
- Enhanced security with account password and CVV2
- Users can charge their wallet and purchase different subscription types
  - Bronze: Basic default service with no special benefits
  - Silver: 20% cashback on the next three purchases
  - Gold: 50% cashback and a free energy drink for one month
- Users can view and reserve movie sessions
- Birthday discounts and membership-based discounts
- Restrictions on reserving past sessions or sessions with full capacity
- Age restrictions on viewing and reserving movies for higher age ratings
- Separate script for cinema managers to set up movie sessions
- Two approaches for differentiating managers and users:
  - Using an Enum field in the User model class
  - Inheriting from an abstract base Human model
- Modular design with separate modules for each functionality
- Test-driven development (TDD) using a `tests` package
- Custom exceptions and exception handling
- Logging events in `cinematicket.log`
- Data persistence using Pickle or JSON files
- Recommended Git Workflow for team collaboration
- Additional features are acceptable after completing the main scenario

## Installation

1. Clone the repository:

```
git clone git@github.com:miladmahmoodi/daneshkar_python_project.git
```

2. Change to the project directory:

```
cd daneshkar_python_project
```

3. Install the required dependencies:

```
pip install -r requirements.txt
```

## Usage

1. Run the main script:

```
python main.py
```

2. Follow the on-screen instructions to interact with the system.

## Testing

To run the tests, execute the following command:

```
python -m unittest discover tests
```
