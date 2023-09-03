Feature: Create Task

Scenario: Create task successfully
    Given I call service to create task with title Task1
    And I receive a response with status code 201