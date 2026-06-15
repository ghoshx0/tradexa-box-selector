# AI Usage Report

## 1. AI Tools Used

* ChatGPT

## 2. Prompts Used

Examples of prompts used during development:

* "Help me plan the architecture for a Django-based box recommendation system."
* "Design Django models for products, boxes, orders, and order items."
* "Create a Django REST Framework API for box recommendations."
* "How can I implement box selection based on dimensions, weight, cost, and unused volume?"
* "Generate test cases for a Django box recommendation API."
* "Help me create README.md, AI_USAGE.md, and TEST_OUTPUT.md files."

## 3. Accepted Output

* Django project structure recommendations.
* API endpoint design suggestions.
* Recommendation algorithm approach.
* Test case ideas.
* Documentation templates.

## 4. Rejected or Modified Output

* Modified the recommendation request structure to support product quantities.
* Added validation for invalid product IDs.
* Added unused-volume tie-breaker logic.
* Simplified some implementation details to fit the assignment scope.
* Chose not to move business logic into a separate service layer.

## 5. Mistakes Found in AI Output

* Initial implementation did not safely handle invalid product IDs.
* Some suggestions introduced unnecessary complexity for the assignment scope.
* Error handling was improved manually using Product.DoesNotExist checks.

## 6. Verification Process

* Manual API testing using Django REST Framework's browsable API.
* Tested multiple product, box, dimension, and weight scenarios.
* Verified error handling for invalid product IDs.
* Executed automated tests using Django Test Framework.
* Performed a fresh-clone test from GitHub, installed dependencies, ran migrations, executed tests, and started the application successfully.

## Final Validation

All automated tests passed successfully and the project was verified from a clean clone before submission.
