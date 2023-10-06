import re
import geopandas as gpd
import json
import geojsonio
from shapely.geometry import Point

name = " "
feature_collection = {"type": "FeatureCollection", "features": []}
lon = 0
lat = 0


def to_geojson():
    from geojsonio import display

    global lon
    global lat
    global name
    feature = {
        "type": "Feature",
        "geometry": {"type": "Point", "coordinates": [lon, lat]},
        "properties": {"name": name},
    }
    feature_collection["features"].append(feature)


def separation(var):
    global name

    list = var.split(" ")
    if len(list) > 2:
        name = " ".join(list[2:])
        coor_converter(list[0:2])
    else:
        coor_converter(list)


def coor_converter(var):
    global lon
    global lat
    point = []
    for i in range(len(var)):
        if "S" in var[i] or "N" in var[i]:  # stand for latitude and Not DD
            lat = convert_to_dd(var[i])
        elif "E" in var[i] or "W" in var[i]:  # stand for longitude and NOT DD
            lon = convert_to_dd(var[i])

        else:  # don't have direction letter, assume it's DD
            point.append(float(var[i]))
    if len(point) > 0:
        dd_to_geojson(point)
    to_geojson()
    # to_display()


def dd_to_geojson(point):
    global lon
    global lat
    if (point[0] > 90 and len(point) > 0) or (point[0] < -90 and len(point) > 0):
        lon = point[0]
        lat = point[1]
    else:
        lon = point[1]
        lat = point[0]
    # to_display()


def convert_to_dd(coor):
    if "°" in coor and "'" in coor and '"' in coor:
        return dms_to_dd(coor)
    elif "°" in coor and "." in coor:
        return ddm_to_dd(coor)
    else:
        return num_to_dd(coor)


# to concert non dd format coordinator to dd
# @param coor : number with direction e.g: 12.123W/ 12W
def num_to_dd(coor):
    if "." in coor:
        new_coor = coor.replace(" ", "")
        numeric_part = ""
        direction_part = ""
        for char in new_coor:
            if char.isdigit() or char == ".":
                numeric_part += char
            else:
                direction_part += char

        dd = float(numeric_part)
    else:
        new_coor = coor.replace(" ", "")

        numeric_part = ""
        direction_part = ""
        for char in new_coor:
            if char.isdigit():
                numeric_part += char
            else:
                direction_part += char

        dd = float(numeric_part)
    if direction_part in ("S", "W"):
        dd = -dd
    return dd


# to convert dms to dd
# @param dms: system detected dms format coordinator
def dms_to_dd(dms):
    if "N" in dms[0] or "S" in dms[0] or "E" in dms[0] or "W" in dms[0]:
        new_dms = dms[1 : len(dms)]
        dir = dms[0]
        parts = re.split("[°'\"]\s*|\s+", new_dms)
        degrees = float(parts[0])
        minutes = float(parts[1])
        seconds = float(parts[2])
        dd = degrees + minutes / 60 + seconds / 3600
    else:
        parts = re.split("[°'\"]\s*|\s+", dms)
        degrees = float(parts[0])
        minutes = float(parts[1])
        seconds = float(parts[2])
        dir = parts[3]
        dd = degrees + minutes / 60 + seconds / 3600
    if dir in ("S", "W"):
        dd = -dd

    return dd


# to convert ddm to dd
# @param dmm: system detected dmm format coordinator
def ddm_to_dd(dmm):
    if "N" in dmm[0] or "S" in dmm[0] or "E" in dmm[0] or "W" in dmm[0]:
        new_dmm = dmm[1 : len(dmm)]
        dir = dmm[0]
        parts = re.split("[°']", new_dmm)
        degree = float(parts[0])
        minutes = parts[1]
        minutes = float(minutes[:-1])
    else:
        parts = re.split("[°']", dmm)
        degree = float(parts[0])
        minutes = parts[1]
        dir = minutes[-1]
        minutes = float(minutes[:-1])
    if dir == "S" or dir == "W":
        dd = -(degree + minutes / 60)
    else:
        dd = degree + minutes / 60
    return dd


def to_display():
    from geojsonio import display

    geojson_str = json.dumps(feature_collection)
    display(geojson_str)


def main():
    try:
        while True:
            var = input(
                "please enter coordinator point(press p for print out and press q for quit)\n"
            )
            if var == "q":
                print("Good bye!")
                exit(1)
            elif var == "p":
                to_display()
            elif ", " in var:
                new_var = var.replace(", ", " ")
                separation(new_var)
            elif "," in var:
                new_var = var.replace(",", " ")
                separation(new_var)
            elif "° " in var and "′ " in var and "″ " in var:
                new_var = var.replace("° ", "°").replace("′ ", "'").replace("″ ", '"')
                separation(new_var)
            elif "° " in var:
                whole_var = var.replace("° ", "°").replace(" ", "")
                if "S" in whole_var and "W" in whole_var:
                    new_var = whole_var.replace("S", "S ").replace("W", "W ")
                elif "S" in whole_var and "E" in whole_var:
                    new_var = whole_var.replace("S", "S ").replace("E", "E ")
                elif "N" in whole_var and "W" in whole_var:
                    new_var = whole_var.replace("N", "N ").replace("W", "W ")
                elif "N" in whole_var and "E" in whole_var:
                    new_var = whole_var.replace("N", "N ").replace("E", "E ")
                separation(new_var)
            elif "°" in var:
                new_var = ""
                if "° " in var:
                    new_var = var.replace("° ", "")

                elif " °" in var:
                    new_var = var.replace(" °", "")

                elif "°" in var:
                    new_var = var.replace("°", "")

                separation(new_var)
            else:
                separation(var)
    except EOFError:
        pass


main()
to_display()
