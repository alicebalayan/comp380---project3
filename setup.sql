-- MySQL script to set up the tables
-- NOT APPROVED BY ALICE, YET!!!

-- Table for deliverables
-- No dependencies
CREATE TABLE IF NOT EXISTS deliverables (
    id INT NOT NULL AUTO_INCREMENT,
    name TEXT,
    description LONGTEXT,
    due_date DATE,
    PRIMARY KEY (id)
);

-- Table for requirements
-- Depends on deliverables
CREATE TABLE IF NOT EXISTS requirements (
    id INT NOT NULL AUTO_INCREMENT,
    name TEXT,
    deliverable_id INT NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (deliverable_id)
      REFERENCES deliverables(id)
);

-- Table for tasks
-- Depends on deliverables
CREATE TABLE IF NOT EXISTS tasks (
    id INT NOT NULL AUTO_INCREMENT,
    name TEXT,
    description LONGTEXT,
    due_date DATE,
    expected_start_date DATE,
    expected_end_date DATE,
    expected_duration DECIMAL,
    expected_effort DECIMAL,
    actual_start_date DATE,
    actual_end_date DATE,
    actual_duration DECIMAL,
    effort_completed DECIMAL,
    actual_effort DECIMAL,
    percent_complete DECIMAL,
    deliverable_id INT NOT NULL
    PRIMARY KEY (id),
    FOREIGN KEY (deliverable_id)
      REFERENCES deliverables(id)
);

-- Table for tasks' predecessors and successors
-- Depends on tasks
CREATE TABLE IF NOT EXISTS task_pred_succ (
    task_id INT NOT NULL,
    predecessor_id INT NOT NULL,
    successor_id INT NOT NULL,
    FOREIGN KEY (task_id)
      REFERENCES tasks(id),
    FOREIGN KEY (predecessor_id)
      REFERENCES tasks(id),
    FOREIGN KEY (successor_id)
      REFERENCES tasks(id)
);

-- Table for issues
-- No dependencies
CREATE TABLE IF NOT EXISTS issues (
    id INT NOT NULL AUTO_INCREMENT,
    name TEXT,
    description LONGTEXT,
    priority TEXT,
    severity TEXT,
    date_raised DATE,
    date_assigned DATE,
    expected_completion_date DATE,
    actual_completion_date DATE,
    status TEXT,
    status_description LONGTEXT,
    update_date DATE,
    PRIMARY KEY (id)
);

-- Table for the task-issue relation
-- Depends on issues and tasks
CREATE TABLE IF NOT EXISTS task_issue (
    issue_id INT NOT NULL,
    task_id INT NOT NULL,
    FOREIGN KEY (issue_id)
      REFERENCES issues(id),
    FOREIGN KEY (task_id)
      REFERENCES tasks(id),
);

-- Table for action items
-- Depends on issues
CREATE TABLE IF NOT EXISTS action_items (
    id INT NOT NULL AUTO_INCREMENT,
    name TEXT,
    description LONGTEXT,
    date_created DATE,
    date_assigned DATE,
    resource_assigned DATE,
    expected_completion_date DATE,
    actual_completion_date DATE,
    status TEXT,
    status_description TEXT,
    update_date DATE,
    issue_id INT NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (issue_id)
      REFERENCES issues(id)
);

-- Table for decisions
-- No dependencies
CREATE TABLE IF NOT EXISTS decisions (
    id INT NOT NULL AUTO_INCREMENT,
    name TEXT,
    description LONGTEXT,
    priority TEXT,
    impact TEXT,
    date_created DATE,
    date_needed DATE,
    date_made DATE,
    expected_completion_date DATE,
    actual_completion_date DATE,
    note_date DATE,
    status TEXT,
    status_description LONGTEXT,
    update_date DATE,
    PRIMARY KEY (id)
);


-- Table for decision-issue relation
CREATE TABLE IF NOT EXISTS decision_issue (
    decision_id INT NOT NULL,
    issue_id INT NOT NULL,
    FOREIGN KEY (decision_id)
      REFERENCES decisions(id),
    FOREIGN KEY (issue_id)
      REFERENCES issues(id)
);

-- Table for resources 
-- Depends on action_items and decisions
CREATE TABLE IF NOT EXISTS resources (
    id INT NOT NULL AUTO_INCREMENT,
    name TEXT,
    action_items_id INT NOT NULL,
    decision_id INT NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (action_items_id)
      REFERENCES action_items(id),
    FOREIGN KEY (decision_id)
      REFERENCES decisions(id)
);

-- Table for the task-resouce relation
-- Depends on tasks decisions
CREATE TABLE IF NOT EXISTS task_resource (
    task_id INT NOT NULL,
    resource_id INT NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (task_id)
      REFERENCES tasks(id),
    FOREIGN KEY (resource_id)
      REFERENCES resources(id)
);

-- Table for reference documents
-- Depends on decisions
CREATE TABLE IF NOT EXISTS reference_documents (
    id INT NOT NULL AUTO_INCREMENT,
    name TEXT,
    decision_id INT NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (decision_id)
      REFERENCES decisions(id)
);

-- Table for meeting notes
-- Depends on decisions
CREATE TABLE IF NOT EXISTS meeting_notes (
    id INT NOT NULL AUTO_INCREMENT,
    name TEXT,
    note LONGTEXT,
    decision_id INT NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (decision_id)
      REFERENCES decisions(id)
);
