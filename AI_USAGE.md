# AI Usage Report

## AI Tools Used

* ChatGPT

## How AI Was Used

AI was used as a development assistant for:

* Project planning
* Django project structure guidance
* Django REST Framework implementation guidance
* Recommendation algorithm design
* Test case suggestions
* Documentation preparation

## Accepted Output

* API structure suggestions
* Django model organization
* Recommendation algorithm approach
* Automated testing ideas
* Documentation templates

## Modified Output

* Updated recommendation request format to support:

  * product_id
  * quantity

* Added validation for invalid product IDs.

* Added cheapest-box selection logic.

* Added unused-volume tie-breaker logic.

* Added Bootstrap dashboard page.

## Rejected Output

* Suggestions that introduced unnecessary complexity for the assignment scope.
* Architectural refactoring that was not required for the assignment.

## Mistakes Found

* Initial implementation did not safely handle invalid product IDs.
* Error handling was improved using Product.DoesNotExist checks.

## Verification Process

* Manual API testing through Django REST Framework.
* Multiple recommendation scenarios tested.
* Validation of dimension and weight constraints.
* Automated testing using Django Test Framework.

## Final Validation

All automated tests passed successfully before submission.
