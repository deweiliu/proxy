#docker build -t proxy .
docker tag proxy docker.pkg.github.com/deweiliu/proxy/proxy
docker push docker.pkg.github.com/deweiliu/proxy/proxy
#docker rmi proxy