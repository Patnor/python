
'''
use rarebooks;

Select customer_numb, credit_card_numb from sale;

Select distinct customer_numb, credit_card_numb from sale;

Select inventory_id, selling_price from volume where selling_price < 100 or selling_price is Null;



-- from slide 33, 4 ways to get the same results
-- Janice	Jones	1	2021-10-13
-- Janice	Jones	2	2021-01-05
-- Janice	Jones	3	2021-06-15
-- Janice	Jones	17	2021-07-25
SELECT 
    c.first_name, c.last_name, s.sale_id, s.sale_date
FROM
    customer c,
    sale s
WHERE
    c.customer_numb = s.customer_numb
        AND c.contact_phone = '518-555-1111';
     
-- inner join
SELECT 
    c.first_name, c.last_name, s.sale_id, s.sale_date
FROM
    customer c
        INNER JOIN
    sale s ON c.customer_numb = s.customer_numb
WHERE
    c.contact_phone = '518-555-1111';
   
   
-- inner join with USING
SELECT 
    c.first_name, c.last_name, s.sale_id, s.sale_date
FROM
    customer c
        INNER JOIN
    sale s USING (customer_numb)
WHERE
    c.contact_phone = '518-555-1111';
   
-- Natural Join
SELECT 
    c.first_name, c.last_name, s.sale_id, s.sale_date
FROM
    customer c
        NATURAL JOIN
    sale s
WHERE
    c.contact_phone = '518-555-1111';
    
-- Self joins - joining a table to itself
-- Find customers that have purchased the books with ISBNs 
-- 978-1-11111-146-1 and 978-1-11111-122-1 in the same sale.
-- results
-- 	first_name	last_name	sale_id
-- 	Franklin	Hayes	6

SELECT 
    c.first_name, c.last_name, s.sale_id
FROM
    volume v1
        INNER JOIN
    volume v2 USING (sale_id)
        NATURAL JOIN
    sale s
        NATURAL JOIN
    customer c
WHERE
    v1.ISBN = '978-1-11111-146-1'
        AND v2.isbn = '978-1-11111-122-1';

SELECT 
    c.first_name, 
    c.last_name, 
    s.sale_id
FROM
    volume v1
    INNER JOIN volume v2 ON v1.sale_id = v2.sale_id
    INNER JOIN sale s ON v1.sale_id = s.sale_id
    INNER JOIN customer c ON s.customer_numb = c.customer_numb
WHERE
    v1.ISBN = '978-1-11111-146-1'
    AND v2.ISBN = '978-1-11111-122-1';


SELECT 
    c.first_name, c.last_name, s.sale_id
FROM
    volume v1
        INNER JOIN
    volume v2 USING (sale_id)
        JOIN
    sale s USING (sale_id)
        INNER JOIN
    customer c USING (customer_numb)
WHERE
    v1.ISBN = '978-1-11111-146-1'
        AND v2.ISBN = '978-1-11111-122-1';
        
-- Let's get rid of USING.  Using only works if the columns are named the same in each table
SELECT 
    c.first_name, c.last_name, s.sale_id
FROM
    volume v1
        INNER JOIN
    volume v2 USING (sale_id)
        JOIN
    sale s USING (sale_id)
        INNER JOIN
    customer c USING (customer_numb)
WHERE
    v1.ISBN = '978-1-11111-146-1'
        AND v2.ISBN = '978-1-11111-122-1';
        
        --  This =
SELECT 
    c.first_name, c.last_name, s.sale_id
FROM
    volume v1
        JOIN
    volume v2
        JOIN
    sale s ON v1.sale_id = s.sale_id
        AND v2.sale_id = s.sale_id
        JOIN
    customer c ON c.customer_numb = s.customer_numb
WHERE
    v1.ISBN = '978-1-11111-146-1'
        AND v2.ISBN = '978-1-11111-122-1';
        
-- --		LEFT JOIN
-- Retrieve all data from table 1, and and the matching records from the right table. Of course, 
-- tables are NOT immutable now.
-- If there is no match, leave some empties on left side.

SELECT 
    c.first_name, c.last_name, s.sale_id, s.sale_date
FROM
    customer c
        LEFT JOIN
    sale s USING (customer_numb);

-- RIGHT (outer) JOIN
-- It’s the opposite of Left Join - B RIGHT JOIN A is the same as A LEFT JOIN B
-- As a declarative language, Right Join simply makes the code more readable
SELECT 
    c.first_name, c.last_name, s.sale_id, s.sale_date
FROM
    customer c
        RIGHT JOIN
    sale s USING (customer_numb);
    
    
-- FULL OUTER JOIN
-- The FULL OUTER JOIN keyword returns all records when there is a match either in left (table1) or right (table2).
--  A.K.A, a union of Left and Right Join. MySql does not have FULL OUTER JOIN so you must use UNION to achieve
-- a FULL OUTER JOIN.

-- Select c.first_name, c.last_name, s.sale_id, s.sale_date
-- from customer c Full Outer join sale s using(customer_numb);
SELECT 
    c.first_name, c.last_name, s.sale_id, s.sale_date
FROM
    customer c
        LEFT JOIN
    sale s USING (customer_numb) 
UNION SELECT 
    c.first_name, c.last_name, s.sale_id, s.sale_date
FROM
    customer c
        RIGHT JOIN
    sale s USING (customer_numb);


-- FROM subquery - aka Table Constructors
-- find all volumes that were purchased by customer 6 and 10
-- 978-1-11111-121-1	Janice	Smith	5
-- 978-1-11111-141-1	Janice	Smith	14
-- 978-1-11111-141-1	Janice	Smith	14
-- 978-1-11111-128-1	Janice	Smith	19
-- 978-1-11111-136-1	Janice	Smith	19
-- 978-1-11111-130-1	Peter	Collins	12
-- 978-1-11111-132-1	Peter	Collins	12


-- Subquery (Inner Query):
-- The inner query selects information about customers (first_name, last_name) and their associated sales (sale_id) from the sale and customer tables.
-- It uses a NATURAL JOIN to join the sale and customer tables based on their common columns, which are likely related to the customer's purchase history.
-- The WHERE clause filters the results to include only customers with a customer number (customer_numb) of 6 or 10.

-- Main Query:
-- The main query selects columns from the volume table (v) and the results of the subquery (t).
-- It joins the volume table with the results of the subquery using a JOIN clause with the USING keyword, specifying the common column sale_id.
-- This join ensures that only volumes associated with sales made by customers with customer numbers 6 or 10 are included in the final result.

SELECT 
    v.isbn, t.first_name, t.last_name, v.sale_id
FROM
    volume v
        JOIN
    (SELECT 
        c.first_name, c.last_name, s.sale_id
    FROM
        sale s
    NATURAL JOIN customer c
    WHERE
        c.customer_numb = 6
            OR c.customer_numb = 10) t USING (sale_id);
		
-- Replacing Joins with Uncorrelated Subqueries
-- Find customers that have purchased the books with ISBNs
-- 978-1-11111-146-1 and 978-1-11111-122-1 in the same sale.
 --         Hayes	Franklin
 
 -- Let's break down the statement step by step:

-- Subquery (Inner Query):
-- The innermost subquery selects the sale_id from the volume table where the ISBN is '987-1-11111-122-1'.
-- This subquery is used to identify sales associated with the volume with ISBN '987-1-11111-122-1'.

-- Middle Subquery:
-- The middle subquery selects the sale_id from the volume table where the ISBN is '987-1-11111-146-1'.
-- It also filters the results to include only the sales that are present in the results of the innermost subquery.
-- This subquery is used to identify sales associated with the volume with ISBN '987-1-11111-146-1', which are also associated with the volume with ISBN '987-1-11111-122-1'.

-- Outer Subquery:
-- The outer subquery selects the customer_numb from the sale table where the sale ID is present in the results of the middle subquery.
-- It identifies customers who have made purchases of both volumes ('987-1-11111-146-1' and '987-1-11111-122-1').

-- Main Query:
-- The main query selects the last_name and first_name columns from the customer table.
-- It filters the results to include only customers whose customer_numb is present in the results of the outer subquery.
-- 
SELECT 
    last_name, first_name
FROM
    customer
WHERE
    customer_numb IN (SELECT 
            customer_numb
        FROM
            sale
        WHERE
            sale_id IN (SELECT 
                    sale_id
                FROM
                    volume
                WHERE
                    isbn = '978-1-11111-146-1'
                        AND sale_id IN (SELECT 
                            sale_id
                        FROM
                            volume
                        WHERE
                            isbn = '978-1-11111-122-1')));
            
-- inner query
SELECT 
    sale_id
FROM
    volume
WHERE
    isbn = '978-1-11111-122-1'; 
-- returns 6

-- Midle query
SELECT 
    sale_id
FROM
    volume
WHERE
    isbn = '978-1-11111-146-1'
        AND sale_id IN (SELECT 
            sale_id
        FROM
            volume
        WHERE
            isbn = '978-1-11111-122-1'); 
-- returns 6

-- 				UNIONS
-- Find the list of books published by Wiley and books that have been
-- purchased by customer number 11.

-- This SQL statement retrieves information about books purchased by a specific customer (customer number 11), including the author's name and the book's title. Let's break down the statement step by step:

-- Tables Involved:
-- The query involves multiple tables: work, book, author, sale, and volume.

-- JOINs:
-- The query uses implicit JOINs (comma-separated table names in the FROM clause) to join the tables together. This type of join is known as a cross join or Cartesian product, where every row from each table is combined with every row from every other table.
-- However, the conditions in the WHERE clause effectively filter out unwanted combinations, making the cross join act like an inner join.

-- Filtering Conditions:
-- The WHERE clause contains filtering conditions to restrict the result set.
-- s.customer_numb = 11: Filters the sales records to include only those belonging to customer number 11.
-- w.author_numb = a.author_numb: Matches the author number in the work table (w) with the author number in the author table (a).
-- w.work_numb = b.work_numb: Matches the work number in the work table (w) with the work number in the book table (b).
-- b.isbn = v.isbn: Matches the ISBN in the book table (b) with the ISBN in the volume table (v).
-- v.sale_id = s.sale_id: Matches the sale ID in the volume table (v) with the sale ID in the sale table (s).            

SELECT 
    a.author_last_first, w.title
FROM
    work w,
    book b,
    author a,
    publisher p
WHERE
    w.author_numb = a.author_numb
        AND w.work_numb = b.work_numb
        AND b.publisher_id = p.publisher_id
        AND p.publisher_name = 'Wiley' 
UNION SELECT 
    a.author_last_first, w.title
FROM
    work w,
    book b,
    author a,
    sale s,
    volume v
WHERE
    s.customer_numb = 11
        AND w.author_numb = a.author_numb
        AND w.work_numb = b.work_numb
        AND b.ISBN = v.ISBN
        AND v.sale_id = s.sale_id;

-- NEGATIVE QUERIES
-- Find the titles of all books for which there is no new copy (i.e., 
-- condition = 1) in stock.
SELECT DISTINCT
    w.title
FROM
    work w,
    book b
WHERE
    w.work_numb = b.work_numb
        AND b.ISBN NOT IN (SELECT 
            isbn
        FROM
            volume
        WHERE
            condition_code = 1);

-- EXISTS Operator (Oracle uses INTERSECT)
-- Find the title of all books that have at least one sale.

SELECT DISTINCT
    title
FROM
    work w
        INNER JOIN
    book b USING (work_numb)
        INNER JOIN
    volume v ON v.ISBN = b.ISBN
WHERE
    v.sale_id IS NOT NULL;

-- this produces the same results but using the EXISTS keyword.
SELECT DISTINCT
    w.title
FROM
    work w,
    book b
WHERE
    b.work_numb = w.work_numb
        AND EXISTS( SELECT 
            *
        FROM
            volume v
        WHERE
            b.ISBN = v.ISBN AND selling_price > 0);

-- NOT IN Operator (Oracle uses EXCEPT)
-- Find all of the customers except those who have made purchases with a total cost of $500 or more

SELECT 
    first_name, last_name
FROM
    customer
WHERE
    customer_numb NOT IN (SELECT 
            customer_numb
        FROM
            customer
                NATURAL JOIN
            sale
        WHERE
            sale_total_amt > 500)
ORDER BY first_name ASC;

 -- Same as
 
 -- Select first_name, last_name
--  from customer
--  except select customer_numb) from customers where sale_total_amt > 500 order by first_name asc;


-- 		EXISTS Operator (Oracle uses INTERSECT)
-- Find all of the customers who have made purchases with a total cost of $500 or more
-- note: this is also an example of a correlated sub-query

-- Notice! You don’t need to specify WHERE {customer_num} EXISTS. The EXISTS operator is used to 
-- test for the existence of any record, a.k.a the whole row in a subquery.

SELECT DISTINCT
    first_name, last_name
FROM
    customer c1
WHERE
    EXISTS( SELECT 
            customer_numb
        FROM
            customer c2
                NATURAL JOIN
            sale
        WHERE
            sale_total_amt > 500
                AND c1.customer_numb = c2.customer_numb)
ORDER BY first_name ASC;

-- same results as

SELECT 
    *
FROM
    customer c
        INNER JOIN
    sale s ON c.customer_numb = s.customer_numb
WHERE
    sale_total_amt > 500
ORDER BY first_name ASC;


-- 	Performing Arithmetic +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
-- Show all books for sale id 6 and a discounted price of .9 of their asking price
-- Arithmetic operators: +, -, *, / 
-- Precedence: unary + and - followed by * and / followed by + and –
-- 12 / 3  * 2 = 8
-- 12 / (3 * 2) = 2
-- 12 / (3 * (2 + 2)) = 1 

SELECT 
    isbn, asking_price, (asking_price * .9) AS discounted_price
FROM
    volume
WHERE
    sale_id = 6
ORDER BY discounted_price DESC
LIMIT 15;

-- String Concatenation Function
-- Concatenate first and last name
-- WARNING: ANSI (American National Standards Institute) SQL is ||, Microsoft SQL Server uses +, MySQL uses CONCAT


SELECT 
    CONCAT(last_name, ' ', first_name)
FROM
    customer
ORDER BY last_name , first_name ASC;


-- UPPER and LOWER Functions
-- Compare two upper case strings
-- WARNING: MySQL can be case sensitive or case insensitive, based on COLLATION settings! utf8_general_ci vs utf8_bin
-- Some databases are case sensitive (PostgreSQL), some are not (Oracle)

SELECT 
    customer_numb, first_name, last_name
FROM
    customer
WHERE
    UPPER(last_name) = 'SMITH';

-- TRIM function
-- Trim the leading characters from the ISBN and show title with publisher

SELECT 
    TRIM(LEADING '978-1-11111-' FROM isbn) AS last_4_isbn,
    title,
    publisher_name
FROM
    book
        NATURAL JOIN
    work
        NATURAL JOIN
    publisher
ORDER BY title ASC;

-- Here's why you don't need to specify a column to join explicitly:

-- Common Columns: NATURAL JOIN automatically matches columns in the joined tables that have the same name. 
-- In this case, the tables likely have columns with the same name that represent the relationship between them. 
-- For example, the book and work tables might both have a column named work_numb that represents the relationship 
-- between a book and its corresponding work.

-- Simplicity and Convenience: Using NATURAL JOIN simplifies the SQL statement by avoiding the need to specify the 
-- join conditions explicitly. This can make the SQL code cleaner and easier to read, especially for simple 
-- queries where the join conditions are straightforward.

-- Reduced Risk of Errors: By letting the database engine handle the join conditions automatically, 
-- there is less risk of errors in specifying the join conditions incorrectly. This can help avoid mistakes 
-- such as misspelling column names or forgetting to include necessary join conditions.

-- However, it's important to note that while NATURAL JOIN can be convenient for simple queries, 
-- it may not always be suitable for more complex join scenarios or when working with tables that 
-- have columns with the same name but different meanings. In such cases, it's recommended to use explicit JOIN syntax 
-- and specify the join conditions explicitly to ensure clarity and accuracy in the query.



-- SUBSTRING function ==============================================================================================================
-- Show the first character of customer's first name with last name
SELECT 
    SUBSTRING(first_name from 1 for 1) AS first_init, last_name
FROM
    customer;
    
-- with a concat
SELECT 
    CONCAT(SUBSTR(first_name FROM 1 FOR 1),
            '.',
            last_name) AS whole_name
FROM
    customer;
    
-- 			Date and Time System Values ==========================================================================================
-- Find all sales made after today
SELECT 
    first_name, last_name, sale_id, sale_date
FROM
    customer
        NATURAL JOIN
    sale
WHERE
    sale_date > CURRENT_DATE();
    
Select current_date() as date;

-- Date and Time Interval Operations
-- Find years to sale, months to sale and delivery date
SELECT 
    sale_id,
    CURRENT_DATE,
    sale_date,
    YEAR(sale_date) - YEAR(CURRENT_DATE) AS year_dif,
    TIMESTAMPDIFF(MONTH,
        CURRENT_DATE,
        sale_date) AS month_dif,
    DATE_ADD(sale_date, INTERVAL 7 DAY) AS delivery_date
FROM
    sale;
    
-- OVERLAPS operator (use BETWEEN in MySQL)
-- Check to see if two date ranges overlap
-- This example simply checks whether 2021-08-18 is overlapped with a date period ranging from 2021-08-16 to 2021-08-31. 
-- The 1 in result means TRUE

SELECT ('2021-08-18' BETWEEN '2021-08-16' AND '2021-08-31') AS overlaps;


-- EXTRACT operator
-- Extract the year from today’s date
SELECT 
    EXTRACT(YEAR FROM CURRENT_DATE) AS current_year,
    EXTRACT(MONTH FROM CURRENT_DATE) AS current_month,
    EXTRACT(DAY FROM CURRENT_DATE) AS current_day;
    
    
-- CASE EXPRESSIONS
-- Find the discount price of a book based on asking_price
SELECT 
    isbn,
    asking_price,
    CASE
        WHEN asking_price < 50 THEN round(asking_price * .95, 2)
        WHEN asking_price < 75 THEN round(asking_price * .9, 2)
        WHEN asking_price < 100 THEN round(asking_price * .8, 2)
        ELSE round(asking_price * .75, 2)
    END AS discounted_price
FROM
    volume;
    
-- Set / Aggregate Functions – COUNT()
select count(*)
from volume;
-- 	count(*)
-- 	70

select count(selling_price)
from volume;
-- 	count(selling_price)
-- 	42

select count(*)
from volume
where isbn = '978-1-11111-141-1';
-- 	count(*)
-- 	7

select count(*)
from volume
where sale_id = 6;
-- 	count(*)
-- 	5

select count(distinct isbn)
from volume;
-- 	count(distinct isbn)
-- 	27
    
    
-- Set / Aggregate Functions – SUM() and AVG()
    
select sum(selling_price)
from volume
where sale_id = 6;
-- 	sum(selling_price)
-- 	505.00

select sum(selling_price * .85)
from volume
where sale_id = 6;
-- 	sum(selling_price * .85)
-- 	429.2500

select sum(selling_price * .85) * 1.0725
from volume
where sale_id = 6;
-- 	sum(selling_price * .85) * 1.0725
-- 	460.37062500

select avg(selling_price)
from volume;
-- 	avg(selling_price)
-- 	68.070238

-- Set / Aggregate Functions – MIN() and MAX()
SELECT MAX(selling_price)
FROM volume;
-- 	MAX(selling_price)
-- 	285.00

SELECT MAX(sale_date)
FROM sale;
-- 	MAX(sale_date)
-- 	2021-10-13

SELECT MIN(last_name)
FROM customer;
-- 	MIN(last_name)
-- 	Brown

-- Set Functions in Predicates
-- Find the titles and cost of all books that were sold that cost more than the average cost of a book

SELECT 
    w.title, selling_price
FROM
    volume v
        INNER JOIN
    book b ON v.ISBN = b.ISBN
        INNER JOIN
    work w ON b.work_numb = w.work_numb
WHERE
    selling_price > (SELECT 
            AVG(selling_price)
        FROM
            volume);
            
-- this also works and look cleaner
SELECT 
    title, selling_price
FROM
    work w,
    book b,
    volume v
WHERE
    w.work_numb = b.work_numb
        AND b.ISBN = v.ISBN
        AND selling_price > (SELECT 
            AVG(selling_price)
        FROM
            volume);


-- Changing Data Types: CAST
-- Restrict the average price of books to two decimal places.
SELECT 
    AVG(selling_price) AS raw_avg,
    CAST(AVG(selling_price) AS DECIMAL (10 , 2 )) AS cast_avg
FROM
    volume; 

-- 	raw_avg	cast_avg
-- 	68.070238	68.07

-- Forming Groups ============================================================================================================== GROUPS
-- Find how many copies of each book edition are in the volume table

SELECT 
    isbn, COUNT(*) AS count
FROM
    volume
GROUP BY isbn
ORDER BY isbn ASC;

-- Groups with Multiple Columns
-- Find how many copies of each book edition have been sold by title

SELECT 
    b.work_numb, w.title, COUNT(*) AS count
FROM
    volume v,
    book b,
    work w
WHERE
    v.ISBN = b.ISBN
        AND b.work_numb = w.work_numb
GROUP BY b.work_numb , w.title
ORDER BY w.title;

-- Groups with SUM Aggregate and ROLLUP
-- Find the total costs of all sales for each customer, by day, with roll-up
-- Roll up is an extension of groupby. It is used as a super-aggregate that groups all NULL values together. 
-- Here in the example: customer 2 has some business with us without a sale date yet. And that are grouped together with ROLLUP.

SELECT 
    c.customer_numb,
    s.sale_date,
    SUM(selling_price) AS total_cost
FROM
    customer c,
    sale s,
    volume v
WHERE
    c.customer_numb = s.customer_numb
        AND s.sale_id = v.sale_id
GROUP BY c.customer_numb , s.sale_date WITH ROLLUP
ORDER BY c.customer_numb;

-- Groups and HAVING clause
-- Find customers that have spent more than $500
SELECT 
    c.customer_numb, SUM(selling_price) AS total_cost
FROM
    customer c,
    sale s,
    volume v
WHERE
    c.customer_numb = s.customer_numb
        AND s.sale_id = v.sale_id
GROUP BY c.customer_numb
HAVING total_cost > 500;
-- 	customer_numb	total_cost
-- 	1	903.00
-- 	12	505.00

-- Selection: Evaluate an Equation
SELECT 3, 'Wolf', 34.5, 0x34, 0+b'10111';

SELECT TRUE, FALSE;

SELECT 3+5, 18014398509481984*18014398509481984.0, ABS(-32), 6 & 3, 6 << 1; 

-- SELECT 18014398509481984*18014398509481984;

SET @name = 'Jane'; SELECT @name;

SELECT FALSE AND FALSE, FALSE AND TRUE;

SELECT 'Tom' IN ('Tom', 'Frank', 'Jane');


-- Data Modification - INSERT
-- Insert rows into customer and book tables

Insert into customer
values(default, 'Helen', 'Jerry', '16 Main Street', 'Newton', 'NJ', '18886', '209-555-888');

insert into book(isbn, work_numb, publisher_id, edition, copyright_year) values
('978-11111-100-1', 16, 2, 12, 1960);


-- Insert summary information about the volume table into summary table

CREATE TABLE summary (
    ISBN CHAR(17),
    how_many INT
);

INSERT INTO summary
SELECT isbn, count(*)
FROM volume
GROUP BY isbn;


-- Data Modification - UPDATE
-- Change a customer with customer_numb 5’s address to 195 Main Street in New Town, with zip code 11111
UPDATE customer 
SET 
    street = '195 Main Street',
    city = 'New Town',
    zip_postcode = '11111'
WHERE
    customer_numb = 5;


-- Raise the asking price of all volumes at $50 to $55
UPDATE volume 
SET 
    asking_price = 55
WHERE
    asking_price = 50;

-- Update a sales_tax column on the sale table
-- Note: sales_tax column does not exist and need to turn off safe update mode in MySQL
UPDATE sale 
SET 
    sales_tax = sale_total_amt * .75;

-- Data Modification - DELETE
-- Cancel an entire sale (fails)
DELETE FROM sale 
WHERE
    customer_numb = 12
    AND sale_date = '2021-07-05';

-- Error Code: 1451. Cannot delete or update a parent row: a foreign key constraint fails (`rarebooks`.`volume`, CONSTRAINT `SaleVolume` FOREIGN KEY (`sale_id`) REFERENCES `sale` (`sale_id`))
-- Must clean up volume with foreign key relationships first

DELETE FROM volume 
WHERE
    sale_id = (SELECT 
        sale_id
    FROM
        sale
    
    WHERE
        customer_numb = 12
        AND sale_date = '2021-07-05');


-- Delete all sales records
-- Both statements will fail if there are foreign keys that reference table
-- Table definition is still valid – just has zero rows
-- TRUNCATE TABLE more efficient – time and space wise


DELETE FROM sale;
Truncate table sale;



-- 	SQL coding style
-- SQL keywords are case-insensitive for most RDBMS, including MySQL. But all SQL keywords should be written in UPPER CASE.
-- For MySQL, column, index, stored routine, and event names are not case-sensitive on any platform, nor are column aliases.
-- snake_case is a widely used convention for column name and database name.
-- In contrast, LetterCase is widely used for table name.
-- Do not mix the usage of single and double quote.
-- Indent when you write sub-query.




'''




