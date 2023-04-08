# g-test
Giooooooooooooooo

## Try it out


1. Start a mysql instance
```
docker run --name test-mysql -e MYSQL_ROOT_PASSWORD=secret-g -p 3307:3306  -d mysql:latest
```
2. Make some tables

```sql
CREATE SCHEMA test_houses;

USE test_houses;

CREATE TABLE person (
 person_id INTEGER PRIMARY KEY,
 name VARCHAR(200)
);

CREATE TABLE house (
  house_id INTEGER PRIMARY KEY,
  name VARCHAR(200)
);

CREATE TABLE person_house (
 person_house_id INTEGER PRIMARY KEY,
 house_id INT REFERENCES house(house_id),
 person_id INT REFERENCES person(person_id)
);
```

3. Make some data
```sql
# person
INSERT INTO person VALUES(1,'Joe');
INSERT INTO person VALUES(2,'Jerry');
INSERT INTO person VALUES(3,'Jamille');
# house
INSERT INTO house VALUES(1,'Detroit');
INSERT INTO house VALUES(2,'Chicago');
INSERT INTO house VALUES(3,'New York');
INSERT INTO house VALUES(4,'Boston');
# junction
INSERT INTO person_house VALUES(1,1,3);
INSERT INTO person_house VALUES(2,2,3);
INSERT INTO person_house VALUES(3,3,3);
INSERT INTO person_house VALUES(4,1,2);
```

4. Make a sproc

```sql
DELIMITER //
DROP PROCEDURE IF EXISTS how_many_houses;
CREATE PROCEDURE how_many_houses (IN person_name CHAR(20), OUT houses INT)
       BEGIN
         SELECT COUNT(*)
         INTO houses
         FROM house h 
           join person_house ph ON ph.house_id = h.house_id
           join person p ON ph.person_id = p.person_id
     WHERE p.name = person_name;
       END //
       
DELIMITER ; 
```

5. Call the sproc
```sql
CALL how_many_houses('Jamille', @houses);

SELECT @houses;
```

6. Python
```
pip3 install mysql-connector-python
```

7. Working example
```
python3 mysqlsproc.py
-- yosefrats-MacBook-Pro:g-test yosefrat$ python3 mysqlsproc.py 
-- Jamille has 3 houses
```

