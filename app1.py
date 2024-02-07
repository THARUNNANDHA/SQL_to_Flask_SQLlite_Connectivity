# from flask import Flask, jsonify
# from sqlalchemy import create_engine, Column, Integer, String, DateTime
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker
# from apscheduler.schedulers.background import BackgroundScheduler
# from datetime import datetime

# app = Flask(__name__)

# # MySQL Database Configuration
# app.config['MYSQL_HOST'] = '192.168.137.183'
# app.config['MYSQL_USER'] = 'sabari'
# app.config['MYSQL_PASSWORD'] = '12345678'
# app.config['MYSQL_DB'] = 'server'

# # SQLite Database Configuration
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///attendance_data.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# mysql_engine = create_engine(
#     f"mysql://{app.config['MYSQL_USER']}:{app.config['MYSQL_PASSWORD']}@{app.config['MYSQL_HOST']}/{app.config['MYSQL_DB']}",
#     echo=True
# )

# sqlite_engine = create_engine('sqlite:///attendance_data.db', echo=True)
# Base = declarative_base()

# class Attendance(Base):
#     __tablename__ = 'Attendance'

#     id = Column(Integer, primary_key=True)
#     emp_id = Column(Integer)
#     intime = Column(DateTime)
#     outtime = Column(DateTime)
#     shift = Column(String(255))

# # Create SQLite table
# Base.metadata.create_all(sqlite_engine)

# # Function to fetch data from MySQL and store it in SQLite
# def fetch_and_store_data():
#     SessionMySQL = sessionmaker(bind=mysql_engine)
#     session_mysql = SessionMySQL()

#     # Assume 'Attendance' table already exists in the MySQL database
#     mysql_data = session_mysql.query(Attendance).all()

#     SessionSQLite = sessionmaker(bind=sqlite_engine)
#     session_sqlite = SessionSQLite()

#     for record in mysql_data:
#         sqlite_record = Attendance(
#             emp_id=record.emp_id,
#             intime=record.intime,
#             outtime=record.outtime,
#             shift=record.shift
#         )
#         session_sqlite.add(sqlite_record)

#     session_sqlite.commit()
#     session_sqlite.close()
#     session_mysql.close()

# # Initialize scheduler
# scheduler = BackgroundScheduler()
# scheduler.add_job(fetch_and_store_data, trigger='interval', seconds=5)
# scheduler.start()

# # API endpoint to trigger data retrieval and storage
# @app.route('/fetch-and-store', methods=['GET'])
# def fetch_and_store():
#     fetch_and_store_data()
#     return jsonify({'message': 'Data fetched and stored successfully'})

# if __name__ == '__main__':
#     app.run(debug=True)











# from flask import Flask, jsonify
# from sqlalchemy import create_engine, Column, Integer, String, DateTime, func, or_
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker
# from apscheduler.schedulers.background import BackgroundScheduler
# from datetime import datetime

# app = Flask(__name__)

# # MySQL Database Configuration
# app.config['MYSQL_HOST'] = '192.168.137.183'
# app.config['MYSQL_USER'] = 'sabari'
# app.config['MYSQL_PASSWORD'] = '12345678'
# app.config['MYSQL_DB'] = 'server'

# # SQLite Database Configuration
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///attendance_data.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# mysql_engine = create_engine(
#     f"mysql://{app.config['MYSQL_USER']}:{app.config['MYSQL_PASSWORD']}@{app.config['MYSQL_HOST']}/{app.config['MYSQL_DB']}",
#     echo=True
# )

# sqlite_engine = create_engine('sqlite:///attendance_data.db', echo=True)
# Base = declarative_base()

# class Attendance(Base):
#     __tablename__ = 'Attendance'

#     id = Column(Integer, primary_key=True)
#     emp_id = Column(Integer)
#     intime = Column(DateTime)
#     outtime = Column(DateTime)
#     shift = Column(String(255))

# # Create SQLite table
# Base.metadata.create_all(sqlite_engine)

# # Function to fetch data from MySQL and store it in SQLite
# def fetch_and_store_data():
#     SessionMySQL = sessionmaker(bind=mysql_engine)
#     session_mysql = SessionMySQL()

#     # Get the current date
#     current_date = datetime.now().date()

#     try:
#         # Print the current date for debugging
#         print("Current date:", current_date)

#         # Filter records based on the current date
#         mysql_data = session_mysql.query(Attendance).filter(
#             or_(func.date(Attendance.intime) == current_date, func.date(Attendance.outtime) == current_date)
#         ).all()

#         # Print the retrieved data for debugging
#         print("Retrieved data:", mysql_data)
#     except Exception as e:
#         # Print the exception details for debugging
#         print("Exception:", e)

#     SessionSQLite = sessionmaker(bind=sqlite_engine)
#     session_sqlite = SessionSQLite()

#     for record in mysql_data:
#         sqlite_record = Attendance(
#             emp_id=record.emp_id,
#             intime=record.intime,
#             outtime=record.outtime,
#             shift=record.shift
#         )
#         session_sqlite.add(sqlite_record)

#     session_sqlite.commit()
#     session_sqlite.close()
#     session_mysql.close()

# # Initialize scheduler
# scheduler = BackgroundScheduler()
# scheduler.add_job(fetch_and_store_data, trigger='interval', seconds=5)
# scheduler.start()

# # API endpoint to trigger data retrieval and storage
# @app.route('/fetch-and-store', methods=['GET'])
# def fetch_and_store():
#     fetch_and_store_data()
#     return jsonify({'message': 'Data fetched and stored successfully'})

# if __name__ == '__main__':
#     app.run(debug=True)

















from flask import Flask, jsonify
from sqlalchemy import create_engine, Column, Integer, String, DateTime, func, or_
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime

app = Flask(__name__)

# MySQL Database Configuration
app.config['MYSQL_HOST'] = '192.168.137.183'
app.config['MYSQL_USER'] = 'sabari'
app.config['MYSQL_PASSWORD'] = '12345678'
app.config['MYSQL_DB'] = 'server'

# SQLite Database Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///attendance_data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

mysql_engine = create_engine(
    f"mysql://{app.config['MYSQL_USER']}:{app.config['MYSQL_PASSWORD']}@{app.config['MYSQL_HOST']}/{app.config['MYSQL_DB']}",
    echo=True
)

sqlite_engine = create_engine('sqlite:///attendance_data.db', echo=True)
Base = declarative_base()

class Attendance(Base):
    __tablename__ = 'Attendance'

    id = Column(Integer, primary_key=True)
    emp_id = Column(Integer)
    intime = Column(DateTime)
    outtime = Column(DateTime)
    shift = Column(String(255))

# Create SQLite table
Base.metadata.create_all(sqlite_engine)

# Function to fetch data from MySQL and store it in SQLite
def fetch_and_store_data():
    SessionMySQL = sessionmaker(bind=mysql_engine)
    SessionSQLite = sessionmaker(bind=sqlite_engine)

    try:
        # Use context manager to ensure session is closed properly
        with SessionMySQL() as session_mysql:
            # Get the current date
            current_date = datetime.now().date()
            print("Current date:", current_date)

            # Filter records based on the current date
            mysql_data = session_mysql.query(Attendance).filter(
                or_(func.date(Attendance.intime) == current_date, func.date(Attendance.outtime) == current_date)
            ).all()

            # Print the retrieved data for debugging
            print("Retrieved data:", mysql_data)

            with SessionSQLite() as session_sqlite:
                for record in mysql_data:
                    # Check if the record already exists in SQLite
                    existing_record = session_sqlite.query(Attendance).filter_by(emp_id=record.emp_id, intime=record.intime, outtime=record.outtime).first()

                    if not existing_record:
                        # Record doesn't exist, add it to SQLite
                        sqlite_record = Attendance(
                            emp_id=record.emp_id,
                            intime=record.intime,
                            outtime=record.outtime,
                            shift=record.shift
                        )
                        session_sqlite.add(sqlite_record)

                session_sqlite.commit()

    except Exception as e:
        # Print the exception details for debugging
        print("Exception:", e)

# Initialize scheduler
scheduler = BackgroundScheduler()
scheduler.add_job(fetch_and_store_data, trigger='interval', seconds=2)
scheduler.start()

# API endpoint to trigger data retrieval and storage
@app.route('/fetch-and-store', methods=['GET'])
def fetch_and_store():
    fetch_and_store_data()
    return jsonify({'message': 'Data fetched and stored successfully'})

if __name__ == '__main__':
    app.run(debug=True)


