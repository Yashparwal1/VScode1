Types of Datatyps
    1. String datatype
    2. Numeric datatype
    3. Date and time datatype

## String Datatype

    CHAR(size) -- used to store character data within the predefined length. can store upto 2000 bytes
    NCHAR(size) -- use to store national character data within the predefined length. -- 2000 bytes
    VARCHAR2(size) -- store variable string data within the predefined length. -- 4000 bytes
    VARCHAR(size) -- same as VARCHAR2() but not recommended over VARCHAR2

## Numeric Datatype
    
    NUMBER(p,s) -- it contains precision p and scale s. The precision p can range from 1 to 38 and the scale s - range -84 to 127
    FLOAT(p) -- a subtype of the number datatype. p - 1 to 126
    DOUBLE PRECISION(DOUBLE, REAL) --
        in mysql DOUBLE and REAL are synonyms for DOUBLE PRECISION.
        double -- 8bytes -- more precise than FLOAT


## Date and Time Datatypes

    DATE -- store a valid date-time format with fixed length. range - january 1, 4712 BC to December 31, 9999 AD.

    Timestamp -- store valid date in yyyy-mm-dd with the hh:mm:ss format


-- Primary Key constraint
CREATE TABLE Orders (
    OrderID INT PRIMARY KEY,
    Product VARCHAR(50),
    Quantity INT
);

-- Foreign Key constraint
CREATE TABLE OrderDetails (
    OrderDetailID INT PRIMARY KEY,
    OrderID INT,
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID)
);