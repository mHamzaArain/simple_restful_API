# Simple Restful API

## Objective 
Build a restful API that supports +, -, *, /

## Methods
GET, POST, DELETE & PUT

## Resources:

| Resources | Method | Path | Description      | Parameter         | Error                                   |
|-----------|--------|------|------------------|-------------------|-----------------------------------------|
| +         | POST   | /add | add 2 nums       | x: float y: float | 200 OK 301 Field Missing                |
| -         | POST   | /sub | subtract 2 nums  | x: float y: float | 200 OK  301 Field Missing               |
| *         | POST   | /mul | multuiply 2 nums | x: float y: float | 200 OK  301 Field Missin                |
| /         | POS    | /div | divide 2 nums    | x: float y: float | 200 OK  301 Field Missing 302 y is zero |


## MongoDB Database
Holds number of visits on ```localhost:5000/hello```

## Docker

### Dockerization

1. Change directory to working folder where ```app.py``` resides
    ```cd 02_simple_Restful_API``` 

2. Build directory
    ```docker-compose build```

3. Run directory
    ```docker-compose up```

