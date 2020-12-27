#!/bin/bash

repository='jonberenguer/zsa-qmk'
tag='new'

isLatest=`docker images --quiet ${repository}:latest | wc -l`


cd qmk_firmware
git pull --rebase
make git-submodule
cd ..

buildimage () {
	docker build -t ${repository}:${tag} .
	docker tag ${repository}:${tag} ${repository}:latest
	docker rmi ${repository}:${tag}
}

# this just replace the recent image with old
if [ $isLatest = 1 ] ; then
	docker tag ${repository}:latest ${repository}:old
	docker rmi ${repository}:latest
fi

buildimage


