################################################################################
# 	      Installation de pythons et des modules nécessaires	       #
################################################################################

sudo apt-get install python
sudo apt-get install python-pip
sudo pip install --upgrade pymongo requests


################################################################################
# 	   		   Téléchargement des données 	  		       #
################################################################################

sudo python downloadData.py


################################################################################
# 		   	   Installation de MongoDB	  		       #
################################################################################

sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 0C49F3730359A14518585931BC711F9BA15703C6

echo "deb [ arch=amd64,arm64 ] http://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/3.4 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.4.list

sudo apt-get update

sudo apt-get install -y mongodb-org

sudo service mongod start


################################################################################
# 		 Chargement des données téléchargées dans MongoDB	       #
################################################################################

sudo python loadData.py


################################################################################
# 			  Lancement des requêtes			       #
################################################################################

sudo python Requests.py
