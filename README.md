# docker-stego-protector

### Description ###

This repository includes a [Docker](https://www.docker.com) container able to mitigate covert channels exploiting the memory of the host to create malicious container-to-container communications.
For an example of such malevolent application, refer to [YehudaCorsia/Docker-Covert-channel](https://github.com/YehudaCorsia/Docker-Covert-channel).
In order to disturb the covert channel, a random amount of memory is periodically allocated by the container.

This repository represent an outcome of a joint research by [CNR-IMATI](https://imati.cnr.it) and [CNR-IEIIT](https://www.ieiit.cnr.it).
In case of exploitation for research purposes, please mention the following paper:

M. Zuppelli, M. Repetto, L. Caviglione, E. Cambiaso, _Information Leakages of Docker Containers: Characterization and Mitigation Strategies_, 5th International Workshop on Cyber-Security Threats, Trust and Privacy Management in Software-defined and Virtualized Infrastructures, within the 9th International Conference on Network Softwarization, Madrid, Spain, June 2023.

### Installation ###

For a manual installation, follow the steps reported below.

* Clone the repository:
```
git clone https://github.com/cybersecurity-cnr/docker-stego-protector
```
* `cd` into the cloned repository:
```
cd docker-stego-protector
```
* Build the Docker image:
```
docker build -t docker-stego-protector .
```
* Optionally, save the Docker image to file:
```
docker save docker-stego-protector:latest|gzip > docker-stego-protector.tar.gz
```

### Usage ###

Just run the Docker container, with a command similar to the following one:
```
docker run -e SIZEFROM=1000000000 -e SIZETO=2000000000 -e TIMEOUTFROM=1 -e TIMEOUTFROM=5 -t docker-stego-protector
```
where:
* `SIZEFROM` identifies the minimum size of memory to allocate at each round, in bytes
* `SIZETO` identifies the maximum size of memory to allocate at each round, in bytes
* `TIMEOUTFROM` identifies the minimum duration of each round, in seconds
* `TIMEOUTTO` identifies the maximum duration of each round, in seconds

### Credits ###

* [Enrico Cambiaso](https://www.ieiit.cnr.it/people/Cambiaso-Enrico)
* [Luca Caviglione](https://www.imati.cnr.it/mypage.php?idk=PG-44)
* [Marco Zuppelli](https://www.imati.cnr.it/mypage.php?idk=PG-157)

## Acknowledgement ###

This work was partially supported by project [SERICS](https://serics.eu/) (PE00000014) under the NRRP MUR program funded by the EU - NGEU.
