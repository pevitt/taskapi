Feature: Update Task

Scenario: Update Task Successfully
    Given I call update status service to update task status to 2
    Then The task services status should be 200
    And The task should be updated to status name in-progress

Scenario: Update Task Fail Status Not Found
    Given I call update status service to update task status to 10
    Then The task services status should be 400

Scenario: Update Task Fail Task Not Found
    Given I call update status service to update task 39606999-1108-47e0-b56e-a320e76bf1f3 to task status to 2
    Then The task services status should be 404
