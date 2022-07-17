import errno
import mysql.connector

(config = {
	"user": "pysports_user",
	"password": "MYSQL8IsGreat!",
	"host : "127.0.0.1",
	"database": "pysports",
	"raise_on_warnings" = True
}
)
db = mysql.connector.connect(**config)
	
	print("\n Database user {} connected to MySQL on host {} with database {}".formart(config["user"], config["host"], config("database"]))

	input("\n\n press any key to continue...")

except mysql.connector.Error as err;
	if err.errno == errorcode.ER_ACCESS.DENIED_ERROR;
		print(* The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print(* The supplied username or password are invalid)
	else:
		print(err)

finally:
	db.close()