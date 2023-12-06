# Michael Castellucci
# Kevin Wright
# CSC423
# Project Part 3

import sqlite3 as sq
import pandas as pd

db_connect = sq.connect("project.db")
cursor = db_connect.cursor()
cursor.execute(
    """
        CREATE TABLE Employee (
        staffNo int,
        fName varchar(255),
        lName varchar(255),
        address varchar(255),
        salary int,
        telNo int,
        PRIMARY KEY (staffNo)
        );
    """
)
cursor.execute(
    """
        CREATE TABLE Client (
        clientNo int,
        fName varchar(255),
        lName varchar(255),
        telNo int,
        PRIMARY KEY (clientNo)
        );
    """
)
cursor.execute(
    """
        CREATE TABLE ServiceRequest (
        requestID int,
        clientNo int,
        startDate date,
        startTime time,
        duration int,
        comments varchar(255),
        PRIMARY KEY (requestID),
        FOREIGN KEY (clientNo) REFERENCES Client ON DELETE NO ACTION ON UPDATE NO ACTION
        );
    """
)
cursor.execute(
    """
        CREATE TABLE Equipment (
        eqID int,
        description varchar(255),
        usage varchar(255),
        cost int,
        PRIMARY KEY (eqID)
        );
    """
)
cursor.execute(
    """
        CREATE TABLE Schedule (
        staffNo int,
        requestID int,
        PRIMARY KEY (staffNo, requestID),
        FOREIGN KEY (staffNo) REFERENCES Employee ON DELETE NO ACTION ON UPDATE NO ACTION,
        FOREIGN KEY (requestID) REFERENCES ServiceRequest ON DELETE NO ACTION ON UPDATE NO ACTION
        );
    """
)
cursor.execute(
    """
        CREATE TABLE EquipmentRequest (
        eqID int,
        requestID int,
        number int,
        PRIMARY KEY (eqID, requestID),
        FOREIGN KEY (eqID) REFERENCES Equipment ON DELETE NO ACTION ON UPDATE NO ACTION,
        FOREIGN KEY (requestID) REFERENCES ServiceRequest ON DELETE NO ACTION ON UPDATE NO ACTION
        );
    """
)
cursor.execute(
    """
        INSERT INTO Employee VALUES 
        (1, 'John', 'Smith', '9 Maple Ave', 50000, 3052153012),
        (2, 'Lebron', 'James', '243 Oak Terrace', 1000000, 3051231234),
        (3, 'Serena', 'Williams', '1280 Lincoln St', 250000, 3042019348);
    """
)
cursor.execute(
    """
        INSERT INTO Client VALUES
        (1, 'Leroy', 'Jenkins', 4328730184),
        (2, 'Wreckit', 'Ralph', 9993827567),
        (3, 'Lionel', 'Messi', 2234520923);
    """
)
cursor.execute(
    """
        INSERT INTO Equipment VALUES
        (1, 'Normal Mop', 'Clean floors', 30),
        (2, 'Pressure Washer', 'Clean tough grime off surfaces', 200),
        (3, 'Towel', 'Dries stuff', 10);
    """
)
cursor.execute(
    """
        INSERT INTO ServiceRequest VALUES
        (1, 2, '2023-12-10', '06:00:00', 3, NULL),
        (2, 1, '2024-01-03', '20:00:00', 2, NULL),
        (3, 3, '2023-12-25', '04:30:00', 12, 'Dont wake the dog');
    """
)
cursor.execute(
    """
        INSERT INTO Schedule VALUES
        (1, 2),
        (2, 3),
        (3, 3);
    """
)
cursor.execute(
    """
        INSERT INTO EquipmentRequest VALUES
        (1, 2, 1),
        (1, 3, 2),
        (3, 3, 2);
    """
)
db_connect.commit()
db_connect.close()
