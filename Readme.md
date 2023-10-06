# Where in the world is CS?

## Description:
The program should allow users to enter a pair of coordinates that represent a location point. Python is the preferred language for this task because it provides convenient data cleaning and validation capabilities.

The program should prompt the user to enter the coordinates and perform the necessary data cleaning and validation to ensure the input is in the correct format. It should handle various coordinate formats, such as degrees-minutes-seconds (DMS) or degrees-decimal minutes (DDM).

Once the coordinates are validated and cleaned, the program should convert them to decimal degrees (DD) format. The conversion should handle coordinates with directional indicators (N, S, E, W) as well as coordinates specified without directional indicators, assuming they are in DD format.

After converting the coordinates to DD format, the program should generate a GeoJSON file containing the location point. The GeoJSON file should include the latitude, longitude, and any additional properties (e.g., name) associated with the location.

Finally, the program should display the GeoJSON file using a suitable tool or library, allowing the user to visualize the location point on a map.

## Accepted Input format : 
|Input |Format regex| Detection Status|
|:------|:----------|:----------------|
|0°00'00.0"N 0°00'00.0"E| D°MM'SS.S"N(DMS - with space) | OK|
|N0°00'00.0" E0°00'00.0"| ND°MM'SS.S"(DMS) | OK|
|0.000000, 0.000000|D.SSSS (DD - no sign/direction)| OK|
|0.000000N, 0.000000E|D.SSSS (DD - direction)| OK|
|+0.000000, -0.000000| (+/-)D.SSS(DD- within sign)| OK|
|00°00.0S 00°00.00E| D°DD.SS(DDS - with space)| OK|
|N 0° 00' 00.0" E 0° 00' 00.0"| ND°MM'SS.S"(DMS - with space) | NOK|
|34 90| DD (numbers) | OK|
|77° S 164° E| DD° Dir(with space)| OK|
## Demo: 
[link](https://altitude.otago.ac.nz/kmao/cosc326/-/blob/main/World/demo.mp4)
<video src= "demo.mp4" controls="controls" style="max-width: 730px;"></video>
## Algorithm :
    1.Import the necessary libraries: re, json, geojsonio, and shapely.geometry.Point.
    2.Define a feature_collection dictionary to store the GeoJSON feature collection.
    3.Implement the to_geojson() function to create a GeoJSON feature object with the given lon, lat, and name values. Append the feature object to the feature_collection.
    4.Implement the separation() function to split the input string and extract the coordinates and name (if available). Call the coor_converter() function with the coordinates
    5.Implement the coor_converter() function to iterate over the coordinates. Check if the coordinate represents latitude or longitude. Convert the coordinate to decimal degrees and store it in the corresponding global variables (lon or lat).
    6.Implement the dd_to_geojson() function to handle coordinates in decimal degrees format. Check if the coordinate is valid latitude or longitude and assign it to the appropriate global variable.

    7.Implement the convert_to_dd() function to convert coordinate formats (DMS or DDM) to decimal degrees.

    8.Implement the dms_to_dd() function to convert a coordinate in degrees, minutes, and seconds format to decimal degrees.

    9.Implement the ddm_to_dd() function to convert a coordinate in degrees and decimal minutes format to decimal degrees.

    10.Implement the to_display() function to read the GeoJSON file and display it using geojsonio.

    11.Implement the main() function to continuously prompt the user for input, clean the input, and process the coordinates and names.

## Usage: 
To run the program, navigate to the `***WORLD***` directory and execute the command python `***coordinater.py***`< file.txt, where file.txt contains the input pairs.

## Testing:

|Test case| Test Summary |Test start | Test result| Test status|
:---------|:-------------|:-----------|:------------|:-----------|
|#1| Using DMS standard format input| input eg: 70°37'25.2"N 47°35'03.7"W| produce correct point the geojson.io | OK|
|#2| Using DMS but no standard format input| input eg: N70°37'25.2" W47°35'03.7"| product same point with standard input in geojson.io| OK|
|#3| Using DDM standard format input| input eg: 77°30.5S 164°45.25E| generate correct point in geojson.io| OK|
|#4| Using DDM but direction letter in the first index| input eg: S77°30.5 E164°45.25| work as it should| OK|
|#5| Using DD with correct order latitude, longitude| input eg: -77.508333E 164.754167| generate right location| OK|
|#6| using DD but reverse order of latitude and longitude| input eg: -180 -90 | Give correct point on the map| OK|
|#7| give one word on the end represent as name| input eg: -180 -90 test| generate geojson has input as their name| OK|
|#8| give multiple word as name| input eg:  -77.508333E 164.754167 I don't know| name generate as input given| OK|


# Test Data: 
```text
<data.txt>
0°00'00.0"N 0°00'00.0"E
N0°00'00.0" E0°00'00.0"
0.000000, 0.000000
0 0
70°37'25.2"N 47°35'03.7"W
N70°37'25.2" W47°35'03.7"
70.623659, -47.584351
77°30.5S 164°45.25E
S77°30.5 E164°45.25
-77.508333E 164.754167
77°30'29.99"S,164°45'15.00"E
36 -69
+36 -98 I don't know
-180 -90 test
70°37'25.2"N,47°35'03.7"W,auckland
9,18,dunedin 
43.123,42.123,test
71°37'25.2"N 47°35'03.7"W
70°37'25.2"N 47°35'03.7"W opps
70°37'25.2"N 7°35'03.7"W Fiji island
70°37'25.2"N 36°35'03.7"W Fiji lander
77°30'29.99"S,14°45'15.00"E land
7°03'05.2"N 36°35'03.7"W Fir
35 89
12 32
12, 12, good point
35 21 bad point
21,12,point
S7°30.5 E14°45.25 somewhere
S6°66.5 E64°04.15
S27°03.1 E164°05.25
S77° E164° 
71.623659, -47.584351
0.623659, -4.5843251
-7.6239, -7.51
-70.623659, -47.58
+7.50 -164.754167 Point
-77.5083 24.7167
18.3535,24.7
12.51, 12.213 O point
5.5,4.6,X point
01°03'29.99"S,35°45'15.00"E fland
25°47'07.1"N 80°13'58.6"W, Miami, Florida
51°30'29.7"N 0°07'48.4"W, London, UK
35°41'22.2"N 139°41'30.5"E, Tokyo, Japan
40°26'47.1"N 79°58'58.8"W, Pittsburgh, Pennsylvania
48°51'29.1"N 2°17'40.2"E, Paris, France
42°20'15.5"N 71°03'37.2"W, Boston, Massachusetts
37°48'39.2"N 122°26'57.6"W, San Francisco, California
22°16'01.6"S 166°27'47.7"E, Noumea, New Caledonia
```


