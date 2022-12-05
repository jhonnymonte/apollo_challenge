

## API Reference
## how to install de project
```
create a virtual enviroment
pipenv shell
```
```
install flask
pip install flask
```
```
run project
python apps.py
```
#### Create a CSV

```http
  GET /createcsv
```
create a csv file with a list of packages
#### Get item

```http
  GET packagename/<string:str_params>
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. name of packages |

returns info searching by name packages
```http
  GET pythonversion/<string:str_params>
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. python version |

```http
  GET all
```

| | Description                       |
| | :-------------------------------- |
| | get a list of all packages |

returns info searching by name packages

