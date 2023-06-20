# Insert 1 row into a table
INSERT INTO employees.employees (first_name, last_name, email, title, active, created_date) 
VALUES ('Admas', 'Kinfu', 'admas@supersqa.com', 'Sr. Engineer', 1, now());

# Insert multiple rows into a table
INSERT INTO employees.employees (first_name, last_name, email, active, created_date) 
VALUES ('Admas', 'Ki4', 'admask4@supersqa.com', 1, now()),
('Admas', 'Ki1', 'admask1@supersqa.com', 1, now()),
('Admas', 'Ki2', 'admask2@supersqa.com', 1, now()),
('Admas', 'Ki3', 'admask3@supersqa.com', 1, now());

# Read from the table to verify the inserted rows
select * from employees.employees order by id desc;

# Insert statement generated by MySQL Workbench automaticaly
INSERT INTO `employees`.`employees`
(`id`,
`first_name`,
`last_name`,
`email`,
`title`,
`active`,
`modified_date`,
`created_date`)
VALUES
(<{id: }>,
<{first_name: }>,
<{last_name: }>,
<{email: }>,
<{title: }>,
<{active: }>,
<{modified_date: CURRENT_TIMESTAMP}>,
<{created_date: }>);
