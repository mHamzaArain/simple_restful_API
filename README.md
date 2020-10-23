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