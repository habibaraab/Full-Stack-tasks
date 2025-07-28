create or replace function 
get_total(id int)
returns int 
language plpgsql
as $$
declare
    total int;
begin 
    select count(customer_id)
    into total
    from orders
    where customer_id = id;
    return total;
end ;
$$;

select get_total(9);

create or replace function 
get_category(id int)
returns varchar(255) 
language plpgsql
as $$
declare
    ans varchar(255);
begin 
    select category_name
    into ans
    from products 
    join categories  on products.category_id = categories.category_id
    where products.product_id = id;
    return ans;
end ;
$$;

select get_category(5);

create or replace procedure 
add_new(
    name varchar(255),
    con_name varchar(255),
    address varchar(255),
    city varchar(255),
    code varchar(255),
    country varchar(255)
)
language plpgsql
as $$
begin 
    insert into customers (customer_name, contact_name, address, city, postal_code, country)
    values (name, con_name, address, city, code, country);
end ;
$$;

call add_new('Habiba', 'bia', '25 Zaid St', 'alex', '7637', 'Eqypt');

create or replace procedure 
update_category(
    id int,
    cat_id int
)
language plpgsql
as $$
begin 
    update products
    set category_id = cat_id
    where product_id = id;
end ;
$$;

call update_category(2,6);


create or replace function prevent()
returns trigger 
language plpgsql
as $$
begin
    if exists (select 1 from products where category_id = id) then
        raise exception 'Cannot be delete';
    end if;
    return id;
end;
$$;

create trigger trg
before delete on categories
for each row 
execute function prevent();


create or replace function 
calclute (id int)
returns  
language plpgsql
as $$
declare
    tot double;
begin 
    select sum(quantity * price)
    into tot
    from order_details 
    join products on order_details.product_id = products.product_id
    where order_details.product_id = id;
    return total_revenue;
end ;
$$;

----------------------------------------------------------------------------------


CREATE TABLE Clerks (
    ClerkNumber INT PRIMARY KEY,
    ClerkName VARCHAR(255)
);

CREATE TABLE Customers (
    CustomerNumber INT PRIMARY KEY,
    CustomerName VARCHAR(255),
    CustomerAddress VARCHAR(255)
);

CREATE TABLE Products (
    ItemNumber INT PRIMARY KEY,
    Description VARCHAR(255),
    UnitPrice NUMERIC(10, 3),
    CategoryID INT
);

CREATE TABLE SalesOrders (
    SalesOrderNumber INT PRIMARY KEY,
    SalesOrderDate DATE,
    CustomerNumber INT REFERENCES Customers(CustomerNumber),
    ClerkNumber INT REFERENCES Clerks(ClerkNumber)
);

CREATE TABLE OrderItems (
    SalesOrderNumber INT REFERENCES SalesOrders(SalesOrderNumber),
    ItemNumber INT REFERENCES Products(ItemNumber),
    Quantity INT,
    PRIMARY KEY (SalesOrderNumber, ItemNumber)
);


Insert data

INSERT INTO Clerks (ClerkNumber, ClerkName) VALUES
(210, 'Martin Lawrence');

INSERT INTO Customers (CustomerNumber, CustomerName, CustomerAddress) VALUES
(1001, 'ABC Company', '100 Points, Manhattan, KS 66502');

INSERT INTO Products (ItemNumber, Description, UnitPrice, CategoryID) VALUES
(800, 'widgit small', 60.00, 1),
(801, 'tingimajigger', 20.00, 2),
(805, 'thingibob', 100.00, 1);

INSERT INTO SalesOrders (SalesOrderNumber, SalesOrderDate, CustomerNumber, ClerkNumber) VALUES
(405, '2000-02-01', 1001, 210);

INSERT INTO OrderItems (SalesOrderNumber, ItemNumber, Quantity) VALUES
(405, 800, 40),
(405, 801, 20),
(405, 805, 10);
 

INSERT INTO Customers (CustomerNumber, CustomerName, CustomerAddress)
VALUES (1002, 'Habiba', '25 Zaid St, Cairo, Egypt');

INSERT INTO Products (ItemNumber, Description, UnitPrice, CategoryID)
VALUES (900, 'katle', 199.00, 3);

SELECT * FROM Products
WHERE UnitPrice > 100;


SELECT * FROM Customers
WHERE CustomerAddress ILIKE '%Egypt%';

SELECT * FROM Products
WHERE UnitPrice < 50;


SELECT * FROM Products
WHERE UnitPrice BETWEEN 50 AND 150;


INSERT INTO Products (ItemNumber, Description, UnitPrice, CategoryID) VALUES
(807, 'Ohiaiak', 100.00, 1);

SELECT * FROM Products
WHERE Description ILIKE 'o%';


INSERT INTO Customers (CustomerNumber, CustomerName, CustomerAddress)
VALUES (1003, 'Asmaa', '20 doki St, Giza, Cairo');

SELECT * FROM Customers
WHERE CustomerAddress ILIKE '%o';


SELECT * FROM Products
WHERE Description ILIKE '%oil%';