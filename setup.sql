-- MySQL script to set up the tables
-- NOT APPROVED BY ALICE, YET!!!

-- Table for deliverables
CREATE TABLE IF NOT EXISTS Deliverables (
    uniqueIdDeliverable INT NOT NULL AUTO_INCREMENT,
    nameDeliverable TEXT,
    descriptionDeliverable LONGTEXT,
    dueDateDeliverable DATE,
    PRIMARY KEY (uniqueIdDeliverable)
);

-- Table for tasks
CREATE TABLE IF NOT EXISTS Tasks (
    uniqueIdTask INT NOT NULL AUTO_INCREMENT,
    nameTask TEXT,
    descriptionTask LONGTEXT,
    dueDateDeliverable DATE,
    expectedStartDateTask DATE,
    expectedEndDateTask DATE,
    expectedDurationTask DECIMAL,
    expectedEffortTask DECIMAL,
    actualStartDateTask DATE,
    actualEndDateTask DATE,
    actualDurationTask DECIMAL,
    effortCompletionTask DECIMAL,
    actualEffortTask DECIMAL,
    percentCompletedTask DECIMAL,
    uniqueIdDeliverable INT NOT NULL
    PRIMARY KEY (uniqueIdTask),
    FOREIGN KEY (uniqueIdDeliverable)
      REFERENCES Deliverables(uniqueIdDeliverable)
);

-- Table for issues
CREATE TABLE IF NOT EXISTS Issues (
    uniqueIdIssue INT NOT NULL AUTO_INCREMENT,
    nameIssue TEXT,
    descriptionIssue LONGTEXT,
    priorityIssue TEXT,
    severityIssue TEXT,
    dateRaisedIssue DATE,
    dateAssignedIssue DATE,
    expectedCompletionDateIssue DATE,
    actualCompletionDateIssue DATE,
    statusIssue TEXT,
    statusDescriptionIssue LONGTEXT,
    updateDateIssue DATE,
    PRIMARY KEY (uniqueIdIssue)
);

-- Table for action items
CREATE TABLE ActionItems (
    uniqueIdActionItem INT NOT NULL AUTO_INCREMENT,
    nameActionItem TEXT,
    descriptionActionItem LONGTEXT,
    dateCreatedActionItem DATE,
    dateAssignedActionItem DATE,
    resourceAssignedActionItem DATE,
    expectedCompletionDateActionItem DATE,
    actualCompletionDateActionItem DATE,
    statusActionItem TEXT,
    statusDescriptionActionItem TEXT,
    updateDateActionItem DATE,
    uniqueIdIssue INT NOT NULL,
    PRIMARY KEY (uniqueIdActionItem),
    FOREIGN KEY (uniqueIdIssue)
      REFERENCES Issues(uniqueIdIssue)
);

-- Table for resources 
CREATE TABLE Resources (
    uniqueIdResource INT NOT NULL AUTO_INCREMENT,
    nameResource TEXT,
    uniqueIdActionItem INT NOT NULL,
    PRIMARY KEY (uniqueIdResource),
    FOREIGN KEY (uniqueIdActionItem)
      REFERENCES ActionItems(uniqueIdActionItem)
); 
