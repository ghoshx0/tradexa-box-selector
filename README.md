# AI-Assisted Box Selection System

## Overview

This project is a Django REST Framework application that recommends the most suitable shipping box for ecommerce orders.

The recommendation engine evaluates product dimensions and weight, then selects the cheapest valid box. If multiple boxes have the same cost, the box with the smallest unused volume is selected.

## Features

* Product Management API
* Box Management API
* Order Management API
* Shipping Box Recommendation API
* Dimension Validation
* Weight Validation
* Cheapest Box Selection
* Unused Volume Tie-Breaker
* Automated Tests
* Bootstrap Dashboard

## Tech Stack

* Python
* Django
* Django REST Framework
* SQLite
* Bootstrap 5

## Assumptions

* Products are stacked vertically for height calculation.
* Required length is the maximum product length.
* Required width is the maximum product width.
* Required height is the sum of product heights multiplied by quantity.
* Total weight is the sum of product weights multiplied by quantity.
* The cheapest valid box is selected.
* If multiple boxes have the same cost, the box with the smallest unused volume is selected.

## Installation

1. Clone the repository

```bash
git clone <repository-url>
cd tradexa-box-selector
```

2. Create a virtual environment

```bash
python -m venv venv
```

3. Activate the virtual environment

Windows:

```bash
venv\Scripts\activate
```

4. Install dependencies

```bash
pip install -r requirements.txt
```

5. Run migrations

```bash
python manage.py migrate
```

6. Start the server

```bash
python manage.py runserver
```

## API Endpoints

### Products

* GET /api/products/
* POST /api/products/

### Boxes

* GET /api/boxes/
* POST /api/boxes/

### Orders

* GET /api/orders/
* POST /api/orders/

### Recommendation

* POST /api/recommend-box/

Sample Request:

```json
{
  "items": [
    {
      "product_id": 1,
      "quantity": 1
    },
    {
      "product_id": 2,
      "quantity": 1
    }
  ]
}
```

Sample Response:

```json
{
  "recommended_box": "Medium Box",
  "cost": 80.0,
  "unused_volume": 28750.0,
  "total_weight": 3.0
}
```

## Running Tests

```bash
python manage.py test
```

Current Test Coverage:

* Successful recommendation
* Invalid product handling
* No suitable box found
* Cheapest box selection
* Unused volume tie-breaker
