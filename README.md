# minio-storage-api
Creates a server of Minio [https://min.io/] with a Flask app which uses minio api [https://docs.min.io/docs/python-client-api-reference] for management storage.

### Info

The minio files and settings are stored in `./minio/data` and `./minio/.minio` respectively by default. This along with other parameters, such as port and credentials, can be modified in the `docker-compose.yml`.

URL: http://localhost:49153

#### Methods
  - `/alive` - returns alive
 
  - `/fm/save_file` - save file in Minio and return an 'objectname'

  - `/fm/get_file/<objectname>` - returns file data

  - `/remove_file/<objectname>` - remove file

#### Requirements:
- docker-compose

#### Init Steps:
1 - `docker-compose build` 

2 - `docker-compose up`

