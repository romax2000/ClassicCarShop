CREATE TABLE "USERS" (
	"id" INT NOT NULL,
	"login" VARCHAR2(20) UNIQUE NOT NULL,
	"password" VARCHAR2(30) NOT NULL,
	"type" VARCHAR2(10) NOT NULL,
	constraint USERS_PK PRIMARY KEY ("id"));

CREATE sequence "USERS_ID_SEQ";

CREATE trigger "BI_USERS_ID"
  before insert on "USERS"
  for each row
begin
  select "USERS_ID_SEQ".nextval into :NEW."id" from dual;
end;

/
CREATE TABLE "CUSTOMERS" (
	"id" INT NOT NULL,
	"login_id" INT UNIQUE NOT NULL,
	"fio" VARCHAR2(200),
	"phone" VARCHAR2(20),
	"address" VARCHAR2(200),
	"email" VARCHAR2(100),
	"person" VARCHAR2(15),
	constraint CUSTOMERS_PK PRIMARY KEY ("id"));

CREATE sequence "CUSTOMERS_ID_SEQ";

CREATE trigger "BI_CUSTOMERS_ID"
  before insert on "CUSTOMERS"
  for each row
begin
  select "CUSTOMERS_ID_SEQ".nextval into :NEW."id" from dual;
end;

/
CREATE TABLE "CARS" (
	"id" INT UNIQUE NOT NULL,
	"mark" VARCHAR2(30) NOT NULL,
	"model" VARCHAR2(60) NOT NULL,
	"carcass" VARCHAR2(100) NOT NULL,
	"years_of_production" VARCHAR2(10) NOT NULL,
	"engines" VARCHAR2(50) NOT NULL,
	"transmissions" VARCHAR2(50) NOT NULL,
	"drive_units" VARCHAR2(20) NOT NULL,
	constraint CARS_PK PRIMARY KEY ("id"));

CREATE sequence "CARS_ID_SEQ";

CREATE trigger "BI_CARS_ID"
  before insert on "CARS"
  for each row
begin
  select "CARS_ID_SEQ".nextval into :NEW."id" from dual;
end;

/
CREATE TABLE "REQUESTS" (
	"id" INT NOT NULL,
	"car_id" INT NOT NULL,
	"date_request" DATE NOT NULL,
	"customer_id" INT NOT NULL,
	"status" VARCHAR2(20) NOT NULL,
	"delivery" CHAR(1) CHECK ("delivery" IN ('N','Y')) NOT NULL,
	"delivery_address" VARCHAR2(200),
	"cost" FLOAT NOT NULL,
	constraint REQUESTS_PK PRIMARY KEY ("id"));

CREATE sequence "REQUESTS_ID_SEQ";

CREATE trigger "BI_REQUESTS_ID"
  before insert on "REQUESTS"
  for each row
begin
  select "REQUESTS_ID_SEQ".nextval into :NEW."id" from dual;
end;

/
CREATE TABLE "ORDERS" (
	"id" INT NOT NULL,
	"request_id" INT NOT NULL,
	"status" VARCHAR2(20) NOT NULL,
	"start_date" DATE,
	"end_date" DATE,
	constraint ORDERS_PK PRIMARY KEY ("id"));

CREATE sequence "ORDERS_ID_SEQ";

CREATE trigger "BI_ORDERS_ID"
  before insert on "ORDERS"
  for each row
begin
  select "ORDERS_ID_SEQ".nextval into :NEW."id" from dual;
end;

/
CREATE TABLE "MYCARS" (
	"id" INT NOT NULL,
	"car_id" INT NOT NULL,
	"body" VARCHAR2(20) NOT NULL,
	"year" VARCHAR2(4) NOT NULL,
	"engine" VARCHAR2(20) NOT NULL,
	"transmission" VARCHAR2(20) NOT NULL,
	"drive_unit" VARCHAR2(5) NOT NULL,
	"color" VARCHAR2(25) NOT NULL,
	"mileage" INT,
	"identification_number" VARCHAR2(20) NOT NULL,
	"cost" FLOAT,
	"photos" VARCHAR2(255),
	"date_of _delivery" DATE,
	"description" VARCHAR2(2000),
	"options" VARCHAR2(200),
	constraint MYCARS_PK PRIMARY KEY ("id"));

CREATE sequence "MYCARS_ID_SEQ";

CREATE trigger "BI_MYCARS_ID"
  before insert on "MYCARS"
  for each row
begin
  select "MYCARS_ID_SEQ".nextval into :NEW."id" from dual;
end;

/
CREATE TABLE "DELIVERIES" (
	"id" INT NOT NULL,
	"shipper_id" INT NOT NULL,
	"car_id" INT NOT NULL,
	"date_order" DATE,
	"cost" FLOAT,
	constraint DELIVERIES_PK PRIMARY KEY ("id"));

CREATE sequence "DELIVERIES_ID_SEQ";

CREATE trigger "BI_DELIVERIES_ID"
  before insert on "DELIVERIES"
  for each row
begin
  select "DELIVERIES_ID_SEQ".nextval into :NEW."id" from dual;
end;

/
CREATE TABLE "SUPPLIERS" (
	"id" INT NOT NULL,
	"name" VARCHAR2(50) NOT NULL,
	"address" VARCHAR2(200),
	"phone" VARCHAR2(20),
	"email" VARCHAR2(100),
	constraint SUPPLIERS_PK PRIMARY KEY ("id"));

CREATE sequence "SUPPLIERS_ID_SEQ";

CREATE trigger "BI_SUPPLIERS_ID"
  before insert on "SUPPLIERS"
  for each row
begin
  select "SUPPLIERS_ID_SEQ".nextval into :NEW."id" from dual;
end;

/

ALTER TABLE "CUSTOMERS" ADD CONSTRAINT "CUSTOMERS_fk0" FOREIGN KEY ("login_id") REFERENCES "USERS"("id");


ALTER TABLE "REQUESTS" ADD CONSTRAINT "REQUESTS_fk0" FOREIGN KEY ("car_id") REFERENCES "MYCARS"("id");
ALTER TABLE "REQUESTS" ADD CONSTRAINT "REQUESTS_fk1" FOREIGN KEY ("customer_id") REFERENCES "CUSTOMERS"("id");

ALTER TABLE "ORDERS" ADD CONSTRAINT "ORDERS_fk0" FOREIGN KEY ("request_id") REFERENCES "REQUESTS"("id");

ALTER TABLE "MYCARS" ADD CONSTRAINT "MYCARS_fk0" FOREIGN KEY ("car_id") REFERENCES "DELIVERIES"("id");

ALTER TABLE "DELIVERIES" ADD CONSTRAINT "DELIVERIES_fk0" FOREIGN KEY ("shipper_id") REFERENCES "SUPPLIERS"("id");
ALTER TABLE "DELIVERIES" ADD CONSTRAINT "DELIVERIES_fk1" FOREIGN KEY ("car_id") REFERENCES "CARS"("id");


