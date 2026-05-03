build app:
docker build -t qa-app .

setup postgress: 
docker network create app-network

docker run -d --name postgres-db --network app-network \
  -e POSTGRES_DB=hillel_db \
  -e POSTGRES_USER=admin \
  -e POSTGRES_PASSWORD=admin \
  postgres

run app:
docker run --rm --network app-network -e DATABASE_URL=postgresql+psycopg2://admin:admin@postgres-db:5432/hillel_db qa-app