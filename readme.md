docker exec -it flask-hello_flask_1 bash
docker exec -it flask-hello_flask_1 python train_model.py



https://www.youtube.com/watch?v=UcN45dPX4LA&list=PLQJ7ptkRY-xYLEAC5Y_sKqrJ9RA-U7Dja&index=14

curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"flower": "1,2,3,7"}' \
  http://localhost:5000/iris_post
  
