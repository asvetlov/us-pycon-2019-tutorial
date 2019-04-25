# test script for REST API


curl http://localhost:8080/api
# {"status": "ok", "data": "ret"}%                                   

curl -X POST http://localhost:8080/api -d '{"title": "test title", "owner": "test user", "text": "test text"}'
# {"status": "ok", "data": {"id": 1, "owner": "test user", "editor": "test user", "title": "test title", "text": "test text"}}

curl http://localhost:8080/api/1
# {"status": "ok", "data": {"id": "1", "owner": "test user", "editor": "test user", "title": "test title", "text": "test text"}}


curl -X DELETE http://localhost:8080/api/1


curl -X PATCH http://localhost:8080/api/1 -d '{"text": "new text"}'
#{"status": "ok", "data": {"id": "1", "owner": "test user", "editor": "test user", "title": "test title", "text": "new text"}}

curl  http://localhost:8080/api/1
# {"status": "ok", "data": {"id": "1", "owner": "test user", "editor": "test user", "title": "test title", "text": "new text"}}%       
