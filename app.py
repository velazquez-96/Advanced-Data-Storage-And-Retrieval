# Homework app
import numpy as np
import datetime as dt

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, desc

from flask import Flask, jsonify

# Database Setup
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

Base = automap_base()

Base.prepare(engine, reflect=True)

Measurement = Base.classes.measurement
Station = Base.classes.station

session = Session(engine)

latest_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first()

app = Flask(__name__)


@app.route("/")
def home():
    return(
        f"Welcome to the Hawaii climate API! <br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation     ------------  Precipitation data from 2010-01-01 to 2017-08-23<br/>"
        f"/api/v1.0/stations          ------------  List of stations <br/>"
        f"/api/v1.0/tobs              ------------  Dates and temperature observations of the most active station for the last year of data.<br/>"        
        f"/api/v1.0/start             ------------  Tmax, Tavg, and Tmax for all dates greater than and equal to the start date<br/>"
        f"/api/v1.0/start/end         ------------  Tmax, Tavg, and Tmax for dates between the start and end date inclusive.<br/>"
    )


@app.route("/api/v1.0/precipitation")
def prcp():
    session = Session(engine)

    query_prcp = session.query(
        Measurement.date, Measurement.prcp).order_by(Measurement.date).all()

    session.close()

    precipitation_data = []
    for date, prcp in query_prcp:
        dict_prcp = {}
        dict_prcp[date] = prcp
        precipitation_data.append(dict_prcp)

    return jsonify(precipitation_data)


@app.route("/api/v1.0/stations")
def stations():
    session = Session(engine)

    stations_results = session.query(Station.station, Station.name).all()

    session.close()

    stations_list = []
    for st, name in stations_results:
        dict_st = {}
        dict_st[st] = name
        stations_list.append(dict_st)
    

    return jsonify(stations_list)


@app.route("/api/v1.0/tobs")
def tobs():
    session = Session(engine)

    results_2 = session.query(Measurement.station, func.count(Measurement.station)).group_by(
        Measurement.station).order_by(func.count(Measurement.station).desc()).all()
    #latest_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first()
    year_ago = dt.date(2017, 8, 23) - dt.timedelta(days=365)

    tobs_results = session.query(Measurement.date, Measurement.tobs).\
        filter(Measurement.station == results_2[0][0], Measurement.date >= year_ago).\
        order_by(Measurement.tobs.desc()).all()

    session.close()

    tobs_data = []
    for date, tobs in tobs_results:
        dict_tobs = {}
        dict_tobs[date] = tobs
        tobs_data.append(dict_tobs)

    return jsonify(tobs_data)


@app.route("/api/v1.0/<start>")
def Start_dt(start):
    session = Session(engine)

    summary_info_temp = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= start).all()

    session.close()

    temp_data = []
    for t in summary_info_temp:
        dict_temp = {}
        dict_temp["Min temp"] = t[0]
        dict_temp["Avg temp"] = t[1]
        dict_temp["Max temp"] = t[2]
        temp_data.append(dict_temp)

    return jsonify(temp_data)

@app.route("/api/v1.0/<start_dt>/<end_dt>")
def StartEnd(start_dt, end_dt):
    session = Session(engine)
    summary_init_end = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= start_dt).filter(Measurement.date <= end_dt).all()

    session.close()

    range_data = []
    for dates in summary_init_end:
        dict_info = {}
        dict_info["Min temp"] = dates[0]
        dict_info["Avg temp"] = dates[1]
        dict_info["Max temp"] = dates[2]
        range_data.append(dict_info)

    return jsonify(range_data)

if __name__ == "__main__":
    app.run(debug=True)
