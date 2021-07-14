
## docker creation
docker build  --network="host" -t milleinnovacion/gr_photos_uploader:latest .

xhost local:root

docker run  -it --rm \
    --name  gr_photos_uploader  \
    --net="host"  \
    -v "$PWD":/var/www \
    --env-file .env \
    -e DISPLAY=unix$DISPLAY \
    milleinnovacion/gr_photos_uploader:latest \
    /bin/bash  # -l -c "yarn run serve"

