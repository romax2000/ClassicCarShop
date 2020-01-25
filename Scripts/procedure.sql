CREATE OR REPLACE PROCEDURE INSERTCUSTOMER(p_userid IN CUSTOMERS."LOGIN_ID"%TYPE,
                                           p_fio IN CUSTOMERS."FIO"%TYPE,
                                           p_phone IN CUSTOMERS."PHONE"%TYPE,
                                           p_address IN CUSTOMERS."ADDRESS"%TYPE,
                                           p_email IN CUSTOMERS."EMAIL"%TYPE,
                                           p_person IN CUSTOMERS."PERSON"%TYPE) IS
BEGIN
 INSERT INTO CUSTOMERS(LOGIN_ID, FIO, PHONE, ADDRESS, EMAIL, PERSON) VALUES (p_userid, p_fio, p_phone, p_address, p_email, p_person);
 COMMIT;
END;
--провектка
DECLARE 
--переменные если хочешь просмотреть результат
BEGIN
--INSERTCUSTOMER(заполняешь все поля);
-- ну и DBMS_output
END;


CREATE OR REPLACE PROCEDURE DELETECUSTOMER(p_customerid IN CUSTOMERS."ID"%TYPE) IS
BEGIN
 DELETE FROM CUSTOMERS WHERE CUSTOMERS."ID" = p_customerid;
 COMMIT;
END;

CREATE OR REPLACE PROCEDURE UPDATECUSTOMER(p_userid IN CUSTOMERS."LOGIN_ID"%TYPE,
                                           p_fio IN CUSTOMERS."FIO"%TYPE,
                                           p_phone IN CUSTOMERS."PHONE"%TYPE,
                                           p_address IN CUSTOMERS."ADDRESS"%TYPE,
                                           p_email IN CUSTOMERS."EMAIL"%TYPE,
                                           p_person IN CUSTOMERS."PERSON"%TYPE) IS
BEGIN
 UPDATE CUSTOMERS SET CUSTOMERS."FIO" = p_fio, CUSTOMERS."PHONE" = p_phone, CUSTOMERS."ADDRESS" = p_address, CUSTOMERS."EMAIL" = p_email, CUSTOMERS."PERSON" = p_person
 WHERE CUSTOMERS."LOGIN_ID" = p_userid;
 COMMIT;
END;

--CAR
CREATE OR REPLACE PROCEDURE INSERTCAR(p_mark IN CARS."MARK"%TYPE,
                                           p_model IN CARS."MODEL"%TYPE,
                                           p_carcass IN CARS."CARCASS"%TYPE,
                                           p_years_of_productions IN CARS."YEARS_OF_PRODUCTIONS"%TYPE,
                                           p_engines IN CARS."ENGINES"%TYPE,
                                           p_transmissions IN CARS."TRANSMISSIONS"%TYPE,
                                           p_drive_units IN CARS."DRIVE_UNITS"%TYPE) IS
BEGIN
 INSERT INTO CARS(MARK, MODEL, CARCASS, YEARS_OF_PRODUCTIONS, ENGINES, TRANSMISSIONS, DRIVE_UNITS ) VALUES (p_mark, p_model, p_carcass, p_years_of_productions, p_engines, p_transmissions, p_drive_units);
 COMMIT;
END;

CREATE OR REPLACE PROCEDURE DELETECAR(p_carid IN CARS."ID"%TYPE) IS
BEGIN
 DELETE FROM CARS WHERE CARS."ID" = p_carid;
 COMMIT;
END;

CREATE OR REPLACE PROCEDURE UPDATECAR(p_carid IN CARS."ID"%TYPE,
                                            p_mark IN CARS."MARK"%TYPE,
                                           p_model IN CARS."MODEL"%TYPE,
                                           p_carcass IN CARS."CARCASS"%TYPE,
                                           p_years_of_productions IN CARS."YEARS_OF_PRODUCTIONS"%TYPE,
                                           p_engines IN CARS."ENGINES"%TYPE,
                                           p_transmissions IN CARS."TRANSMISSIONS"%TYPE,
                                           p_drive_units IN CARS."DRIVE_UNITS"%TYPE) IS
BEGIN
 UPDATE CARS SET CARS."MARK" = p_mark, CARS."MODEL" = p_model, CARS."CARCASS" = p_carcass, CARS."YEARS_OF_PRODUCTIONS" = p_years_of_productions, CARS."ENGINES" = p_engines, CARS."TRANSMISSIONS" = p_transmissions, CARS."DRIVE_UNITS" = p_transmissions
 WHERE CARS."ID" = p_carid;
 COMMIT;
END;

--DELIVER
CREATE OR REPLACE PROCEDURE INSERTDELIVER(p_shipperid IN DELIVERIES."SHIPPER_ID"%TYPE,
                                           p_carid IN DELIVERIES."CAR_ID"%TYPE,
                                           p_date_order IN DELIVERIES."DATE_ORDER"%TYPE,
                                           p_cost IN DELIVERIES."COST"%TYPE) IS
BEGIN
 INSERT INTO DELIVERIES(SHIPPER_ID, CAR_ID, DATE_ORDER, COST ) VALUES (p_shipperid, p_carid, p_date_order, p_cost);
 COMMIT;
END;


CREATE OR REPLACE PROCEDURE DELETEDELIVER(p_deliverid IN DELIVERIES."ID"%TYPE) IS
BEGIN
 DELETE FROM DELIVERIES WHERE DELIVERIES."ID" = p_deliverid;
 COMMIT;
END;

CREATE OR REPLACE PROCEDURE UPDATEDELIVER(p_deliverid IN DELIVERIES."ID"%TYPE,
                                            p_shipperid IN DELIVERIES."SHIPPER_ID"%TYPE,
                                           p_carid IN DELIVERIES."CAR_ID"%TYPE,
                                           p_date_order IN DELIVERIES."DATE_ORDER"%TYPE,
                                           p_cost IN DELIVERIES."COST"%TYPE) IS
BEGIN
 UPDATE DELIVERIES SET DELIVERIES."SHIPPER_ID" = p_shipperid, DELIVERIES."CAR_ID" = p_carid, DELIVERIES."DATE_ORDER" = p_date_order, DELIVERIES."COST" = p_cost
 WHERE DELIVERIES."ID" = p_deliverid;
 COMMIT;
END;

--MYCAR
CREATE OR REPLACE PROCEDURE INSERTMYCAR(p_carid IN MYCARS."CAR_ID"%TYPE,
                                        p_car_body IN MYCARS."CAR_BODY"%TYPE,
                                        p_car_year IN MYCARS."CAR_YEAR"%TYPE,
                                        p_engine IN MYCARS."ENGINE"%TYPE,
                                        p_transmission IN MYCARS."TRANSMISSION"%TYPE,
                                        p_drive_unit IN MYCARS."DRIVE_UNIT"%TYPE,
                                        p_color IN MYCARS."COLOR"%TYPE,
                                        p_mileage IN MYCARS."MILEAGE"%TYPE,
                                        p_identification_number IN MYCARS."IDENTIFICATION_NUMBER"%TYPE,
                                        p_cost IN MYCARS."COST"%TYPE,
                                        p_photos IN MYCARS."PHOTOS"%TYPE,
                                        p_date_of_delivery IN MYCARS."DATE_OF_DELIVERY"%TYPE,
                                        p_description IN MYCARS."DESCRIPTION"%TYPE,
                                        p_options IN MYCARS."OPTIONS"%TYPE,
                                        p_visible IN MYCARS."VISIBLE"%TYPE,
                                        p_slug IN MYCARS."SLUG"%TYPE,
                                        p_imageb IN MYCARS."IMAGEB"%TYPE) IS
BEGIN
 INSERT INTO MYCARS(CAR_ID, CAR_BODY, CAR_YEAR, ENGINE, TRANSMISSION, DRIVE_UNIT, COLOR, MILEAGE, IDENTIFICATION_NUMBER, COST, PHOTOS, DATE_OF_DELIVERY, DESCRIPTION, OPTIONS, VISIBLE, SLUG, IMAGEB)
 VALUES (p_carid, p_car_body, p_car_year, p_engine, p_transmission, p_drive_unit, p_color, p_mileage, p_identification_number, p_cost, p_photos, p_date_of_delivery, p_description, p_options, p_visible, p_slug, p_imageb);
 COMMIT;
END;


CREATE OR REPLACE PROCEDURE DELETEMYCAR(p_carid IN MYCARS."ID"%TYPE) IS
BEGIN
 DELETE FROM MYCARS WHERE MYCARS."ID" = p_carid;
 COMMIT;
END;

CREATE OR REPLACE PROCEDURE UPDATEMYCAR(p_carid IN MYCARS."ID"%TYPE,
                                        p_car_id IN MYCARS."CAR_ID"%TYPE,
                                           p_car_body IN MYCARS."CAR_BODY"%TYPE,
                                        p_car_year IN MYCARS."CAR_YEAR"%TYPE,
                                        p_engine IN MYCARS."ENGINE"%TYPE,
                                        p_transmission IN MYCARS."TRANSMISSION"%TYPE,
                                        p_drive_unit IN MYCARS."DRIVE_UNIT"%TYPE,
                                        p_color IN MYCARS."COLOR"%TYPE,
                                        p_mileage IN MYCARS."MILEAGE"%TYPE,
                                        p_identification_number IN MYCARS."IDENTIFICATION_NUMBER"%TYPE,
                                        p_cost IN MYCARS."COST"%TYPE,
                                        p_photos IN MYCARS."PHOTOS"%TYPE,
                                        p_date_of_delivery IN MYCARS."DATE_OF_DELIVERY"%TYPE,
                                        p_description IN MYCARS."DESCRIPTION"%TYPE,
                                        p_options IN MYCARS."OPTIONS"%TYPE,
                                        p_visible IN MYCARS."VISIBLE"%TYPE,
                                        p_slug IN MYCARS."SLUG"%TYPE,
                                        p_imageb IN MYCARS."IMAGEB"%TYPE) IS
BEGIN
 UPDATE MYCARS SET MYCARS."CAR_ID" = p_car_id, MYCARS."CAR_BODY" = p_car_body, MYCARS."CAR_YEAR" = p_car_year, MYCARS."ENGINE" = p_engine, MYCARS."TRANSMISSION" = p_transmission, MYCARS."DRIVE_UNIT" = p_drive_unit, 
 MYCARS."COLOR" = p_color, MYCARS."MILEAGE" = p_mileage, MYCARS."IDENTIFICATION_NUMBER" = p_identification_number, MYCARS."COST" = p_cost, MYCARS."PHOTOS" = p_photos, MYCARS."DATE_OF_DELIVERY" = p_date_of_delivery,
 MYCARS."DESCRIPTION" = p_description, MYCARS."OPTIONS" = p_options, MYCARS."VISIBLE" = p_visible, MYCARS."SLUG" = p_slug, MYCARS."IMAGEB" = p_imageb 
 WHERE MYCARS."ID" = p_carid;
 COMMIT;
END;

--ORDER
CREATE OR REPLACE PROCEDURE INSERTORDER(p_request_id IN ORDERS."REQUEST_ID"%TYPE,
                                           p_order_status IN ORDERS."ORDER_STATUS"%TYPE,
                                           p_start_date IN ORDERS."START_DATE"%TYPE,
                                           p_end_date IN ORDERS."END_DATE"%TYPE) IS
BEGIN
 INSERT INTO ORDERS(REQUEST_ID, ORDER_STATUS, START_DATE, END_DATE ) VALUES (p_request_id, p_order_status, p_start_date, p_end_date);
 COMMIT;
END;


CREATE OR REPLACE PROCEDURE DELETEORDER(p_orderid IN ORDERS."ID"%TYPE) IS
BEGIN
 DELETE FROM ORDERS WHERE ORDERS."ID" = p_orderid;
 COMMIT;
END;

CREATE OR REPLACE PROCEDURE UPDATEORDER(p_orderid IN ORDERS."ID"%TYPE,
                                        p_request_id IN ORDERS."REQUEST_ID"%TYPE,
                                           p_order_status IN ORDERS."ORDER_STATUS"%TYPE,
                                           p_start_date IN ORDERS."START_DATE"%TYPE,
                                           p_end_date IN ORDERS."END_DATE"%TYPE) IS                       
BEGIN
 UPDATE ORDERS SET  ORDERS."REQUEST_ID" = p_request_id, ORDERS."ORDER_STATUS" = p_order_status, ORDERS."START_DATE" = p_start_date, ORDERS."END_DATE" = p_start_date
 WHERE ORDERS."ID" = p_orderid;
 COMMIT;
END;

--REQUEST
CREATE OR REPLACE PROCEDURE INSERTREQUEST(p_car_id IN REQUESTS."CAR_ID"%TYPE,
                                        p_date_request IN REQUESTS."DATE_REQUEST"%TYPE,
                                        p_customer_id IN REQUESTS."CUSTOMER_ID"%TYPE,
                                        p_request_status IN REQUESTS."REQUEST_STATUS"%TYPE,
                                        p_delivery IN REQUESTS."DELIVERY"%TYPE,
                                        p_delivery_address IN REQUESTS."DELIVERY_ADDRESS"%TYPE,
                                        p_cost IN REQUESTS."COST"%TYPE) IS
BEGIN
 INSERT INTO REQUESTS(CAR_ID, DATE_REQUEST, CUSTOMER_ID, REQUEST_STATUS, DELIVERY, DELIVERY_ADDRESS, COST)
 VALUES (p_car_id, p_date_request, p_customer_id, p_request_status, p_delivery, p_delivery_address, p_cost);
 COMMIT;
END;

CREATE OR REPLACE PROCEDURE DELETEREQUEST(p_requestid IN REQUESTS."ID"%TYPE) IS
BEGIN
 DELETE FROM REQUESTS WHERE REQUESTS."ID" = p_requestid;
 COMMIT;
END;

CREATE OR REPLACE PROCEDURE UPDATEREQUEST(p_requestid IN REQUESTS."ID"%TYPE,
                                        p_car_id IN REQUESTS."CAR_ID"%TYPE,
                                        p_date_request IN REQUESTS."DATE_REQUEST"%TYPE,
                                        p_customer_id IN REQUESTS."CUSTOMER_ID"%TYPE,
                                        p_request_status IN REQUESTS."REQUEST_STATUS"%TYPE,
                                        p_delivery IN REQUESTS."DELIVERY"%TYPE,
                                        p_delivery_address IN REQUESTS."DELIVERY_ADDRESS"%TYPE,
                                        p_cost IN REQUESTS."COST"%TYPE) IS
                                                                   
BEGIN
 UPDATE REQUESTS SET  REQUESTS."CAR_ID" = p_car_id, REQUESTS."DATE_REQUEST" = p_date_request, REQUESTS."CUSTOMER_ID" = p_customer_id, REQUESTS."REQUEST_STATUS" = p_request_status, REQUESTS."DELIVERY" = p_delivery, 
 REQUESTS."DELIVERY_ADDRESS" = p_delivery_address,  REQUESTS."COST" = p_cost
 WHERE REQUESTS."ID" = p_requestid;
 COMMIT;
END;


--SUPPLIERS
CREATE OR REPLACE PROCEDURE INSERTSUPPLIER(p_name IN SUPPLIERS."NAME"%TYPE,
                                           p_address IN SUPPLIERS."ADDRESS"%TYPE,
                                           p_phone IN SUPPLIERS."PHONE"%TYPE,
                                           p_email IN SUPPLIERS."EMAIL"%TYPE) IS
BEGIN
 INSERT INTO SUPPLIERS(NAME, ADDRESS, PHONE, EMAIL ) VALUES (p_name, p_address, p_phone, p_email);
 COMMIT;
END;

CREATE OR REPLACE PROCEDURE DELETESUPPLIER(p_supplierid IN SUPPLIERS."ID"%TYPE) IS
BEGIN
 DELETE FROM SUPPLIERS WHERE SUPPLIERS."ID" = p_supplierid;
 COMMIT;
END;

CREATE OR REPLACE PROCEDURE UPDATESUPPLIER(p_supplierid IN SUPPLIERS."ID"%TYPE,
                                            p_name IN SUPPLIERS."NAME"%TYPE,
                                           p_address IN SUPPLIERS."ADDRESS"%TYPE,
                                           p_phone IN SUPPLIERS."PHONE"%TYPE,
                                           p_email IN SUPPLIERS."EMAIL"%TYPE) IS
                                                                   
BEGIN
 UPDATE SUPPLIERS SET  SUPPLIERS."NAME" = p_name, SUPPLIERS."ADDRESS" = p_address, SUPPLIERS."PHONE"= p_phone, SUPPLIERS."EMAIL" = p_email
 WHERE SUPPLIERS."ID" = p_supplierid;
 COMMIT;
END;

--USER
CREATE OR REPLACE PROCEDURE INSERTUSER(p_login IN USERS."LOGIN"%TYPE,
                                           p_password IN USERS."PASSWORD"%TYPE,
                                           p_user_type IN USERS."USER_TYPE"%TYPE) IS
BEGIN
 INSERT INTO USERS(LOGIN, PASSWORD, USER_TYPE ) VALUES (p_login, p_password, p_user_type);
 COMMIT;
END;

CREATE OR REPLACE PROCEDURE DELETEUSER(p_userid IN USERS."ID"%TYPE) IS
BEGIN
 DELETE FROM USERS WHERE USERS."ID" = p_userid;
 COMMIT;
END;

CREATE OR REPLACE PROCEDURE UPDATEUSER(p_userid IN USERS."ID"%TYPE,
                                        p_login IN USERS."LOGIN"%TYPE,
                                           p_password IN USERS."PASSWORD"%TYPE,
                                           p_user_type IN USERS."USER_TYPE"%TYPE) IS 
BEGIN
 UPDATE USERS SET  USERS."LOGIN" = p_login, USERS."PASSWORD" = p_password, USERS."USER_TYPE" = p_user_type
 WHERE USERS."ID" = p_userid;
 COMMIT;
END;


create or replace directory XML_DIR as 'd:\Dokuments\XML'

--IMPORT XML
create or replace procedure table_to_xml_file(table_name in varchar2) as
ctx dbms_xmlgen.ctxhandle;
clb clob;
file utl_file.file_type;
buffer varchar2(32767);
position pls_integer := 1;
chars pls_integer := 32767;
begin
ctx := dbms_xmlgen.newcontext('select * from "' || table_name || '"');
dbms_xmlgen.setrowsettag(ctx, 'RECORDS');
dbms_xmlgen.setrowtag(ctx, 'RECORD');

select xmlserialize(document
xmlelement("XML",
xmlelement(evalname(table_name),
dbms_xmlgen.getxmltype(ctx)))
indent size = 2)
into clb
from dual;

dbms_xmlgen.closecontext(ctx);

file := utl_file.fopen('XML_DIR', table_name || '.xml', 'w', 32767);
while position < dbms_lob.getlength(clb) loop
dbms_lob.read(clb, chars, position, buffer);
utl_file.put(file, buffer);
utl_file.fflush(file);
position := position + chars;
end loop;
utl_file.fclose(file);
commit;
end table_to_xml_file;


--EXPORT

DECLARE
xml_file BFILE;
xml_data CLOB;
BEGIN
xml_file := BFILENAME ('XML_DIR', 'USERS.xml');
DBMS_LOB.createtemporary (xml_data, TRUE, DBMS_LOB.SESSION);
DBMS_LOB.fileopen (xml_file, DBMS_LOB.file_readonly);
DBMS_LOB.loadfromfile (xml_data, xml_file, DBMS_LOB.getlength(xml_file));
DBMS_LOB.fileclose (xml_file);
INSERT INTO USERS (login,password,user_type)
SELECT ExtractValue(Value(x),'//LOGIN') as login,
ExtractValue(Value(x),'//PASSWORD') as password, ExtractValue(Value(x),'//USER_TYPE') as user_type
FROM TABLE(XMLSequence(Extract(XMLType(xml_data),'/XML/USERS/RECORDS/RECORD'))) x;
DBMS_OUTPUT.PUT_LINE( SQL%ROWCOUNT || ' rows inserted.' );
DBMS_LOB.freetemporary (xml_data);
COMMIT;
END;

