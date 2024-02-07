from flask import Flask, jsonify
from sqlalchemy import create_engine, Column, Integer, String, DateTime, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from apscheduler.schedulers.background import BackgroundScheduler
import requests
from datetime import datetime

app = Flask(__name__)

# SQLite Database Configuration
engine = create_engine('sqlite:///attendance_data.db', echo=True)
Base = declarative_base()
metadata = MetaData()

class Attendance(Base):
    __tablename__ = 'attendance'

    id = Column(Integer, primary_key=True)
    emp_id = Column(Integer)
    intime = Column(DateTime)
    outtime = Column(DateTime)
    shift = Column(String(255))

# Create table
Base.metadata.create_all(engine)

# Function to fetch data from the API and store it in SQLite
# Function to fetch data from the API and store it in SQLite
# Import the datetime class from the datetime module
from datetime import datetime

# ...

def fetch_and_store_data():
    response = requests.get('http://192.168.137.243:5000/attendance')
    data = response.json().get('attendance', [])

    Session = sessionmaker(bind=engine)
    session = Session()

    for record in data:
        if isinstance(record, dict):
            # If 'record' is a dictionary, process it
            emp_id = int(record.get('Emp_id', 0))
            intime_str = record.get('intime')
            outtime_str = record.get('outtime')
            shift = record.get('shift')

        elif isinstance(record, list):
            # If 'record' is a list, handle it accordingly
            if len(record) >= 5:
                emp_id = int(record[1])
                intime_str = record[2]
                outtime_str = record[3]
                shift = record[4]
            else:
                print(f"Skipping invalid list record: {record}")
                continue
        else:
            # If 'record' is neither a dictionary nor a list, skip it
            print(f"Skipping invalid record: {record}")
            continue

        # Convert string to datetime
        intime = datetime.strptime(intime_str, '%a, %d %b %Y %H:%M:%S %Z')
        print(f"outtime_str: {outtime_str}")
        outtime = datetime.strptime(outtime_str, '%a, %d %b %Y %H:%M:%S %Z') if outtime_str else None

        attendance_record = Attendance(
            emp_id=emp_id,
            intime=intime,
            outtime=outtime,
            shift=shift
        )
        session.add(attendance_record)

    session.commit()
    session.close()



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


