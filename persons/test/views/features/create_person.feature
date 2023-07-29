Feature: Create Person

Scenario: Create customer successfully
    Given I call service to create person with email rigoberto@gmail.com
    And I receive a response with status code 201
    Then I call service to get person with email rigoberto@gmail.com
    And I receive a response with status code 200 and email rigoberto@gmail.com

Scenario: Create customer successfully and get by email with wrong case
    Given I call service to create person with email rigoberto@gmail.com
    And I receive a response with status code 201
    Then I call service to get person with email rigobert@gmail.com
    And I receive a response error with status code 404

Scenario: Create customer fail already exist
    Given I call service to create person with email rigoberto@gmail.com
    And I receive a response with status code 201
    Then I call service to create another person with same email rigoberto@gmail.com
    And I receive a response with status code 400

Scenario: Create customer fail email wrong
    Given I call service to create person with email rigobertogmail.com
    And I receive a response with status code 400 for wrong email

