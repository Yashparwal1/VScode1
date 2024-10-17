CREATE TABLE customer (
    cid number(13, 0) PRIMARY KEY,
    cname VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL,
    phone VARCHAR(15),
    userId VARCHAR(20) NOT NULL CHECK (LENGTH(userId) >= 5 AND LENGTH(userId) <= 20),
    password VARCHAR(30) NOT NULL,
    cnf_password VARCHAR(30) NOT NULL,
    status VARCHAR(8) NOT NULL CHECK (status = 'active' OR status = 'inactive')
);

INSERT INTO customer (cid, cname, email, phone, userId, password, cnf_password, status)
VALUES
(1234567890123, 'yash', 'yash@gmail.com', '1234567890', 'yash_01', 'yash@123', 'yash@123', 'active'),
(2345678901234, 'parwal', 'parwal@reddif.com', '2345678901', 'parwal_01', 'parwal@123', 'parwal@123', 'inactive'),
(3456789012345, 'Zed', 'zed@hotmail.com', '3456789012', 'zed_01', 'zed@123', 'zed@123', 'active'),
(4567890123456, 'Shadow', 'shadow@gmail.com', '4567890123', 'shadow_01', 'shadow@123', 'shadow@123', 'inactive'),
(5678901234567, 'yoda', 'yoda@yahoo.com', '5678901234', 'yoda_01', 'yoda@123', 'yoda@123', 'active'),
(5678901234568, 'sara', 'yoda@yahoo.com', '5678901234', 'yoda_01', 'yoda@123', 'yoda@123', 'active');

alter table customer
add title VARCHAR(10) check(title in ('Mr.','Ms.', 'Mrs.')), 
add bill_number number(5);

-- retrieving the customer details whose name ends with 'a'. Sort it descending order based on customer name. Display CustomerId| CustomerName |  Email

select cid, cname, email from customer where cname like '%a' order by cname desc;
-- -----------------

CREATE TABLE customer_bill(
    cid number(13) PRIMARY KEY,
    cname VARCHAR(50) NOT NULL,
    address VARCHAR(100),
    city VARCHAR(50) NOT NULL,
    bill NUMBER(7,2) NOT NULL;
)

INSERT INTO customer_bills (cid, cname, address, city, bill) 
VALUES
(1234567890123, 'yash', 'A8 JNC', 'Jaipur', 150.75),
(1234567890123, 'yash', 'A8 JNC', 'Jaipur', 450.50),
(3456789012345, 'Zed', '456 aravali', 'Jodhpur', 100.09),
(3456789012345, 'Zed', '456 aravali', 'Jodhpur', 340.00),
(3456789012345, 'Zed', '456 aravali', 'Jodhpur', 280.11),
(4567890123456, 'Shadow', '789 Pine Rd', 'Sikar', 225.00),
(4567890123456, 'Shadow', '789 Pine Rd', 'Sikar', 245.19),  
(4567890123456, 'Shadow', '789 Pine Rd', 'Sikar', 215.05),
(5678901234567, 'yoda', '321 Maple St', 'Alwar', 250.75),
(5678901234567, 'yoda', '321 Maple St', 'Alwar', 290.75);

-- the average bill per city and arrange them in descending order
select city, avg(bill) as avg_bill from customer bill
group by city order by avg_bill desc;

-- --------------------

CREATE TABLE Consumers (
    consumerID NUMBER(3) PRIMARY KEY,
    consumerName VARCHAR(50) NOT NULL,
    address VARCHAR(100),
    city VARCHAR(50),
    phone NUMBER(10)
);

CREATE TABLE Monthly_Bills (
    billID NUMBER(3) PRIMARY KEY,
    consumerID NUMBER(3),
    billAmount DECIMAL(7, 2) NOT NULL,
    payment VARCHAR(4) CHECK (payment IN ('Paid', 'Due')),
    month VARCHAR(10) DEFAULT 'June',
    FOREIGN KEY (consumerID) REFERENCES Consumers(consumerID)
);

INSERT INTO Consumers (consumerID, consumerName, cddress, city, phone) 
VALUES
(1, 'Rajesh Kumar', 'Street 1', 'Jaipur', '9876543210'),
(2, 'Sunita Sharma', 'Block A', 'Ajmer', '8765432109'),
(3, 'Amit Singh', 'Near Park', 'Udaipur', '7654321098'),
(4, 'Pooja Mehta', 'Sector 5', 'Jodhpur', '6543210987'),
(5, 'Rahul Verma', 'Lane 3', 'Bikaner', '5432109876'),
(6, 'Neha Agarwal', 'Road 4', 'Kota', '4321098765'),
(7, 'Vikram Joshi', 'Area 2', 'Alwar', '3210987654'),
(8, 'Anita Yadav', 'Locality 7', 'Sikar', '2109876543'),
(9, 'Deepak Jain', 'Zone 3', 'Churu', '1098765432'),
(10, 'Kiran Rathi', 'Region 8', 'Pali', '0987654321');

INSERT INTO Monthly_Bills (billID, CID, billAmount, payment) 
VALUES
(101, 1, 150.75, 'Paid'),
(102, 2, 200.50, 'Due'),
(103, 3, 175.25, 'Paid'),
(104, 4, 100.00, 'Due'),
(105, 5, 120.50, 'Paid'),
(106, 6, 95.75, 'Due'),
(107, 7, 225.00, 'Paid'),
(108, 8, 190.00, 'Paid'),
(109, 9, 175.25, 'Due'),
(110, 10, 250.75, 'Paid');

-- give the ConsumerId and ConsumerName from the Consumers table based upon the ConsumerIDs of, Bills table who failed to pay the bill.
select consumerID, consumerName from Consumers
where consumerID IN (select CID from Monthly_Bills where payment IN ("Due"));
