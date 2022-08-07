

DROP USER 'whatabook_user'@'localhost';


CREATE USER 'whatabook_user'@'localhost' IDENTIFIED BY 'MySQL8IsGreat!';

USE mysql;
CREATE USER 'whatabook_user'@'localhost' IDENTIFIED BY 'MySQL8IsGreat!';
GRANT ALL PRIVILEGES ON whatabook.* TO'whatabook_user'@'localhost';



CREATE TABLE store (
 store_id INT NOT NULL AUTO_INCREMENT,
 locale VARCHAR(500) NOT NULL,
 PRIMARY KEY(store_id)
);

INSERT INTO store (store_id, locale)
 VALUES('1', '900 Gregory Ln Grand Prairie Tx 75050');


CREATE TABLE book (
 book_id INT NOT NULL AUTO_INCREMENT,
 book_name VARCHAR(200) NOT NULL,
 author VARCHAR(200)  NOT NULL,
 PRIMARY KEY(book_id)
);

INSERT INTO book (book_id, book_name, author)
 VALUES('1', 'Return to Phoenix', 'Anna Roberts');

INSERT INTO book (book_id, book_name, author)
 VALUES('2', 'Lion and the Jewel', 'Wole Soyinka');

INSERT INTO book (book_id, book_name, author)
 VALUES('3', 'The gods are not to Blame', 'Ola Rotimi');

INSERT INTO book (book_id, book_name, author)
 VALUES('4', 'The Tragedy of Macbeth', 'William Shakespeare');

INSERT INTO book (book_id, book_name, author)
 VALUES('5', 'The Adventures of Huckleberry Finn', 'Mark Twain');

INSERT INTO book (book_id, book_name, author)
 VALUES('6', 'The Adventures of Tom Sawyer', 'Mark Twain');

INSERT INTO book (book_id, book_name, author)
 VALUES('7', 'King Solomons Mines', 'H. Rider Haggard');

INSERT INTO book (book_id, book_name, author)
 VALUES('8', 'Alice Adventures in Wonderland', 'Lewis Carroll');

INSERT INTO book (book_id, book_name, author)
 VALUES('9', 'Go Tell It on the Mountain', 'James Baldwin');




CREATE TABLE user (
 user_id INT NOT NULL AUTO_INCREMENT,
 first_name VARCHAR(75) NOT NULL,
 last_name VARCHAR(75) NOT NULL,
 PRIMARY KEY(user_id)
);


INSERT INTO user (user_id, first_name, last_name)
 VALUES('1', 'Jacob', 'Lulu');

INSERT INTO user (user_id, first_name, last_name)
 VALUES('2', 'Billy', 'Boy');

INSERT INTO user (user_id, first_name, last_name)
 VALUES('3', 'Henry', 'Townsend');



CREATE TABLE wishlist (
 wishlist_id INT NOT NULL AUTO_INCREMENT,
 user_id INT NOT NULL,
 book_id INT NOT NULL ,
 PRIMARY KEY(wishlist_id),
 CONSTRAINT fk_user
 FOREIGN KEY(user_id)
 REFERENCES user(user_id)
);


INSERT INTO wishlist (wishlist_id, user_id, book_id)
 VALUES('1', '3', '9');

INSERT INTO wishlist (wishlist_id, user_id, book_id)
 VALUES('2', '2', '5');

INSERT INTO wishlist (wishlist_id, user_id, book_id)
 VALUES('3', '1', '7');



CREATE TABLE bookavailable (
 bookavailable_id INT NOT NULL AUTO_INCREMENT,
 book_id INT NOT NULL ,
 store_id INT NOT NULL,
 quantity INT NOT NULL,
 PRIMARY KEY(bookavailable_id),
 CONSTRAINT fk_store
 FOREIGN KEY(store_id)
 REFERENCES store(store_id)
);